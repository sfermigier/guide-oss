# Gestion de projet

Un outil de gestion de projet rassemble les tâches, les responsables, les échéances et les documents. Selon les équipes, il prend la forme d’un diagramme de Gantt, d’un tableau Kanban, d’un backlog Scrum ou d’une liste de tâches partagée.

Le critère décisif est l’adéquation au fonctionnement de l’équipe : un outil trop riche est contourné, un outil trop simple ne résiste pas au suivi budgétaire ou au portefeuille de projets. Les exports et l’API comptent également, car l’historique d’un projet dure plus longtemps que l’outil qui l’a produit.

Les outils liés à une forge logicielle, notamment [Redmine](../developpement/outils-de-developpement.md#redmine) et [Tuleap](../developpement/outils-de-developpement.md#tuleap), sont traités dans la partie consacrée au développement.

## OpenProject

Site
: <https://www.openproject.org/>

Porteur
: un éditeur (OpenProject GmbH)

Licence
: GPL v3 (édition Community) et propriétaire pour les fonctions Enterprise

OpenProject est une plateforme de gestion de projet développée par la société berlinoise OpenProject GmbH. Elle est issue d’un fork de ChiliProject, lui-même issu de Redmine.

Elle couvre le diagramme de Gantt, les tableaux agiles, le temps passé, les budgets, les réunions et un wiki. Elle s’intègre à Nextcloud pour les fichiers. Son périmètre convient aux organisations qui mélangent méthodes classiques et agiles.

Certaines fonctions relèvent de l’édition Enterprise, par abonnement. La comparaison des éditions est à examiner avant l’installation. OpenProject est écrit en Ruby (Rails) et TypeScript.

## Taiga

Site
: <https://taiga.io/>

Porteur
: une entreprise (Taiga Cloud Services)

Licence
: MPL 2.0 (serveur) et AGPL v3 (interface)

Taiga est né en 2013 lors d’un hackathon de la société espagnole Kaleidos. C’est un outil destiné aux équipes qui appliquent Scrum ou Kanban.

Il propose backlog, sprints, récits utilisateurs, suivi d’anomalies et wiki, avec une interface que des non-développeurs prennent facilement en main.

Son périmètre est volontairement centré sur l’agilité : pas de budget ni de plan de charge. Depuis 2024, Taiga Cloud Services maintient la version 6, tandis que la coopérative BIRU développe une suite distincte, Tenzu (<https://tenzu.net/>) : la trajectoire de Taiga est à examiner avant un déploiement de longue durée. Le serveur est écrit en Python (Django).

## Vikunja

Site
: <https://vikunja.io/>

Porteur
: une communauté (projet de Konrad Langenberg)

Licence
: AGPL v3

Vikunja est un gestionnaire de tâches auto-hébergeable, pour un individu ou une petite équipe : listes, tableau Kanban, Gantt, calendrier, rappels et partage.

Son déploiement est léger (un exécutable et une base de données) et il échange avec des clients CalDAV.

Le projet repose sur un mainteneur principal, qui finance son travail par une offre hébergée. Vikunja est écrit en Go et Vue.js.

## Autres

- Plane, alternative à Jira en ligne ou sur site (AGPL v3 pour l’édition Community) : <https://plane.so/>
- Leantime, gestion de projet pour équipes non techniques (AGPL v3) : <https://leantime.io/>
- Kanboard, tableau Kanban minimal en PHP (MIT) : <https://kanboard.org/>
- WeKan, tableau Kanban (MIT) : <https://wekan.fi/>
