# PaaS

Un PaaS (*Platform as a Service*) prend en charge ce qui sépare le code d'une application en service : construction, processus, nom de domaine, certificat TLS, base de données, sauvegarde. Les solutions présentées ici s'installent sur ses propres serveurs et reprennent, pour la plupart, le modèle popularisé par Heroku, où un simple `git push` déclenche le déploiement.

Elles visent des équipes sans administrateur à plein temps, les PME, les associations ou les services qui hébergent quelques dizaines d'applications. Au-delà, ou lorsque la haute disponibilité est requise, on se tournera vers un [orchestrateur de conteneurs](conteneurs-orchestration.md). Pour installer des applications existantes sur un serveur personnel, les distributions de la page [auto-hébergement](auto-hebergement.md) sont mieux adaptées.

Les critères de choix sont l'empreinte sur le serveur, la dépendance à Docker, la prise en charge de plusieurs machines, les sauvegardes fournies et la santé du projet, plusieurs d'entre eux reposant sur un très petit nombre de mainteneurs. Précision d'intérêt : Hop3 et Nua avant lui sont édités par Abilian, qui maintient ce guide.

## Hop3

Site
: <https://hop3.cloud>

Porteur
: une entreprise (Abilian)

Licence
: Apache 2.0

Hop3 est un PaaS pour serveur unique, développé par la société française Abilian, par ailleurs mainteneur de ce guide. Il a pris la suite de Nua.

Les applications se déploient par Git, en Python, Node.js, Go, Ruby, Rust, PHP, Java ou d'autres langages, avec leurs services (PostgreSQL, MySQL, Redis, stockage objet). Docker est facultatif : la construction peut être native ou passer par Nix ou par Docker. Certificats Let's Encrypt, sauvegardes, rôles d'accès, pare-feu applicatif optionnel et catalogue d'applications prêtes à installer complètent l'ensemble.

Ses auteurs qualifient le logiciel de version bêta : architecture et API peuvent encore changer d'une version à l'autre, ce qui est à prendre en compte pour une mise en production.

Hop3 est écrit en Python.

## Nua

Site
: <https://nua.rocks>

Porteur
: une entreprise (Abilian)

Licence
: AGPL v3

Nua est l'ancien PaaS d'Abilian, construit autour de Docker et des formats de l'*Open Container Initiative*. Son site annonce qu'il a été renommé Hop3, vers lequel on s'orientera pour un nouveau projet ; cette fiche est conservée pour les utilisateurs existants.

## Piku

Site
: <https://github.com/piku/piku>

Porteur
: une communauté

Licence
: MIT

Piku est un PaaS minimal qui permet de déployer des applications par `git push` sur de petits serveurs, jusqu'au Raspberry Pi.

Il gère Python, Node.js, Ruby, Go, Clojure et d'autres langages sans recourir à Docker : les processus sont confiés à uWSGI, l'exposition sur le web à nginx et la configuration se lit dans un `Procfile`.

Sa simplicité en fait un outil pour un développeur ou une petite équipe. Il n'offre ni interface web, ni gestion des bases de données, ni cloisonnement par conteneur entre les applications.

Piku est écrit en Python.

## Dokku

Site
: <https://dokku.com>

Porteur
: une communauté

Licence
: MIT

Dokku est un PaaS fondé sur Docker et inspiré de Heroku, lancé en 2013, qui s'administre en ligne de commande.

Il construit les applications à partir de *buildpacks* ou d'un Dockerfile. Un système d'extensions ajoute bases de données, certificats Let's Encrypt ou tâches planifiées. Il fonctionne d'origine sur un seul serveur ; un ordonnanceur K3s permet d'en utiliser plusieurs.

Le projet est ancien, stable et bien documenté. Son développement est communautaire, une édition commerciale, Dokku Pro, ajoutant une interface web.

Dokku est écrit principalement en Shell et en Go.

## Coolify

Site
: <https://coolify.io/>

Porteur
: une entreprise (coolLabs)

Licence
: Apache 2.0

Coolify est une plateforme de déploiement d'applications, de bases de données et de services, présentée comme une alternative à Heroku, Netlify et Vercel.

Pilotée par une interface web, elle déploie depuis les principales forges Git vers un ou plusieurs serveurs accessibles par SSH, au moyen de Docker. Elle apporte certificats, sauvegardes de bases vers un stockage S3, aperçus de branches et un large catalogue de services. Les applications continuent de fonctionner si Coolify est arrêté.

Toutes les fonctions sont libres ; l'éditeur se rémunère sur une version hébergée du tableau de bord. Ce tableau de bord détenant un accès SSH à l'ensemble des serveurs, son exposition et ses mises à jour demandent de la rigueur.

Coolify est écrit en PHP (Laravel).

## Autres

- Kubero, PaaS de type Heroku au-dessus de Kubernetes : <https://www.kubero.dev/>
- Cozystack, plateforme de services managés sur Kubernetes (Apache 2.0) : <https://cozystack.io/>
- Cloud Foundry, PaaS d'entreprise porté par une fondation (Apache 2.0) : <https://www.cloudfoundry.org/>
