#!/usr/bin/env python3
# /// script
# dependencies = ["docutils", "markdown"]
# ///
"""Convertit les sources reStructuredText (source/) en Markdown (src/), pour Zensical.

Le script est idempotent : il régénère intégralement `src/` à partir de `source/`,
et peut donc être relancé tant que les deux arborescences coexistent.

La conversion proprement dite est faite par pandoc ; ce script s'occupe de ce que
pandoc ne sait pas traduire, faute de connaître Sphinx :

- les rôles `:doc:` deviennent des liens Markdown relatifs, avec pour libellé le
  titre du document cible (ce que fait Sphinx au rendu) ;
- les directives `toctree` deviennent des listes de liens, la navigation étant
  par ailleurs déclarée dans zensical.toml ;
- les admonitions (`.. warning::`) prennent la syntaxe de Material/Zensical ;
- les ancres de titres divergentes sont figées explicitement, pour que les liens
  profonds vers l'ancien site continuent de fonctionner (voir `pin_anchors`).

Utilisation :

    uv run rst_to_md.py            # convertit source/ vers src/
    uv run rst_to_md.py --nav      # affiche en plus le bloc `nav` pour zensical.toml
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

from docutils.nodes import make_id
from markdown.extensions.toc import slugify

ROOT = Path(__file__).parent
SRC_RST = ROOT / "source"
SRC_MD = ROOT / "src"

# pandoc : on désactive `smart` des deux côtés pour préserver à l'identique la
# typographie française du guide (apostrophes courbes, guillemets), et on
# n'autorise que les tableaux « pipe », seuls compris par Python-Markdown.
PANDOC_FROM = "rst-smart"
PANDOC_TO = "markdown-smart-simple_tables-multiline_tables-grid_tables+pipe_tables"

RE_DOC_ROLE = re.compile(r"`([^`]+)`\{\.interpreted-text role=\"doc\"\}")
RE_TOCTREE = re.compile(
    r"^:{3,}\s*\{\.toctree([^}]*)\}\n(.*?)^:{3,}\s*$", re.MULTILINE | re.DOTALL
)
RE_TITLE_REF = re.compile(r"\[([^\]]+)\]\{\.title-ref\}")
RE_ADMONITION = re.compile(
    r"^(:{3,})\s*(\w+)\n:{3,}\s*title\n.*?\n:{3,}\n\n(.*?)^\1\s*$",
    re.MULTILINE | re.DOTALL,
)

# Les trois dimensions annoncées par l'introduction du guide. Elles forment les
# onglets du bandeau supérieur ; les parties se rangent dessous, en sections du
# menu de gauche. Huit onglets pour huit parties encombraient le bandeau sans
# rien dire du plan de l'ouvrage.
# Chaque entrée : intitulé de l'onglet, page d'introduction de la dimension,
# parties qu'elle regroupe. Infrastructure n'a pas de page propre : la dimension
# s'y confond avec la partie, dont l'introduction fait office des deux.
DIMENSIONS = (
    (
        "Applications",
        "applications",
        (
            "applications-generiques",
            "applications-metiers",
            "web-communication",
            "poste-client-bureautique",
        ),
    ),
    (
        "Développement et couches intermédiaires",
        "developpement-et-middleware",
        ("developpement", "sgbd-middleware", "devops"),
    ),
    ("Infrastructure", None, ("infrastructure",)),
)

# Pages liminaires et annexes : elles tiennent sous l'onglet d'accueil, dont
# elles sont le prolongement naturel, plutôt que d'occuper le bandeau.
HOME_TAB = ("introduction", "conclusion", "licences", "remerciements", "changelog", "todo")

# Icônes des parties sur la page d'accueil.
PART_ICONS = {
    "applications-generiques/index": "material-apps",
    "applications-metiers/index": "material-briefcase-outline",
    "web-communication/index": "material-web",
    "poste-client-bureautique/index": "material-laptop",
    "developpement/index": "material-code-braces",
    "sgbd-middleware/index": "material-database",
    "devops/index": "material-infinity",
    "infrastructure/index": "material-server",
}

# Titres des admonitions, que Sphinx traduisait et que Material laisse en anglais
# si on ne les nomme pas explicitement.
ADMONITION_TITLES = {
    "warning": "Avertissement",
    "note": "Note",
    "tip": "Astuce",
    "important": "Important",
    "caution": "Attention",
}


def rst_files() -> list[Path]:
    """Toutes les sources RST, dans un ordre stable."""
    return sorted(SRC_RST.rglob("*.rst"))


def docname(path: Path) -> str:
    """`source/web-communication/cms.rst` -> `web-communication/cms`."""
    return path.relative_to(SRC_RST).with_suffix("").as_posix()


def title_of(path: Path) -> str:
    """Le titre de premier niveau d'un document RST."""
    lines = path.read_text(encoding="utf-8").splitlines()
    for line, underline in zip(lines, lines[1:]):
        if line.strip() and set(underline) == {"="} and len(underline) >= len(line.strip()):
            return line.strip()
    sys.exit(f"{path}: pas de titre de premier niveau")


