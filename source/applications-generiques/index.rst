Applications génériques
=======================

Les applications génériques, dites aussi horizontales, sont celles dont toute organisation a besoin quel que soit son secteur : gérer une relation client, tenir une comptabilité et une chaîne logistique, piloter l'activité par des indicateurs, conserver et retrouver des documents.

C'est le terrain de la gestion, et l'histoire de l'open source y est particulière. Les briques d'infrastructure libres se sont imposées par leur supériorité technique ; ici, il a fallu convaincre des directions financières et des directions métier, sur un terrain occupé de longue date par des éditeurs solidement installés. Les solutions présentées dans cette partie y sont parvenues : Odoo équipe des dizaines de milliers d'entreprises, Dolibarr est devenu un standard des TPE et PME françaises, Alfresco et Nuxeo se sont imposés dans la GED d'entreprise avant d'être rachetés par le même acteur américain, et Metabase a fait basculer une génération entière d'équipes vers un décisionnel en libre-service.

Trois points de vigilance structurent le choix dans cette catégorie.

**Le modèle de diffusion.** C'est ici que l'« open core » est le plus répandu, et que la frontière entre édition communautaire et édition commerciale se déplace le plus souvent. Plusieurs fiches de cette partie racontent la même histoire : un produit largement adopté pour sa version libre, puis un resserrement : fonctions réservées, limites d'usage, arrêt pur et simple de l'édition communautaire, comme Talend Open Studio en 2024. Il faut donc instruire ce que fait le produit aujourd'hui, et ce que sa licence garantira demain.

**La convergence des périmètres.** Les frontières entre CRM, ERP, GED et décisionnel se sont estompées : un ERP moderne embarque un CRM convenable, un CMS gère un catalogue produits, une GED propose des workflows métier. Il est souvent plus économique d'étendre un outil déjà en place que d'en ajouter un spécialisé, au prix d'une intégration supplémentaire. Les sections « Voir également » de chaque chapitre signalent ces recouvrements.

**Le coût de sortie.** Ces applications accumulent le patrimoine informationnel de l'organisation. La qualité de leurs exports, la documentation de leur modèle de données et l'existence d'une communauté capable de reprendre une instance abandonnée pèsent, à cinq ans, plus lourd que l'écart de couverture fonctionnelle qui départage deux candidats au moment du choix.

Cette partie recense une centaine de solutions, réparties dans les catégories suivantes :

.. toctree::
    :maxdepth: 1

    crm.rst
    erp-pgi.rst
    decisionnel-etl.rst
    decisionnel-reporting.rst
    decisionnel-suite.rst
    ged-ecm.rst
    autres.rst
