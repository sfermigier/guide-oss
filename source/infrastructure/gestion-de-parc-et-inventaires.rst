Gestion de parc et inventaires
==============================

Les outils de gestion de parc et d’inventaires open source sont de plus en plus plébiscités dans les entreprises avec des références phares comme GLPI ou OCS Inventory NG utilisées par de nombreux acteurs du CAC 40.

Ces solutions ont un périmètre fonctionnel large incluant la gestion du parc matériel de la société, la gestion des contrats associés (ordinateurs, périphériques, imprimantes, éléments réseau, consommables, etc.), des fonctions d'assistance (accès utilisateur ou non, gestion fine des droits, notifications automatiques avec modèles personnalisables, SLA), la gestion des licences, etc.

Les outils de gestion de parc et d’inventaires peuvent également disposer d’une dimension financière (module de suivi de coûts, calcul d’amortissement, etc.).


GLPI
----

:Site: https://glpi-project.org/
:Porteur: une communauté et un éditeur français (Teclib')
:Licence: GPL v3

GLPI est un outil d'inventaire de parc informatique et de Helpdesk, lancé en 2003 et porté par Julien Dombre, Jean-Mathieu Doléans et Bazile Lebeau.

Il permet :

- la gestion du parc matériel de la société et des contrats associés : ordinateurs (avec remontée automatique s'il est couplé à GLPI Agent ou à OCS Inventory NG), périphériques, imprimantes, éléments réseau, consommables ;

- des fonctions d'assistance : accès utilisateur ou non, gestion fine des droits, notifications automatiques avec modèles personnalisables, SLA.

- une grande extensibilité grâce à ses plugins : intégration à des logiciels de supervision, gestion de projets, nouveaux éléments d'inventaire, etc.

GLPI est fondé sur les technologies PHP et MariaDB/MySQL. Le projet est aujourd'hui édité par la société française Teclib', qui en assure le développement et propose une offre hébergée ainsi que des extensions commerciales.


OCS Inventory NG
----------------

:Site: https://ocsinventory-ng.org/
:Porteur: une communauté
:Licence: GPL v2

OCS Inventory NG est un outil d'inventaire automatique de postes informatiques, d’origine française, créé en 2001.

OCS remonte aussi bien les caractéristiques matérielles des postes que les logiciels qui y sont installés. Toutes ces informations sont ensuite visualisables au travers d'une interface web avec des fonctions d'exports. Des dictionnaires de logiciels peuvent être également définis pour effectuer des regroupements (MAJ Windows par exemple). Au niveau du télédéploiement, OCS permet de gérer les installations de logiciels aussi bien pour les postes Windows que Mac ou Linux au travers de packages créés par les administrateurs. Les télédéploiements sont sécurisés et peuvent être planifiés ; de plus l'architecture des serveurs OCS peut être répartie pour ne pas congestionner le réseau lors de gros télédéploiements.

OCS repose sur les technologies Perl et MySQL principalement.


Autres
------

Parmi les produits de l’univers Gestion de parc et inventaires, on peut compléter la liste avec les outils ci-dessous :

- GLPI Agent, l'agent d'inventaire multiplateforme de GLPI, qui succède à FusionInventory (dont l'agent n'est plus maintenu): https://github.com/glpi-project/glpi-agent
- Snipe-IT, gestion des actifs et des licences, à l'ergonomie très soignée: https://snipeitapp.com/
- NetBox, référentiel d'infrastructure réseau et de centre de données (adressage, câblage, racks): https://netbox.dev/
- Foreman, gestion du cycle de vie des serveurs (provisionnement, configuration, correctifs): https://theforeman.org/
- Uyuni, gestion de parc et de correctifs pour distributions Linux, amont de SUSE Manager: https://www.uyuni-project.org/