def relative_link(from_doc: str, to_doc: str) -> str:
    """Lien Markdown relatif entre deux documents, tel que Zensical le réécrira."""
    from_dir = Path(from_doc).parent
    return Path(os.path.relpath(to_doc, from_dir)).as_posix() + ".md"


def convert_roles(text: str, cur_doc: str, titles: dict[str, str]) -> str:
    """`:doc:` -> lien Markdown, avec le titre du document cible pour libellé."""

    def replace(match: re.Match[str]) -> str:
        target = match.group(1).lstrip("/")
        if target not in titles:
            sys.exit(f"{cur_doc}: cible :doc: inconnue -> {target}")
        return f"[{titles[target]}]({relative_link(cur_doc, target)})"

    return RE_DOC_ROLE.sub(replace, text)


def entries_of(doc: str) -> list[str]:
    """Les documents listés par le toctree d'un index."""
    source = SRC_RST / f"{doc}.rst"
    return nav_entries(source) if source.exists() else []


def home_grid(docs: list[str], titles: dict[str, str]) -> str:
    """La page d'accueil : une carte par partie, contenant ses chapitres.

    Sphinx y déroulait une liste à puces de plus de cent entrées. La grille de
    Material donne la même information — l'arborescence complète du guide — sous
    une forme lisible d'un coup d'œil.
    """
    parts = [f"{part}/index" for _, _, group in DIMENSIONS for part in group]
    dimensions = {intro for _, intro, _ in DIMENSIONS if intro} | set(parts)

    cards, others = [], []
    for doc in docs:
        # Le sommaire général liste les dimensions ; la grille, elle, descend
        # jusqu'aux parties, seul niveau qui dise au lecteur ce qu'il va trouver.
        if doc not in dimensions:
            others.append(f"- [{titles[doc]}]({doc}.md)")
    for doc in parts:
        icon = PART_ICONS.get(doc)
        head = f":{icon}:{{ .lg .middle }} " if icon else ""
        card = f"-   {head}__[{titles[doc]}]({doc}.md)__"
        chapters = entries_of(doc)
        if chapters:
            links = "\n".join(f"    - [{titles[c]}]({c}.md)" for c in chapters)
            card += f"\n\n    ---\n\n{links}"
        cards.append(card)

    grid = '<div class="grid cards" markdown>\n\n' + "\n\n".join(cards) + "\n\n</div>"
    if others:
        grid += "\n\n## Autour du guide\n\n" + "\n".join(others)
    return grid + "\n"


RE_LEADING_FIELDS = re.compile(r"\A(# .+?\n\n)((?:\S.*\n:[ \t]+.*\n\n)+)", re.MULTILINE)

# Libellés du bloc d'en-tête de index.rst, traduits pour la ligne de pied de
# page. `Title` en est écarté (il répète le titre de niveau 1 juste au-dessus)
# et `Date` aussi, qui a droit à sa propre ligne en tête de page.
METADATA_LABELS = {
    "Authors": "Auteurs",
    "Maintainer": "Mainteneur",
}


