# Bases de données et middleware { #bases-de-donnees-tous-types-et-middleware }

Cette partie réunit les moteurs qui conservent les données et les couches qui font dialoguer les applications : bases relationnelles, bases NoSQL et analytiques, moteurs de recherche, bus de services, middlewares de messages, moteurs de processus et serveurs d'applications.

Ce sont les fondations : ce que l'on installe en premier, ce que l'on remplace en dernier et ce dont le choix engage le plus longtemps. Une application se réécrit en deux ans ; une base de données de production accompagne une organisation pendant quinze.

Trois évolutions ont profondément remodelé ce paysage depuis la précédente édition de ce guide.

**PostgreSQL est devenu le choix par défaut.** Longtemps réputé austère face à la simplicité de MySQL, il a absorbé l'essentiel de ce qui justifiait le recours à des moteurs spécialisés : type JSON natif, recherche plein texte, partitionnement, réplication logique et un système d'extensions qui lui ajoute l'information géographique (PostGIS), les séries temporelles (TimescaleDB) ou la recherche vectorielle (pgvector). Pour un nouveau projet, la question raisonnable est devenue « pourquoi pas PostgreSQL ? » plutôt que l'inverse.

**Les licences se sont durcies.** Redis, MongoDB, Elasticsearch, ArangoDB ont quitté les licences libres pour des licences dites « source-available », déclenchant chaque fois un fork communautaire (Valkey, OpenSearch) et obligeant leurs utilisateurs à arbitrer. Les produits qui ne sont pas revenus à une licence libre ne figurent plus dans ce guide ; la licence est devenu le premier critère d'instruction d'un projet, avant même les performances.

**L'intégration a changé de forme.** Le bus de services centralisé des années 2000 a cédé la place à deux approches : la bibliothèque d'intégration embarquée dans l'application (Apache Camel en est le représentant) et l'architecture événementielle bâtie sur un journal distribué, dont Apache Kafka est devenu le standard. Symétriquement, le serveur d'applications JEE dans lequel on déployait des archives a reculé devant l'application autonome embarquant son propre serveur, popularisée par Spring Boot.

Un dernier point, enfin : c'est dans cette partie que se mesure la **réversibilité** d'un système d'information. Un schéma documenté, des exports exploitables et des formats ouverts valent, le jour d'une migration, tous les engagements commerciaux.

- [Bases de données relationnelles](bases-de-donnees.md)
- [Big data et NoSQL](nosql.md)
- [Moteurs de recherche](../web-communication/moteurs-de-recherche.md)
- [ESB](esb.md)
- [MOM et EAI](mom-eai.md)
- [BPM et workflow](bpm-workflow.md)
- [Serveurs d’applications](serveurs-applications.md)
