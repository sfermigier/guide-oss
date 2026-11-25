# ERP / PGI

Le monde du progiciel de gestion intégré (PGI, ou ERP en anglais), est à son tour gagné par des solutions open source arrivées à maturité.

Dans un premier temps, les ERP open source permettent à des petites PME de disposer d'outils de gestion complets au meilleur coût, leur procurant rapidement un gain de compétitivité. Mais déjà, ils remontent l'échelle et s'adressent à des PME de plus de 1000 salariés, que ce soit dans les secteurs industriels, distribution ou services.

Le domaine étant extrêmement vaste, des différences de couverture fonctionnelle peuvent destiner un produit de préférence à tel ou tel secteur d'activité. Mais l'un des critères de choix les plus importants est la flexibilité, l'extensibilité et donc les bases technologiques qui permettront à un produit donné d'être adapté à une diversité de contextes, avec très peu de développements spécifiques.

Des produits comme Odoo, Dolibarr, ERPNext ou ERP5 tiennent la corde des ERP open source. La convergence ERP/CRM/CMS/e-business, poussée par l'intégration du e-commerce au cœur du métier de l'entreprise, conduit également des logiciels de e-commerce à proposer des fonctions de plus en plus proches de celles d'un ERP.

## ERP5

Site
: <https://www.erp5.com/>

Porteur
: un éditeur (Nexedi)

Licence
: GPL

ERP5 a été développé à partir de 2001 par Jean-Paul Smets et la société française Nexedi, pour des activités aux processus particuliers, plutôt que comme un progiciel prêt à l'emploi.

Son originalité est un modèle de données unifié, réduit à quelques classes abstraites, qui couvre comptabilité, achats, ventes, stocks, production, RH, projets et CRM. Le stockage associe la base objet NEO à un index relationnel (MariaDB).

Cette architecture convient aux projets sur mesure et suppose une équipe formée à ses concepts. L'essentiel des compétences se trouve chez Nexedi.

ERP5 est développé principalement en Python.

## Odoo

Site
: <https://www.odoo.com/>

Porteur
: un éditeur (Odoo)

Licence
: LGPL v3 (édition Community) et propriétaire (édition Enterprise)

Odoo (anciennement Tiny ERP puis OpenERP) a été fondé en 2005 en Belgique par Fabien Pinckaers. Depuis la version 9 (2015), le produit est décliné en deux éditions : une édition Community sous licence LGPL v3 et une édition Enterprise propriétaire, qui ajoute notamment des modules métier, les applications mobiles et le support de l'éditeur.

Odoo combine à la fois la force d'un éditeur et celle d'une large communauté, comprenant ses intégrateurs présents dans le monde entier, qui balise l’ensemble des cas d'usages et fournit de précieux retours, notamment sous forme de modules réutilisables. Tout ceci est rendu possible par une réelle innovation technologique qui s'appuie sur des standards reconnus en termes de base de données et de webservices. Odoo couvre tous les besoins, tels que ventes, achats, rh, projets, comptabilité, logistique, stock, production, facturation. Son framework permet de l'adapter rapidement aux contextes spécifiques, que ce soit par le paramétrage de nouveaux workflows, de nouvelles informations, ou de tableaux de bord pour une toujours plus grande efficacité de l'ERP en entreprise.

Odoo est écrit en Python et repose sur un framework orienté objet. La base de données PostgreSQL est utilisée.

## OFBiz

Site
: <https://ofbiz.apache.org/>

Porteur
: une fondation (Apache)

Licence
: Apache

Le projet Open For Business (« Ofbiz ») est né en 2001 et a terminé sa première phase de développement vers 2003 sous l’impulsion de ses 2 créateurs : David Jones et Andrew Zenesky.

