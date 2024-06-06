Serveurs http
=============

Dans cette rubrique, nous présentons les serveurs HTTP open source du marché.

Les serveurs HTTP (également appelé serveurs Web) servent les requêtes (pages, images souvent) des internautes en respectant le protocole http.

Dans l’univers des serveurs HTTP, le serveur Apache domine très largement avec une notoriété exceptionnelle. Il n’est pas difficile de trouver des prestataires pour du conseil ou de l’intégration.


Apache Httpd
------------

:Site: http://httpd.apache.org
:Porteur: une fondation (Apache)
:Licence: Apache

Apache est le serveur web le plus utilisé au monde. Son développement a commencé en 1995 alors qu’il s'agissait uniquement d'une collection de correctifs et d'additions au serveur NCSA HTTPd 1.3.

Il offre une grande souplesse de configuration et un grand nombre modules pour une couverture fonctionnelle toujours inégalée. La version 2 a notamment apportée le support de plusieurs plateformes (dont Windows), une nouvelle API et le support d’IPv6. En plus de son périmétre initial, Apache est conçu pour être modulaire et permettre l’accueil de fonctionnalités additionnelles comme l’interprétation du language PERL, PHP, Python et Ruby, le support des tags SSI et des CGI, etc.


Nginx
------------

:Site: https://nginx.org
:Porteur: NGINX, Inc. (acquise par F5 Networks)
:Licence: 2-clause BSD

Nginx est un serveur web open source et un reverse proxy fondé par Igor Sysoev en 2004. Il est conçu pour offrir des performances élevées, une faible utilisation des ressources et une grande stabilité.

Nginx se distingue par son architecture asynchrone et événementielle, qui lui permet de gérer un grand nombre de connexions simultanées avec une empreinte mémoire réduite. Cette architecture le rend particulièrement adapté aux applications web modernes à fort trafic.

Caractéristiques et fonctionnalités :

- Serveur HTTP statique, proxy inverse et proxy de messagerie
- Équilibrage de charge avec gestion des sessions
- SSL/TLS pour des connexions sécurisées
- Compression et mise en cache des réponses HTTP
- Support de FastCGI, SCGI, uWSGI, et des passerelles de serveurs d'applications
- Gestion des redirections et réécritures d'URL
- Module de streaming pour la diffusion en continu de contenu multimédia

Nginx est également extensible grâce à ses modules dynamiques, permettant aux utilisateurs d'ajouter des fonctionnalités supplémentaires en fonction de leurs besoins spécifiques. En raison de ses performances et de sa flexibilité, Nginx est devenu un choix populaire pour les grandes entreprises et les services de cloud computing, surpassant même Apache dans de nombreux déploiements à grande échelle.

Sa popularité croissante et ses capacités robustes en font un élément clé de l'infrastructure web moderne.


Lighttpd
------------

:Site: https://www.lighttpd.net
:Porteur: un projet open source (initié par Jan Kneschke)
:Licence: BSD

Lighttpd, souvent prononcé "lighty", est un serveur web open source conçu pour être sécurisé, rapide, conforme aux standards et flexible. Il a été développé par Jan Kneschke en 2003 pour répondre aux besoins des environnements à haute performance avec une faible consommation de mémoire.

Caractéristiques et fonctionnalités :

- Conception légère et optimisation pour les environnements à haute performance
- Utilisation d'une architecture asynchrone basée sur des événements pour gérer efficacement les connexions simultanées
- Support complet de FastCGI, SCGI et CGI pour les applications dynamiques
- Support de la compression HTTP (mod_compress) et de la mise en cache des réponses
- Gestion avancée des redirections et réécritures d'URL
- Support de SSL/TLS pour des connexions sécurisées
- Modules pour la gestion des sessions, l'authentification, la génération de statistiques, et plus encore

Lighttpd est particulièrement adapté aux environnements où la performance et la faible utilisation des ressources sont cruciales. Grâce à son architecture légère, il peut gérer un grand nombre de connexions simultanées avec une empreinte mémoire minimale, ce qui le rend idéal pour les serveurs web à faible coût ou les systèmes embarqués.

