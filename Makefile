# Guide des solutions libres et open source.
#
# Les sources sont en reStructuredText dans source/. rst_to_md.py les convertit
# en Markdown dans src/, et Zensical construit le site statique dans site/.

.PHONY: all build serve convert nav clean deploy

all: build

# source/**/*.rst -> src/**/*.md
convert:
	uv run rst_to_md.py

# Site statique complet dans site/
build: convert
	uvx zensical build

# Aperçu local sur http://localhost:8000
serve: convert
	uvx zensical serve

# Régénère le sommaire (`nav`) à recopier dans zensical.toml, à faire après
# tout ajout, retrait ou déplacement de page dans les toctrees.
nav:
	uv run rst_to_md.py --nav

clean:
	rm -rf site

# Production : Hop3 sert site/ sur guide-solutions-opensource.com.
deploy: build
	hop3 deploy --app guide-oss
