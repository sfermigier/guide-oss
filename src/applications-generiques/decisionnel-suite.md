# Décisionnel : suites { #decisionnel-suite }

Les suites décisionnelles regroupent généralement les deux catégories présentées précédemment ; c'est-à-dire l’ETL et le reporting.

Ainsi, le périmètre des suites décisionnelles est très vaste : exécution des rapports, analyse OLAP, aide à la création de requêtes, ETL, module de gestion du workflow de publication, etc.

## Metabase

Site
: <https://www.metabase.com/>

Porteur
: une entreprise (Metabase)

Licence
: AGPL v3 (édition Open Source) et propriétaire

Créé en 2015, Metabase s'est imposé comme la solution décisionnelle open source la plus simple à mettre en œuvre, conçue pour que des utilisateurs non techniciens puissent interroger les données de l'entreprise.

Son originalité tient à son interface de construction de questions sans SQL, complétée par un éditeur SQL pour les analystes, des tableaux de bord interactifs, des filtres partagés, des alertes et abonnements par courriel ou messagerie et une gestion fine des permissions (jusqu'au niveau ligne dans les éditions commerciales). Metabase se connecte à la plupart des bases relationnelles et des entrepôts (PostgreSQL, MySQL/MariaDB, BigQuery, Snowflake, ClickHouse, etc.).

Metabase est écrit en Clojure et JavaScript.

## Apache Superset

Site
: <https://superset.apache.org/>

Porteur
: une fondation (Apache)

Licence
: Apache 2.0

Superset a été créé en 2015 chez Airbnb, puis confié à la fondation Apache, dont il est devenu projet de haut niveau en 2021.

Plus riche que Metabase sur la partie visualisation, Superset propose des dizaines de types de graphiques, un explorateur de données sans code, un éditeur SQL (SQL Lab), une couche sémantique légère et des tableaux de bord paramétrables. Il vise en particulier les entrepôts et bases analytiques à grand volume (Trino, ClickHouse, Druid, BigQuery, Snowflake…), avec mise en cache des résultats.

Superset est écrit en Python (Flask) et TypeScript (React).

## Knowage (anciennement SpagoBI)

Voir la fiche [Knowage](decisionnel-reporting.md#knowage-anciennement-spagobi) dans la section Décisionnel : Reporting.

<span id="jaspersoft"></span>

<span id="rapidminer-n-est-plus-open-source"></span>
<span id="pentaho"></span>

## Autres

- KNIME: <https://www.knime.com/>
- Eclipse BIRT: <https://eclipse-birt.github.io/birt-website/>
- Lightdash (BI au-dessus de dbt): <https://www.lightdash.com/>
- Redash (requêtes et tableaux de bord SQL): <https://redash.io/>
