Suivi d’audience
================

Il existe deux catégories d’outils extérieurs aux applicatifs (au sens large) pour la mesure de l’audience : les analyseurs de log, qui travaillent à partir des fichiers de log du serveur HTTP, et les applications distantes qui collectent leurs données au moyen de balises spéciales insérées dans les pages.

Dans l’univers des solutions open source, on utilise fréquemment des outils comme AWStats (analyse de logs) ou Piwik (analyse sur base de marqueur).




AWStats
-------

:Version: 7.0
:Site: http://awstats.sourceforge.net
:Porteur: une communauté
:Licence: GPL

AWStats est un outil de suivi d’audience basé sur l’analyse des logs web. Il a été écrit par Laurent Destailleur, il y a quelques années déjà.

AWStats fournit de nombreuses statistiques, graphiques et rapports à partir de l’analyse des logs web (mais également FTP, Streaming et mail). Il supporte nativement la lecture des fichiers de  logs de la pluparts des serveurs web comme Apache, WebStar, IIS, etc. Parmi les fonctionnalités d’AWStats, on peut citer : le nombre de visites, de visiteurs uniques, de pages, de hits, de transfert, par domaine/pays, hôte, heure, navigateur, OS, etc. Un des points forts d’AWStats consiste en la possibilité de générer des tableaux de façon dynamique sans perte de performances notamment grâce à une politique de cache efficace. Il est très populaire au près des administrateurs système et réseau.

Écrit en Perl, AWStats peut être installé et exécuté sur la plupart des systèmes. C'est un outil de supervision très mature disposant de packages sur toutes les distributions Linux.


Piwik
-----

:Version: 1.5.1
:Site: http://piwik.org
:Porteur: une communauté
:Licence: GPL v3

Piwik est le successeur de la solution phpMyVisites. Dirigé par Matthieu Aubry, la solution a vu le jour recemment. Piwik ayant comme objectif de devenir une alternative de choix à Google Analytics.

Le défit est important ; pourtant, ses débuts sont prometteurs. En quelques clics, on accède aux graphiques des dernières visites, à la durée des visites, aux navigateurs des visiteurs, aux pays des visiteurs, à la liste de mots clés utilisés, à la liste de sites externes, aux classements des moteurs de recherche, à la répartition des visites par fuseau horaire, suivi des objectifs, répartition géographique, etc. Très jeune, Piwik fait déjà l’unanimité ; il a d’ailleurs reçu le prix du meilleur projet Sourceforge pour le mois de juillet 2010 ; de quoi lui prévoir de beaux jours.

Piwik est bâti sur une architecture LAMP, dispose d’un système de plugins, d’une API et d’une interface très simple d’utilisation grâce à l’utilisation combinée de l’Ajax et du Flash.
