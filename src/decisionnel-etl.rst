Décisionnel : ETL
=================

L’ETL est souvent une brique du décisionnel même si on l’utilise parfois en dehors de ce cadre.

ETL signifie « Extract Transform Load ». Ce sont des outils qui permettent la réalisation de synchronisations massives d’informations d’une source de données vers une autre. Dans les faits, les ETL peuvent être utilisés dans des cas bien plus simples d’extraction, de transformation et/ou de chargement.

Les outils d’ETL disposent généralement de connecteurs permettant l’importation ou l’exportation de données dans les applications tierces. Les transformations peuvent être réalisées à partir de « plugins » existant ou via programmation.

Parmi les outils open source, on citera Talend ou Pentaho Data Integration (anciennement kettle).




Talend
------

:Version: 4.2.3
:Site: www.talend.com
:Porteur: un éditeur (Talend)

Talend Open Studio est un ETL open source apparu en 2005, développé par la société Talend, basée en France. C’est un ETL de type « générateur de code », c’est-à-dire qu’il permet de créer graphiquement des processus de manipulation et de transformation de données puis de générer l’exécutable correspondant sous forme de programme Java ou Perl. Une liste très exhaustive de composants permet de se connecter à tout type de base de données ou d’applications (SAP, SugarCRM,…). En 2010, une brique MDM a vu le jour.

Talend Open Studio, la brique de base de Talend, ne comprenant que l’ETL, est sous licence GPL. Les autres versions sont sous licences commerciales, avec une souscription par an. Deux versions sont disponibles : l’ETL  « TIS (Talend Integration Suite) » et le MDM « Talend MDM ». Le périmètre de TIS comprend la définition de processus (jobs), de modèles métiers, de déploiement des processus, et d’administration des déploiements. La version MDM comprend, en plus, la gestion de données référentielles ainsi qu’un module de qualité de données.




Pentaho Data Integration
------------------------

:Version: 4.1.0
:Site: http://kettle.pentaho.com
:Porteur: un éditeur (Pentaho)

Pentaho Data Integration (PDI) est un ETL open source qui permet de concevoir et d’exécuter des opérations de manipulation et de transformation de données. Au moment où nous écrivons ces lignes,  Pentaho Data Integration est disponible dans sa version 4.1.

Grâce à un modèle graphique à base d’étapes, il est possible de créer sans programmation des processus composés d’imports et d’exports de données, et de différentes opérations de transformation telles que des conversions, des jointures, l’application de filtres, ou même l’exécution de fonctions javascript. Un planificateur permet aussi de planifier l’exécution des jobs. Un module commercial « Agile BI » permet de visualiser graphiquement les résultats de transformations de données dès les premières étapes de développement.

PDI est disponible en version GPL, le module Agile BI étant sous licence commerciale.



Décisionnel : Reporting

Une des briques essentielles du décisionnel constiste à établir des rapports.

Les outils de reporting, tel que BIRT, permettent non seulement de générer des rapports (paramétrés ou non) au format HTML, PDF, XLS, DOC, PPT, etc.) mais aussi de construire des tableaux croisés dynamiques.

Les données affichées peuvent provenir de bases et de requêtes différentes. D’ailleurs, les outils de reporting fournissent généralement des plugins pour se greffer facilement à des sources ou applications externes.

Les outils comme JasperReports, vont jusqu’à offrir des analyses multidimensionnelles ce qui permet d’exploiter les possibilités d’un serveur Mondrian directement dans des rapports.




BIRT
----

:Version: 3.7
:Site: www.eclipse.org/birt
:Porteur: une fondation (Eclipse)

BIRT (The Business Intelligence and Reporting Tool) est un projet de la communauté Eclipse comprenant un générateur de graphiques, un générateur de rapports et un environnement de conception. Le projet a été initié en 2005.

Le moteur de BIRT est une bibliothèque qui permet de générer des rapports (paramétrés ou non) au format HTML, PDF, XLS, DOC ou PPT. Ces rapports peuvent être complexes et contenir plusieurs tableaux, graphiques avancés et images. BIRT propose également la réalisation de tableaux croisés dynamiques. Les données affichées peuvent provenir de bases et de requêtes différentes. Le moteur de BIRT peut être intégré dans toute application développée avec le langage Java, que ce soit dans une application web ou dans une application de type « client lourd ». Le concepteur de rapport est un plugin s’intégrant à Eclipse (pouvant aussi être exécuté en stand-alone).

BIRT est sous licence GPL uniquement.




JasperReports / IReport
-----------------------

:Version: 4.0.2
:Site: http://jasperforge.org/project/ireport
:Porteur: un éditeur (JasperSoft)

JasperReports est un moteur de rapport développé par la société  JasperSoft et distribué sous licence open source. IReport est l'éditeur de rapport de JasperSoft. Au moment où nous écrivons ces lignes,  JasperReports et iReport sont disponibles dans leur version 4.0.2. Ces outils existent depuis 2001 et sont déjà largement utilisés dans de nombreuses applications métiers pour leurs parties reporting.

Le moteur JasperReports permet la génération de rapports au format PDF, HTML, XML, CSV, RTF, XLS et TXT. Il utilise JFreeChart pour générer les graphiques et peut être intégré dans toute application développée avec le langage Java. Il supporte, en plus des bases de données classiques, les serveurs d’analyse multidimensionnelle ce qui permet d’exploiter les possibilités du serveur Mondrian directement dans  un rapport JasperReports. Le concepteur de rapport, IReport, est utilisé pour le design des rapports.

JasperReports existe en version communautaire (GPL) et commerciale (licence propriétaire).




Pentaho Report Designer
-----------------------

:Version: 3.8
:Site: http://reporting.pentaho.com
:Porteur: un éditeur (Pentaho)

JFreeReport a rejoint le projet Pentaho début 2006. Au fur et à mesure, le nom JFreeReport a été abandonné au profit de Pentaho Report Designer (PRD). PRD permet de développer des rapports complexes et, en association avec la plateforme Pentaho, de les publier directement sur le serveur décisionnel. Au moment où nous écrivons ces lignes,  PRD est disponible dans sa version 3.8.

Pentaho Report Designer est un outil simple à manipuler, bien intégré à la suite décisionnelle Pentaho pour la gestion des paramètres ou la publication sur la plateforme web. Il permet la génération de rapports au format PDF, HTML, XML, CSV, RTF, XLS et supporte les sources de données multiples. Par contre, la création de tableaux croisés dynamiques n’est pas encore évidente (fonctionnalité cachée), et est attendue pour la version 4.

Pentaho Report Designer existe en version communautaire (GPL) et commerciale (licence propriétaire).

