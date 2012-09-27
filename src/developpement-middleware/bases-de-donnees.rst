Bases de données
================

Les bases de données sont devenues des éléments incontournables du paysage informatique. Elles permettent de stocker un lot d’informations dans une structure définie par avance. Les technologies actuelles permettent d'organiser et de structurer la base de données de manière à pouvoir facilement manipuler le contenu et stocker efficacement de très grandes quantités d'informations.

Les bases de données, comme MySQL ou PostgreSQL, sont de type relationnel utilisant le langage SQL pour l’interrogation de leurs données.

Depuis 2009, une nouvelle mouvance – le NoSQL – est apparue. Elle propose une alternative au SQL et au modèle relationnel afin de permettre un haut niveau de scalabilité (extensibilité).


MySQL
-----

:Version: 5.5.15
:Site: www.mysql.fr
:Porteur: un éditeur (Oracle)
:Licence: GPL avec lining exception, et propriétaire pour la version entreprise

MySQL est un SGBDR rapide et robuste, particulièrement déployé dans les environnements Internet. MySQL a été créé en 1995, par Michael "Monty" Widenius.

A l'origine principalement orienté vitesse et simplicité, MySQL s'est peu à peu enrichi de fonctionnalités réservées aux bases de données traditionnelles dites d'entreprise. MySQL supporte les transactions, l'intégrité référentielle, les procédures stockées, les déclencheurs, la réplication asynchrone, le clustering, la récupération des données en cas de coupure.

MySQL est largement utilisé auprès de sociétés comme Google ou Facebook, ou auprès de sites majeurs tels que Wikipedia.

MySQL est développé en C et C++ et fonctionne sur un très large nombre de plateformes, que ce soit celles basées sous Unix (Linux, Solaris, BSD) que sous Windows.


MariaDB
-------

:Version: 5.5
:Site: mariadb.org
:Porteur: une communauté
:Licence: GPL avec lining exception

MariaDB est un SGBDR rapide et robuste, particulièrement déployé dans les environnements Internet. MariaDB est un fork de MySQL développé par Michael "Monty" Widenius, l'auteur de MySQL, suite au rachet de MySQL par Oracle.

MariaDB comporte de nombreuses extensions par rapport à MySQL, notamment dans le domaine de l'indexation plein texte et pour le support des langues asiatiques. MariaDB comporte plusieurs moteurs de stockage à hautes performances qui ne sont pas encore présents dans MySQL.

Le mode de développement communautaire ainsi que des offres de maintenances commerciales attractives provenant de plusieurs sociétés independantes assurent à MariaDB un avenir certain.


PostgreSQL
----------

:Version: 9.2.1
:Site: www.postgresql.org
:Porteur: une communauté
:Licence: PostgreSQL License, approuvée par l'Open Source Initiative

PostgreSQL est le SGBDR open source le plus complet aujourd’hui. PostgreSQL est issue de Ingres. Le projet a été lancé en 1985 par Michael Stonebraker. La première version bâtie sur l'architecture actuelle est sortie en 1995.

Le périmètre fonctionnel de PostGreSQL est très large et comparable aux autres bases de données *entreprise* du marché. Il supporte les procédures stockées, les déclencheurs, les fonctions spécifiques, indexes sur fonctions, transactions, règles customs permettant de modifier le chemin d'exécution des requêtes, un large types de données, de l'héritage de tables, de la recherche full-text, la répartition de charge sur plusieurs bases, etc. Ses performances et sa stabilité lui permettent de s'intégrer à une plateforme de production exigeante.

PostgreSQL est écrit en C et fonctionne sur un très large nombre de plateformes, que ce soit celles basées sous Unix (Linux, Solaris, BSD) que sous Windows.

PostGIS
-------

:Version: 2.0.1
:Site: http://postgis.refractions.net/
:Porteur: une communauté
:Licence: GPL-2.0

PostGIS est la cartouche spatiale de PostgreSQL. PostGIS permet de traiter de l'information géographique dans la base de donnée PostgreSQL de la même façon que l'on traite des données alphanumériques. Cette solution implémente les standards normalisés par l'OGC et l'ISO dans ce domaine. 
De nombreuses fonctionnalités sont disponibles, permettant le traitement de géométries vectorielles, d'images raster et de topologie. Des modules additionnels offrent d'autres services, tels que pgRouting pour le calcul d'itinéraire. Les fonctionnalités de stockage et traitement d'objets 3D sont actuellement en développement.

