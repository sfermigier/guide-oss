Contrôle de postes à distance
=============================

Les solutions de contrôle de postes à distance sont de plus en nombreuses avec des changements notables en termes de technologies ces dernières années.

Elles ont été créées pour répondre à une problématique de support et d'assistance aux utilisateurs. Ces solutions de prise en main à distance peuvent selon les besoins, être localisées ou bien généralisées à tout ou partie des postes clients de l'entreprise.

Elles permettent de  répondre à différentes problématiques rencontrées dans les entreprises dont la vision partagée du poste de travail et le transfert de fichiers.

Parmi l’offre open source, on peut citer des outils comme X2Go, TigerVNC, RustDesk, Apache Guacamole ou OpenSSH, ce dernier étant le favori des administrateurs systèmes dans le monde des serveurs UNIX.


X2Go (successeur de FreeNX)
---------------------------

:Site: https://wiki.x2go.org/
:Porteur: une communauté
:Licence: GPL v2

FreeNX était une implémentation libre du protocole NX de la société NoMachine, qui permettait l'accès distant à des environnements graphiques UNIX avec d'excellentes performances sur les réseaux à faible bande passante. NoMachine ayant cessé de publier les versions récentes de son protocole sous licence libre, et le site berlios.de ayant fermé, FreeNX a disparu.

C'est **X2Go** qui en a repris le flambeau : fondé sur la dernière version libre du protocole NX, il permet l'ouverture de sessions graphiques distantes persistantes (reconnexion sans perte de la session), le partage d'imprimantes, du son et des dossiers locaux, et dispose de clients pour Linux, Windows et macOS. Il reste très employé pour l'accès à des postes de travail Linux distants.


TightVNC
--------

:Site: https://www.tightvnc.com
:Porteur: une communauté
:Licence: GPL v2

TightVNC est un ensemble d'outils implémentant le protocole VNC.

Ce protocole permet l'affichage graphique à distance via le protocole réseau RFB (*Remote Frame Buffer*). Il est très répandu pour l'administration graphique des postes de travail et l'assistance utilisateur, quel que soit le système d'exploitation.

Sur les systèmes Linux actuels, on lui préférera **TigerVNC** (https://tigervnc.org/), mieux maintenu, plus performant et compatible avec les serveurs graphiques récents, ou **wayvnc** pour les sessions Wayland.

TightVNC est développé en C/C++.


OpenSSH
-------

:Site: https://www.openssh.com
:Porteur: une fondation (OpenBSD)
:Licence: BSD

OpenSSH est un ensemble de logiciels permettant l'administration de serveurs à distance.

Dans le monde des serveurs UNIX, il s'agit du logiciel favori des administrateurs systèmes. Au fil des années, OpenSSH s’est étoffé de nombreuses fonctionnalités qui permettent de l’utiliser bien au delà de la classique « console réseau ». OpenSSH permet notamment de mettre en place des formes simples de VPN, et l'affichage déporté d'applications graphiques.

OpenSSH est développé depuis 1999 par la fondation OpenBSD, qui référence un certain nombre de sociétés assurant son support.

Comme la majorité des projets BSD, OpenSSH est écrit en C.


Autres
------

- RustDesk, alternative libre à TeamViewer et AnyDesk, avec serveur de relais auto-hébergeable: https://rustdesk.com/
- Apache Guacamole, passerelle d'accès distant (RDP, VNC, SSH) utilisable depuis un simple navigateur: https://guacamole.apache.org/
- MeshCentral, administration de parc et prise en main à distance depuis le navigateur: https://meshcentral.com/
- FreeRDP, implémentation libre du protocole RDP: https://www.freerdp.com/
- Remmina, client multiprotocole (RDP, VNC, SSH, SPICE) pour Linux: https://remmina.org/
- KRDC: https://apps.kde.org/krdc/
