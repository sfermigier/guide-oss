ERP / PGI
=========

Le monde du progiciel de gestion intégré (PGI, ou ERP en anglais), est à son tour gagné par des solutions open source arrivées à maturité.

Dans un premier temps, les ERP open source permettent à des petites PME de disposer d'outils de gestion complets au meilleur coût, leur procurant rapidement un gain de compétitivité. Mais déjà, ils remontent l'échelle, et s'adressent à des PME de plus de 1000 salariés, que ce soit dans les secteurs industriels, distribution ou services.

Le domaine étant extrêmement vaste, des différences de couverture fonctionnelle peuvent destiner un produit de préférence à tel ou tel secteur d'activité. Mais l'un des critères de choix les plus importants est la flexibilité, l'extensibilité, et donc les bases technologiques qui permettront à un produit donné d'être adapté à une diversité de contextes, avec très peu de développements spécifiques.

Des produits comme Odoo, Dolibarr, ERPNext ou ERP5 tiennent la corde des ERP open source. La convergence ERP/CRM/CMS/e-business, poussée par l'intégration du e-commerce au cœur du métier de l'entreprise, conduit également des logiciels de e-commerce à proposer des fonctions de plus en plus proches de celles d'un ERP.



ERP5
----

:Site: https://www.erp5.com/
:Porteur: un éditeur français (Nexedi)
:Licence: GPL

ERP5 a été développé à partir de 2001 par l'Ingénieur de Mines Jean-Paul Smets. Grâce à sa conception radicalement différente des autres ERP, ERP5 a remplacé avec succès des ERP propriétaires dans plusieurs entreprises multinationales, notamment au Japon et en Allemagne, ainsi que dans une banque centrale.

Selon Brian Prentice, analyste chez Gartner, la force d'ERP5 tient à la fois à son modèle conceptuel et à son architecture technique.

Alors que la plupart des ERP a besoin de milliers de tables, ERP5 parvient à unifier les sciences de gestion autour d'un modèle abstrait à 5 classes qui a fait l'objet de plusieurs publications scientifiques et a prouvé sa capacité à épouser un très large spectre de besoins fonctionnels: budget, comptabilité, CRM, achats, ventes, stock, production, RH, supply chain, projets, logistique, KM. Il intègre également un CMS multilingue complet, une suite bureautique en ligne, une GED, un moteur de workflows d'entreprise et un système de e-business capable d'intégrer les ventes de plusieurs sites, notamment Prestashop, Magento et OSCommerce. C'est aussi depuis peu un système de gestion et de facturation pour le Cloud Computing.

Alors que la plupart des ERP modernes fait appel à une architecture de type Object Relational Mapper (ORM), ERP5 fait appel à une base NoSQL de type objet (NEO) associée à un moteur d'indexation relationnel (MariaDB) et plein texte (Mroonga, Sphinx). ERP5 permet ainsi la migration de données sans interruption de service lors des mises à jour. Cette architecture "search based" est adaptée aux systèmes critiques en 24/7. Son moteur de sécurité par règles simplifie la gestion de droits d'accès dans les grandes organisations à organigramme matriciel (site, fonction, projet, service). ERP5 intègre le support natif du protocole git et permet le développement en ligne du code dans le navigateur de façon collaborative.

ERP5 est développé principalement en Python par la société française Nexedi.


Odoo
----

:Site: https://www.odoo.com/
:Porteur: un éditeur belge (Odoo)
:Licence: LGPL v3 (édition Community) et propriétaire (édition Enterprise)

Odoo (anciennement Tiny ERP puis OpenERP) a été fondé en 2005 en Belgique par Fabien Pinckaers. Depuis la version 9 (2015), le produit est décliné en deux éditions : une édition Community sous licence LGPL v3 et une édition Enterprise propriétaire, qui ajoute notamment des modules métier, les applications mobiles et le support de l'éditeur.

Odoo combine à la fois la force d'un éditeur et celle d'une large communauté, comprenant ses intégrateurs présents dans le monde entier, qui balise l’ensemble des cas d'usages et fournit de précieux retours, notamment sous forme de modules réutilisables. Tout ceci est rendu possible par une réelle innovation technologique qui s'appuie sur des standards reconnus en termes de base de données et de webservices. Odoo couvre tous les besoins, tels que ventes, achats, rh, projets, comptabilité, logistique, stock, production, facturation, ... et son framework permet de l'adapter rapidement aux contextes spécifiques, que ce soit par le paramétrage de nouveaux workflows, de nouvelles informations, ou de tableaux de bord pour une toujours plus grande efficacité de l'ERP en entreprise.

Odoo est écrit en Python et repose sur un framework orienté objet. La base de données PostgreSQL est utilisée.


