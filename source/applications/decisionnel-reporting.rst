Décisionnel : Reporting
=======================

Une des briques essentielles du décisionnel consiste à établir des rapports.

Les outils de reporting, tel que BIRT, permettent non seulement de générer des rapports (paramétrés ou non) au format HTML, PDF, XLS, DOC, PPT, etc.) mais aussi de construire des tableaux croisés dynamiques.

Les données affichées peuvent provenir de bases et de requêtes différentes. D’ailleurs, les outils de reporting fournissent généralement des plugins pour se greffer facilement à des sources ou applications externes.

Les outils comme JasperReports, vont jusqu’à offrir des analyses multidimensionnelles ce qui permet d’exploiter les possibilités d’un serveur Mondrian directement dans des rapports.




BIRT
----

:Site: www.eclipse.org/birt
:Porteur: une fondation (Eclipse)
:Licence: Eclipse Public Licence (EPL)

BIRT (The Business Intelligence and Reporting Tool) est un projet de la communauté Eclipse comprenant un générateur de graphiques, un générateur de rapports et un environnement de conception. Le projet a été initié en 2005.

Le moteur de BIRT est une bibliothèque qui permet de générer des rapports (paramétrés ou non) au format HTML, PDF, XLS, DOC ou PPT. Ces rapports peuvent être complexes et contenir plusieurs tableaux, graphiques avancés et images. BIRT propose également la réalisation de tableaux croisés dynamiques. Les données affichées peuvent provenir de bases et de requêtes différentes. Le moteur de BIRT peut être intégré dans toute application développée avec le langage Java, que ce soit dans une application web ou dans une application de type « client lourd ». Le concepteur de rapport est un plugin s’intégrant à Eclipse (pouvant aussi être exécuté en stand-alone).



JasperReports / IReport
-----------------------

:Site: http://jasperforge.org/project/ireport
:Porteur: un éditeur (JasperSoft)
:Licence: GPL et proprietaire

JasperReports est un moteur de rapport développé par la société  JasperSoft et distribué sous licence open source. IReport est l'éditeur de rapport de JasperSoft. Au moment où nous écrivons ces lignes,  JasperReports et iReport sont disponibles dans leur version 4.0.2. Ces outils existent depuis 2001 et sont déjà largement utilisés dans de nombreuses applications métiers pour leurs parties reporting.

Le moteur JasperReports permet la génération de rapports au format PDF, HTML, XML, CSV, RTF, XLS et TXT. Il utilise JFreeChart pour générer les graphiques et peut être intégré dans toute application développée avec le langage Java. Il supporte, en plus des bases de données classiques, les serveurs d’analyse multidimensionnelle ce qui permet d’exploiter les possibilités du serveur Mondrian directement dans  un rapport JasperReports. Le concepteur de rapport, IReport, est utilisé pour le design des rapports.


Jedox / Palo
------------

:Site: http://www.palo.net/
:Porteur: un éditeur (Jedox)
:Licence: GPL et proprietaire

Palo est un moteur OLAP comportant un ETL et des modules simplifiant son usage sous Excel ou OpenOffice. Jedox est l'éditeur
de Palo. Jedox fournit en licence open source la version précédente de Palo alors que la dernière version est diffusée sous licence propriétaire.

Palo est probablement aujourd'hui l'outil de reporting le plus simple d'emploi. Palo ne nécessite aucune programmation et s'utilise soit à partir d'un tableur (Excel, OpenOffice) soit au travers d'un tableur Web intégré. Palo convient à des applications de type reporting budgétaire, reporting comptable, analayse des ventes. Palo intègre un portail Web et une gestion des utilisateurs et peut donc être utilisé dans devoir installer un logiciel client.


Pentaho Report Designer
-----------------------

:Site: http://reporting.pentaho.com
:Porteur: un éditeur (Pentaho)
:Licence: GPL et propriétaire

JFreeReport a rejoint le projet Pentaho début 2006. Au fur et à mesure, le nom JFreeReport a été abandonné au profit de Pentaho Report Designer (PRD). PRD permet de développer des rapports complexes et, en association avec la plateforme Pentaho, de les publier directement sur le serveur décisionnel. Au moment où nous écrivons ces lignes,  PRD est disponible dans sa version 3.8.

Pentaho Report Designer est un outil simple à manipuler, bien intégré à la suite décisionnelle Pentaho pour la gestion des paramètres ou la publication sur la plateforme web. Il permet la génération de rapports au format PDF, HTML, XML, CSV, RTF, XLS et supporte les sources de données multiples. Par contre, la création de tableaux croisés dynamiques n’est pas encore évidente (fonctionnalité cachée), et est attendue pour la version 4.
