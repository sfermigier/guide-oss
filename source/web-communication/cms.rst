CMS
===

La gestion de contenu web recouvre aujourd’hui une large palette de besoins : sites d’informations, sites Corporate, sites de services, extranets sécurisés, intranets participatifs, espaces communautaire...

Pour couvrir ce périmètre, il existe d’excellentes solutions open source au périmètre très large qui sont devenues des standards dans l’univers de la gestion de contenus tant elles dominent par leur capacité, leur modularité et leur périmètre fonctionnel et technique.

Au côté de ces solutions dominantes, la convergence ERP/CRM/CMS/e-business poussée par la croissance e-commerce conduit des applicatifs issus d'autres domaines fonctionnels (ERP, CRM) à intégrer des fonctions de CMS équivalents aux meilleurs produits dédiés du marché.


Drupal
------

:Site: https://www.drupal.org/
:Porteur: une communauté
:Licence: GPL

Drupal est un CMS aux multiples facettes. Conçu à l’origine pour être un blog collectif, il trouve aujourd’hui des applications très variées, du site corporate au portail communautaire. Il a été conçu dans les années 2000 par Dries Buytaert et connaît depuis un succès mondial. Une importante communauté s’est créée autour du produit.

La force de ce CMS est son extensibilité. Il accueille très facilement de nombreux modules complémentaires (forum, galerie photos, sondage, formulaire, newsletter, messagerie, chat, enquête, paiement en ligne, calendrier partagé, etc.). Il possède notamment des modules communautaires très soignés et appréciés ce qui le rend particulièrement adapté aux réseaux sociaux d’entreprise.

