# Guide des solutions libres et open source.
#
# Les sources sont en Markdown dans src/. Zensical construit le site statique
# dans site/, que Hop3 sert en production.

.PHONY: all build serve clean deploy

all: build deploy

# Site statique complet dans site/
build:
	uvx zensical build

# Aperçu local sur http://localhost:8000
serve:
	uvx zensical serve

clean:
	rm -rf site

# Production : Hop3 sert site/ sur guide-solutions-opensource.com.
deploy: build
	hop3 deploy --app guide-oss
