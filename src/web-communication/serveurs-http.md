# Serveurs HTTP

Les serveurs HTTP (également appelés serveurs web) répondent aux requêtes des navigateurs et des applications. Ils servent des contenus statiques, transmettent les requêtes dynamiques aux applications et terminent le plus souvent les connexions TLS.

Deux familles sont présentées ici : les serveurs web et proxys inverses (Apache httpd, Nginx, Lighttpd, Caddy) et les serveurs d'application Python (Gunicorn, uWSGI), qui se placent derrière les premiers. Le choix dépend surtout de l'existant, du mode de configuration souhaité, de la gestion des certificats et de la gouvernance du projet.

## Apache Httpd

Site
: <https://httpd.apache.org>

Porteur
: une fondation (Apache)

Licence
: Apache 2.0

Né en 1995 d'un ensemble de correctifs apportés au serveur NCSA HTTPd, Apache httpd a longtemps été le serveur web le plus utilisé. Il reste l'un des plus déployés, derrière Nginx. Il demeure très présent dans l'hébergement mutualisé.

Son architecture modulaire couvre l'authentification, la réécriture d'URL, le proxy inverse, TLS, HTTP/2 et l'exécution de langages comme PHP ou Perl. Les fichiers `.htaccess` permettent de déléguer une partie de la configuration aux responsables de chaque site, au prix d'un coût à l'exécution.

Apache httpd est écrit en C.

## Nginx

Site
: <https://nginx.org>

Porteur
: un éditeur (F5)

Licence
: BSD 2 clauses

Nginx est un serveur web et un proxy inverse publié en 2004 par Igor Sysoev. Son architecture asynchrone et événementielle lui permet de tenir de nombreuses connexions simultanées avec une mémoire réduite.

Il sert de serveur de fichiers statiques, de proxy HTTP, TCP et de messagerie, de répartiteur de charge et de cache et transmet les requêtes aux applications par FastCGI, uwsgi ou SCGI. Certaines fonctions (administration par API, vérifications de santé actives) sont réservées à l'édition commerciale NGINX Plus.

Un point de gouvernance est à suivre. À la suite d'un désaccord avec F5, propriétaire du projet depuis 2019, l'un des développeurs historiques a lancé en 2024 le fork *freenginx* (<https://freenginx.org/>). Un autre fork, Angie (<https://angie.software/>), est maintenu par d'anciens développeurs de Nginx. Ces projets restent pour l'instant marginaux.

Nginx est écrit en C.

## Lighttpd

Site
: <https://www.lighttpd.net>

Porteur
: une communauté (projet initié par Jan Kneschke)

Licence
: BSD 3 clauses

Lighttpd, prononcé « lighty », a été créé en 2003 par Jan Kneschke pour servir de nombreuses connexions avec peu de ressources, grâce à une boucle d'événements asynchrone.

Il prend en charge TLS, HTTP/2, la compression, la réécriture d'URL et l'exécution d'applications par FastCGI, SCGI ou CGI. Sa faible empreinte le destine aux systèmes embarqués, aux équipements réseau et aux petits serveurs. Le développement se poursuit, à un rythme modeste. L'écosystème est plus réduit que celui de Nginx.

Lighttpd est écrit en C.

## Caddy

Site
: <https://caddyserver.com>

Porteur
: une communauté (projet initié par Matthew Holt)

Licence
: Apache 2.0

Caddy a été créé par Matthew Holt en 2015. Il se distingue par l'obtention et le renouvellement automatiques des certificats TLS auprès d'autorités ACME comme Let's Encrypt, actifs par défaut.

La configuration tient dans un fichier court, le Caddyfile, ou passe par une API JSON. Caddy fait office de serveur de fichiers, de proxy inverse avec répartition de charge et de frontal FastCGI et gère HTTP/2 et HTTP/3. Les fonctions absentes du binaire standard s'ajoutent par des modules, ce qui demande de recompiler le serveur avec l'outil xcaddy.

Caddy est écrit en Go.

## Gunicorn

Site
: <https://gunicorn.org>

Porteur
: une communauté (projet initié par Benoît Chesneau)

Licence
: MIT

Gunicorn (« Green Unicorn ») est un serveur d'application pour les applications Python au standard WSGI, comme celles écrites avec Django ou Flask.

Un processus maître pilote plusieurs processus de travail, synchrones, à threads ou asynchrones, dont le nombre se règle en fonction de la charge. Les journaux, les délais d'expiration et le rechargement se configurent en ligne de commande ou dans un fichier Python. En production, on le place derrière un proxy inverse, généralement Nginx.

Gunicorn est écrit en Python.

## uWSGI

Site
: <https://uwsgi-docs.readthedocs.io>

Porteur
: une communauté (projet initié par Roberto De Ioris)

Licence
: GPL v2+ avec exception d'édition de liens

uWSGI est un serveur d'application écrit en C, conçu pour Python (WSGI) et étendu à d'autres langages par des plugins.

Le projet est officiellement en mode maintenance : il ne reçoit plus que des corrections et des adaptations aux nouvelles versions des langages. Il reste utilisable dans les installations existantes ; les nouveaux déploiements Python lui préfèrent Gunicorn ou, pour les applications asynchrones (ASGI), Uvicorn et Granian.

## Comparaison

| Serveur | Site | Porteur | Licence | Langages et protocoles pris en charge | Caractéristiques distinctives | Année de création |
|----|----|----|----|----|----|----|
| Apache Httpd | <https://httpd.apache.org> | une fondation (Apache) | Apache License 2.0 | Perl, PHP, Python, Ruby, SSI, CGI | Souplesse de configuration, nombreux modules | 1995 |
| Nginx | <https://nginx.org> | un éditeur (F5) | 2-clause BSD | HTTP, FastCGI, SCGI, uWSGI, SSL/TLS | Architecture asynchrone, proxy inverse et répartition de charge | 2004 |
| Lighttpd | <https://www.lighttpd.net> | une communauté | BSD 3 clauses | HTTP, FastCGI, SCGI, CGI, SSL/TLS | Empreinte réduite, systèmes embarqués | 2003 |
| Caddy | <https://caddyserver.com> | une communauté | Apache License 2.0 | HTTP/2, HTTP/3, FastCGI, WebSockets, SSL/TLS | Configuration facile, HTTPS automatique, architecture modulaire | 2015 |
| Gunicorn | <https://gunicorn.org> | une communauté | MIT | WSGI, Unix Sockets, TCP Sockets | Serveur d'application Python à processus multiples | 2009 |
| uWSGI | <https://uwsgi-docs.readthedocs.io> | une communauté | GPL v2+ avec exception d'édition de liens | HTTP, FastCGI, SCGI, uWSGI, Python, Perl, Ruby, Lua, PHP | Multi-langages, extensible par plugins, en mode maintenance | 2008 |