De plus, Lighttpd offre une flexibilité importante via son système de modules, permettant aux administrateurs de configurer et d'étendre ses fonctionnalités en fonction des besoins spécifiques de leurs applications. Ses capacités de gestion de la charge et de performance en font un choix populaire pour les développeurs cherchant à optimiser l'efficacité de leurs serveurs web.

Caddy
------------

:Site: https://caddyserver.com
:Porteur: une entreprise (Light Code Labs)
:Licence: Apache 2.0

Caddy est un serveur web open source connu pour sa configuration facile et son support natif de HTTPS. Il a été créé par Matthew Holt en 2015 et se distingue par sa simplicité d'utilisation et ses fonctionnalités modernes.

Caractéristiques et fonctionnalités :

- Configuration simple et intuitive via un fichier de configuration Caddyfile ou en utilisant JSON
- HTTPS automatique pour chaque site avec des certificats SSL/TLS obtenus et renouvelés automatiquement via Let's Encrypt
- Support intégré de HTTP/2 et HTTP/3 pour des connexions web plus rapides et plus sécurisées
- Architecture modulaire permettant une grande extensibilité avec des plugins
- Capacités de reverse proxy avec gestion des équilibrages de charge et du clustering
- Support de FastCGI, WebSockets et d'autres protocoles pour des applications dynamiques
- Gestion des redirections, des réécritures d'URL et des en-têtes HTTP
- Système de cache intégré pour améliorer les performances

Caddy se distingue par sa capacité à gérer automatiquement les certificats SSL/TLS, simplifiant ainsi considérablement le déploiement de sites web sécurisés. Sa configuration via Caddyfile est conçue pour être accessible et facile à comprendre, même pour les utilisateurs moins expérimentés.

En plus de ses fonctionnalités de serveur web, Caddy peut également être utilisé comme un reverse proxy, un équilibreur de charge et un serveur de streaming, offrant une solution tout-en-un pour diverses exigences de déploiement web. Sa conception modulaire permet aux développeurs de créer des plugins personnalisés pour étendre les capacités du serveur en fonction de leurs besoins spécifiques.

La popularité de Caddy réside dans sa simplicité d'utilisation et sa capacité à automatiser les tâches courantes liées à la gestion de serveurs web sécurisés. Ces caractéristiques en font un choix privilégié pour les développeurs et les administrateurs système cherchant à minimiser la complexité tout en maintenant des standards de sécurité élevés.


Gunicorn
------------

:Site: https://gunicorn.org
:Porteur: un projet open source (initié par Benoit Chesneau)
:Licence: MIT

Gunicorn, abréviation de "Green Unicorn", est un serveur HTTP pour les applications Python WSGI. Il a été développé par Benoit Chesneau et est conçu pour être simple à utiliser, rapide et compatible avec une large gamme de frameworks Python.

Caractéristiques et fonctionnalités :

- Compatibilité avec les applications WSGI standard, permettant une intégration facile avec les frameworks comme Django, Flask, Pyramid, etc.
- Modèle de concurrence basé sur des travailleurs multiples (workers) pouvant être configurés pour utiliser des threads, des processus ou des coroutines
- Gestion efficace des ressources avec une faible latence et une haute performance
- Prise en charge des configurations de déploiement flexibles grâce à des options de ligne de commande et des fichiers de configuration
- Capacité à gérer les connexions multiples avec une architecture robuste et résiliente
- Fonctionnalités de logging et monitoring pour une gestion simplifiée en production
- Support pour les sockets Unix et les sockets TCP
- Extensible via des hooks et des plugins pour répondre à des besoins spécifiques

Gunicorn est souvent utilisé en combinaison avec des serveurs proxy inverses comme Nginx pour créer des environnements de déploiement web performants et sécurisés. Son architecture de travailleurs multiples permet de gérer un grand nombre de requêtes simultanées, ce qui en fait un choix idéal pour les applications web à fort trafic.

L'un des avantages de Gunicorn est sa simplicité d'utilisation, avec une configuration minimale nécessaire pour démarrer une application Python WSGI. Les utilisateurs peuvent ajuster le nombre de travailleurs et choisir parmi différents types de travailleurs (synchrones, asynchrones, gévent, etc.) en fonction des besoins de leur application.

