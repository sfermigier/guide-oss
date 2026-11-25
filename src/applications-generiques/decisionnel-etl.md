# Décisionnel : ETL

L’ETL est souvent une brique du décisionnel même si on l’utilise parfois en dehors de ce cadre.

ETL signifie « Extract Transform Load ». Ce sont des outils qui permettent la réalisation de synchronisations massives d’informations d’une source de données vers une autre. Dans les faits, les ETL peuvent être utilisés dans des cas bien plus simples d’extraction, de transformation et/ou de chargement.

Les outils d’ETL disposent généralement de connecteurs permettant l’importation ou l’exportation de données dans les applications tierces. Les transformations peuvent être réalisées à partir de « plugins » existant ou via programmation.

## Airflow

Site
: <https://airflow.apache.org/>

Porteur
: une fondation (Apache)

Licence
: Apache 2.0

Apache Airflow a été créé par Airbnb et est un outil de gestion de flux de travail open source. Il peut être utilisé pour créer des pipelines ETL de données. À proprement parler, c'est un outil d'orchestration : il crée, planifie et surveille des flux de travail. Cela signifie que vous pouvez utiliser Airflow pour créer un pipeline en consolidant divers modules écrits indépendamment de votre processus ETL.

Le workflow Airflow suit le concept de DAG (Directed Acyclic Graph). Airflow, comme les autres outils de la liste, dispose également d'un tableau de bord fondé sur un navigateur pour visualiser le flux de travail et suivre l'exécution de plusieurs flux de travail. Airflow est un bon choix si vous souhaitez créer un flux de travail ETL complexe en enchaînant des modules indépendants et existants.

## Bonobo

Bonobo (<https://www.bonobo-project.org/>), petit ETL Python sous licence Apache 2.0, n’évolue plus : son dépôt n’a reçu aucune modification depuis mai 2023. Apache Hop, Meltano ou une orchestration Airflow ou Dagster couvrent le même besoin.

## Luigi

Site
: <https://github.com/spotify/luigi>

Porteur
: une entreprise (Spotify)

Licence
: Apache 2.0

Luigi est un outil ETL fondé sur Python qui a été créé par Spotify mais qui est disponible en open source. Il possède des fonctionnalités étendues pour créer des pipelines ETL complexes. Selon sa page GitHub, il gère la résolution des dépendances, la gestion des flux de travail, la visualisation, le traitement des pannes et l'intégration en ligne de commande.

Il est également doté d'un tableau de bord web permettant de suivre tous les travaux ETL. Si vous cherchez à construire une solution d'entreprise, Luigi peut être un bon choix.

## Apache Hop

Site
: <https://hop.apache.org/>

Porteur
: une fondation (Apache)

Licence
: Apache 2.0

Apache Hop (*Hop Orchestration Platform*) est né en 2020 d'un fork de Pentaho Kettle, devenu projet de haut niveau de la fondation Apache en 2021.

Hop conserve l'approche graphique qui a fait le succès de Kettle, où l'on assemble visuellement des *pipelines* (transformations de données) et des *workflows* (orchestration), en la modernisant : conception « design once, run anywhere » avec exécution locale, sur Spark, Flink ou Google Dataflow via Apache Beam, gestion des projets et des environnements, intégration au cycle de vie logiciel (métadonnées versionnables dans Git, tests unitaires de pipelines).

C'est aujourd'hui l'ETL graphique open source de référence.

Apache Hop est écrit en Java.

<span id="airbyte"></span>

<span id="talend"></span>
<span id="pentaho-data-integration"></span>

## Autres

- Apache NiFi (flux de données temps réel) : <https://nifi.apache.org/>
- Meltano (ELT, écosystème de connecteurs Singer) : <https://meltano.com/>
- dbt Core (transformation SQL dans l'entrepôt) : <https://github.com/dbt-labs/dbt-core>
- Dagster (orchestration orientée données) : <https://dagster.io/>
- Prefect (orchestration Python) : <https://www.prefect.io/>
