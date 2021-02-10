Bases de données relationnelles
===============================

Les bases de données sont devenues des éléments incontournables du paysage informatique. Elles permettent de stocker un lot d’informations dans une structure définie par avance. Les technologies actuelles permettent d'organiser et de structurer la base de données de manière à pouvoir facilement manipuler le contenu et stocker efficacement de très grandes quantités d'informations.

Les bases de données traditionnelles, comme MySQL ou PostgreSQL, sont de type relationnel et utilisent le langage SQL pour l’interrogation de leurs données.


PostgreSQL
----------

:Site: www.postgresql.org
:Porteur: une communauté
:Licence: PostgreSQL License, approuvée par l'Open Source Initiative

PostgreSQL est le SGBDR open source le plus complet aujourd’hui. PostgreSQL est issue de Ingres. Le projet a été lancé en 1985 par Michael Stonebraker. La première version bâtie sur l'architecture actuelle est sortie en 1995.

Le périmètre fonctionnel de PostGreSQL est très large et comparable aux autres bases de données *entreprise* du marché. Il supporte les procédures stockées, les déclencheurs, les fonctions spécifiques, les indexes sur fonctions, les transactions, les règles customs permettant de modifier le chemin d'exécution des requêtes, un large éventail de types de données, de l'héritage de tables, de la recherche full-text, la répartition de charge sur plusieurs bases, etc. Ses performances et sa stabilité lui permettent de s'intégrer à une plateforme de production exigeante.

PostgreSQL est écrit en C et fonctionne sur un très grand nombre de plateformes Unix (Linux, Solaris, BSD) ou Windows.


MySQL
-----

:Site: www.mysql.fr
:Porteur: un éditeur (Oracle)
:Licence: GPL avec lining exception, et propriétaire pour la version entreprise

MySQL est un SGBDR rapide et robuste, particulièrement déployé dans les environnements Internet. MySQL a été créé en 1995, par Michael "Monty" Widenius.

A l'origine principalement orienté vitesse et simplicité, MySQL s'est peu à peu enrichi de fonctionnalités réservées aux bases de données traditionnelles dites d'entreprise. MySQL supporte les transactions, l'intégrité référentielle, les procédures stockées, les déclencheurs, la réplication asynchrone, le clustering, la récupération des données en cas de coupure.

MySQL est largement utilisé auprès de sociétés comme Google ou Facebook, ou auprès de sites majeurs tels que Wikipedia.

MySQL est développé en C et C++ et fonctionne sur un très large nombre de plateformes, que ce soit celles basées sous Unix (Linux, Solaris, BSD) que sous Windows.


MariaDB
-------

:Site: mariadb.org
:Porteur: une communauté
:Licence: GPL avec lining exception

MariaDB est un SGBDR rapide et robuste, particulièrement déployé dans les environnements Internet. MariaDB est un fork de MySQL développé par Michael "Monty" Widenius, l'auteur de MySQL, suite au rachet de MySQL par Oracle.

MariaDB comporte de nombreuses extensions par rapport à MySQL, notamment dans le domaine de l'indexation plein texte et pour le support des langues asiatiques. MariaDB comporte plusieurs moteurs de stockage à hautes performances qui ne sont pas encore présents dans MySQL.

Le mode de développement communautaire ainsi que des offres de maintenances commerciales attractives provenant de plusieurs sociétés independantes assurent à MariaDB un avenir certain.


Cubrid
------

:Site: www.cubrid.org
:Porteur: un éditeur (Naver)
:Licence: GPL

Cubrid est une base de données relationnelle développée par le géant coréen de l'Internet Naver. Cubrid a été conçu par Naver pour remplacer une base de données propriétaire très connue et propulser toutes ses applications de réseaux sociaux, dont le plus grand réseau social de gamers.

Cubrid a la particularité de tenir la charge grâce à une version clusterisée et de d'utiliser Java comme langage procédural à la place de PL/SQL. Cubrid a été optimisée pour les architectures à base de disques SSD.


PostGIS
-------

:Site: http://postgis.refractions.net/
:Porteur: une communauté
:Licence: GPL-2.0

PostGIS est la cartouche spatiale de PostgreSQL. PostGIS permet de traiter de l'information géographique dans la base de donnée PostgreSQL de la même façon que l'on traite des données alphanumériques. Cette solution implémente les standards normalisés par l'OGC et l'ISO dans ce domaine.

De nombreuses fonctionnalités sont disponibles, permettant le traitement de géométries vectorielles, d'images raster et de topologie. Des modules additionnels offrent d'autres services, tels que pgRouting pour le calcul d'itinéraire. Les fonctionnalités de stockage et traitement d'objets 3D sont actuellement en développement.

PostGIS est aujourd'hui le standard pour les bases de données spatiales open source. Elle est supportée par la grande majorité des outils SIG du marché. Elle est utilisée par de nombreux organismes sur des bases transactionnelles comme pour le traitement de données avancé dans des domaines d'applications variés.


Autres
------

Parmi les produits de l’univers Base de données relationnelles (et incidemment, objets ou clef/valeur), on peut compléter la liste avec les outils ci-dessous :

- Berkeley DB:	http://www.oracle.com/us/products/database/berkeley-db

- db4o:	http://www.db4o.com

- Apache Derby:	http://db.apache.org/derby

- FireBird:	http://www.firebirdsql.org

- HSQLDB:	http://hsqldb.org

- SQLite:	http://www.sqlite.org