Depuis le projet s’est enrichi de nombreux modules fonctionnels. En 2006, il a même été soumis comme projet « incubator » à la fondation Apache. Il en est très rapidement sorti comme projet approuvé de très bon niveau. À la différence de Compiere ou d’Odoo, OFBiz n’a pas vocation à être un ERP prêt à l’emploi. Il s’agit d’un framework ERP pour développer des logiciels d’entreprise. D’ailleurs l’outil s’est fortement spécialisé dans les interfaces d’e-commerce ces dernières années.

OFBiz est écrit en Java.

## iDempiere (héritier de Compiere)

Site
: <https://idempiere.org>

Porteur
: une communauté

Licence
: GPL v2

Compiere, développé à partir de 1999 par l’allemand Jörg Janke (fort de ses 20 années d’expérience chez SAP puis Oracle), a longtemps été l’ERP open source Java de référence. Racheté par Consona en 2010, puis passé dans le giron d’Aptean, il n’existe plus en tant que projet open source : ce sont ses forks communautaires qui poursuivent son histoire, d’abord ADempiere (2006) puis iDempiere (2011), aujourd’hui le plus actif des deux.

iDempiere hérite du concept d’*application dictionary* (modèle de méta-programmation permettant d’ajuster la persistance relationnelle aux structures de données métier personnalisées et à leurs interfaces), prototypé dès la fin des années 1980. D’un point de vue fonctionnel, la couverture est large et adaptée aux PME/PMI : gestion des ventes, achats, stock et logistique, gestion comptable et financière, gestion de la production, etc.

iDempiere est écrit en Java, s’appuie sur OSGi et sur les bases PostgreSQL ou Oracle.

## Dolibarr

Site
: <https://www.dolibarr.org/>

Porteur
: une communauté

Licence
: GPL v3

Dolibarr a été développé initialement par Rodolphe Quiédeville en avril 2002 (depuis basculé sur GitHub). La gestion des contributions est pilotée par Laurent Destailleur (Benevolent Dictator for Life).

Dolibarr est porté par une large communauté d'intégrateurs, notamment en France, en Allemagne, en Italie et en Espagne. Il dispose désormais d'une diffusion internationale.

Une association a été créée en France. Elle a pour objet la promotion, la documentation, la protection, la sécurisation et la diffusion du logiciel libre de gestion d'activité professionnelle ou associative Dolibarr ERP et CRM.

Une place de marché gérée par l'association Dolibarr <https://www.dolistore.com/> met à disposition plusieurs centaines de modules complémentaires permettant de compléter les fonctionnalités standard de Dolibarr.

Dolibarr est écrit en PHP. La base de données MySQL/MariaDB ou PostgreSQL (support limité sur les modules complémentaires) est utilisée.

## ERPNext

Site
: <https://frappe.io/erpnext>

Porteur
: un éditeur (Frappe Technologies)

Licence
: GPL v3

Lancé en 2008 par Frappe Technologies, ERPNext est devenu l'un des ERP open source les plus déployés au monde, en particulier dans les PME et les pays émergents.

Sa couverture fonctionnelle est large : comptabilité, ventes, achats, stocks, production, projets, RH et paie, CRM, maintenance des actifs. Le produit s'appuie sur le framework low-code Frappe, qui permet de définir de nouveaux objets métier, formulaires et workflows sans développement lourd, ce qui explique en grande partie son adoption.

ERPNext est écrit en Python et JavaScript et s'appuie sur MariaDB (ou PostgreSQL, en support plus récent).

## Tryton

Site
: <https://www.tryton.org/>

Porteur
: une fondation (Tryton Foundation)

Licence
: GPL v3

Tryton est né en 2008 d'un fork de TinyERP (l'ancêtre d'Odoo), avec le parti pris d'un noyau minimal et strictement communautaire, sans édition commerciale parallèle.

Le projet privilégie la rigueur du modèle de données et la stabilité des interfaces de programmation, avec deux versions par an et un chemin de migration documenté. La couverture fonctionnelle (comptabilité, ventes, achats, stock, production, projets) s'étend par modules, y compris pour des secteurs spécifiques (santé avec GNU Health, par exemple).

Tryton est écrit en Python et s'appuie sur PostgreSQL.
