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

MySQL est un SGBDR rapide et robuste, particulièrement déployé dans les environnements Internet. MySQL a été créé en 1995, par Michael "Monty" Widenius.

A l'origine principalement orienté vitesse et simplicité, MySQL s'est peu à peu enrichi de fonctionnalités réservées aux bases de données traditionnelles dites d'entreprise. MySQL supporte les transactions, l'intégrité référentielle, les procédures stockées, les déclencheurs, la réplication asynchrone, le clustering, la récupération des données en cas de coupure.

MySQL est sous licence GPL, assortie de la linking exception, permettant l'utilisation des bibliothèques clientes au sein de programme non compatible avec la GPL. Une version Enterprise est également disponible fournissant un certains nombre d'outils graphiques et le support de la société éditrice Oracle. MySQL est largement utilisé auprès de sociétés comme Google ou Facebook, ou auprès de sites majeurs tels que Wikipedia.

MySQL est développé en C et C++ et fonctionne sur un très large nombre de plateformes, que ce soit celles basées sous Unix (Linux, Solaris, BSD) que sous Windows.




PostgreSQL
----------

:Version: 9.0.4
:Site: www.postgresql.org
:Porteur: une communauté
:Licence: PostgreSQL License, approuvée par l'Open Source Initiative

PostgreSQL est le SGBDR open source le plus complet aujourd’hui. PostgreSQL est issue de Ingres. Le projet a été lancé en 1985 par Michael Stonebraker. La première version bâtie sur l'architecture actuelle est sortie en 1995.

Le périmètre fonctionnel de PostGreSQL est très large et comparable aux autres bases de données Entreprise du marché. Il supporte les procédures stockées, les déclencheurs, les fonctions spécifiques, indexes sur fonctions, transactions, règles customs permettant de modifier le chemin d'exécution des requêtes, un large types de données, de l'héritage de tables, de la recherche full-text, etc. Ses performances et sa stabilité lui permettent de s'intégrer à une plateforme de production exigeante.

PostgreSQL est écrit en C et fonctionne sur un très large nombre de plateformes, que ce soit celles basées sous Unix (Linux, Solaris, BSD) que sous Windows.




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
