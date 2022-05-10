Firewalls
=========

La notion de firewall est souvent liée à celle de routage, c'est-à-dire l'acheminement des flux réseau entre les différentes machines.

Les firewalls sont donc généralement installés sur des équipements de routage, dont ils sont une partie intégrante. Ce qui signifie que le routage peut être modifié par une décision du firewall, et que le firewall appliquera des règles de filtrage différentes selon l'origine et la destination du trafic. C'est la mission principale du firewall.

Le firewall peut également être utilisé dans un rôle plus qualitatif, plus fin, comme le volume de bande passante autorisé pour telle ou telle application dans tel ou tel contexte.

En matière de firewall, l'offre open source est très riche avec des produits tels que Packet Filter, NetFilter ou pfSense.


pf (Packet Filter)
------------------

:Site: https://www.openbsd.org/faq/pf
:Porteur: une communauté
:Licence: BSD

pf (Packet Filter) est la couche de filtrage intégrée aux systèmes libres hérités de BSD UNIX (FreeBSD, NetBSD, OpenBSD...). pf a été créé en 2001 par Daniel Hartmeier en remplacement du logiciel IPFilter.

Ce système présente l'avantage d'avoir un langage de configuration simple, et d'intégrer les fonctionnalités de NAT et de QoS. Packet Filter est devenu l'outil libre le plus puissant pour jouer le rôle de pare-feu. Il peut également servir pour équilibrer la charge et gérer le trafic réseau sur des Unix libres BSD.


NetFilter
---------

:Site: https://www.netfilter.org/
:Porteur: une communauté
:Licence: GPL v2

Netfilter, parfois appelé iptables, est la couche de filtrage intégrée au noyau Linux. Il a été créé en 1998 par Rusty Russell.

Il s'agit d'un système extrêmement souple, qui s'intègre avec les fonctionnalités de routage et de QoS du noyau, et comprend les fonctions de NAT. Il dispose de nombreux critères de filtrage (temps, volume de données), et des modules de suivi de connexions pour les protocoles complexes (FTP, SIP, H323). Il est en revanche complexe à configurer, et on utilise souvent un outil tiers pour générer sa configuration (Shorewall, ferm, etc.).


DynFi Firewall
--------------

:Site: https://dynfi.com/dynfi-firewall/
:Porteur: la société Française DynFi
:Licence: BSD

DynFi Firewall est un pare-feu français dérivé de pfSense et OPNsense qui apporte des nouvelles fonctionnalités et un système de compilation issue de FreeBSD (projet poudrière).

Il intègre directement un certain nombre de packages (zerotier, Clamav, Ntopng et Nprobe) ainsi q’un nouveau système de filtrage basé sur les DNS.

Le code est disponibile sur Github, le firewall est agrémenté d’un gestionnaire centralisé unique en son genre.

pfSense
-------

:Site: https://www.pfsense.org/
:Porteur: un éditeur (BSD Perimeter)
:Licence: BSD

pfSense est une distribution logicielle permettant de réaliser une passerelle réseau à partir d'un serveur x86. Elle date de 2004 à partir d'un fork de m0n0wall par Chris Buechler et Scott Ullrich.

Très fréquemment rencontrée dans les PME et les petites structures, pfSense offre une solution complète de routage, filtrage, VPN et partage de connexion. Il est basé sur pf, et intègre un grand nombre de composants tiers : serveur DHCP/DNS, serveur de temps, proxy web, monitoring... La configuration se fait entièrement via une interface web.

Depuis 2014 la solution a été reprise par la société Netgate et s’éloigne progressivement de l’Open Source. 
Un support officiel est proposé par la société Netgate.


Autres
------

Parmi les produits de l'univers Firewalls, on peut compléter la liste avec les outils ci-dessous :

- ShoreWall: https://shorewall.org/
- Uncomplicated Firewall (UFW): https://launchpad.net/ufw
- Firewall Builder: https://github.com/fwbuilder/fwbuilder/
- Ferm: http://ferm.foo-projects.org
