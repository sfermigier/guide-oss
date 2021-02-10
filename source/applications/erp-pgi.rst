ERP / PGI
=========

Le monde du progiciel de gestion intégré (PGI, ou ERP en anglais), est à son tour gagné par des solutions open source arrivées à maturité.

Dans un premier temps, les ERP open source permettent à des petites PME de disposer d'outils de gestion complets au meilleur coût, leur apportant rapidement un vrai bénéfice en termes de compétitivité. Mais déjà, ils remontent l'échelle, et s'adressent à des PME de plus de 1000 salariés, que ce soit dans les secteurs industriels, distribution ou services.

Le domaine étant extrêmement vaste, des différences de couverture fonctionnelle peuvent destiner un produit de préférence à tel ou tel secteur d'activité. Mais l'un des critères de choix les plus importants est la flexibilité, l'extensibilité, et donc les bases technologiques qui permettront à un produit donné d'être adapté à une diversité de contextes, avec très peu de développements spécifiques.

Des produits comme Compiere, ERP5 ou Odoo tiennent la corde des ERP open source. la convergence ERP/CRM/CMS/e-business poussée par l'intégration du e-commerce au coeur de métier de l'entreprise conduit égalemet des logiciels de e-commerce à proposer des fonctions de plus en plus proches de celles d'un ERP.



ERP5
----

:Version: 5.4.7
:Site: www.erp5.com
:Porteur: un éditeur (Nexedi)
:Licence: GPL

ERP5 a été développé à partir de 2001 par l'Ingénieur de Mines Jean-Paul Smets. Grâce à sa conception radicalement différente des autres ERP, ERP5 a remplacé avec succès des ERP propriétaires dans plusieurs entreprises multinationales, notamment au Japon et en Allemagne, ainsi que dans une banque centrale.

Selon Brian Prentice, analyste chez Gartner, la force d'ERP5 tient à la fois à son modèle conceptuel et à son architecture technique.

Alors que la plupart des ERP a besoin de milliers de tables, ERP5 parvient à unifier les sciences de gestion autour d'un modèle abstrait à 5 classes qui a fait l'objet de plusieurs publications scientifiques et a prouvé sa capacité à épouser un très large spectre de besoins fonctionnels: budget, comptabilité, CRM, achats, ventes, stock, production, RH, supply chain, projets, logistique, KM. Il intègre également un CMS multilingue complet, une suite bureautique en ligne, une GED, un moteur de workflows d'entreprise et un système de e-business capable d'intégrer les ventes de plusieurs sites, notamment Prestashop, Magento et OSCommerce. C'est aussi depuis peu un système de gestion et de facturation pour le Cloud Computing.

Alors que la plupart des ERP modernes fait appel à une architecture de type Object Relational Mapper (ORM), ERP5 fait appel à une base NoSQL de type objet (NEO) associée à un moteur d'indexation relationnel (MariaDB) et plein texte (Mroonga, Sphinx). ERP5 permet ainsi la migration de données sans interruption de service lors des mises à jour. Cette architecture "search based" est adaptée aux systèmes critiques en 24/7. Son moteur de sécurité par règles simplifie la gestion de droits d'accès dans les grandes organisations à organigramme matriciel (site, fonction, projet, service). ERP5 intègre le support natif du protocole git et permet le développement en ligne du code dans le navigateur de façon collaborative.

ERP5 est développé par la société française Nexedi.


Odoo
----

:Version: 14.0
:Site: www.odoo.com
:Porteur: un éditeur (Odoo)
:Licence: AGPL v3

Odoo (anciennement Tiny ERP puis OpenERP) a été fondé en 2005 en Belgique par Fabien Pinckaers.

Odoo combine à la fois la force d'un éditeur et celle d'une large communauté, comprenant ses intégrateurs présents dans le monde entier, qui balise l’ensemble des cas d'usages et fournit de précieux retours, notamment sous forme de modules réutilisables. Tout ceci est rendu possible par une réelle innovation technologique qui s'appuie sur des standards reconnus en termes de base de données et de webservices. Odoo couvre tous les besoins, tels que ventes, achats, rh, projets, comptabilité, logistique, stock, production, facturation, ... et son framework permet de l'adapter rapidement aux contextes spécifiques, que ce soit par le paramétrage de nouveaux workflows, de nouvelles informations, ou de tableaux de bord pour une toujours plus grande efficacité de l'ERP en entreprise.

Odoo est écrit en Python et repose sur un framework orienté objet. La base de données PostgreSQL est utilisée.

OFBiz
-----

:Version: 10.04
:Site: http://ofbiz.apache.org
:Porteur: une fondation (Apache)
:Licence: Apache

Le projet Open For Business (« Ofbiz ») est né en 2001, et a terminé sa première phase de développement vers 2003 sous l’impulsion de ses 2 créateurs : David Jones et Andrew Zenesky.

Depuis le projet s’est enrichi de nombreux modules fonctionnels. En 2006, il a même été soumis comme projet « incubator » à la fondation Apache. Il en est très rapidement sorti comme projet approuvé de très bon niveau. A la différence de Compiere ou d’Odoo, OFBiz n’a pas la vocation à être un ERP clé en main. Il s’agit d’un framework ERP pour développer des logiciels d’entreprise. D’ailleurs l’outil s’est fortement spécialisé dans les interfaces d’e-commerce ces dernières années.

OFBiz est écrit en Java.



Compiere
--------

:Version: 3.2 (Community Edition)
:Site: www.compiere.com
:Porteur: un éditeur (Compiere Inc.)
:Licence: MPL

Compiere a été développé à ses débuts par l’allemand Jorg Janke, lequel a su mettre à profit ses 20 années d’expérience chez SAP puis Oracle et sa maitrise des produits ADV/Orga, Unisys, R/2, R/3.

Les concepts de « l’application dictionnary » (modèle de méta-programmation à la base de Compiere permettant l’adéquation de la persistance relationnelle avec les structures de données métiers personnalisées et leurs interfaces) ont été prototypés dès 1988 pour SAP, puis mis au service du projet libre Compiere. Ce dernier a connu de beaux succès ses dernières années (dans le secteur de la distribution et du service tout particulièrement) grâce notamment à son support de la base de données Oracle et à son socle Java. D’un point de vue fonctionnel, Compiere est relativement complète notamment pour les PME/PMI, on peut par exemple citer : gestion des ventes, des fonctions d’achats, de fonctions de stock et de logistique, gestion comptable et financière, gestion de la production, etc.

Compiere est écrit sur une base Java.


