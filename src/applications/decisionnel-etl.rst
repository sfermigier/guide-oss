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
:Licence: GPL et propriétaire

Talend Open Studio est un ETL open source apparu en 2005, développé par la société Talend, basée en France. C’est un ETL de type « générateur de code », c’est-à-dire qu’il permet de créer graphiquement des processus de manipulation et de transformation de données puis de générer l’exécutable correspondant sous forme de programme Java ou Perl. Une liste très exhaustive de composants permet de se connecter à tout type de base de données ou d’applications (SAP, SugarCRM,…). En 2010, une brique MDM a vu le jour.


Pentaho Data Integration
------------------------

:Version: 4.1.0
:Site: http://kettle.pentaho.com
:Porteur: un éditeur (Pentaho)
:Licence: GPL

Pentaho Data Integration (PDI) est un ETL open source qui permet de concevoir et d’exécuter des opérations de manipulation et de transformation de données. Au moment où nous écrivons ces lignes,  Pentaho Data Integration est disponible dans sa version 4.1.

Grâce à un modèle graphique à base d’étapes, il est possible de créer sans programmation des processus composés d’imports et d’exports de données, et de différentes opérations de transformation telles que des conversions, des jointures, l’application de filtres, ou même l’exécution de fonctions javascript. Un planificateur permet aussi de planifier l’exécution des jobs.

Un module complémentaire propriétaire commercial, « Agile BI », permet de visualiser graphiquement les résultats de transformations de données dès les premières étapes de développement.


Autres
------

Nom	URL / Site web

Scriptella	http://scriptella.javaforge.com/
JasperETL	http://www.jaspersoft.com/jasperetl
CloverETL	http://www.cloveretl.com/
Benetl	http://www.benetl.net/	
Toolsverse ETL Framework	http://www.toolsverse.com/
