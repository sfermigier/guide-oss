# CMS

La gestion de contenu web recouvre aujourd’hui une large palette de besoins : sites d’informations, sites Corporate, sites de services, extranets sécurisés, intranets participatifs, espaces communautaire...

Pour couvrir ce périmètre, il existe d’excellentes solutions open source au périmètre très large qui sont devenues des standards dans l’univers de la gestion de contenus tant elles dominent par leur capacité, leur modularité et leur périmètre fonctionnel et technique.

Au côté de ces solutions dominantes, la convergence ERP/CRM/CMS/e-business poussée par la croissance e-commerce conduit des applicatifs issus d'autres domaines fonctionnels (ERP, CRM) à intégrer des fonctions de CMS équivalents aux meilleurs produits dédiés du marché.

## Drupal

Site
: <https://www.drupal.org/>

Porteur
: une communauté

Licence
: GPL

Drupal est un CMS aux multiples facettes. Conçu à l’origine pour être un blog collectif, il trouve aujourd’hui des applications très variées, du site corporate au portail communautaire. Il a été conçu dans les années 2000 par Dries Buytaert et connaît depuis un succès mondial. Une importante communauté s’est créée autour du produit.

La force de ce CMS est son extensibilité. Il accueille très facilement de nombreux modules complémentaires (forum, galerie photos, sondage, formulaire, newsletter, messagerie, chat, enquête, paiement en ligne, calendrier partagé, etc.). Les modules communautaires permettent de construire des espaces de publication collaboratifs ; pour un réseau social d’entreprise clés en main, voir plutôt la section [Réseaux sociaux d’entreprise](reseaux-sociaux-entreprise-rse.md), la distribution Drupal Commons n’étant plus maintenue.

