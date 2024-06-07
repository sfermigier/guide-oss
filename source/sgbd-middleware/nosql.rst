Big Data et NoSQL
=================

Depuis 2009, un nouveau paradigme de stockage de données - le NoSQL - est apparue. Il propose une alternative au SQL et au modèle relationnel afin de permettre un haut niveau de scalabilité, et permettre aux entreprises de toutes tailles d'exploiter au mieux le déluge de données (*big data*) qu'elles sont capables de générer ou d'acquérir.


Apache Hadoop
-------------

:Site: http://hadoop.apache.org/
:Porteur: une fondation (Apache)
:Licence: Apache 2.0

Apache Hadoop est une plateforme Java pour développer des applications distribuées autour de jeux de données massifs. Hadoop comprend un nombre significatif de sous-projets, dont les plus fondamentaux sont MapReduce, framework de calcul distribué massivement parallèle et HDFS, système de fichier distribué qui permet l'accès à haut débit à des jeux de données massifs.

Plusieurs autres projets Apache viennent compléter Hadoop, comme par exemple ZooKeeper, qui permet de coordonner la configurations des différents serveurs d'un cluster de calcul, ou Hive et Pig, qui implémentent des langages de requêtes spécifiques aux jobs MapReduce exécutés par Hadoop.

Hadoop est écrit en Java, et soutenu par plusieurs startups américaines.


MongoDB
-------

:Site: http://www.mongodb.org
:Porteur: un éditeur (MongoDB Inc)
:Licence: Affero GPL

MongoDB est une base de données "orientée documents" de la mouvance NoSQL permettant le stockage de documents au format BSON (une forme binaire de JSON).

Elle dispose de capacité à évoluer en environnement distribué via des mécanismes de réplication et de sharding. Son intégration particulièrement réussie avec la plupart des langages de programmation ainsi que sa documentation de qualité lui confèrent une popularité importante. MongoDB profite du fort regain d'intérêts pour les bases documentaires qui permettent de mieux coller aux environnements modernes qui se doivent de manipuler des données fortement hétérogènes et pour lesquels les SGBD relationnels ne sont pas nécessairement les plus adaptés.

La base de données est par ailleurs supportée par une entité commerciale, la société MongoDB Inc, cotée en bourse depuis 2017.

MongoDB est écrit en C++.


NEO
---

:Site: http://www.neoppod.org/
:Porteur: un éditeur (Nexedi)
:Licence: GPL 2.0

NEO est une base de données objet qui est la fois transactionnelle, répartie et redondante. NEO a fait l'objet d'un projet de recherche conjoint de Nexedi, Pilot Systems, l'Université de Paris 13 et l'Université de Paris 6. La cohérence transactionnelle de NEO sur un cluster de stockage réparti a ainsi pu être démontrée ce qui ouvre la voie à une application des technologes NoSQL aux systèmes de paiements et aux systèmes bancaires.

NEO est écrit en Python et en C.


Redis
-----

:Site: http://redis.io
:Porteur: un éditeur (VMware)
:Licence: BSD

Redis est un dépot de données clé/valeur issue de la mouvance NoSQL. Le projet est sponsorisé par VMware. La première version a été publiée en 2009 par Salvatore Sanfilippo et Pieter Noordhuis.

Comme la plupart des *datastores* key / value, Redis propose une interface HTTP REST. Son originalité par rapport aux autres solutions disponibles réside dans le fait que Redis dispose d'un ensemble de fonctions de manipulation de données principalement axées sur la manipulation des chaines de caractères qui sont stockées, conférant à Redis la capacité de construire des requêtes légèrement plus complexes que ses concurrents traditionnellement limités aux opérations CRUD (Create Reade Update Delete). Les bonnes performances de Redis, que ce soit en lecture ou en écriture, le positionnent comme un excellent choix pour l'implémentation de backend de cache ou de gestionnaire de session.

Redis est écrit en C.


Apache Cassandra
----------------

:Site: http://cassandra.apache.org
:Porteur: une fondation (Apache)
:Licence: Apache 2.0

Cassandra est une autre base de données de la mouvance NoSQL. Initialement développée par Facebook en 2008, elle a été par la suite libérée et son développement est aujourd'hui assuré par la fondation Apache.

Cassandra est une base de données dite "orientée colonne". Etudiée pour des déploiements massivement distribués (éventuellement sur plusieurs datacenters), Cassandra est l'une des bases les plus performantes dès lors qu'il s'agit de répondre à des problématiques de traitement de données massif. Son architecture complètement décentralisée lui confère par ailleurs une résistance à la panne très importante. Comme la plupart des bases orientées colonnes, elle est par ailleurs particulièrement adaptée aux problématiques décisionnelles.