Gunicorn offre également des fonctionnalités avancées comme le rechargement à chaud, les délais de timeout configurables, et la gestion des erreurs, ce qui facilite la maintenance et la mise à jour des applications en production.


uWSGI
------------

:Site: https://uwsgi-docs.readthedocs.io
:Porteur: un projet open source (initié par Roberto De Ioris)
:Licence: GPL

uWSGI est un serveur d'application web pour les applications Python WSGI, mais il supporte également plusieurs autres langages et protocoles. Créé par Roberto De Ioris, uWSGI est conçu pour offrir des performances élevées, une grande flexibilité et une extensibilité robuste.

Caractéristiques et fonctionnalités :

- Support de multiples langages et protocoles, y compris Python, Perl, Ruby, Lua, et PHP, ainsi que des protocoles comme HTTP, FastCGI, SCGI, et uWSGI
- Modèle de travail multi-processus et multi-thread avec gestion automatique des processus pour une haute performance et une résilience accrue
- Capacité à gérer un grand nombre de connexions simultanées grâce à une architecture scalable et performante
- Extensible via des plugins, permettant d'ajouter des fonctionnalités spécifiques en fonction des besoins de l'application
- Outils de gestion et de monitoring intégrés, tels que uWSGI Emperor, pour une administration simplifiée des instances et des processus
- Support de la journalisation avancée et des métriques pour une meilleure surveillance en production
- Options de configuration flexibles via des fichiers ini, xml, yaml, ou directement en ligne de commande
- Support des sockets Unix et TCP, ainsi que des fonctionnalités avancées comme les threads asynchrones, les coroutines, et le chargement à chaud des applications

uWSGI est souvent utilisé conjointement avec des serveurs web comme Nginx ou Apache en tant que reverse proxy, créant une architecture robuste et scalable pour les applications web. Son support étendu de divers langages et protocoles le rend particulièrement adapté pour des environnements hétérogènes où plusieurs technologies coexistent.

L'une des forces de uWSGI est sa capacité à être hautement configurable et extensible, permettant aux développeurs de fine-tuner leur environnement de déploiement pour des performances optimales. Les fonctionnalités comme le rechargement à chaud, la gestion des workers, et les capacités de clustering offrent une grande flexibilité pour le déploiement et la gestion des applications.

Comparaison
------------

.. list-table::
   :header-rows: 1

   * - Serveur
     - Site
     - Porteur
     - Licence
     - Langages/Protocoles Supportés
     - Caractéristiques Distinctives
     - Année de Création
   * - Apache Httpd
     - http://httpd.apache.org
     - Apache Software Foundation
     - Apache License 2.0
     - PERL, PHP, Python, Ruby, SSI, CGI
     - Grande souplesse de configuration, nombreux modules, support IPv6
     - 1995
   * - Nginx
     - https://nginx.org
     - NGINX, Inc. (acquise par F5 Networks)
     - 2-clause BSD
     - HTTP, FastCGI, SCGI, uWSGI, SSL/TLS
     - Architecture asynchrone, faible utilisation des ressources, haute performance
     - 2004
   * - Lighttpd
     - https://www.lighttpd.net
     - un projet open source (initié par Jan Kneschke)
     - BSD
     - HTTP, FastCGI, SCGI, CGI, SSL/TLS
     - Conception légère, optimisation pour haute performance, faible utilisation des ressources
     - 2003
   * - Caddy
     - https://caddyserver.com
     - Light Code Labs
     - Apache License 2.0
     - HTTP/2, HTTP/3, FastCGI, WebSockets, SSL/TLS
     - Configuration facile, HTTPS automatique, architecture modulaire
     - 2015
   * - Gunicorn
     - https://gunicorn.org
     - un projet open source (initié par Benoit Chesneau)
     - MIT
     - WSGI, Unix Sockets, TCP Sockets
     - Simplicité d'utilisation, gestion efficace des ressources, flexible
     - 2009
   * - uWSGI
     - https://uwsgi-docs.readthedocs.io
     - un projet open source (initié par Roberto De Ioris)
     - GPL
     - HTTP, FastCGI, SCGI, uWSGI, Python, Perl, Ruby, Lua, PHP
     - Extensible via plugins, support multi-langages, haute configurabilité
     - 2008