Drupal est publié sous licence GNU GPL v2 (ou ultérieure) et est pleinement open source. Des offres de support existent, notamment via la société Acquia (https://www.acquia.com), fondée par le créateur du projet.

D'un point de vue technique, Drupal s'est profondément modernisé depuis Drupal 8 (2015) : le cœur s'appuie désormais sur les composants Symfony, Twig pour les gabarits et Composer pour la gestion des dépendances. Les versions majeures se succèdent à un rythme régulier (Drupal 10 en 2022, Drupal 11 en 2024), avec une distribution clés en main, Drupal CMS, destinée à réduire le coût d'entrée pour les sites standards. Attention aux migrations : Drupal 7, longtemps majoritaire, est en fin de vie depuis janvier 2025 et ne reçoit plus de correctifs de sécurité.

Drupal fonctionne avec PHP et MySQL/MariaDB ou PostgreSQL.


Wagtail
-------

:Site: https://wagtail.org/
:Porteur: une entreprise (Torchbox) et une communauté
:Licence: BSD

Wagtail est un CMS développé depuis 2014 sur la base du framework web Django.

Wagtail comprend toutes les fonctionnalités de publication de base dont la plupart des grands sites complexes ont besoin, sans limitations concernant l'apparence ou le comportement des pages construites dans Wagtail. Pour les cas particuliers qui ne sont pas couverts par le framework de base, une architecture de plugins permet de l'étendre. `Plusieurs centaines de plugins <https://wagtail.org/packages/>`_ sont disponibles couvrant des besoins comme: types de contenus, SEO, workflows (validation), E-commerce, etc.

Wagtail est développé en Python.


Ibexa DXP (anciennement eZ Publish)
-----------------------------------

:Site: https://www.ibexa.co/
:Porteur: un éditeur (Ibexa, anciennement eZ Systems)
:Licence: GPL v2 pour l'édition open source, propriétaire pour les éditions commerciales

La solution eZ Publish a été créée en 1999 par la société norvégienne eZ Systems. Renommée eZ Platform lors de sa réécriture sur Symfony, elle est devenue Ibexa DXP en 2020, en même temps que l'éditeur prenait le nom d'Ibexa.

Sur les fondamentaux de la gestion de contenus, le produit reste l'un des plus puissants du marché. Il pousse l'approche objet jusqu'au bout, en faisant de chaque contenu un objet auquel s'appliquent toutes les méthodes disponibles : multi-positionnement, gestion des versions, multilinguisme, relations entre contenus, droits d'accès, workflow. Cette conception en fait un CMS hautement paramétrable, désormais positionné comme une plateforme d'expérience numérique (DXP) incluant des briques e-commerce et PIM.

Attention à l'évolution du modèle : la branche historique eZ Publish Legacy n'est plus maintenue, et les fonctionnalités les plus riches sont réservées aux éditions commerciales. Une édition open source (Ibexa OSS, sous GPL v2) reste disponible.

Sur le plan technique, le produit est écrit en PHP sur le framework Symfony, et s'appuie sur MySQL/MariaDB ou PostgreSQL, avec Solr ou Elasticsearch pour la recherche.


Jahia
-----

:Site: https://www.jahia.com/
:Porteur: un éditeur (Jahia Corp)
:Licence: GPL

Jahia est un produit franco-suisse, créé dans les années 2000, qui tient une place à part dans le monde des portails et des CMS JEE. En effet, Jahia est une des rares solutions qui réunit portail JEE et gestion de contenu en un produit unique, parfaitement intégré.

Librement téléchargeable, Jahia est d’un niveau de finition et de packaging impressionnant. Jahia se distingue des autres CMS par son interface d’administration des contenus, qui est fondue dans le site lui-même. Au niveau fonctionnel, Jahia est une des solutions CMS les plus abouties : gestion multi-sites, gestion des versions, workflows efficaces, données structurées, multilinguisme, gestion des droits très fine, etc. La gamme s'est élargie autour de la plateforme d'expérience numérique (jExperience, jContent) et d'une approche *headless* via GraphQL.

Jahia constitue une excellente alternative aux solutions de portail des grands éditeurs propriétaires, la possibilité de voir et de modifier  les sources (licence GPL pour la version Community) assurant la pérennité et l’adéquation de l’outil aux besoins. Jahia propose également une version Entreprise sous licence commerciale apportant stabilité, support et garantie.

Jahia est bâtie sur des technologies JEE : persistance via Hibernate, support des normes JSR 170, moteur de recherche Apache Lucene, support des standards de portlets JSR 168, etc.


Joomla
------

:Site: https://www.joomla.org/
:Porteur: une communauté
:Licence: GPL

Joomla est un CMS développé à partir de Mambo en 2005. Il a été créé suite à un différend entre les développeurs principaux et la société coordinatrice des développements. Aujourd’hui, la majorité des développeurs de la communauté se consacre à Joomla, ce qui fait nettement pencher la balance en sa faveur.

Cet outil se démarque principalement par la convivialité de son interface d’administration. Le mot d’ordre étant de « donner un contrôle total du produit à un non-technicien ». Création de pages, catégorisation, recherche, statistiques d’accès, urls significatives ainsi que de nombreux modules sont directement intégrés et ne demandent pas de connaissances spécifiques pour leur mise en œuvre. Ce CMS conviendra parfaitement pour des sites personnels mais pourra également répondre aux besoins de certains sites professionnels ; ceux notamment de type Corporate (simple publication).

Joomla est une solution 100% communautaire publiée sous licence GNU GPL.

Joomla est écrit en PHP et utilise une base de données MySQL.


SPIP
----

:Site: https://www.spip.net/
:Porteur: une communauté
:Licence: GPL

A l’origine, en 2001, SPIP était principalement utilisé par des internautes pour gérer leur site web personnel, ou pour des sites d'associations, mais SPIP a grandi et est maintenant utilisé par des organismes privés ou publics, pour gérer leur site web professionnel.

SPIP fait partie des rares CMS à pouvoir prétendre à plusieurs milliers de références à travers le monde. Cette réussite s’explique par la simplicité du produit : simplicité d’utilisation, mais aussi simplicité de déploiement et d’adaptation. En contrepartie de cette simplicité, SPIP présente quelques limitations sur des fonctionnalités clés de gestion de contenus, ce qui le limite clairement au monde des outils de gestion de contenus orienté ‘web’, et non pas ‘entreprise’.

SPIP est un projet open source français (licence GPL), et sa communauté peut être qualifiée d’active, avec plusieurs versions par an et des centaines – voire des milliers – de membres.

SPIP est un logiciel écrit en PHP qui s'appuie sur les bases de données MySQL, PostgreSQL et SQLite. Il propose un interface privée simplifiée basée sur l’Ajax, une page de téléchargement et d’installation de plugins, la gestion des conflits, une API et de nouvelles fonctions pour le développement de templates.


TYPO3
-----

:Site: https://typo3.org/
:Porteur: une association (TYPO3 Association) et une communauté
:Licence: GPL

TYPO3 est le fruit de plusieurs années de travail d’un gourou danois du nom de Kasper Skårhøj. Le produit est sorti fin 2000, et depuis, une communauté très active s’est développée, particulièrement dans les pays germaniques.

En termes de fonctionnalités prêtes à l’emploi, TYPO3 est l’un des outils les plus riches que nous ayons trouvés à ce jour. Il offre à peu près tout ce que l’on peut souhaiter, et cela avec un bon niveau de finition. Gestion des droits et des contributions, cache, habilitations, gabarits, etc., tout y est, avec peu de limitations. Parmi les fonctionnalités offertes par TYPO3, on peut citer la manipulation d’images, qui permet de redimensionner des images, de créer des vignettes et également de générer dynamiquement des titres en tant qu’images. L’une des grandes forces de TYPO3 réside dans son extensibilité par modules. Un module peut ajouter un ensemble de fonctionnalités à TYPO3, mais aussi modifier une fonctionnalité déjà intégrée, sans modifier le code de TYPO3, et donc, le laissant compatible avec les futures versions de TYPO3.

TYPO3 est écrit en PHP (avec des composants Symfony depuis TYPO3 8) et s'appuie sur MySQL/MariaDB, PostgreSQL ou SQLite.


Autres
------

Dans l’univers de la gestion de contenu, l’offre open source est particulièrement vigoureuse. Pour preuve, au-delà des produits présentés précédemment, on peut également citer les outils ci-dessous :

- WordPress, qui dépasse largement le cadre du blog et motorise une part considérable du web (section :doc:`/web-communication/blog-wiki-et-forum`): https://wordpress.org
- Plone: https://plone.org
- SilverStripe: https://www.silverstripe.org
- MODX: https://modx.com
- CMS Made Simple: https://www.cmsmadesimple.org
- ApostropheCMS (anciennement Apostrophe): https://apostrophecms.com
- Magnolia: https://www.magnolia-cms.com
- Silverpeas: https://www.silverpeas.org
- Umbraco: https://umbraco.com
- OpenCMS: https://www.opencms.org
- Sulu (CMS Symfony): https://sulu.io
- Grav (CMS sans base de données): https://getgrav.org

Une catégorie s'est imposée depuis la précédente édition de ce guide, celle des CMS *headless*, qui exposent le contenu via une API et laissent le rendu à une application front-end :

- Strapi (Node.js, éditeur français): https://strapi.io
- Directus (Node.js, s'appuie sur une base SQL existante): https://directus.io
- Payload CMS (Node.js/TypeScript): https://payloadcms.com
- Ghost, orienté publication éditoriale et lettres d'information: https://ghost.org

Les éditions précédentes de ce guide citaient également Zope, Infoglue, Mambo, Apache Lenya (retiré à l'*Attic* d'Apache) et Centurion : ces projets ne sont plus maintenus et ne doivent plus être retenus pour de nouveaux développements.

Comparaison synthétique
-----------------------

Le tableau ci-dessous synthétise les principales solutions de gestion de contenu web, y compris les CMS *headless* traités plus haut.

.. list-table::
   :header-rows: 1

   * - CMS
     - Site
     - Porteur
     - Licence
     - Langages/Technologies
     - Caractéristiques distinctives
     - Année de création
   * - Drupal
     - https://www.drupal.org/
     - une communauté
     - GPL v2+
     - PHP (Symfony), MySQL/MariaDB, PostgreSQL
     - Extensibilité, écosystème de modules considérable, gestion fine des droits
     - 2000
   * - WordPress
     - https://wordpress.org
     - une communauté (WordPress Foundation)
     - GPL v2+
     - PHP, MySQL/MariaDB
     - CMS le plus déployé au monde, écosystème d'extensions et de thèmes gigantesque
     - 2003
   * - Wagtail
     - https://wagtail.org/
     - une entreprise (Torchbox) et une communauté
     - BSD
     - Python, Django
     - Ergonomie éditoriale soignée, socle Django, architecture de plugins
     - 2014
   * - Ibexa DXP (ex-eZ Publish)
     - https://www.ibexa.co/
     - un éditeur (Ibexa)
     - GPL v2 (édition OSS) et propriétaire
     - PHP (Symfony), MySQL/MariaDB, PostgreSQL, Solr
     - Modèle de contenu objet, multilinguisme, positionnement DXP
     - 1999
   * - Jahia
     - https://www.jahia.com/
     - un éditeur (Jahia)
     - GPL v2 et propriétaire
     - Java, JCR (JSR-283), GraphQL
     - Portail JEE et CMS intégrés, édition en contexte, gestion multi-sites
     - 2002
   * - Joomla
     - https://www.joomla.org/
     - une communauté
     - GPL v2+
     - PHP, MySQL/MariaDB
     - Interface d'administration conviviale, adapté aux non-techniciens
     - 2005
   * - SPIP
     - https://www.spip.net/
     - une communauté
     - GPL
     - PHP, MySQL/MariaDB, PostgreSQL, SQLite
     - Simplicité d'utilisation et de déploiement, forte implantation associative et publique en France
     - 2001
   * - TYPO3
     - https://typo3.org/
     - une association (TYPO3 Association)
     - GPL v2+
     - PHP (Symfony), MySQL/MariaDB, PostgreSQL
     - Extensibilité par modules, richesse fonctionnelle, forte implantation germanophone
     - 2000
   * - Plone
     - https://plone.org
     - une fondation (Plone Foundation)
     - GPL v2
     - Python, Zope
     - Sécurité et gestion des droits avancées, workflow de publication
     - 2001
   * - Silverpeas
     - https://www.silverpeas.org
     - un éditeur français (Silverpeas)
     - AGPL v3
     - Java
     - Gestion de contenu et collaboration intégrées
     - 2002
   * - Magnolia
     - https://www.magnolia-cms.com
     - une entreprise (Magnolia International)
     - GPL et propriétaire
     - Java, JCR
     - Support des normes JCR, extensibilité, orientation entreprise
     - 2003
   * - Umbraco
     - https://umbraco.com
     - une entreprise (Umbraco HQ)
     - MIT
     - C#, .NET
     - Référence du CMS open source dans l'écosystème Microsoft
     - 2000
   * - Sulu
     - https://sulu.io
     - une entreprise (Sulu GmbH)
     - MIT
     - PHP (Symfony)
     - CMS Symfony natif, orienté développeurs et sites d'entreprise
     - 2013
   * - Strapi
     - https://strapi.io
     - un éditeur français (Strapi)
     - MIT (Community) et propriétaire (Enterprise)
     - Node.js, TypeScript
     - CMS headless, API REST et GraphQL générées, très large adoption
     - 2015
   * - Directus
     - https://directus.io
     - une entreprise (Monospace)
     - BSL 1.1 (source-available)
     - Node.js, TypeScript, SQL
     - Couche d'administration et d'API au-dessus d'une base SQL existante
     - 2004
   * - Ghost
     - https://ghost.org
     - une fondation (Ghost Foundation)
     - MIT
     - Node.js
     - Publication éditoriale, abonnements et lettres d'information
     - 2013