Cassandra est écrit en Java.


CouchDB
-------

:Site: https://couchdb.apache.org/
:Porteur: une fondation (Apache)
:Licence: Apache 2.0

Apache CouchDB est une base de données NoSQL orientée documents qui utilise JSON pour le stockage des données, JavaScript pour les requêtes MapReduce et HTTP pour une API RESTful. CouchDB est conçue pour être hautement disponible et partitionnée, ce qui la rend adaptée pour des applications distribuées. CouchDB offre également des capacités de synchronisation, ce qui permet une utilisation efficace dans des environnements déconnectés.

CouchDB est écrit en Erlang.


HBase
-----

:Site: https://hbase.apache.org/
:Porteur: une fondation (Apache)
:Licence: Apache 2.0

Apache HBase est une base de données NoSQL orientée colonnes qui est construite sur le système de fichiers distribué Hadoop (HDFS). HBase est conçu pour fournir un accès aléatoire en temps réel à de grandes quantités de données structurées. Il est particulièrement utilisé pour les applications nécessitant des opérations de lecture/écriture fréquentes sur des ensembles de données volumineux. HBase est souvent comparé à Google Bigtable et est utilisé dans des environnements nécessitant une haute scalabilité et performance.

HBase est écrit en Java.


RavenDB
-------

:Site: https://ravendb.net/
:Porteur: une entreprise (Hibernating Rhinos Ltd.)
:Licence: Affero GPL

RavenDB est une base de données NoSQL orientée documents, conçue pour être facile à utiliser et à déployer. Elle offre des fonctionnalités avancées telles que l'indexation automatique, les requêtes full-text, la réplication entre nœuds, et la haute disponibilité. RavenDB propose également une API RESTful et des SDK pour plusieurs langages de programmation, ce qui facilite son intégration dans diverses applications.

RavenDB est écrit en C#.


OrientDB
--------

:Site: https://www.orientdb.org/
:Porteur: une entreprise (OrientDB Ltd.)
:Licence: Apache 2.0

OrientDB est une base de données multi-modèles qui prend en charge les modèles de données orientés graphes, documents, clé/valeur et objets. Cette polyvalence permet à OrientDB de répondre à une large gamme de besoins applicatifs. Elle est conçue pour être hautement performante et scalable, avec des fonctionnalités avancées telles que la gestion des transactions ACID, la réplication, et la sharding.

OrientDB est écrit en Java.


Neo4j
-----

:Site: https://neo4j.com/
:Porteur: une entreprise (Neo4j, Inc.)
:Licence: GNU Affero General Public License (AGPL)

Neo4j est une base de données orientée graphes, conçue pour stocker et gérer des données fortement connectées. Elle est particulièrement adaptée aux applications nécessitant une navigation et une exploration efficaces des relations entre les données, telles que les réseaux sociaux, la détection de fraudes, et la gestion de réseaux IT. Neo4j offre un langage de requête graphique appelé Cypher, qui permet de formuler des requêtes complexes de manière intuitive.

Neo4j est écrit en Java.


ArangoDB
--------

:Site: https://www.arangodb.com/
:Porteur: une entreprise (ArangoDB GmbH)
:Licence: Apache 2.0

ArangoDB est une base de données multi-modèles qui supporte les modèles de données orientés documents, graphes et clé/valeur. Cette flexibilité permet aux développeurs de travailler avec plusieurs types de données au sein d'un même moteur de base de données. ArangoDB propose un langage de requête propre, AQL, et supporte également les transactions ACID, la réplication, et le sharding. Elle est conçue pour des applications nécessitant des performances élevées et une scalabilité.

ArangoDB est écrit en C++.


JanusGraph
----------

:Site: https://janusgraph.org/
:Porteur: une fondation (The Linux Foundation)
:Licence: Apache 2.0

JanusGraph est une base de données orientée graphes distribuée et évolutive, dérivée de Titan. Elle est conçue pour la gestion de graphes massifs contenant des milliards de sommets et d'arêtes, et pour répondre aux requêtes en temps quasi réel. JanusGraph supporte plusieurs moteurs de stockage backend comme Apache Cassandra, HBase, Google Bigtable, et Oracle BerkeleyDB. Elle offre des fonctionnalités avancées telles que les transactions ACID, la réplication multi-région, et l'intégration avec des systèmes analytiques comme Hadoop et Spark.

JanusGraph est écrit en Java.