Drupal est publié sous licence GNU GPL v2 (ou ultérieure) et est pleinement open source. Des offres de support existent, notamment via la société Acquia (<https://www.acquia.com>), fondée par le créateur du projet.

D'un point de vue technique, Drupal s'est profondément modernisé depuis Drupal 8 (2015) : le cœur s'appuie désormais sur les composants Symfony, Twig pour les gabarits et Composer pour la gestion des dépendances. Les versions majeures se succèdent à un rythme régulier (Drupal 10 en 2022, Drupal 11 en 2024), avec une distribution clés en main, Drupal CMS, destinée à réduire le coût d'entrée pour les sites standards. Attention aux migrations : Drupal 7, longtemps majoritaire, est en fin de vie depuis janvier 2025 et ne reçoit plus de correctifs de sécurité.

Drupal fonctionne avec PHP et MySQL/MariaDB ou PostgreSQL.

## Wagtail

Site
: <https://wagtail.org/>

Porteur
: une entreprise (Torchbox) et une communauté

Licence
: BSD

Wagtail est un CMS développé depuis 2014 sur la base du framework web Django.

Wagtail comprend toutes les fonctionnalités de publication de base dont la plupart des grands sites complexes ont besoin, sans limitations concernant l'apparence ou le comportement des pages construites dans Wagtail. Pour les cas particuliers qui ne sont pas couverts par le framework de base, une architecture de plugins permet de l'étendre. [Plusieurs centaines de plugins](https://wagtail.org/packages/) sont disponibles couvrant des besoins comme: types de contenus, SEO, workflows (validation), E-commerce, etc.

Wagtail est développé en Python.

## Ibexa DXP (anciennement eZ Publish)

Site
: <https://ibexa.ai/>

Porteur
: un éditeur (Ibexa, anciennement eZ Systems)

Licence
: GPL v2 pour l'édition open source, propriétaire pour les éditions commerciales

La solution eZ Publish a été créée en 1999 par la société norvégienne eZ Systems. Renommée eZ Platform lors de sa réécriture sur Symfony, elle est devenue Ibexa DXP en 2020, en même temps que l'éditeur prenait le nom d'Ibexa.

Sur les fondamentaux de la gestion de contenus, le produit pousse l'approche objet jusqu'au bout, en faisant de chaque contenu un objet auquel s'appliquent toutes les méthodes disponibles : multi-positionnement, gestion des versions, multilinguisme, relations entre contenus, droits d'accès, workflow. Cette conception en fait un CMS hautement paramétrable, désormais positionné comme une plateforme d'expérience numérique (DXP) incluant des briques e-commerce et PIM.

Attention à l'évolution du modèle : la branche historique eZ Publish Legacy n'est plus maintenue. Les fonctionnalités les plus riches sont réservées aux éditions commerciales. Une édition open source (Ibexa OSS, sous GPL v2) reste disponible.

Sur le plan technique, le produit est écrit en PHP sur le framework Symfony et s'appuie sur MySQL/MariaDB ou PostgreSQL, avec Solr ou Elasticsearch pour la recherche.

## Jahia

Site
: <https://www.jahia.com/>

Porteur
: un éditeur (Jahia Solutions Group)

Licence
: Apache 2.0 ou licence commerciale de l'éditeur

Jahia est une plateforme de gestion de contenu et de portail en Java, éditée par une société suisse. Elle réunit l'édition en contexte, la gestion multisite, les versions, les workflows, le multilinguisme et des droits fins et expose ses contenus par une API GraphQL pour les usages *headless*.

Le code de la plateforme est publié sous double licence. Les modules commerciaux et le support relèvent de l'offre de l'éditeur : on vérifiera de quel côté tombent les fonctions attendues.

Jahia est écrite en Java.

## Joomla

Site
: <https://www.joomla.org/>

Porteur
: une communauté

Licence
: GPL

Joomla est un CMS développé à partir de Mambo en 2005. Il a été créé suite à un différend entre les développeurs principaux et la société coordinatrice des développements. Aujourd’hui, la majorité des développeurs de la communauté se consacre à Joomla, ce qui fait pencher la balance en sa faveur.

Cet outil se démarque principalement par la convivialité de son interface d’administration. Le mot d’ordre étant de « donner un contrôle total du produit à un non-technicien ». Création de pages, catégorisation, recherche, statistiques d’accès, urls significatives ainsi que de nombreux modules sont directement intégrés et ne demandent pas de connaissances spécifiques pour leur mise en œuvre. Ce CMS conviendra parfaitement pour des sites personnels mais pourra également répondre aux besoins de certains sites professionnels ; ceux notamment de type Corporate (simple publication).

Joomla est une solution 100% communautaire publiée sous licence GNU GPL.

Joomla est écrit en PHP et utilise une base de données MySQL.

## SPIP

Site
: <https://www.spip.net/>

Porteur
: une communauté

Licence
: GPL

A l’origine, en 2001, SPIP était principalement utilisé par des internautes pour gérer leur site web personnel, ou pour des sites d'associations, mais SPIP a grandi et est maintenant utilisé par des organismes privés ou publics, pour gérer leur site web professionnel.

SPIP fait partie des rares CMS à pouvoir prétendre à plusieurs milliers de références à travers le monde. Cette réussite s’explique par la simplicité du produit : simplicité d’utilisation, mais aussi simplicité de déploiement et d’adaptation. En contrepartie de cette simplicité, SPIP présente quelques limitations sur des fonctionnalités clés de gestion de contenus, ce qui le limite clairement au monde des outils de gestion de contenus orienté ‘web’.

SPIP est un projet open source français (licence GPL). Sa communauté peut être qualifiée d’active, avec plusieurs versions par an et des centaines – voire des milliers – de membres.

SPIP est un logiciel écrit en PHP qui s'appuie sur les bases de données MySQL, PostgreSQL et SQLite. Il propose un interface privée simplifiée fondée sur l’Ajax, une page de téléchargement et d’installation de plugins, la gestion des conflits, une API et de nouvelles fonctions pour le développement de templates.

## TYPO3

Site
: <https://typo3.org/>

Porteur
: une association (TYPO3 Association) et une communauté

Licence
: GPL

TYPO3 a été créé par le Danois Kasper Skårhøj. Sorti en 2000, il est aujourd’hui porté par la TYPO3 Association et reste particulièrement implanté dans les pays germaniques.

TYPO3 vise les sites institutionnels et les ensembles de sites : gestion multi-sites et multilingue, droits et circuits de validation, espaces de travail, versions, cache et gabarits. Ses extensions peuvent ajouter des fonctions ou modifier celles du cœur sans toucher à son code, ce qui préserve les montées de version. En contrepartie, la prise en main est plus longue que celle des CMS plus simples.

TYPO3 est écrit en PHP (avec des composants Symfony depuis TYPO3 8) et s'appuie sur MySQL/MariaDB, PostgreSQL ou SQLite.

## Autres

Dans l’univers de la gestion de contenu, l’offre open source est particulièrement vigoureuse. Pour preuve, au-delà des produits présentés précédemment, on peut également citer les outils ci-dessous :

- WordPress, qui dépasse largement le cadre du blog et motorise une part considérable du web (section [Blogs, wikis et forums](blog-wiki-et-forum.md)): <https://wordpress.org>
- Plone: <https://plone.org>
- SilverStripe: <https://www.silverstripe.org>
- MODX: <https://modx.com>
- CMS Made Simple: <https://www.cmsmadesimple.org>
- ApostropheCMS (anciennement Apostrophe): <https://apostrophecms.com>
- Magnolia: <https://www.magnolia-cms.com>
- Silverpeas: <https://www.silverpeas.org>
- Umbraco: <https://umbraco.com>
- OpenCMS: <https://www.opencms.org>
- Sulu (CMS Symfony): <https://sulu.io>
- Grav (CMS sans base de données): <https://getgrav.org>

Les CMS *headless* exposent le contenu via une API et laissent le rendu à une application front-end :

- Strapi (Node.js, éditeur français): <https://strapi.io>
- Payload CMS (Node.js/TypeScript): <https://payloadcms.com>
- Ghost, orienté publication éditoriale et lettres d'information: <https://ghost.org>

Zope (comme CMS), Infoglue, Mambo, Apache Lenya (retiré à l'*Attic* d'Apache) et Centurion ne doivent plus être retenus pour de nouveaux développements.

## Comparaison synthétique

Le tableau ci-dessous synthétise les principales solutions de gestion de contenu web, y compris les CMS *headless* traités plus haut.

| CMS | Site | Porteur | Licence | Langages/Technologies | Caractéristiques distinctives | Année de création |
|----|----|----|----|----|----|----|
| Drupal | <https://www.drupal.org/> | une communauté | GPL v2+ | PHP (Symfony), MySQL/MariaDB, PostgreSQL | Extensibilité, écosystème de modules considérable, gestion fine des droits | 2000 |
| WordPress | <https://wordpress.org> | une communauté (WordPress Foundation) | GPL v2+ | PHP, MySQL/MariaDB | CMS le plus déployé au monde, écosystème d'extensions et de thèmes gigantesque | 2003 |
| Wagtail | <https://wagtail.org/> | une entreprise (Torchbox) et une communauté | BSD | Python, Django | Ergonomie éditoriale soignée, socle Django, architecture de plugins | 2014 |
| Ibexa DXP (ex-eZ Publish) | <https://ibexa.ai/> | un éditeur (Ibexa) | GPL v2 (édition OSS) et propriétaire | PHP (Symfony), MySQL/MariaDB, PostgreSQL, Solr | Modèle de contenu objet, multilinguisme, positionnement DXP | 1999 |
| Jahia | <https://www.jahia.com/> | un éditeur (Jahia Solutions Group) | Apache 2.0 ou commerciale | Java, JCR (JSR-283), GraphQL | Portail JEE et CMS intégrés, édition en contexte, gestion multi-sites | 2002 |
| Joomla | <https://www.joomla.org/> | une communauté | GPL v2+ | PHP, MySQL/MariaDB | Interface d'administration conviviale, adapté aux non-techniciens | 2005 |
| SPIP | <https://www.spip.net/> | une communauté | GPL | PHP, MySQL/MariaDB, PostgreSQL, SQLite | Simplicité d'utilisation et de déploiement, forte implantation associative et publique en France | 2001 |
| TYPO3 | <https://typo3.org/> | une association (TYPO3 Association) | GPL v2+ | PHP (Symfony), MySQL/MariaDB, PostgreSQL | Extensibilité par modules, richesse fonctionnelle, forte implantation germanophone | 2000 |
| Plone | <https://plone.org> | une fondation (Plone Foundation) | GPL v2 | Python, Zope | Sécurité et gestion des droits avancées, workflow de publication | 2001 |
| Silverpeas | <https://www.silverpeas.org> | un éditeur français (Silverpeas) | AGPL v3 | Java | Gestion de contenu et collaboration intégrées | 2002 |
| Magnolia | <https://www.magnolia-cms.com> | une entreprise (Magnolia International) | GPL v3 et propriétaire | Java, JCR | Support des normes JCR, extensibilité, orientation entreprise | 2003 |
| Umbraco | <https://umbraco.com> | une entreprise (Umbraco HQ) | MIT | C#, .NET | Référence du CMS open source dans l'écosystème Microsoft | 2000 |
| Sulu | <https://sulu.io> | une entreprise (Sulu GmbH) | MIT | PHP (Symfony) | CMS Symfony natif, orienté développeurs et sites d'entreprise | 2013 |
| Strapi | <https://strapi.io> | un éditeur français (Strapi) | MIT (Community) et propriétaire (Enterprise) | Node.js, TypeScript | CMS headless, API REST et GraphQL générées, très large adoption | 2015 |
| Ghost | <https://ghost.org> | une fondation (Ghost Foundation) | MIT | Node.js | Publication éditoriale, abonnements et lettres d'information | 2013 |
