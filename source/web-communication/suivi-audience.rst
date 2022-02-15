Suivi d’audience
================

Il existe deux catégories d’outils extérieurs aux applicatifs (au sens large) pour la mesure de l’audience : les analyseurs de log, qui travaillent à partir des fichiers de log du serveur HTTP, et les applications distantes qui collectent leurs données au moyen de balises spéciales insérées dans les pages.

Dans l’univers des solutions open source, on utilise fréquemment des outils comme AWStats (analyse de logs) ou Matomo (analyse sur base de marqueur).

.. warning::

    La CNIL a statué le 10 février 2022 que l'utilisation de Google Analytics était illégale en France. Les solutions qui suivent constituent des alternatives à Google Analytics conformes au RGPD.


Matomo
------

:Site: https://matomo.org
:Porteur: une communauté
:Licence: GPL v3

Matomo (anciennement Piwik) est le successeur de la solution phpMyVisites. Dirigé par Matthieu Aubry, la solution a vu le jour récemment. Matomo a comme objectif de devenir une alternative de choix à Google Analytics.

Le défi est important ; pourtant, ses débuts sont prometteurs. En quelques clics, on accède aux graphiques des dernières visites, à la durée des visites, aux navigateurs des visiteurs, aux pays des visiteurs, à la liste de mots clés utilisés, à la liste de sites externes, aux classements des moteurs de recherche, à la répartition des visites par fuseau horaire, suivi des objectifs, répartition géographique, etc. Matomo a reçu le prix du meilleur projet Sourceforge pour le mois de juillet 2010.

Matomo est bâti sur une architecture LAMP, dispose d’un système de plugins, d’une API et d’une interface.


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


Un outil d'analyse de trafic Web sous forme de logiciel libre auto-hébergé. Ves données vous appartiennent donc. Il fonctionne sans cookies et recueille juste assez de données pour être utile, mais pas assez pour être effrayant. Et vous pouvez même trouver l'interface facile à utiliser.

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

Umami est une solution d'analyse web simple, facile à utiliser et auto-hébergée. L'objectif est d;offrir une alternative à Google Analytics, plus conviviale et respectueuse de la vie privée, ainsi qu'une alternative gratuite et ouverte aux solutions payantes. Umami ne recueille que les mesures qui vous intéressent et tout tient sur une seule page.

Développé en JavaScript avec le MySQL ou Postgresql comme base de données.

AWStats
-------

:Site: http://awstats.sourceforge.net/
:Porteur: une communauté
:Licence: GPL

AWStats est un outil de suivi d’audience basé sur l’analyse des logs web. Il a été écrit par Laurent Destailleur, il y a quelques années déjà.

AWStats fournit de nombreuses statistiques, graphiques et rapports à partir de l’analyse des logs web (mais également FTP, Streaming et mail). Il supporte nativement la lecture des fichiers de  logs de la pluparts des serveurs web comme Apache, WebStar, IIS, etc. Parmi les fonctionnalités d’AWStats, on peut citer : le nombre de visites, de visiteurs uniques, de pages, de hits, de transfert, par domaine/pays, hôte, heure, navigateur, OS, etc. Un des points forts d’AWStats consiste en la possibilité de générer des tableaux de façon dynamique sans perte de performances notamment grâce à une politique de cache efficace. Il est très populaire au près des administrateurs système et réseau.

Écrit en Perl, AWStats peut être installé et exécuté sur la plupart des systèmes. C'est un outil de supervision très mature disposant de packages sur toutes les distributions Linux.
