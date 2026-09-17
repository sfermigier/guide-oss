Moteurs de recherche
====================

Les moteurs de recherche sont, comme les systèmes d’exploitation et les bases de données, des pierres angulaires de notre quotidien.

Ils permettent de retrouver et d’accéder à des ressources (au sens large : pages web, images, vidéos, fichiers, etc.) indexées avec un ensemble de mots clés.

Les moteurs de recherche sont généralement composés de deux services : l’indexation et la  recherche.

Les moteurs de recherche se différencient généralement par leurs capacités d’indexation (format, rapidité, algorithme de pertinence) et leurs fonctions de traitements linguistiques (pluriels, conjugaisons, phonétique, etc.).

Dans l’univers de l’open source, tout ou presque repose sur la bibliothèque Apache Lucene, soit directement, soit à travers les serveurs qui l’encapsulent : Apache Solr, Elasticsearch et OpenSearch. Depuis quelques années, des moteurs légers et orientés « recherche instantanée » (Meilisearch, Typesense) et des bases vectorielles destinées à la recherche sémantique et aux applications d’IA générative (Qdrant, Weaviate, Vespa) complètent ce paysage.

Apache Lucene
-------------

:Site: https://lucene.apache.org/
:Porteur: une fondation (Apache)
:Licence: Apache 2.0

Porté par la fondation Apache, Lucene est le socle d'indexation et de recherche sur lequel sont bâtis Solr, Elasticsearch et OpenSearch, et donc, indirectement, l'essentiel des moteurs de recherche d'entreprise du marché, y compris celui de Wikipédia. Créé par Doug Cutting en 2000, il reste l'outil de recherche le plus utilisé et le plus actif de l'open source.

Lucene se définit avant tout comme une bibliothèque de recherche et d'indexation de contenus. Comme la plupart des moteurs de recherche, Lucene repose sur le concept de l’indexation automatique, c'est-à-dire en traitant une seule fois les données d’entrée et en leur donnant de multiples liens. Coté fonctionnel, Lucene support la recherche de formes approximatives d'un même mot (féminin, pluriel, conjugaison), la gestion des synonymes, la pertinence paramétrable, etc. Le tout avec un niveau de performances exceptionnels.

Lucene est écrit en Java. Il peut être intégré au sein d’applications écrites dans différents langages : Java, Python, Ruby, Perl, PHP, C++, etc.


Apache Solr
-----------

:Site: https://solr.apache.org/
:Porteur: une fondation (Apache)
:Licence: Apache 2.0

Solr est une surcouche de Lucene qui ajoute des fonctionnalités et facilite le déploiement de certaines fonctions de Lucene reconnues comme trop techniques. Son développement a été initié par CNET Networks, qui a décidé en 2006 de publier son travail ; Solr est devenu en 2021 un projet de haut niveau de la fondation Apache, distinct de Lucene.

Le mode SolrCloud assure la distribution et la réplication des index sur un cluster. Solr reste très présent comme moteur d'indexation de solutions de GED et de CMS (Alfresco, Nuxeo, Ibexa, Drupal).

Solr est un serveur de recherche d'entreprise, qui centralise l'indexation et la restitution des résultats. Solr est capable de communiquer avec les autres applications via de nombreux protocoles fondés sur des standards ouverts, il dispose également d’une interface d’administration en mode Web. L’une des caractéristiques majeures de Lucene est la capacité à indexer les contenus par champ, ou par attribut, c’est à dire qu’un document n’est pas analysé comme un simple ensemble de mots, il est constitué de champs, chaque champ étant une suite de mots (terms). Solr permet de tirer pleinement parti de cette fonctionnalité. Ce fonctionnement permet une gestion beaucoup plus fine de la pertinence, et de la recherche avancée.


Elasticsearch
-------------

:Site: https://www.elastic.co/elasticsearch
:Porteur: un éditeur (Elastic)
:Licence: AGPL v3, SSPL ou Elastic License, au choix de l'utilisateur

Créé en 2010 par Shay Banon sur la base de Lucene, Elasticsearch s'est imposé comme le moteur de recherche et d'analyse distribué le plus déployé du marché, aussi bien pour la recherche applicative que pour l'exploitation de journaux et la métrologie (au sein de la « suite Elastic » avec Kibana, Beats et Logstash).

Ses atouts sont la distribution et la réplication natives, une API REST/JSON simple, des capacités d'agrégation, et, depuis les versions récentes, la recherche vectorielle et hybride.

Le point d'attention porte sur la licence, qui a beaucoup varié : publié sous Apache 2.0 jusqu'en 2021, Elasticsearch est passé à un double modèle SSPL / Elastic License (deux licences non reconnues comme libres par l'*Open Source Initiative*), ce qui a provoqué le fork OpenSearch par AWS. L'éditeur a ajouté en septembre 2024 l'AGPL v3 comme troisième option, ce qui redonne au produit le statut de logiciel libre.

Elasticsearch est écrit en Java.


OpenSearch
----------

:Site: https://opensearch.org/
:Porteur: une fondation (Linux Foundation)
:Licence: Apache 2.0

OpenSearch est le fork d'Elasticsearch 7.10 et de Kibana réalisé par Amazon Web Services en 2021, à la suite du changement de licence d'Elastic, afin de disposer d'un moteur équivalent sous licence Apache 2.0.

Le projet a rattrapé puis dépassé sur certains points son point de départ : tableaux de bord (OpenSearch Dashboards), sécurité intégrée, recherche vectorielle et *machine learning*, observabilité. AWS l'a placé en septembre 2024 sous la gouvernance de la Linux Foundation (OpenSearch Software Foundation), ce qui répond à la principale critique adressée au projet, celle d'un contrôle par un acteur unique.

OpenSearch est écrit en Java.


Autres
------

Parmi les produits de l’univers Moteurs de recherche, on peut compléter la liste avec les outils ci-dessous :

- Meilisearch (moteur léger orienté « recherche instantanée », éditeur français): https://www.meilisearch.com/
- Typesense (moteur léger, alternative à Algolia): https://typesense.org/
- Qdrant (base vectorielle pour la recherche sémantique et le RAG): https://qdrant.tech/
- Weaviate (base vectorielle): https://weaviate.io/
- Vespa (moteur de recherche et de recommandation à grande échelle): https://vespa.ai/
- Manticore Search (fork libre et maintenu de Sphinx, dont les versions récentes ne sont plus open source): https://manticoresearch.com/
- Xapian (bibliothèque d'indexation C++): https://xapian.org/
- Apache Nutch (robot d'indexation web): https://nutch.apache.org/
- Apache Tika, utilisé par la plupart de ces moteurs pour extraire le texte des documents bureautiques: https://tika.apache.org/

OpenSearchServer, présenté dans les éditions précédentes de ce guide, n'est plus maintenu (son site n'est plus en service et son dépôt est à l'arrêt depuis 2022) ; la bibliothèque Python Whoosh, également citée, est dans le même cas.

