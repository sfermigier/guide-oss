# Support et helpdesk

Un outil de support reçoit les demandes par courriel, formulaire, téléphone ou messagerie, les transforme en tickets, les affecte et en suit le traitement. Il sert aussi bien un service client qu’un centre d’assistance interne.

Les points à comparer sont les canaux d’entrée, la gestion des délais de réponse (SLA), la base de connaissances et les règles d’automatisation. Les tickets contiennent des données personnelles : leur conservation et les droits d’accès doivent être définis dès l’installation.

Lorsque le support concerne un parc informatique, [GLPI](../infrastructure/gestion-de-parc-et-inventaires.md#glpi) associe les tickets à l’inventaire des équipements.

## Zammad

Site
: <https://zammad.com/>

Porteur
: une fondation (Zammad Foundation) et un éditeur (Zammad GmbH)

Licence
: AGPL v3

Zammad est un centre d’assistance web. La Zammad Foundation abrite le projet depuis 2014, tandis que la société allemande Zammad GmbH commercialise l’hébergement, le support et la formation.

Il réunit courriel, formulaire, messageries et téléphonie dans une file unique, avec groupes, SLA, macros, base de connaissances et moteur de recherche. L’API facilite le lien avec un CRM.

Le déploiement s’appuie sur PostgreSQL, Redis et, pour la recherche, Elasticsearch : il est plus exigeant que celui d’un outil PHP. Zammad est écrit en Ruby (Rails) et TypeScript.

## FreeScout

Site
: <https://freescout.net/>

Porteur
: une communauté

Licence
: AGPL v3

FreeScout est une boîte de réception partagée pour équipes de support, proche de Help Scout ou de Zendesk dans son usage.

Le cœur gratuit suffit à traiter les courriels à plusieurs : attribution, notes internes, réponses types, détection de collision. Il fonctionne sur un hébergement PHP ordinaire.

Plusieurs fonctions (base de connaissances, canaux supplémentaires, SLA) viennent de modules payants : leur coût et leur licence entrent dans la comparaison. FreeScout est écrit en PHP (Laravel).

## Autres

- osTicket (GPL v2) : <https://osticket.com/>
- Znuny, fork communautaire d’OTRS (GPL v3) : <https://www.znuny.org/>
- UVdesk (OSL 3.0) : <https://www.uvdesk.com/>
- Chatwoot, support multicanal (MIT, hors modules Enterprise) : <https://www.chatwoot.com/>
- Le support sous forme de projet peut aussi passer par [Redmine](../developpement/outils-de-developpement.md#redmine)
