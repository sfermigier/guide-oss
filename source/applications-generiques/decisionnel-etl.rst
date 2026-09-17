Décisionnel : ETL
=================

L’ETL est souvent une brique du décisionnel même si on l’utilise parfois en dehors de ce cadre.

ETL signifie « Extract Transform Load ». Ce sont des outils qui permettent la réalisation de synchronisations massives d’informations d’une source de données vers une autre. Dans les faits, les ETL peuvent être utilisés dans des cas bien plus simples d’extraction, de transformation et/ou de chargement.

Les outils d’ETL disposent généralement de connecteurs permettant l’importation ou l’exportation de données dans les applications tierces. Les transformations peuvent être réalisées à partir de « plugins » existant ou via programmation.


Airflow
-------

:Site: https://airflow.apache.org/
:Porteur: une fondation (Apache)
:Licence: Apache 2.0

Apache Airflow a été créé par Airbnb et est un outil de gestion de flux de travail open source. Il peut être utilisé pour créer des pipelines ETL de données. À proprement parler, c'est un outil d'orchestration : il crée, planifie et surveille des flux de travail. Cela signifie que vous pouvez utiliser Airflow pour créer un pipeline en consolidant divers modules écrits indépendamment de votre processus ETL.

Le workflow Airflow suit le concept de DAG (Directed Acyclic Graph). Airflow, comme les autres outils de la liste, dispose également d'un tableau de bord fondé sur un navigateur pour visualiser le flux de travail et suivre l'exécution de plusieurs flux de travail. Airflow est un bon choix si vous souhaitez créer un flux de travail ETL complexe en enchaînant des modules indépendants et existants

Bonobo
------

:Site: https://www.bonobo-project.org/
:Porteur: une communauté
:Licence: Apache 2.0

Bonobo est un outil ETL léger construit en Python. Il est simple et relativement facile à apprendre. Il utilise le concept de graphe pour créer des pipelines et prend également en charge le traitement parallèle de plusieurs éléments dans le pipeline. Il possède également une interface visuelle où l'utilisateur peut suivre la progression du pipeline ETL.

Dans l'ensemble, c'est un outil ETL Python facile à prendre en main, qui peut être une bonne option pour les cas d'utilisation simples. Son développement est toutefois à l'arrêt depuis plusieurs années : pour un nouveau projet, on lui préférera Apache Hop, Meltano ou une orchestration Airflow/Dagster.

Luigi
-----

:Site: https://github.com/spotify/luigi
:Porteur: Une entreprise (Spotify)
:Licence: Apache 2.0

Luigi est un outil ETL fondé sur Python qui a été créé par Spotify mais qui est maintenant disponible en tant qu'outil open-source. Il s'agit d'un outil plus sophistiqué que beaucoup d'autres sur cette liste et il possède des fonctionnalités étendues pour créer des pipelines ETL complexes. Selon leur page Github, "Il gère la résolution des dépendances, la gestion des flux de travail, la visualisation, le traitement des pannes, l'intégration en ligne de commande, et bien plus encore".

Il est également doté d'un tableau de bord web permettant de suivre tous les travaux ETL. Si vous cherchez à construire une solution d'entreprise, Luigi peut être un bon choix.


Talend
------

:Site: https://www.qlik.com/us/products/talend-open-studio
:Porteur: un éditeur (Qlik)
:Licence: propriétaire (l'édition open source a été arrêtée)

Talend Open Studio a été, de 2006 à 2024, l'ETL open source de référence. Développé par la société française Talend, c'était un ETL de type « générateur de code » : il permettait de créer graphiquement des processus de manipulation et de transformation de données, puis de générer l'exécutable correspondant sous forme de programme Java ou Perl, avec une très large bibliothèque de composants de connexion (bases de données, SAP, applications métier…).

Talend a été racheté par Qlik en 2023, qui a annoncé l'arrêt de Talend Open Studio : les téléchargements ont été retirés le 31 janvier 2024 et les installations existantes ne reçoivent plus de correctifs, y compris de sécurité. Seules subsistent les offres commerciales (Qlik Talend Cloud).

Les utilisateurs à la recherche d'un remplaçant open source se tournent principalement vers Apache Hop (proche dans l'esprit et dans l'outillage graphique), Airbyte ou Meltano pour l'extraction/chargement, et Airflow ou Dagster pour l'orchestration.


Pentaho Data Integration
------------------------

:Site: https://pentaho.com/
:Porteur: un éditeur (Hitachi Vantara)
:Licence: LGPL (édition communautaire) et propriétaire

Pentaho Data Integration (PDI, historiquement « Kettle ») est un ETL qui permet de concevoir et d'exécuter des opérations de manipulation et de transformation de données. Le projet appartient à Hitachi Vantara depuis le rachat de Pentaho en 2015.

Grâce à un modèle graphique à base d'étapes, il est possible de créer sans programmation des processus composés d'imports et d'exports de données, et de différentes opérations de transformation telles que des conversions, des jointures, l'application de filtres, ou même l'exécution de fonctions JavaScript. Un ordonnanceur permet de planifier l'exécution des jobs.

Une partie de la communauté historique de Kettle a essaimé en 2020 vers Apache Hop (voir ci-dessous), qui en reprend les concepts sous gouvernance de la fondation Apache.


Apache Hop
----------

:Site: https://hop.apache.org/
:Porteur: une fondation (Apache)
:Licence: Apache 2.0

Apache Hop (*Hop Orchestration Platform*) est né en 2020 d'un fork de Pentaho Kettle, devenu projet de haut niveau de la fondation Apache en 2021.

Hop conserve l'approche graphique qui a fait le succès de Kettle, où l'on assemble visuellement des *pipelines* (transformations de données) et des *workflows* (orchestration), en la modernisant : conception « design once, run anywhere » avec exécution locale, sur Spark, Flink ou Google Dataflow via Apache Beam, gestion des projets et des environnements, intégration au cycle de vie logiciel (métadonnées versionnables dans Git, tests unitaires de pipelines).

C'est aujourd'hui le successeur naturel de Pentaho Data Integration et de Talend Open Studio pour qui cherche un ETL graphique entièrement open source.

Apache Hop est écrit en Java.


Airbyte
-------

:Site: https://airbyte.com/
:Porteur: un éditeur (Airbyte)
:Licence: ELv2 et MIT selon les composants

Airbyte, créé en 2020, s'est imposé comme la référence de l'extraction/chargement (EL) open source, avec un catalogue de plusieurs centaines de connecteurs vers des sources SaaS, des bases de données et des entrepôts.

L'outil privilégie l'approche ELT : les données sont chargées telles quelles dans l'entrepôt, la transformation étant déléguée à des outils dédiés (dbt, SQL). Les connecteurs sont développés dans un cadre standardisé (CDK) qui facilite l'écriture de connecteurs spécifiques.

Attention au modèle de licence : la plateforme est majoritairement publiée sous Elastic License v2, qui n'est pas une licence open source au sens de l'OSI, tandis que les connecteurs restent sous licence MIT.

Airbyte est écrit en Java, Python et TypeScript.


Autres
------

- Apache NiFi (flux de données temps réel) : https://nifi.apache.org/
- Meltano (ELT, écosystème de connecteurs Singer) : https://meltano.com/
- dbt Core (transformation SQL dans l'entrepôt) : https://github.com/dbt-labs/dbt-core
- Dagster (orchestration orientée données) : https://dagster.io/
- Prefect (orchestration Python) : https://www.prefect.io/