OFBiz
-----

:Site: https://ofbiz.apache.org/
:Porteur: une fondation (Apache)
:Licence: Apache

Le projet Open For Business (« Ofbiz ») est né en 2001, et a terminé sa première phase de développement vers 2003 sous l’impulsion de ses 2 créateurs : David Jones et Andrew Zenesky.

Depuis le projet s’est enrichi de nombreux modules fonctionnels. En 2006, il a même été soumis comme projet « incubator » à la fondation Apache. Il en est très rapidement sorti comme projet approuvé de très bon niveau. A la différence de Compiere ou d’Odoo, OFBiz n’a pas vocation à être un ERP prêt à l’emploi. Il s’agit d’un framework ERP pour développer des logiciels d’entreprise. D’ailleurs l’outil s’est fortement spécialisé dans les interfaces d’e-commerce ces dernières années.

OFBiz est écrit en Java.


iDempiere (héritier de Compiere)
--------------------------------

:Site: https://idempiere.org
:Porteur: une communauté
:Licence: GPL v2

Compiere, développé à partir de 1999 par l’allemand Jörg Janke (fort de ses 20 années d’expérience chez SAP puis Oracle), a longtemps été l’ERP open source Java de référence. Racheté par Consona en 2010, puis passé dans le giron d’Aptean, il n’existe plus en tant que projet open source : ce sont ses forks communautaires qui poursuivent son histoire, d’abord ADempiere (2006) puis iDempiere (2011), aujourd’hui le plus actif des deux.

iDempiere hérite du concept d’*application dictionary* (modèle de méta-programmation permettant d’ajuster la persistance relationnelle aux structures de données métier personnalisées et à leurs interfaces), prototypé dès la fin des années 1980. D’un point de vue fonctionnel, la couverture est large et adaptée aux PME/PMI : gestion des ventes, achats, stock et logistique, gestion comptable et financière, gestion de la production, etc.

iDempiere est écrit en Java, s’appuie sur OSGi et sur les bases PostgreSQL ou Oracle.


Dolibarr
--------

:Site: https://www.dolibarr.org/
:Porteur: Communautaire
:Licence: GPL v3

Dolibarr a été développé initialement par Rodolphe Quiédeville en avril 2002 (depuis basculé sur GitHub). La gestion des contributions est pilotée par Laurent Destailleur (Benevolent Dictator for Life).

Dolibarr est porté par une large communauté d'intégrateur français, mais aussi allemand, italien, espagnol, etc... et dispose désormais d'une diffusion internationale.

Une association a été créée en France. Elle a pour objet le développement (au sens promotion et non codage informatique), la documentation, la protection, la promotion, la sécurisation et la diffusion du logiciel libre de gestion d'activité professionnelle ou associative Dolibarr ERP et CRM.

Une place de marché gérée par l'association Dolibarr https://www.dolistore.com/ met à disposition plusieurs centaines de modules complémentaires permettant de compléter les fonctionnalités standard de Dolibarr.

Dolibarr est écrit en PHP. La base de données MySQL/MariaDB ou PostgreSQL (support limité sur les modules complémentaires) est utilisée.


ERPNext
-------

:Site: https://frappe.io/erpnext
:Porteur: un éditeur indien (Frappe Technologies)
:Licence: GPL v3

Lancé en 2008 par Frappe Technologies, ERPNext est devenu l'un des ERP open source les plus déployés au monde, en particulier dans les PME et les pays émergents.

Sa couverture fonctionnelle est large : comptabilité, ventes, achats, stocks, production, projets, RH et paie, CRM, maintenance des actifs. Le produit s'appuie sur le framework low-code Frappe, qui permet de définir de nouveaux objets métier, formulaires et workflows sans développement lourd, ce qui explique en grande partie son adoption.

ERPNext est écrit en Python et JavaScript, et s'appuie sur MariaDB (ou PostgreSQL, en support plus récent).


Tryton
------

:Site: https://www.tryton.org/
:Porteur: une fondation (Tryton Foundation)
:Licence: GPL v3

Tryton est né en 2008 d'un fork de TinyERP (l'ancêtre d'Odoo), avec le parti pris d'un noyau minimal et strictement communautaire, sans édition commerciale parallèle.

Le projet privilégie la rigueur du modèle de données et la stabilité des interfaces de programmation, avec deux versions par an et un chemin de migration documenté. La couverture fonctionnelle (comptabilité, ventes, achats, stock, production, projets) s'étend par modules, y compris pour des secteurs spécifiques (santé avec GNU Health, par exemple).

Tryton est écrit en Python et s'appuie sur PostgreSQL.
