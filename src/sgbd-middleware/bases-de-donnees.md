# Bases de données relationnelles

Les bases de données sont devenues des éléments centraux du paysage informatique. Elles permettent de stocker un lot d’informations dans une structure définie par avance. Les technologies actuelles permettent d'organiser et de structurer la base de données de manière à pouvoir facilement manipuler le contenu et stocker efficacement de très grandes quantités d'informations.

Les bases de données traditionnelles, comme MySQL ou PostgreSQL, sont de type relationnel et utilisent le langage SQL pour l’interrogation de leurs données.

## PostgreSQL

Site
: <https://www.postgresql.org/>

Porteur
: une communauté

Licence
: PostgreSQL License, approuvée par l'Open Source Initiative

PostgreSQL est le SGBDR open source le plus complet aujourd’hui. PostgreSQL est issue de Ingres, un projet lancé en 1985 par Michael Stonebraker. La première version bâtie sur l'architecture actuelle est sortie en 1995.

Le périmètre fonctionnel de PostgreSQL est très large et comparable à celui des autres bases de données *entreprise* du marché : procédures stockées, déclencheurs, fonctions définies par l'utilisateur, index sur expressions, transactions, large éventail de types de données (dont JSONB), héritage de tables et partitionnement déclaratif, recherche plein texte, réplication physique et logique, etc. Ses performances et sa stabilité lui permettent de s'intégrer à une plateforme de production exigeante.

Son autre grande force est son système d'extensions, qui lui permet de couvrir des besoins généralement dévolus à des moteurs spécialisés : PostGIS pour l'information géographique (voir ci-dessous), TimescaleDB pour les séries temporelles, pgvector pour la recherche vectorielle et les applications d'IA, Citus pour la distribution. PostgreSQL est aujourd'hui, de l'avis général, le choix par défaut pour un nouveau projet.

PostgreSQL est écrit en C et fonctionne sur un très grand nombre de plateformes Unix (Linux, Solaris, BSD) ou Windows.

## MySQL

Site
: <https://www.mysql.com/>

Porteur
: un éditeur (Oracle)

Licence
: GPL v2 avec *linking exception* et propriétaire pour l'édition Enterprise

MySQL est un SGBDR rapide et robuste, particulièrement déployé dans les environnements Internet. MySQL a été créé en 1995, par Michael "Monty" Widenius.

À l'origine principalement orienté vitesse et simplicité, MySQL s'est peu à peu enrichi de fonctionnalités réservées aux bases de données traditionnelles dites d'entreprise. MySQL gère les transactions, l'intégrité référentielle, les procédures stockées, les déclencheurs, la réplication asynchrone, le clustering, la récupération des données en cas de coupure.

MySQL reste très largement déployé, notamment comme socle des applications PHP (WordPress, Drupal, PrestaShop…). Depuis le rachat de Sun par Oracle en 2010, une partie de l'écosystème communautaire s'est toutefois reportée sur MariaDB. Plusieurs distributions Linux ont fait de cette dernière leur base par défaut.

MySQL est développé en C et C++ et fonctionne sur un très large nombre de plateformes, que ce soit sous Unix (Linux, Solaris, BSD) ou sous Windows.

## MariaDB

Site
: <https://mariadb.org/>

Porteur
: une fondation (MariaDB Foundation) et un éditeur (MariaDB plc)

Licence
: GPL v2

MariaDB est un SGBDR rapide et robuste, particulièrement déployé dans les environnements Internet. MariaDB est un fork de MySQL développé par Michael "Monty" Widenius, l'auteur de MySQL, suite au rachet de MySQL par Oracle.

MariaDB comporte de nombreuses extensions par rapport à MySQL, notamment dans le domaine de l'indexation plein texte et pour le support des langues asiatiques. MariaDB comporte plusieurs moteurs de stockage qui ne sont pas encore présents dans MySQL.

