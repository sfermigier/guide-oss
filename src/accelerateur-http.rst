Accélérateur Http
=================

Les accélérateurs http, également appelés « Reverse Proxy » sont implémentés du côté des serveurs Internet. Ils ont différents usages comme : la sécurité, la répartition de charge, l’accélération SSL, la compression et le cache.

C’est notamment ce dernier point que nous évaluons dans cette rubrique. Les internautes « passent » par l’intermédiaire des reverses proxy pour accéder aux applications de serveurs internes. Des politiques de cache avancées permettent de décharger les serveurs d’applications Web quel que soit le langage utilisé. Certains accélérateurs HTTP gèrent le cache par fragment en supportant notamment la norme ESI.




Squid
-----

:Version: 3.1
:Site: www.squid-cache.org
:Porteur: une communauté

Squid est un serveur proxy HTTP fréquemment utilisé en entreprise. La première version de Squid date de 1996.

Sa fonction principale est celle de proxy direct, utilisée pour réguler le trafic web et mettre en cache les contenus fréquemment consultés. Il est parfois également utilisé comme proxy inverse dans les architectures web. Lorsqu'il est utilisé à des fins de contrôle d'accès, il est possible de se procurer des listes noires d'URL auprès de fournisseurs tiers.

Squid est distribué sous licence GPL.

Squid est inspiré du projet Harvest. Il est compatible avec IPv6 à partir de sa version 3.




Varnish
-------

:Version: 3.0.1
:Site: www.varnish-cache.org
:Porteur: un éditeur (Varnish Software)

Varnish est un cache HTTP hautes performances. La première version stable de Varnish date de 2006, et a été initiée pour le journal norvégien Verdens Gang. L’architecte du produit est le danois Poul-Henning Kamp.

Utilisé pour améliorer les performances des sites web à fort trafic, Varnish dispose également de fonctionnalités de répartition de charge et permet de tester la disponibilité des serveurs produisant le contenu web. Varnish est notamment utilisé par Facebook. Varnish stocke une partie de ses données dans la mémoire virtuelle. La configuration de l’outil est réalisée à partir de fichiers VCL (language spécifique) ; cela permet d’aller très loin dans la définition des régles de gestion. Enfin, Varnish supporte les tags ESI (Edge Side Includes).

Varnish est distribué sous licence BSD.




Autres
------

Parmi les produits de l’univers Accélérateurs http, on peut compléter la liste avec les outils ci-dessous :



Nom	URL / Site web

nginx	http://nginx.org