def compact_metadata(text: str) -> str:
    """Répartit l'état civil de l'ouvrage sur la page d'accueil.

    La date de révision est annoncée entre l'entrée en matière et le sommaire :
    assez haut pour qu'on la voie sans défiler — c'est ce que vient vérifier en
    premier le lecteur d'un guide remis à jour par éditions successives — mais
    après le paragraphe d'introduction, qui ouvre la page. Les auteurs et le
    mainteneur forment une ligne de crédits en pied de page. En liste de
    définitions et en tête de page, ces quatre champs occupaient un écran entier
    avant l'entrée en matière, avec des libellés restés en anglais.
    """
    match = RE_LEADING_FIELDS.match(text)
    if not match:
        return text
    fields = re.findall(r"^(\S.*)\n:[ \t]+(.*)$", match.group(2), re.MULTILINE)
    date = next((value for label, value in fields if label == "Date"), None)
    credits = " · ".join(
        f"{METADATA_LABELS[label]} : {value}"
        for label, value in fields
        if label in METADATA_LABELS
    )
    body = text[match.end() :].rstrip()
    grid = '<div class="grid cards"'
    if date and grid in body:
        cut = body.index(grid)
        body = f"{body[:cut]}**Dernière révision : {date}**\n\n{body[cut:]}"
    return f"{match.group(1)}{body}\n\n---\n\n*{credits}*\n"


def convert_toctrees(text: str, cur_doc: str, titles: dict[str, str]) -> str:
    """`toctree` -> liste de liens vers les pages filles.

    La page d'accueil fait exception : son sommaire général prend la forme d'une
    grille de cartes (voir `home_grid`).
    """

    def replace(match: re.Match[str]) -> str:
        cur_dir = Path(cur_doc).parent
        docs = [
            (cur_dir / e).with_suffix("").as_posix()
            for e in match.group(2).split()
            if e.endswith(".rst")
        ]
        for target in docs:
            if target not in titles:
                sys.exit(f"{cur_doc}: entrée de toctree inconnue -> {target}")
        if cur_doc == "index":
            return home_grid(docs, titles)  # métadonnées déplacées en aval
        return "\n".join(
            f"- [{titles[t]}]({relative_link(cur_doc, t)})" for t in docs
        ) + "\n"

    return RE_TOCTREE.sub(replace, text)


def convert_admonitions(text: str) -> str:
    """Divs pandoc -> syntaxe Material (`!!! warning`, corps indenté)."""

    def replace(match: re.Match[str]) -> str:
        kind = match.group(2).lower()
        body = match.group(3).rstrip()
        indented = "\n".join(
            ("    " + line if line.strip() else "") for line in body.splitlines()
        )
        title = ADMONITION_TITLES.get(kind)
        head = f'!!! {kind} "{title}"' if title else f"!!! {kind}"
        return f"{head}\n\n{indented}\n"

    return RE_ADMONITION.sub(replace, text)


def pin_anchors(text: str) -> str:
    """Fige les ancres qui changeraient en passant de docutils à Python-Markdown.

    Les deux découpeurs de titres ne traitent pas de la même façon les
    apostrophes, les points et les titres commençant par un chiffre : « 389
    directory server » donnait `#directory-server` sous Sphinx et donnerait
    `#389-directory-server` ici. On rétablit l'ancienne ancre avec `attr_list`
    partout où elle diffère, afin de ne pas casser les liens entrants profonds.

    Les titres répétés dans une même page (« Autres ») sont laissés de côté :
    docutils les numérotait en `#id1`, `#id2`, ancres instables qui changeaient
    au moindre remaniement et qui ne valent pas d'être préservées.
    """
    seen: set[str] = set()
    out = []
    for line in text.splitlines():
        heading = re.match(r"^(#+) +(.+?)\s*$", line)
        if heading:
            title = heading.group(2)
            old, new = make_id(title), slugify(title, "-")
            if title in seen:
                pass  # doublon : ancre auto-numérotée des deux côtés
            elif old and old != new:
                line = f"{line} {{ #{old} }}"
            seen.add(title)
        out.append(line)
    return "\n".join(out) + "\n"


