VPN
===

Un VPN, Réseau Privé Virtuel en français, peut être définie, assez largement, par les différentes techniques permettant d’étendre le Réseau de l’entreprise en préservant la confidentialité des données et en traversant les barrières physiques des réseaux traditionnels.

Les solutions VPN apportent généralement les bénéfices suivants : authentification par clé publique, confidentialité des échanges, confidentialité a posteriori en cas de compromission des secrets cryptographiques et transport de paquets à destination d’un réseau privé via un réseau public.

Dans l’univers de l’open source, on compte de nombreuses solutions de qualité dont OpenVPN et OpenSWAN présenté ci-après.




OpenVPN
-------

:Version: 2.2.1
:Site: http://openvpn.net
:Porteur: un éditeur (OpenVPN Technologies)

OpenVPN est le fer de lance d’une catégorie de VPN assez récente : les VPN SSL. Il existe depuis 2002 et a été écrit par James Yonan.

Ces derniers réutilisent les mécanismes du chiffrement SSL pour authentifier et chiffrer les connexions. OpenVPN est basé sur le produit OpenSSL, la principale implémentation libre du protocole SSL, tant en termes de qualité que d’adoption, et s’appuie sur ses routines de chiffrement et de vérification d’identité pour assurer une très bonne sécurisation des données.

OpenVPN est distribué sous licence GPL v2.

Disponible sous Solaris, Linux, OpenBSD, FreeBSD, NetBSD, Mac OS X, Windows 2000, XP, Vista et 7, il offre aussi de nombreuses fonctions de sécurité et de contrôle.




OpenSwan
--------

:Version: 2.6.35
:Site: www.openswan.org
:Porteur: une communauté

Openswan est une implémentation IPsec pour Linux, descendante du projet FreeS/WAN (remontant à 1999).

OpenSwan permet la mise en place de liens IPsec entre machines, mais également de tunnels VPN, et ce aussi bien entre réseaux d'entreprises que pour des clients nomades. Il est compatible avec un grand nombre de systèmes d’exploitation et de solutions propriétaires.

OpenSwan est disponible sous licence GPL.



Firewalls

La notion de firewall est souvent liée à celle de routage, c'est-à-dire l'acheminement des flux réseau entre les différentes machines.

Les firewalls sont donc généralement installés sur des équipements de routage, dont ils sont une partie intégrante. Ce qui signifie que le routage peut être modifié par une décision du firewall, et que le firewall appliquera des règles de filtrage différentes selon l'origine et la destination du trafic. C’est la mission principale du firewall.

Le firewall peut également être utilisé dans un rôle plus qualitatif, plus fin, comme le volume de bande passante autorisé pour telle ou telle application dans tel ou tel contexte. 

En matière de firewall, l’offre open source est très riche avec des produits tels que Packet Filter, NetFilter ou pfSense.




pf (Packet Filter)
------------------

:Version: 4.9 (suit les versions d’OpenBSD)
:Site: www.openbsd.org/faq/pf
:Porteur: une communauté

pf (Packet Filter) est la couche de filtrage intégrée aux systèmes libres hérités de BSD UNIX (FreeBSD, NetBSD, OpenBSD...). pf a été crée en 2001 par Daniel Hartmeier en remplacement du logiciel IPFilter.

Ce système présente l'avantage d'avoir un langage de configuration simple, et d'intégrer les fonctionnalités de NAT et de QoS. Packet Filter est devenu l'outil libre le plus puissant pour jouer le rôle de pare-feu. Il peut également servir pour équilibrer la charge et gérer le trafic réseau sur des Unix libres BSD.

pf est distribué sous la licence BSD.




NetFilter
---------

:Version: 1.4.12
:Site: www.netfilter.org
:Porteur: une communauté

Netfilter, parfois appelé iptables, est la couche de filtrage intégrée au noyau Linux. Il a été créé en 1998 par Rusty Russell.

Il s'agit d'un système extrêmement souple, qui s'intègre avec les fonctionnalités de routage et de QoS du noyau, et comprend les fonctions de NAT. Il dispose de nombreux critères de filtrage (temps, volume de données), et des modules de suivi de connexions pour les protocoles complexes (FTP, SIP, H323). Il est en revanche complexe à configurer, et on utilise souvent un outil tiers pour générer sa configuration (Shorewall, ferm, etc.).

NetFilter est distribué sous la licence sous GPL v2.




pfSense
-------

:Version: 2.0
:Site: www.pfsense.org
:Porteur: un éditeur (BSD Perimeter)

pfSense est une distribution logicielle permettant de réaliser une passerelle réseau à partir d'un serveur x86. Il date de 2004 à partir d’un fork de m0n0wall par Chris Buechler et Scott Ullrich.

Très fréquemment rencontré dans les PME et les petites structures, pfSense offre une solution complète de routage, filtrage, VPN et partage de connexion. Il est basé sur pf, et intègre un grand nombre de composants tiers : serveur DHCP/DNS, serveur de temps, proxy web, monitoring... La configuration se fait entièrement via une interface web.

pfSense est disponible sous licence BSD. Un support officiel est proposé par la société BSD Perimeter.




Autres
------

Parmi les produits de l’univers Firewalls, on peut compléter la liste avec les outils ci-dessous :



Nom	URL / Site web

NuFW	http://www.nufw.org

Uncomplicated Firewall	https://launchpad.net/ufw

Firewall Builder	http://www.fwbuilder.org

Ferm	http://ferm.foo-projects.org

ShoreWall	http://shorewall.net

