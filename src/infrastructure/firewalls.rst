Firewalls
=========

La notion de firewall est souvent liée à celle de routage, c'est-à-dire l'acheminement des flux réseau entre les différentes machines.

Les firewalls sont donc généralement installés sur des équipements de routage, dont ils sont une partie intégrante. Ce qui signifie que le routage peut être modifié par une décision du firewall, et que le firewall appliquera des règles de filtrage différentes selon l'origine et la destination du trafic. C’est la mission principale du firewall.

Le firewall peut également être utilisé dans un rôle plus qualitatif, plus fin, comme le volume de bande passante autorisé pour telle ou telle application dans tel ou tel contexte.

En matière de firewall, l’offre open source est très riche avec des produits tels que Packet Filter, NetFilter ou pfSense.


pf (Packet Filter)
------------------

:Version: 4.9 (suit les versions d’OpenBSD)
:Site: www.openbsd.org/faq/pf
:Porteur: une communauté
:Licence: BSD

pf (Packet Filter) est la couche de filtrage intégrée aux systèmes libres hérités de BSD UNIX (FreeBSD, NetBSD, OpenBSD...). pf a été crée en 2001 par Daniel Hartmeier en remplacement du logiciel IPFilter.

Ce système présente l'avantage d'avoir un langage de configuration simple, et d'intégrer les fonctionnalités de NAT et de QoS. Packet Filter est devenu l'outil libre le plus puissant pour jouer le rôle de pare-feu. Il peut également servir pour équilibrer la charge et gérer le trafic réseau sur des Unix libres BSD.


NetFilter
---------

:Version: 1.4.12
:Site: www.netfilter.org
:Porteur: une communauté
:Licence: GPL v2

Netfilter, parfois appelé iptables, est la couche de filtrage intégrée au noyau Linux. Il a été créé en 1998 par Rusty Russell.

Il s'agit d'un système extrêmement souple, qui s'intègre avec les fonctionnalités de routage et de QoS du noyau, et comprend les fonctions de NAT. Il dispose de nombreux critères de filtrage (temps, volume de données), et des modules de suivi de connexions pour les protocoles complexes (FTP, SIP, H323). Il est en revanche complexe à configurer, et on utilise souvent un outil tiers pour générer sa configuration (Shorewall, ferm, etc.).


pfSense
-------

:Version: 2.0
:Site: www.pfsense.org
:Porteur: un éditeur (BSD Perimeter)
:Licence: BSD

pfSense est une distribution logicielle permettant de réaliser une passerelle réseau à partir d'un serveur x86. Il date de 2004 à partir d’un fork de m0n0wall par Chris Buechler et Scott Ullrich.

Très fréquemment rencontré dans les PME et les petites structures, pfSense offre une solution complète de routage, filtrage, VPN et partage de connexion. Il est basé sur pf, et intègre un grand nombre de composants tiers : serveur DHCP/DNS, serveur de temps, proxy web, monitoring... La configuration se fait entièrement via une interface web.

Un support officiel est proposé par la société BSD Perimeter.


Autres
------

Parmi les produits de l’univers Firewalls, on peut compléter la liste avec les outils ci-dessous :


- NuFW:  http://www.nufw.org

- Uncomplicated Firewall:  https://launchpad.net/ufw

- Firewall Builder:  http://www.fwbuilder.org

- Ferm: http://ferm.foo-projects.org

- ShoreWall: http://shorewall.net

