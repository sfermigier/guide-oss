# Accélérateurs HTTP { #accelerateur-http }

Les accélérateurs HTTP, également appelés « Reverse Proxies », sont implémentés du côté des serveurs Internet. Ils ont différents usages comme : la sécurité, la répartition de charge, l’accélération SSL, la compression et le cache.

C’est notamment ce dernier point que nous présentons dans cette rubrique. Les internautes « passent » par l’intermédiaire des reverse proxies pour accéder aux applications de serveurs internes. Des politiques de cache adaptées permettent de réduire la charge des serveurs d’applications Web quel que soit le langage utilisé. Certains accélérateurs HTTP gèrent le cache par fragment et prennent notamment en charge le standard ESI (Edge Side Includes).

Plus d'infos: <https://fr.wikipedia.org/wiki/Proxy_inverse>

## Squid

Site
: <https://www.squid-cache.org>

Porteur
: une communauté

Licence
: GPL v2

Squid est un serveur proxy HTTP fréquemment utilisé en entreprise. La première version de Squid date de 1996.

Sa fonction principale est celle de proxy direct, utilisée pour réguler le trafic web et mettre en cache les contenus fréquemment consultés. Il est parfois également utilisé comme proxy inverse dans les architectures web. Lorsqu'il est utilisé à des fins de contrôle d'accès, il est possible de se procurer des listes noires d'URL auprès de fournisseurs tiers.

Squid est inspiré du projet Harvest. Il est compatible avec IPv6 à partir de sa version 3.

## Varnish

Site
: <https://www.varnish.org/> (Varnish Cache) et <https://vinyl-cache.org/> (Vinyl Cache)

Porteur
: un éditeur (Varnish Software) pour Varnish Cache, une communauté pour Vinyl Cache

Licence
: BSD 2-clauses

Varnish est un cache HTTP à hautes performances, dont la première version date de 2006. Il a été conçu par le Danois Poul-Henning Kamp pour le journal norvégien Verdens Gang.

Placé devant un site à fort trafic, il sert les contenus depuis la mémoire, répartit la charge et teste la disponibilité des serveurs d'origine. La politique de cache s'écrit dans un langage dédié, VCL, qui permet des règles très fines ; l'assemblage de fragments par ESI (*Edge Side Includes*) est pris en charge.

Le projet a connu une séparation en 2026 : le projet communautaire d'origine s'appelle **Vinyl Cache** depuis sa version 9.0 (mars 2026), tandis que le nom Varnish Cache est conservé par Varnish Software pour sa propre distribution, qui ajoute notamment TLS natif et images de conteneurs. Les distributions Linux adoptent progressivement le nouveau nom ; avant une mise à jour, on vérifiera lequel des deux projets fournit le paquet.

Varnish et Vinyl Cache sont écrits en C.

## Autres

- HAProxy, davantage orienté répartition de charge que cache (section [Haute disponibilité](haute-disponibilite.md)): <https://www.haproxy.org/>
- Traefik, Envoy et les passerelles d'API, présentés à la page [Proxys inverses et API gateways](proxys-inverses-api-gateways.md)
- Apache Traffic Server, cache HTTP de classe opérateur: <https://trafficserver.apache.org/>
- nginx et Caddy, qui assurent également les fonctions de proxy inverse et de cache (section [Serveurs HTTP](../web-communication/serveurs-http.md))
