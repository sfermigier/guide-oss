# Proxys inverses et API gateways

Un proxy inverse reçoit les requêtes des clients et les transmet aux serveurs applicatifs. Il termine le chiffrement TLS, répartit la charge, applique des règles de routage et masque la topologie interne. Une *API gateway* y ajoute ce qui relève de l'exposition d'API : authentification, quotas, transformation des requêtes, mesure de la consommation.

Le choix dépend d'abord de l'environnement. Pour quelques serveurs stables, nginx, Apache ou Caddy, présentés à la page [Serveurs HTTP](../web-communication/serveurs-http.md), ou [HAProxy](haute-disponibilite.md#haproxy) suffisent. Dans un environnement de conteneurs, la découverte automatique des services devient déterminante. L'API *Gateway* de Kubernetes définit une configuration commune à plusieurs produits. Le cache est traité à la page [Accélérateurs HTTP](accelerateur-http.md), le filtrage applicatif à la page [SIEM et WAF](siem-waf.md).

Le domaine des passerelles d'API est marqué par l'open core : authentification par OpenID Connect, interface d'administration ou portail des développeurs sont fréquemment réservés aux éditions payantes. La liste des greffons libres est à confronter au besoin avant de choisir.

## Traefik

Site
: <https://traefik.io/traefik>

Porteur
: un éditeur (Traefik Labs)

Licence
: MIT

Traefik est un proxy inverse conçu pour les environnements dynamiques, créé en 2015 par le Français Émile Vauge, fondateur de la société Traefik Labs.

Il découvre les services auprès de Docker, de Kubernetes, de Consul ou de fichiers, crée les routes sans redémarrage et obtient les certificats par ACME. Des intergiciels assurent l'authentification, la limitation de débit, les redirections ou la réécriture. Il sert d'entrée à de nombreuses installations Docker et est le contrôleur fourni d'origine par K3s.

Les fonctions de passerelle et de gestion d'API relèvent de l'offre commerciale Traefik Hub. Le stockage des certificats ACME n'est pas partagé entre instances dans la version libre, ce qui compte en haute disponibilité.

Traefik est écrit en Go.

## Envoy

Site
: <https://www.envoyproxy.io/>

Porteur
: une fondation (CNCF)

Licence
: Apache 2.0

Envoy est un proxy développé chez Lyft, publié en 2016 et confié en 2017 à la CNCF, dont il est diplômé depuis 2018.

Il traite HTTP/1.1, HTTP/2, HTTP/3, gRPC et TCP, avec une observabilité détaillée, la répartition de charge avancée, les reprises sur erreur et une configuration pilotée à chaud par API (xDS). Il sert de plan de données à plusieurs maillages de services (dont Istio) et à des passerelles.

Sa configuration directe est verbeuse. On l'utilise plutôt à travers un plan de contrôle : Envoy Gateway, qui met en œuvre l'API *Gateway* de Kubernetes, Contour ou Istio.

Envoy est écrit en C++.

## Kong Gateway

Site
: <https://developer.konghq.com/gateway/>

Porteur
: un éditeur (Kong Inc.)

Licence
: Apache 2.0 pour l'édition OSS, licence commerciale pour l'édition Enterprise

Kong est une passerelle d'API publiée en 2015, construite sur nginx et OpenResty.

Un système de greffons, en Lua notamment, couvre l'authentification, les quotas, la transformation des requêtes et la journalisation. Elle fonctionne avec une base PostgreSQL ou en mode déclaratif sans base.

L'écart entre les éditions est le point décisif. Les versions libres publiées dans le dépôt appartiennent à la branche 3.9, dont les corrections se poursuivent, tandis que l'édition commerciale est plus avancée. Ce décalage est à mesurer avant tout nouveau déploiement.

Kong est écrit en Lua.

## Apache APISIX

Site
: <https://apisix.apache.org/>

Porteur
: une fondation (Apache Software Foundation)

Licence
: Apache 2.0

APISIX est une passerelle d'API créée par la société API7 et donnée en 2019 à la fondation Apache.

Construite elle aussi sur nginx et OpenResty, elle conserve sa configuration dans etcd, ce qui permet des modifications à chaud sur l'ensemble des nœuds. Ses greffons couvrent l'authentification (y compris OpenID Connect), les quotas, le routage avancé, l'observabilité et, plus récemment, l'accès aux modèles de langage. Un tableau de bord et un contrôleur Kubernetes sont publiés par le projet.

La gouvernance par une fondation la distingue des passerelles d'éditeur. etcd est en contrepartie un composant supplémentaire à administrer, sauf en mode autonome.

APISIX est écrit en Lua.

## Autres

- HAProxy, répartiteur de charge, présenté à la page [Haute disponibilité](haute-disponibilite.md#haproxy)
- nginx, Apache Httpd et Caddy, présentés à la page [Serveurs HTTP](../web-communication/serveurs-http.md)
- Nginx Proxy Manager, interface web pour nginx et Let's Encrypt (MIT) : <https://nginxproxymanager.com/>
- KrakenD Community Edition, passerelle sans base de données (Apache 2.0) : <https://www.krakend.io/>
- Gravitee API Management, plateforme d'origine française (Apache 2.0, édition Enterprise distincte) : <https://www.gravitee.io/>
- Tyk, passerelle d'API (MPL 2.0, avec un répertoire sous licence commerciale) : <https://tyk.io/>
