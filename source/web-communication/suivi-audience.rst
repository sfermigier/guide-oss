Suivi d’audience
================

Il existe deux catégories d’outils extérieurs aux applicatifs (au sens large) pour la mesure de l’audience : les analyseurs de log, qui travaillent à partir des fichiers de log du serveur HTTP, et les applications distantes qui collectent leurs données au moyen de balises spéciales insérées dans les pages.

Dans l’univers des solutions open source, on utilise fréquemment des outils comme AWStats (analyse de logs) ou Matomo (analyse sur base de marqueur).

.. warning::

    La CNIL a mis en demeure, à partir du 10 février 2022, plusieurs éditeurs de sites utilisant Google Analytics, les transferts de données vers les États-Unis étant alors dépourvus de base légale. L'adoption du *Data Privacy Framework* en juillet 2023 a modifié ce cadre juridique, mais celui-ci reste contesté devant les juridictions européennes, et l'obligation de recueillir le consentement pour les traceurs non exemptés demeure. Les solutions qui suivent permettent de s'affranchir de ce risque : hébergées par vos soins, correctement configurées, plusieurs d'entre elles bénéficient de l'exemption de consentement prévue par la CNIL pour la mesure d'audience.


Matomo
------

:Site: https://matomo.org
:Porteur: une communauté
:Licence: GPL v3

Matomo (renommé en 2018, il s'appelait auparavant Piwik) est le successeur de la solution phpMyVisites. Lancé en 2007 par Matthieu Aubry, c'est aujourd'hui l'alternative open source à Google Analytics la plus complète et la plus déployée, avec plus d'un million de sites équipés.

En quelques clics, on accède aux graphiques des visites, à leur durée, aux navigateurs et aux pays des visiteurs, aux mots clés et aux sites référents, au suivi des objectifs et des conversions, aux entonnoirs, aux cartes de chaleur et aux enregistrements de sessions. Matomo est utilisable en version hébergée par ses soins (*on premise*) ou en SaaS, propose une configuration conforme aux recommandations de la CNIL permettant l'exemption de consentement, et sait importer les données historiques de Google Analytics.

Matomo est bâti sur une architecture LAMP, dispose d'un système de plugins, d'une API de reporting et d'un mode d'intégration sans JavaScript (analyse de journaux).


Plausible Analytics
-------------------

:Site: https://plausible.io/
:Porteur: une entreprise
:Licence: AGPL v3


Plausible Analytics est une alternative simple, légère (< 1 KB), open-source et respectueuse de la vie privée à Google Analytics.
Elle n'utilise pas de cookies et est entièrement conforme au RGPD.


Shynet
------

:Site: https://github.com/milesmcc/shynet
:Porteur: un particulier
:Licence: Apache 2.0


Un outil d'analyse de trafic web libre et auto-hébergé : vos données vous appartiennent. Il fonctionne sans cookies et recueille juste assez de données pour être utile, mais pas assez pour être intrusif, avec une interface volontairement simple.

Ackee
-----

:Site: https://ackee.electerious.com/
:Porteur: un particulier
:Licence: MIT

Ackee est un outil d'analyse auto-hébergé qui se soucie de la confidentialité. Ackee conserve les données suivies de manière anonyme pour éviter que les utilisateurs soient identifiables, tout en fournissant des informations utiles. C'est l'outil idéal pour toutes celles et ceux qui n'ont pas besoin d'une plateforme d'analyse marketing complète comme Google Analytics ou Matomo.

Umami
-----

:Site: https://umami.is/
:Porteur: un particulier
:Licence: MIT

Umami est une solution d'analyse web simple, facile à utiliser et auto-hébergée. L'objectif est d'offrir une alternative à Google Analytics, plus conviviale et respectueuse de la vie privée, ainsi qu'une alternative gratuite et ouverte aux solutions payantes. Umami ne recueille que les mesures qui vous intéressent et tout tient sur une seule page.

Développé en JavaScript (Next.js), avec MySQL/MariaDB ou PostgreSQL comme base de données.

AWStats
-------

:Site: https://awstats.sourceforge.io/
:Porteur: une communauté
:Licence: GPL

AWStats est un outil de suivi d’audience fondé sur l’analyse des journaux du serveur web. Écrit par Laurent Destailleur (également à l'origine de Dolibarr) à partir de 2000, il conserve l'avantage propre aux analyseurs de journaux : aucun marqueur dans les pages, donc aucune dépendance au JavaScript, aux cookies ni au consentement, et une mesure insensible aux bloqueurs de publicité.

AWStats fournit de nombreuses statistiques, graphiques et rapports à partir de l’analyse des logs web (mais également FTP, Streaming et mail). Il supporte nativement la lecture des fichiers de  logs de la pluparts des serveurs web comme Apache, WebStar, IIS, etc. Parmi les fonctionnalités d’AWStats, on peut citer : le nombre de visites, de visiteurs uniques, de pages, de hits, de transfert, par domaine/pays, hôte, heure, navigateur, OS, etc. Un des points forts d’AWStats consiste en la possibilité de générer des tableaux de façon dynamique sans perte de performances notamment grâce à une politique de cache efficace. Il est très populaire au près des administrateurs système et réseau.

Écrit en Perl, AWStats peut être installé et exécuté sur la plupart des systèmes. C'est un outil très mature, empaqueté dans toutes les distributions Linux, mais dont le rythme d'évolution est aujourd'hui très lent : sa lecture des données reste pertinente, son interface a vieilli. GoAccess constitue une alternative moderne pour l'analyse de journaux.


Autres
------

- GoAccess (analyse de journaux en temps réel, en console ou en HTML): https://goaccess.io/
- Open Web Analytics: https://www.openwebanalytics.com/
- PostHog (analyse produit, enregistrements de sessions, tests A/B): https://posthog.com/
- Piwik PRO Core, déclinaison commerciale issue du même projet que Matomo: https://piwik.pro/