def convert(path: Path, titles: dict[str, str]) -> str:
    """Convertit un fichier RST en Markdown prêt pour Zensical."""
    result = subprocess.run(
        ["pandoc", "-f", PANDOC_FROM, "-t", PANDOC_TO, "--wrap=none", str(path)],
        capture_output=True,
        text=True,
        check=True,
    )
    doc = docname(path)
    text = result.stdout
    text = convert_roles(text, doc, titles)
    text = convert_admonitions(text)
    # `openssl ca` : rôle RST par défaut (title-ref), rendu en code ici.
    text = RE_TITLE_REF.sub(r"`\1`", text)
    # pandoc échappe des caractères qui n'ont pas besoin de l'être en prose,
    # dont les marqueurs d'emphase accolés à un mot (« d'**Apache KIE** »), que
    # l'extension betterem sait pourtant interpréter.
    text = text.replace("\\'", "'").replace('\\"', '"').replace("\\*", "*")
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return pin_anchors(text)


def nav_entries(path: Path) -> list[str]:
    """Les documents listés par le toctree d'un index, dans l'ordre déclaré."""
    cur_dir = Path(docname(path)).parent
    entries: list[str] = []
    inside = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith(".. toctree::"):
            inside = True
        elif inside:
            stripped = line.strip()
            # Une ligne non indentée et non vide termine la directive ; les
            # lignes d'options (`:maxdepth: 2`) et les lignes vides sont ignorées.
            if stripped and not line[0].isspace():
                inside = False
            elif stripped.endswith(".rst"):
                entries.append((cur_dir / stripped).with_suffix("").as_posix())
    return entries


def build_nav(titles: dict[str, str]) -> str:
    """Le bloc `nav` de zensical.toml.

    Le bandeau supérieur porte les trois dimensions du guide ; le menu de gauche
    déroule les parties de la dimension courante, puis leurs chapitres.
    L'introduction de chaque partie y figure sous son propre intitulé, sans quoi
    elle ne serait atteignable que par le titre de section et passerait
    inaperçue. Une dimension qui ne compte qu'une partie est aplatie : imbriquer
    « Infrastructure » sous « Infrastructure » n'apprendrait rien au lecteur.
    """

    def part_entries(part: str, indent: str) -> list[str]:
        doc = f"{part}/index"
        entries = [f'{indent}{{ "Présentation" = "{doc}.md" }},']
        entries += [
            f'{indent}{{ "{titles[child]}" = "{child}.md" }},'
            for child in nav_entries(SRC_RST / f"{doc}.rst")
        ]
        return entries

    lines = ["nav = [", '    { "Accueil" = [', '        { "Accueil" = "index.md" },']
    for doc in HOME_TAB:
        lines.append(f'        {{ "{titles[doc]}" = "{doc}.md" }},')
    lines.append("    ] },")

    for dimension, intro, parts in DIMENSIONS:
        lines.append(f'    {{ "{dimension}" = [')
        if intro:
            lines.append(f'        {{ "Présentation" = "{intro}.md" }},')
            for part in parts:
                lines.append(f'        {{ "{titles[part + "/index"]}" = [')
                lines += part_entries(part, " " * 12)
                lines.append("        ] },")
        else:
            lines += part_entries(parts[0], " " * 8)
        lines.append("    ] },")

    lines.append("]")
    return "\n".join(lines)


def main() -> None:
    paths = rst_files()
    titles = {docname(p): title_of(p) for p in paths}

    for path in paths:
        doc = docname(path)
        text = convert_toctrees(convert(path, titles), doc, titles)
        if doc == "index":
            text = compact_metadata(text)
        target = SRC_MD / path.relative_to(SRC_RST).with_suffix(".md")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    print(f"{len(paths)} fichiers convertis dans {SRC_MD.relative_to(ROOT)}/")

    if "--nav" in sys.argv:
        print()
        print(build_nav(titles))


if __name__ == "__main__":
    main()
