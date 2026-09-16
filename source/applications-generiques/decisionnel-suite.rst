Décisionnel : Suite
===================

Les suites décisionnelles regroupent généralement les deux catégories présentées précédemment ; c'est-à-dire l’ETL et le reporting.

Ainsi, le périmètre des suites décisionnelles est très vaste : exécution des rapports, analyse OLAP, aide à la création de requêtes, ETL, module de gestion du workflow de publication, etc..


Metabase
--------

:Site: https://www.metabase.com/
:Porteur: une entreprise (Metabase)
:Licence: AGPL v3 (édition Open Source) et propriétaire

Créé en 2015, Metabase s'est imposé comme la solution décisionnelle open source la plus simple à mettre en œuvre, conçue pour que des utilisateurs non techniciens puissent interroger les données de l'entreprise.

Son originalité tient à son interface de construction de questions sans SQL, complétée par un éditeur SQL pour les analystes, des tableaux de bord interactifs, des filtres partagés, des alertes et abonnements par courriel ou messagerie, et une gestion fine des permissions (jusqu'au niveau ligne dans les éditions commerciales). Metabase se connecte à la plupart des bases relationnelles et des entrepôts (PostgreSQL, MySQL/MariaDB, BigQuery, Snowflake, ClickHouse, etc.).

Metabase est écrit en Clojure et JavaScript.


Apache Superset
---------------

:Site: https://superset.apache.org/
:Porteur: une fondation (Apache)
:Licence: Apache 2.0

Superset a été créé en 2015 chez Airbnb, puis confié à la fondation Apache, dont il est devenu projet de haut niveau en 2021.

Plus riche que Metabase sur la partie visualisation, Superset propose des dizaines de types de graphiques, un explorateur de données sans code, un éditeur SQL (SQL Lab), une couche sémantique légère et des tableaux de bord paramétrables. Il vise en particulier les entrepôts et bases analytiques à grand volume (Trino, ClickHouse, Druid, BigQuery, Snowflake…), avec mise en cache des résultats.

Superset est écrit en Python (Flask) et TypeScript (React).


Knowage (anciennement SpagoBI)
------------------------------

:Site: https://www.knowage-suite.com/

SpagoBI, la suite décisionnelle de la société italienne Engineering Ingegneria Informatica présentée dans les éditions précédentes de ce guide, a été renommée Knowage en 2016 ; le site historique spagoworld.org n'est plus en service. Le produit couvre toujours l'ensemble de la chaîne décisionnelle (rapports JasperReports et BIRT, OLAP avec Mondrian, *Query By Example*, métadonnées, analyse géolocalisée, tableaux de bord, workflow de publication).

Voir la fiche détaillée dans la section :doc:`/applications-generiques/decisionnel-reporting`.


RapidMiner (n'est plus open source)
-----------------------------------

:Site: https://www.siemens.com/en-us/products/rapidminer/
:Porteur: un éditeur (Siemens)
:Licence: propriétaire

Issu de la recherche universitaire allemande (université de Dortmund), RapidMiner a longtemps été une suite d'analyse de données publiée sous licence AGPL, largement diffusée dans les banques et l'industrie outre-Rhin.

L'éditeur a progressivement abandonné le modèle open source à la fin des années 2010, avant d'être racheté par Altair en 2022, lui-même absorbé par Siemens en 2025. Le produit, désormais commercialisé sous la marque Siemens, n'a plus sa place dans un guide de solutions open source : cette fiche n'est conservée qu'à titre d'avertissement pour les lecteurs des éditions précédentes. Les alternatives open source sont KNIME pour l'analyse et la science des données, Metabase ou Apache Superset pour le décisionnel classique.


JasperSoft
----------

:Site: https://www.jaspersoft.com/
:Porteur: un éditeur (Cloud Software Group)
:Licence: AGPL et propriétaire

JasperReports Server (ex-JasperServer) est la plateforme décisionnelle de Jaspersoft, éditeur du générateur d'états JasperReports disponible depuis 2001, passé chez TIBCO en 2014 puis chez Cloud Software Group en 2022. Cette plateforme propose des fonctionnalités de reporting et d'analyse.

En version communautaire, JasperReports Server propose la conception et la génération de rapports (avec Jaspersoft Studio, successeur d'iReport). Dans sa version commerciale, il propose la création de domaines métier, couches sémantiques et techniques au dessus des bases SQL relationnelles, permettant à la fois de définir un lexique métier, de s’abstraire de la technique et du SQL, ainsi que d’ajouter simplement une sécurité d’accès aux données. Une autre fonctionnalité majeure consiste en la création de rapport Ad Hoc, c’est-à-dire que l’utilisateur final peut créer ses propres rapports via une interface web conviviale. De plus, à l’instar des autres plateformes BI, Jasper propose la création de cube OLAP (brique Mondrian) et intègre Talend en tant qu’ETL.


Pentaho
-------

:Site: https://pentaho.com/
:Porteur: un éditeur (Hitachi Vantara)
:Licence: LGPL (édition communautaire) et propriétaire

Pentaho est une suite logicielle qui permet la distribution de fonctionnalités et de documents décisionnels à un grand nombre de personnes par l'intermédiaire d'une interface web. Le projet a été fondé en 2004 et racheté par Hitachi Data Systems (devenu Hitachi Vantara) en 2015.

À l'instar de JasperReports Server, Pentaho regroupe toutes les fonctionnalités d'une suite BI : l'ETL (Pentaho Data Integration), l'analyse OLAP (Mondrian), le reporting ad hoc, la couche de métadonnées et le reporting classique (Pentaho Report Designer). L'édition communautaire reste disponible, mais l'essentiel des investissements de l'éditeur porte désormais sur les offres commerciales et sur l'intégration à la plateforme de données d'Hitachi ; une partie de la communauté historique a migré vers Apache Hop.


Autres
------

- KNIME: https://www.knime.com/
- Eclipse BIRT: https://eclipse-birt.github.io/birt-website/
- Lightdash (BI au-dessus de dbt): https://www.lightdash.com/
- Redash (requêtes et tableaux de bord SQL): https://redash.io/
