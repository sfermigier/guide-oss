# Big data et NoSQL

À partir de 2009, un nouveau paradigme de stockage de données, le NoSQL, est apparu. Il proposait une alternative au SQL et au modèle relationnel afin de permettre un haut niveau de scalabilité et de traiter les volumes de données (*big data*) que les entreprises génèrent ou acquièrent.

Quinze ans plus tard, le paysage s'est stabilisé et partiellement rééquilibré. D'un côté, les bases relationnelles ont absorbé une bonne partie des apports du NoSQL (types JSON, réplication, partitionnement, extensions vectorielles), au point que PostgreSQL suffit à couvrir bien des besoins pour lesquels on aurait choisi une base NoSQL en 2012. De l'autre, les usages qui justifient réellement un moteur spécialisé se sont clarifiés : très gros volumes distribués (Cassandra), analytique temps réel (ClickHouse), graphes (Neo4j), cache et files d'attente (Redis, Valkey), recherche (Elasticsearch, OpenSearch, voir la section [Moteurs de recherche](../web-communication/moteurs-de-recherche.md)), recherche vectorielle pour l'IA (Qdrant, Weaviate).

Les licences constituent un dernier point d'attention, devenu central sur cette catégorie. Plusieurs éditeurs de bases NoSQL ont abandonné les licences libres au profit de licences dites *source-available* (SSPL, BSL), parfois suivies de forks communautaires. Ces produits ne figurent pas dans le guide ; les fiches ci-dessous signalent les changements de licence des autres.

## Apache Hadoop

Site
: <https://hadoop.apache.org/>

Porteur
: une fondation (Apache)

Licence
: Apache 2.0

Apache Hadoop est une plateforme Java pour développer des applications distribuées autour de jeux de données massifs. Hadoop comprend un nombre significatif de sous-projets, dont les plus fondamentaux sont MapReduce (framework de calcul distribué massivement parallèle) et HDFS, système de fichiers distribué qui permet l'accès à haut débit à des jeux de données massifs.

Plusieurs autres projets Apache viennent compléter Hadoop, comme ZooKeeper, qui coordonne la configuration des différents serveurs d'un cluster, ou Hive, qui expose les données sous forme de tables interrogeables en SQL.

Il faut toutefois mesurer le recul de cet écosystème : MapReduce a été supplanté par Apache Spark, HDFS par le stockage objet compatible S3 (Ceph, Garage, SeaweedFS ou les offres des fournisseurs de cloud). La consolidation du marché (fusion de Cloudera et Hortonworks, disparition de MapR) a tari une bonne partie de son élan. Les architectures actuelles combinent plutôt un stockage objet, des formats de tables ouverts (Apache Iceberg, Delta Lake) et des moteurs de requête comme Spark, Trino ou DuckDB. Hadoop reste pertinent pour les plateformes déjà en place et pour certains traitements par lots de très grande ampleur.

Hadoop est écrit en Java.

## Apache Spark

Site
: <https://spark.apache.org/>

Porteur
: une fondation (Apache)

Licence
: Apache 2.0

Né en 2009 à l'université de Berkeley, confié à la fondation Apache en 2013, Spark est devenu le moteur de traitement de données distribué de référence, en remplacement de MapReduce dont il corrige le principal défaut : les traitements s'exécutent en mémoire, avec des gains d'un ordre de grandeur sur les charges itératives.

Spark propose une API unifiée pour le traitement par lots et en flux (*Structured Streaming*), en Scala, Java, Python (PySpark) et R, ainsi qu'un moteur SQL, une bibliothèque d'apprentissage automatique (MLlib) et un module de traitement de graphes. Il s'exécute indifféremment sur Kubernetes, YARN ou en local et lit la plupart des sources de données, y compris les formats de tables ouverts (Iceberg, Delta Lake, Hudi).

Spark est écrit en Scala.

## FerretDB

<span id="mongodb"></span>

Site
: <https://github.com/FerretDB/FerretDB>

Porteur
: une entreprise (FerretDB Inc.)

