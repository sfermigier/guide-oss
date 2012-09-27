ERP / PGI
=========

Le monde du progiciel de gestion intégré (PGI, ou ERP en anglais), est à son tour gagné par des solutions open source arrivées à maturité.

Dans un premier temps, les ERP open source permettent à des petites PME de disposer d'outils de gestion complets au meilleur coût, leur apportant rapidement un vrai bénéfice en termes de compétitivité. Mais déjà, ils remontent l'échelle, et s'adressent à des PME de plus de 1000 salariés, que ce soit dans les secteurs industriels, distribution ou services.

Le domaine étant extrêmement vaste, des différences de couverture fonctionnelle peuvent destiner un produit de préférence à tel ou tel secteur d'activité. Mais l'un des critères de choix les plus importants est la flexibilité, l'extensibilité, et donc les bases technologiques qui permettront à un produit donné d'être adapté à une diversité de contextes, avec très peu de développements spécifiques.

Des produits comme Compiere, ERP5, OpenBravo ou OpenERP tiennent la corde des ERP open source. la convergence ERP/CRM/CMS/e-business poussée par l'intégration du e-commerce au coeur de métier de l'entreprise conduit égalemet des logiciels de e-commerce à proposer des fonctions de plus en plus proches de celles d'un ERP.


Compiere
--------

:Version: 3.2 (Community Edition)
:Site: www.compiere.com
:Porteur: un éditeur (Compiere Inc.)
:Licence: MPL

Compiere a été développé à ses débuts par l’allemand Jorg Janke, lequel a su mettre à profit ses 20 années d’expérience chez SAP puis Oracle et sa maitrise des produits ADV/Orga, Unisys, R/2, R/3.

Les concepts de « l’application dictionnary » (modèle de méta-programmation à la base de Compiere permettant l’adéquation de la persistance relationnelle avec les structures de données métiers personnalisées et leurs interfaces) ont été prototypés dès 1988 pour SAP, puis mis au service du projet libre Compiere. Ce dernier a connu de beaux succès ses dernières années (dans le secteur de la distribution et du service tout particulièrement) grâce notamment à son support de la base de données Oracle et à son socle Java. D’un point de vue fonctionnel, Compiere est relativement complète notamment pour les PME/PMI, on peut par exemple citer : gestion des ventes, des fonctions d’achats, de fonctions de stock et de logistique, gestion comptable et financière, gestion de la production, etc.

Compiere est écrit sur une base Java.




ERP5
----

:Version: 5.4.7
:Site: www.erp5.com
:Porteur: un éditeur (Nexedi)
:Licence: GPL

ERP5 a été développé à partir de 2001 par l'ingénieur de Mines Jean-Paul Smets, pour gérer l'émission monétaire d'une banque centrale et la production d'un industriel de l'habillement. Grâce à sa conception radicalement différente des autres ERP, c'est aujourd'hui probablement le seul ERP open source à avoir remplacé des ERP propriétaires dans plusieurs entreprises multinationales, notamment au Japon et en Allemagne.

La force d'ERP5 tient à la fois à son modèle conceptuel à de son architecture technique.

Alors que la plupart des ERP a besoin de milliers de tables ou d'ontologies à plusieurs milliers de termes, ERP5 parvient à unifier les sciences de gestion autour d'un modèle abstrait à 5 classes qui a fait l'objet de plusieurs publications scientifiques et a prouvé sa capacité à épouser un très large spectre de besoins fonctionnels:  finance et comptabilité, gestion de la relation client (CRM), gestion des achats, des ventes et de l'e-commerce, gestion de la chaine d'approvisionnement (SCM), gestion de la production (PDM), gestion des stocks, de la logistique et des ressources humaines, gestion documentaire, gestion des connaissances. Ainsi ERP5 est à la fois un ERP, mais aussi un CRM, un MRP, un SCM, un PDM, un ECM, une plate-forme de e-Business et un KM.

Alors que la plupart des ERP modernes fait appel à une architecture de type Object Relational Mapper (ORM), ERP5 fait appel à une base NoSQL de type objet (NEO) associée à un moteur d'indexation relationnel (MariaDB) et plein texte (Mroonga). ERP5 résoud ainsi les limites des ORM sur l'adaptation d'impédance et permet la migration de données sans interruption de service lors des mises à jour du code ou des changements de modèles de données. Cette architecture "search based" permet la mise en oeuvres de systèmes critiques en 24/7, notamment dans l'aérospatiale et pour les systèmes de paiements. ERP5 permet également un développement intégralement en ligne dans le navigateur "à chaud", à l'image des PaaS les plus récents, avec une gestion native du protocole git pour la gestion des révisions.

