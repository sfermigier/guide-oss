Outils de tests de charge
=========================

Les outils de tests de charge, comme leur nom l’indique, sont des applications permettant de simuler une forte charge sur un service.

Cela peut être un site Web mais également une base de données, un annuaire LDAP, un webservice, etc. Les possibilités sont très nombreuses.

Une interface graphique est généralement disponible pour permettre la saisie des scénarios de tests : passage par telle page, clic sur tel menu, remplissage de tel formulaire, soumission, etc. Les scénarios en eux-mêmes peuvent être d'une grande complexité, avec des boucles, conditions, extraction et réutilisation de variables, chargement de variables depuis un fichier externe, etc.

En sortie des tests de charge, les applications proposent généralement de nombreux de graphes et statistiques exportables sous la forme de rapports.

Locust
------

:Site: https://locust.io/
:Porteur: une communauté
:Licence: MIT

Locust est un outil de test de performance scriptable et facile à prendre en main. Vous définissez le comportement de vos utilisateurs dans un code Python ordinaire, au lieu d'utiliser une interface utilisateur maladroite ou un langage spécifique à un domaine. Cela rend Locust infiniment extensible et très convivial pour les développeurs.


JMeter
------

:Site: https://jmeter.apache.org/
:Porteur: une fondation (Apache)
:Licence: Apache 2.0

Jmeter est un outil d'injection de trafic édité par la fondation Apache.

Il est utilisé pour réaliser des tests de charge sur plusieurs types de serveurs : Web, LDAP, Bases de données, etc. Il dispose d'une interface graphique qui rend la création de scénarios d'utilisation plus facile. Les scénarios en eux-mêmes peuvent être d'une grande complexité, avec des boucles, conditions, extraction et réutilisation de variables, chargement de variables depuis un fichier externe, et de nombreux types de graphes et de statistiques.

JMeter est distribué sous licence Apache.

Son développement a commencé en 2001, il est réalisé en Java.


Tsung
-----

:Site: http://tsung.erlang-projects.org
:Porteur: une communauté
:Licence: GPL

Tsung est un outil d'injection de trafic, utilisé pour les tests de charge de différents types de serveurs.

Il supporte HTTP et quelques dérivés (SOAP, WebDAV), les bases MySQL et PostgreSQL, ainsi que XMPP. Réalisé en Erlang, un langage spécialisé dans les applications hautes performances, il ne souffre pas des limites traditionnelles de ce type d'outils, et peut donc simuler un trafic très important. Il dispose d'un générateur automatique de statistiques.

Initialement créé par la société française IDEALX, il est désormais maintenu par une communauté restreinte, à un rythme très ralenti.


k6
--

:Site: https://k6.io/
:Porteur: une entreprise (Grafana Labs)
:Licence: AGPL v3

k6, créé en 2016 par Load Impact et passé en 2021 dans le giron de Grafana Labs, s'est imposé comme l'outil de test de charge de référence pour les équipes DevOps.

Les scénarios s'écrivent en JavaScript, mais le moteur est écrit en Go, ce qui permet de générer une charge importante avec une consommation de ressources réduite. L'outil s'intègre naturellement aux chaînes d'intégration continue (exécution en ligne de commande, seuils d'échec déclarés dans le script) et à l'observabilité (export des métriques vers Prometheus, InfluxDB ou Grafana Cloud). Il prend en charge HTTP, WebSocket, gRPC et les navigateurs.


Gatling
-------

:Site: https://gatling.io/
:Porteur: une entreprise française (Gatling Corp)
:Licence: Apache 2.0

Créé en 2011 par le français Stéphane Landelle, Gatling est l'autre grand outil de test de charge open source, particulièrement présent dans les environnements Java.

Ses scénarios s'écrivent sous forme de code (Scala, Java, Kotlin ou JavaScript) selon une syntaxe déclarative très lisible. Son architecture asynchrone lui permet de simuler un grand nombre d'utilisateurs avec peu de ressources, et ses rapports HTML détaillés sont l'un de ses points forts reconnus.


Autres
------

- Vegeta (injecteur HTTP en ligne de commande, Go): https://github.com/tsenart/vegeta
- Artillery (scénarios en YAML, Node.js): https://www.artillery.io/
- wrk et oha, pour des mesures rapides en ligne de commande: https://github.com/wg/wrk et https://github.com/hatoo/oha

FunkLoad, outil de tests fonctionnels et de charge développé par la société française Nuxeo et présenté dans les éditions précédentes de ce guide, n'est plus maintenu : son dépôt est archivé depuis 2018.