Licence
: Apache 2.0

FerretDB est une base de données orientée documents qui met en œuvre le protocole de MongoDB au-dessus de PostgreSQL. Les pilotes et outils prévus pour ce protocole peuvent donc s'y connecter, dans la limite des commandes prises en charge : la compatibilité se teste sur l'application réelle.

FerretDB est écrit en Go.

## NEO

Site
: <https://neo.nexedi.com/>

Porteur
: un éditeur (Nexedi)

Licence
: GPL 2.0

NEO est un moteur de stockage transactionnel, réparti et redondant pour ZODB, la base d'objets Python. Issu d'un projet de recherche mené par Nexedi avec Pilot Systems et les universités Paris 13 et Paris 6, il est toujours développé par Nexedi, principalement pour ses propres besoins autour d'ERP5. En dehors de cet écosystème, son usage est confidentiel.

## Redis

Site
: <https://redis.io>

Porteur
: un éditeur (Redis Ltd)

Licence
: AGPL v3, RSALv2 ou SSPLv1 au choix, depuis Redis 8 (2025)

Redis est un entrepôt de données clé-valeur en mémoire, issu de la mouvance NoSQL. La première version a été publiée en 2009 par Salvatore Sanfilippo.

Son originalité tient à la richesse de ses structures de données (chaînes, listes, ensembles, ensembles ordonnés, tables de hachage, flux, compteurs probabilistes), qui lui permettent d'aller bien au-delà des opérations CRUD des autres entrepôts clé-valeur. On y accède par un protocole binaire simple (RESP) et non par HTTP. Ses excellentes performances en lecture comme en écriture en font le choix par défaut pour un cache, un magasin de sessions, une file d'attente de travaux ou un système de publication/abonnement.

Attention à l'histoire mouvementée de sa licence : Redis a quitté la licence BSD en mars 2024 pour un double modèle RSALv2 / SSPLv1, non reconnu comme libre. La Linux Foundation a aussitôt lancé **Valkey** (<https://valkey.io/>), fork de Redis 7.2.4 resté sous licence BSD, soutenu par AWS, Google Cloud, Oracle et Ericsson et adopté depuis par la plupart des distributions Linux. Redis Ltd a partiellement corrigé le tir en ajoutant l'AGPL v3 comme troisième option à partir de Redis 8 (mai 2025). Les deux projets coexistent désormais, avec une compatibilité qui devrait s'éroder au fil des versions.

Redis est écrit en C.

## Apache Cassandra

Site
: <https://cassandra.apache.org>

Porteur
: une fondation (Apache)

Licence
: Apache 2.0

Cassandra est une autre base de données de la mouvance NoSQL. Initialement développée par Facebook en 2008, elle a été par la suite libérée et son développement est aujourd'hui assuré par la fondation Apache.

Cassandra est une base dite « orientée colonnes » au sens des familles de colonnes (*wide column*). Son architecture sans maître, éventuellement répartie sur plusieurs centres de données, lui donne une bonne résistance aux pannes et des débits d'écriture élevés. Les tables se conçoivent à partir des requêtes à servir. Elle n'est pas faite pour le décisionnel : les agrégations et requêtes ad hoc relèvent d'un moteur analytique à stockage en colonnes comme ClickHouse, ou de Spark au-dessus de Cassandra.

Cassandra est écrit en Java.

## CouchDB

Site
: <https://couchdb.apache.org/>

Porteur
: une fondation (Apache)

Licence
: Apache 2.0

Apache CouchDB est une base de données NoSQL orientée documents qui utilise JSON pour le stockage des données, JavaScript pour les requêtes MapReduce et HTTP pour une API RESTful. CouchDB est conçue pour être hautement disponible et partitionnée, ce qui la rend adaptée pour des applications distribuées. CouchDB offre également des capacités de synchronisation, ce qui permet une utilisation efficace dans des environnements déconnectés.

CouchDB est écrit en Erlang.

## HBase

Site
: <https://hbase.apache.org/>

Porteur
: une fondation (Apache)