ERP5 est développé par la société française Nexedi, membre de Systematic. La base de données "NEO" d'ERP5, seule base de données NoSQL à la fois transactionnelle et répartie, a fait l'objet d'un projet labellisé par le pôle Systematic qui a fait la preuve théorique de sa cohérence transactinelle. ERP5 fait également partie du portail du logiciel public du gouvernement brésilien avec un communauté de plus de 9000 membres et est enseigné dans plusieurs dizaines d'universités dans le monde dans le cadre du programme "One Student One ERP".

Dernière différence: suivant les recommandations Brian Prentice, analyste chez Gartner, Nexedi considère que la communauté d'ERP5 sont ses utilisateurs et non les intégrateurs. C'est pourquoi Nexedi encourage les entreprises qui adoptent ERP5 à développer en interne des compétences et à contribuer à son coeur fonctionnel.



OFBiz
-----

:Version: 10.04
:Site: http://ofbiz.apache.org
:Porteur: une fondation (Apache)
:Licence: Apache

Le projet Open For Business (« Ofbiz ») est né en 2001, et a terminé sa première phase de développement vers 2003 sous l’impulsion de ses 2 créateurs : David Jones et Andrew Zenesky.

Depuis le projet s’est enrichi de nombreux modules fonctionnels. En 2006, il a même été soumis comme projet « incubator » à la fondation Apache. Il en est très rapidement sorti comme projet approuvé de très bon niveau. A la différence de Compiere ou d’OpenERP, OFBiz n’a pas la vocation à être un ERP clé en main. Il s’agit d’un framework ERP pour développer des logiciels d’entreprise. D’ailleurs l’outil s’est fortement spécialisé dans les interfaces d’e-commerce ces dernières années.

OFBiz est écrit en Java.




Openbravo
---------

:Version: 3.0
:Site: www.openbravo.com
:Porteur: un éditeur (Openbravo)
:Licence: licence publique Openbravo, basée sur la licence open source MPL (1.1).

Openbravo est une solution d’origine espagnole basée sur l’ERP Compiere (autre produit open source présenté dans ce livre) créé en 2001. Le projet, appelé initialement Tecnicia est devenu open source en 2005.

Openbravo a forké tout le code métier en PL/SQL de Compiere ainsi que son moteur de gestion d’entities et l’a transposé dans une interface web assise sur un serveur Java. Interfaces qui constituent le point fort du produit : parmi les plus séduisantes et les plus ergonomiques. Malgré une grosse levée de fonds en 2005, le produit a un dynamisme modéré notamment en termes de références. Openbravo cible le marché des ERP pour PME et dispose d’un périmètre large bien qu’inférieur à OpenERP.

L’éditeur est solide et apte à fournir un support professionnel.

D’un point de vue technique, Openbravo est basé sur des technologies web dont le JEE et l’Ajax.




OpenERP
-------

:Version: 6.0.3
:Site: www.openerp.com
:Porteur: un éditeur (OpenERP)
:Licence: AGPL v3

OpenERP (anciennement Tiny ERP) a été fondé en 2005 en Belgique par Fabien Pinckaers.

OpenERP combine à la fois la force d'un éditeur et celle d'une large communauté, comprenant ses intégrateurs présents dans le monde entier, qui balise l’ensemble des cas d'usages et fournit de précieux retours, notamment sous forme de modules réutilisables. Tout ceci est rendu possible par une réelle innovation technologique qui s'appuie sur des standards reconnus en termes de base de données et de webservices. OpenERP couvre tous les besoins, tels que ventes, achats, rh, projets, comptabilité, logistique, stock, production, facturation, ... et son framework permet de l'adapter rapidement aux contextes spécifiques, que ce soit par le paramétrage de nouveaux workflows, de nouvelles informations, ou de tableaux de bord pour une toujours plus grande efficacité de l'ERP en entreprise.

OpenERP est écrit en Python et repose sur un framework orienté objet. La base de données PostgreSQL est utilisée.

