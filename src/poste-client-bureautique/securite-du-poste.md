# Sécurité et confidentialité du poste

Les outils de cette section relèvent d'une logique différente de celle des sections [Sécurité](../infrastructure/securite.md) et [PKI](../infrastructure/pki.md) : il s'agit d'équiper l'utilisateur, sur son poste, contre les risques auxquels il est le premier exposé. Vol ou perte de la machine, réutilisation de mots de passe, interception d'un document en transit : ce sont ses gestes quotidiens qui sont en jeu.

C'est le domaine où l'open source présente l'avantage le plus difficile à contester. Un logiciel de chiffrement dont le code n'est pas public demande une confiance que rien ne vient étayer : seuls la publication du code et son audit par des tiers permettent de vérifier qu'il fait ce qu'il annonce et rien d'autre. Les produits ci-dessous ont pour la plupart fait l'objet d'audits indépendants publiés.

Une remarque sur la conduite du changement : ces outils ne produisent leurs effets que s'ils sont réellement utilisés. Un gestionnaire de mots de passe imposé sans formation ni reprise des mots de passe existants finit contourné. Un chiffrement de disque dont personne n'a séquestré les clés de récupération transforme une panne bénigne en perte de données définitive.

## KeePassXC

Site
: <https://keepassxc.org/>

Porteur
: une communauté

Licence
: GPL v2 et GPL v3

KeePassXC est un gestionnaire de mots de passe local : la base est un fichier chiffré que l'utilisateur maîtrise, sans service en ligne ni compte à créer.

Il gère les mots de passe, les clés SSH, les jetons d'authentification à deux facteurs (TOTP), les pièces jointes et les entrées expirantes, avec un générateur de mots de passe, une intégration aux navigateurs, un agent SSH et une base au format KDBX4, lisible par l'ensemble de la famille KeePass, y compris les clients mobiles tiers.

Son modèle convient particulièrement aux organisations qui refusent de confier leurs secrets à un service tiers : la base peut être placée sur un partage réseau ou synchronisée par les outils de l'organisation. Le partage d'équipe s'obtient par bases distinctes plutôt que par gestion centralisée des droits. C'est sa limite dans les parcs importants, où l'on adjoint au poste un coffre d'équipe centralisé : Bitwarden ou sa réimplémentation libre Vaultwarden, qui relèvent de l'infrastructure.

KeePassXC est écrit en C++ (Qt).

## GnuPG

Site
: <https://gnupg.org/>

Porteur
: une communauté

Licence
: GPL v3

GnuPG (*GNU Privacy Guard*) est l'implémentation libre de référence du standard OpenPGP : chiffrement et signature de messages et de fichiers, gestion des clés et des trousseaux, vérification de signatures.

Son rôle dépasse largement le courrier électronique : c'est GnuPG qui signe les paquets des distributions Linux, les publications des projets open source et les images système et qui permet donc de vérifier qu'un logiciel téléchargé est bien celui que son auteur a publié. À ce titre, c'est une brique d'infrastructure autant qu'un outil de poste.

Sur Windows, la distribution **Gpg4win** (<https://www.gpg4win.org/>) réunit GnuPG, le gestionnaire de clés Kleopatra et les greffons d'intégration à Outlook ; elle a été financée par l'office fédéral allemand de la sécurité des systèmes d'information, ce qui témoigne du statut de ce logiciel dans l'administration européenne.

GnuPG est écrit en C.

## Cryptomator

Site
: <https://cryptomator.org/>

Porteur
: une entreprise (Skymatic)

Licence
: GPL v3

Cryptomator répond à un besoin précis : chiffrer des fichiers *avant* qu'ils ne partent vers un espace de stockage en ligne, qu'il s'agisse d'un service commercial ou d'un Nextcloud d'entreprise.

Il crée un coffre qui se présente comme un disque ordinaire ; les fichiers y sont chiffrés individuellement, noms de fichiers compris. L'arborescence chiffrée se synchronise comme n'importe quel dossier. À la différence d'un conteneur chiffré, la synchronisation reste efficace puisque seuls les fichiers modifiés remontent ; un conteneur monolithique obligerait à retransmettre l'ensemble.

Les applications de bureau sont publiées sous licence libre ; les applications mobiles Android et iOS sont payantes, ce qui finance le développement. Le code a fait l'objet d'un audit indépendant.

Cryptomator est écrit en Java.

<span id="veracrypt"></span>

## Autres

- LUKS et l'outil cryptsetup, standard du chiffrement de disque sous Linux: <https://gitlab.com/cryptsetup/cryptsetup>
- Age, outil de chiffrement de fichiers moderne et volontairement minimal, alternative à GnuPG pour les usages simples: <https://github.com/FiloSottile/age>
- OnionShare, pour transmettre un fichier volumineux sans passer par un service tiers: <https://onionshare.org/>
- Picocrypt NG, chiffrement de fichiers à interface simplifiée, suite communautaire de Picocrypt, dont le dépôt est archivé depuis septembre 2025 (l’auteur d’origine ne la cautionne pas) : <https://github.com/Picocrypt-NG/Picocrypt-NG>
- ClamAV, pour l'analyse antivirale des fichiers (section [Sécurité](../infrastructure/securite.md)): <https://www.clamav.net>