Licence
: Apache 2.0

Apache HBase est une base de données NoSQL orientée colonnes qui est construite sur le système de fichiers distribué Hadoop (HDFS). HBase est conçu pour fournir un accès aléatoire en temps réel à de grandes quantités de données structurées. Il est particulièrement utilisé pour les applications nécessitant des opérations de lecture/écriture fréquentes sur des ensembles de données volumineux. HBase est souvent comparé à Google Bigtable et est utilisé dans des environnements nécessitant une haute scalabilité et performance.

HBase est écrit en Java.

## RavenDB

Site
: <https://ravendb.net/>

Porteur
: un éditeur (RavenDB Ltd)

Licence
: AGPL v3 ou commerciale

RavenDB est une base documentaire écrite en C#, surtout utilisée dans l'écosystème .NET : transactions ACID, indexation automatique, recherche plein texte et réplication. Le serveur est proposé, au choix, sous AGPL v3 ou sous une licence commerciale (les bibliothèques clientes sont sous MIT) ; son contrat d'utilisation combine les deux régimes et doit être lu avant tout déploiement. Sa diffusion est restreinte.

## OrientDB

Site
: <https://orientdb.dev/>

Porteur
: une communauté

Licence
: Apache 2.0

Développée à l'origine par OrientDB Ltd, rachetée depuis par SAP, OrientDB est une base de données multi-modèles qui prend en charge les modèles de données orientés graphes, documents, clé/valeur et objets. Cette polyvalence permet à OrientDB de répondre à une large gamme de besoins applicatifs. Elle est conçue pour être hautement performante et scalable, avec des fonctionnalités avancées telles que la gestion des transactions ACID, la réplication et le sharding.

OrientDB est écrit en Java.

## Neo4j

Site
: <https://neo4j.com/>

Porteur
: un éditeur (Neo4j, Inc.)

Licence
: GPL v3 (Community Edition), propriétaire (Enterprise Edition)

Neo4j est une base de données orientée graphes, conçue pour stocker et gérer des données fortement connectées. Elle est particulièrement adaptée aux applications nécessitant une navigation et une exploration efficaces des relations entre les données, telles que les réseaux sociaux, la détection de fraudes et la gestion de réseaux IT. Neo4j offre un langage de requête graphique appelé Cypher, qui permet de formuler des requêtes complexes de manière intuitive.

Neo4j est écrit en Java.

## JanusGraph

Site
: <https://janusgraph.org/>

Porteur
: une fondation (The Linux Foundation)

Licence
: Apache 2.0

JanusGraph est une base de données orientée graphes distribuée et évolutive, dérivée de Titan. Elle est conçue pour la gestion de graphes massifs contenant des milliards de sommets et d'arêtes et pour répondre aux requêtes en temps quasi réel. JanusGraph s'appuie sur plusieurs moteurs de stockage comme Apache Cassandra, HBase, Google Bigtable et Oracle BerkeleyDB. Elle offre des fonctionnalités avancées telles que les transactions ACID, la réplication multi-région et l'intégration avec des systèmes analytiques comme Hadoop et Spark.

JanusGraph est écrit en Java.

## ClickHouse

Site
: <https://clickhouse.com/>

Porteur
: une entreprise (ClickHouse, Inc.)

Licence
: Apache 2.0

Développée à l'origine chez Yandex pour ses besoins d'analyse d'audience et publiée en 2016, ClickHouse est une base de données orientée colonnes conçue pour l'analytique temps réel sur de très gros volumes.

Ses performances sur les requêtes d'agrégation, souvent supérieures d'un ou deux ordres de grandeur à celles des moteurs relationnels classiques, en ont fait le choix de référence pour les entrepôts analytiques, l'exploitation de journaux, l'observabilité et les tableaux de bord temps réel. Elle est compatible SQL, se déploie aussi bien sur une seule machine que sur un cluster et lit directement des données stockées en objet (S3, Parquet).

ClickHouse est écrit en C++.

<span id="arangodb"></span>