La gouvernance est partagée entre la MariaDB Foundation (qui garantit l'ouverture du projet) et la société MariaDB plc, qui en assure l'essentiel du développement et commercialise support et services. MariaDB est la base par défaut de plusieurs distributions Linux majeures. Les deux moteurs, MySQL et MariaDB, ont par ailleurs progressivement divergé : la compatibilité n'est plus totale, en particulier sur les fonctions récentes.

## CUBRID

Site
: <https://www.cubrid.org/>

Porteur
: une fondation (CUBRID Foundation)

Licence
: Apache 2.0 pour le moteur, BSD pour les connecteurs

CUBRID est une base de données relationnelle développée à l'origine par le groupe coréen Naver pour remplacer une base propriétaire. Elle propose la haute disponibilité, des procédures stockées en Java et une compatibilité SQL étendue ; son adoption reste essentiellement coréenne.

## PostGIS

Site
: <https://postgis.net/>

Porteur
: une communauté (OSGeo)

Licence
: GPL v2+

PostGIS est la cartouche spatiale de PostgreSQL. PostGIS permet de traiter de l'information géographique dans la base de données PostgreSQL de la même façon que l'on traite des données alphanumériques. Cette solution implémente les standards normalisés par l'OGC et l'ISO dans ce domaine.

De nombreuses fonctionnalités sont disponibles, permettant le traitement de géométries vectorielles, d'images raster, de topologie et d'objets 3D. Des modules additionnels offrent d'autres services, tels que pgRouting pour le calcul d'itinéraires.

PostGIS est aujourd'hui le standard pour les bases de données spatiales open source. Elle est prise en charge par la grande majorité des outils SIG du marché. Elle est utilisée par de nombreux organismes sur des bases transactionnelles comme pour le traitement de données avancé dans des domaines d'applications variés.

## SQLite

Site
: <https://www.sqlite.org>

Porteur
: un consortium (SQLite Consortium)

Licence
: domaine public

SQLite est une bibliothèque qui met en œuvre un moteur SQL complet dans un simple fichier, sans serveur. Créée en 2000 par D. Richard Hipp, elle est présente dans les navigateurs, les téléphones et une grande partie des applications de bureau.

Elle convient au stockage local d'une application, à l'échange de jeux de données et à des sites web modestes : aucune administration, transactions fiables, sauvegarde par simple copie encadrée. Un seul processus peut écrire à un instant donné. Les fichiers ne doivent pas être partagés sur un système de fichiers réseau. Au-delà, on choisira PostgreSQL ou MariaDB.

Le code est dans le domaine public, mais le projet est peu ouvert aux contributions extérieures. Son financement passe par les membres d'un consortium et par la vente de support.

SQLite est écrit en C.

## DuckDB

Site
: <https://duckdb.org/>

Porteur
: une fondation (DuckDB Foundation)

Licence
: MIT

DuckDB est un moteur SQL analytique embarqué, né au centre de recherche néerlandais CWI. Il s'exécute dans le processus de l'application, comme SQLite, mais stocke et traite les données par colonnes.

Il interroge directement des fichiers Parquet, CSV ou JSON, locaux ou sur un stockage objet, ainsi que des tableaux pandas ou Arrow. Il sert à l'analyse exploratoire, aux chaînes de préparation de données et aux traitements qui tiennent sur une machine, en évitant souvent le déploiement d'un cluster. Il n'est pas prévu pour un usage transactionnel concurrent.

La DuckDB Foundation, association à but non lucratif, détient la propriété intellectuelle du projet et garantit sa licence. La société de ses auteurs, DuckLabs, a rejoint Amazon Web Services en 2026 : la place de ce nouvel acteur dans la feuille de route est à suivre.

DuckDB est écrit en C++.

<span id="firebird"></span>

## Autres

Parmi les produits de l’univers Base de données relationnelles (et incidemment, objets ou clef/valeur), on peut compléter la liste avec les outils ci-dessous :

### Bases SQL embarquées

- Apache Derby: <https://db.apache.org/derby>

### Bases clefs-valeurs embarquées

- Berkeley DB: <https://www.oracle.com/us/products/database/berkeley-db>
- LevelDB: <https://github.com/google/leveldb>
- LMDB: <https://symas.com/lmdb/>
- Tarantool: <https://www.tarantool.io/en/>
- RocksDB: <https://rocksdb.org/>

### Autres bases SQL

- HSQLDB: <https://hsqldb.org/>
