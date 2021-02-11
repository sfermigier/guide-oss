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

Apache Airflow a été créé par Airbnb et est un outil de gestion de flux de travail open source. Il peut être utilisé pour créer des pipelines ETL de données. À proprement parler, ce n'est pas un outil ETL en soi, mais plutôt un outil d'orchestration qui peut être utilisé pour créer, planifier et surveiller des flux de travail. Cela signifie que vous pouvez utiliser Airflow pour créer un pipeline en consolidant divers modules écrits indépendamment de votre processus ETL.

Le workflow Airflow suit le concept de DAG (Directed Acyclic Graph). Airflow, comme les autres outils de la liste, dispose également d'un tableau de bord basé sur un navigateur pour visualiser le flux de travail et suivre l'exécution de plusieurs flux de travail. Airflow est un bon choix si vous souhaitez créer un flux de travail ETL complexe en enchaînant des modules indépendants et existants

Bonobo
------

:Site: https://www.bonobo-project.org/
:Porteur: une communauté
:Licence: Apache 2.0

Bonobo est un outil ETL léger construit en Python. Il est simple et relativement facile à apprendre. Il utilise le concept de graphe pour créer des pipelines et prend également en charge le traitement parallèle de plusieurs éléments dans le pipeline. Il possède également une interface visuelle où l'utilisateur peut suivre la progression du pipeline ETL.

Dans l'ensemble, c'est juste un autre outil Python ETL facile à utiliser, qui peut être une bonne option pour les cas d'utilisation simples, mais qui ne possède pas beaucoup de caractéristiques qui le séparent du reste du paquet.

Luigi
-----

:Site: https://github.com/spotify/luigi
:Porteur: Une entreprise (Spotify)
:Licence: Apache 2.0

Luigi est un outil ETL basé sur Python qui a été créé par Spotify mais qui est maintenant disponible en tant qu'outil open-source. Il s'agit d'un outil plus sophistiqué que beaucoup d'autres sur cette liste et il possède des fonctionnalités puissantes pour créer des pipelines ETL complexes. Selon leur page Github, "Il gère la résolution des dépendances, la gestion des flux de travail, la visualisation, le traitement des pannes, l'intégration en ligne de commande, et bien plus encore".

Il est également doté d'un tableau de bord web permettant de suivre tous les travaux ETL. Si vous cherchez à construire une solution d'entreprise, Luigi peut être un bon choix.


Talend
------

:Site: www.talend.com
:Porteur: un éditeur (Talend)
:Licence: GPL et propriétaire

Talend Open Studio est un ETL open source apparu en 2005, développé par la société Talend, basée en France. C’est un ETL de type « générateur de code », c’est-à-dire qu’il permet de créer graphiquement des processus de manipulation et de transformation de données puis de générer l’exécutable correspondant sous forme de programme Java ou Perl. Une liste très exhaustive de composants permet de se connecter à tout type de base de données ou d’applications (SAP, SugarCRM,…). En 2010, une brique MDM a vu le jour.


Pentaho Data Integration
------------------------

:Site: http://www.pentaho.fr/explore/pentaho-data-integration/
:Porteur: un éditeur (Pentaho)
:Licence: GPL

Pentaho Data Integration (PDI) est un ETL open source qui permet de concevoir et d’exécuter des opérations de manipulation et de transformation de données. Au moment où nous écrivons ces lignes,  Pentaho Data Integration est disponible dans sa version 4.1.

Grâce à un modèle graphique à base d’étapes, il est possible de créer sans programmation des processus composés d’imports et d’exports de données, et de différentes opérations de transformation telles que des conversions, des jointures, l’application de filtres, ou même l’exécution de fonctions javascript. Un planificateur permet aussi de planifier l’exécution des jobs.

Un module complémentaire propriétaire commercial, « Agile BI », permet de visualiser graphiquement les résultats de transformations de données dès les premières étapes de développement.


Autres
------

- Scriptella:	http://scriptella.javaforge.com/
- JasperETL:	http://www.jaspersoft.com/jasperetl
- CloverETL:	http://www.cloveretl.com/
- Benetl:	http://www.benetl.net/
- Toolsverse ETL Framework:	http://www.toolsverse.com/
