# Automatisation et no-code

Cette catégorie regroupe deux familles : les outils d’automatisation (ils relient des applications par des flux déclenchés sur événement) et les bases de données *no-code*, qui permettent de bâtir de petites applications sans développement classique.

Ces outils réduisent le temps entre un besoin et sa mise en service, au prix d’un risque de dispersion : flux non documentés, clés d’API stockées dans plusieurs endroits, données métier hors du système d’information. Un inventaire, des sauvegardes et une revue des droits sont à prévoir dès le premier flux.

## Node-RED

Site
: <https://nodered.org/>

Porteur
: une fondation (OpenJS Foundation)

Licence
: Apache 2.0

Node-RED est un environnement de programmation par flux, né au début de 2013 chez IBM et désormais hébergé par l’OpenJS Foundation.

On y assemble des nœuds dans le navigateur pour relier équipements, API, files de messages et bases. Il est très présent dans l’internet des objets et l’industrie. Il s’exécute aussi bien sur un Raspberry Pi que sur un serveur.

L’éditeur exécute du code et manipule des secrets : il doit être protégé par authentification et tenu à l’écart de l’internet public. Node-RED est écrit en JavaScript (Node.js).

## Baserow

Site
: <https://baserow.io/>

Porteur
: un éditeur (Baserow B.V.)

Licence
: MIT (cœur) et propriétaire (répertoires premium et enterprise)

Baserow est une base de données collaborative en ligne, comparable à Airtable : tables, vues, formulaires, droits, API et création d’applications simples.

La société est néerlandaise et le cœur publié sous MIT. Les fonctions avancées, notamment sur les droits et l’authentification, se trouvent dans des répertoires à licence commerciale.

Le choix de l’édition et de la date de publication de chaque fonction se vérifie avant de s’engager. Baserow est écrit en Python (Django) et Vue.js.

## Activepieces

Site
: <https://www.activepieces.com/>

Porteur
: un éditeur (Activepieces Inc.)

Licence
: MIT (cœur) et propriétaire (répertoires ee)

Activepieces relie des services en ligne par des flux visuels, dans un esprit proche de Zapier. Les connecteurs, appelés *pieces*, sont écrits en TypeScript et publics.

Il convient aux équipes qui veulent automatiser sans développeur tout en pouvant ajouter leurs propres connecteurs.

Les modules d’entreprise (répertoires *ee*) ne sont pas sous MIT. L’activité du projet comme de son catalogue reste à surveiller. Activepieces est écrit en TypeScript.

## Autres

- Huginn, agents d’automatisation personnels (MIT) : <https://github.com/huginn/huginn>
- Appsmith, outils internes *low-code* (Apache 2.0 pour l’édition Community) : <https://www.appsmith.com/>
- ToolJet, applications internes (AGPL v3) : <https://www.tooljet.com/>
- [Grist](suites-collaboratives.md#grist), tableur et base de données