PostGIS est aujourd'hui le standard pour les bases de données spatiales opensource. Elle est supportée par la grande majorité des outils SIG du marché. Elle est utilisée par de nombreux organismes sur des bases transactionnelles comme pour le traitement de données avancé dans des domaines d'applications variés.

MongoDB
-------

:Version: 2.2.0
:Site: http://www.mongodb.org
:Porteur: 10gen Inc
:Licence: Affero GPL

MongoDB est une base de données "orientée documents" de la mouvance NoSQL permettant le stockage de documents au format BSON (une forme binaire de JSON).

Elle dispose de capacité à évoluer en environnement distribué via des mécanismes de réplication et de sharding. Son intégration particulièrement réussie avec la plupart des langages de programmation ainsi que sa documentation de qualité lui confèrent une popularité importante. MongoDB profite du fort regain d'intérêts pour les bases documentaires qui permettent de mieux coller aux environnements modernes qui se doivent de manipuler des données fortement hétérogènes et pour lesquels les SGBD relationnels ne sont pas nécessairement les plus adaptés.

La base de données est par ailleurs supportée par une entité commerciale, la société 10gen Inc.

MongoDB est écrit en C++.

NEO
---

:Version: 1.0
:Site: http://www.neoppod.org/
:Porteur: un éditeur (Nexedi)
:Licence: GPL-2.0

NEO est une base de données NoSQL de type objet qui est la fois transactionnelle, répartie et redondante. NEO a fait l'objet dans le cadre de Systematic  d'un projet de recherche conjoint de Nexedi, Pilot Systems, l'Université de Paris 13 et l'Université de Paris 6. La cohérence transactionnelle de NEO sur un cluster de stockage réparti a ainsi pu être démontrée ce qui ouvre la voie à une application des technologes NoSQL aux systèmes de paiements et aux systèmes bancaires. 

NEO est écrit en python et en C.


Redis
-----

:Version: 2.2.13
:Site: http://redis.io
:Porteur: un éditeur (VMware)
:Licence: BSD

Redis est un dépot de données clé/valeur issue de la mouvance NoSQL. Le projet est sponsorisé par VMware. La première version a été publiée en 2009 par Salvatore Sanfilippo et Pieter Noordhuis.

Comme la plupart des datastore key / value, Redis propose une interface HTTP REST. Son originalité par rapport aux autres solutions disponibles réside dans le fait que Redis dispose d'un ensemble de fonctions de manipulation de données principalement axées sur la manipulation des chaines de caractères qui sont stockées, conférant à Redis la capacité de construire des requêtes légèrement plus complexes que ses concurrents traditionnellement limités aux opérations CRUD (Create Reade Update Delete). Les bonnes performances de Redis, que ce soit en lecture ou en écriture, le positionnent comme un excellent choix pour l'implémentation de backend de cache ou de gestionnaire de session.

Redis est écrit en C.


Apache Cassandra
----------------

:Version: 1.1.5
:Site: http://cassandra.apache.org
:Porteur: une fondation (Apache)
:Licence: Apache

Cassandra est une autre base de données de la mouvance NoSQL. Initialement développée par Facebook en 2008, elle a été par la suite libérée et son développement est aujourd'hui assuré par la fondation Apache.

Cassandra est une base de données orientée colonne. Etudiée pour des déploiements massivement distribués (éventuellement sur plusieurs datacenters), Cassandra est l'une des bases les plus performantes dès lors qu'il s'agit de répondre à des problématiques de traitement de données massif. Son architecture complètement décentralisée lui confère par ailleurs une résistance à la panne très importante. Comme la plupart des bases orientées colonnes, elle est par ailleurs particulièrement adaptée aux problématiques décisionnelles.

Cassandra est écrit en Java.


Autres
------

Parmi les produits de l’univers Base de données, on peut compléter la liste avec les outils ci-dessous :



Nom	URL / Site web

Berkeley DB	http://www.oracle.com/us/products/database/berkeley-db

db4o	http://www.db4o.com

Apache Derby	http://db.apache.org/derby

FireBird	http://www.firebirdsql.org

HSQLDB	http://hsqldb.org

Ingres	http://www.ingres.com/products/ingres-database

SQLite	http://www.sqlite.org

CouchDB	http://couchdb.apache.org

Neo4j	http://neo4j.org

Voldemort	http://www.project-voldemort.com
