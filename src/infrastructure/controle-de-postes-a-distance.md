# Contrôle de postes à distance

Les solutions de contrôle de postes à distance sont de plus en plus nombreuses avec des changements notables en termes de technologies ces dernières années.

Elles ont été créées pour répondre à une problématique de support et d'assistance aux utilisateurs. Ces solutions de prise en main à distance peuvent selon les besoins, être localisées ou bien généralisées à tout ou partie des postes de travail de l'entreprise.

Elles permettent de répondre à différentes problématiques rencontrées dans les entreprises dont la vision partagée du poste de travail et le transfert de fichiers.

Parmi l’offre open source, on peut citer des outils comme X2Go, TigerVNC, RustDesk, Apache Guacamole ou OpenSSH, ce dernier étant le favori des administrateurs systèmes dans le monde des serveurs UNIX.

## X2Go (successeur de FreeNX)

Site
: <https://wiki.x2go.org/>

Porteur
: une communauté

Licence
: GPL v2

FreeNX était une implémentation libre du protocole NX de la société NoMachine, qui permettait l'accès distant à des environnements graphiques UNIX avec d'excellentes performances sur les réseaux à faible bande passante. NoMachine ayant cessé de publier les versions récentes de son protocole sous licence libre et le site berlios.de ayant fermé, FreeNX a disparu.

C'est **X2Go** qui en a repris le flambeau : fondé sur la dernière version libre du protocole NX, il permet l'ouverture de sessions graphiques distantes persistantes (reconnexion sans perte de la session), le partage d'imprimantes, du son et des dossiers locaux. Il dispose de clients pour Linux, Windows et macOS. Il reste très employé pour l'accès à des postes de travail Linux distants.

## TightVNC

Site
: <https://www.tightvnc.com>

Porteur
: un éditeur (GlavSoft)

Licence
: GPL v2, avec une licence commerciale en option

TightVNC implémente le protocole VNC, qui affiche un bureau à distance. La version pour Windows reste maintenue ; celle pour Linux et UNIX en est restée à la branche 1.3. Sous Linux, on lui préférera **TigerVNC** (<https://tigervnc.org/>), ou **wayvnc** pour les sessions Wayland.

## OpenSSH

Site
: <https://www.openssh.org/>

Porteur
: une communauté (projet OpenBSD)

Licence
: BSD

OpenSSH est un ensemble de logiciels permettant l'administration de serveurs à distance.

Dans le monde des serveurs UNIX, il s'agit du logiciel favori des administrateurs systèmes. Au fil des années, OpenSSH s’est étoffé de nombreuses fonctionnalités qui permettent de l’utiliser bien au-delà de la classique « console réseau ». OpenSSH permet notamment de mettre en place des formes simples de VPN et l'affichage déporté d'applications graphiques.

OpenSSH est développé depuis 1999 par le projet OpenBSD.

Comme la majorité des projets BSD, OpenSSH est écrit en C.

## Autres

- RustDesk, alternative libre à TeamViewer et AnyDesk, avec serveur de relais auto-hébergeable: <https://rustdesk.com/>
- Apache Guacamole, passerelle d'accès distant (RDP, VNC, SSH) utilisable depuis un simple navigateur: voir [Bastions et accès privilégiés](bastions.md#apache-guacamole)
- MeshCentral, administration de parc et prise en main à distance depuis le navigateur: <https://meshcentral.com/>
- FreeRDP, implémentation libre du protocole RDP: <https://www.freerdp.com/>
- Remmina, client multiprotocole (RDP, VNC, SSH, SPICE) pour Linux: <https://remmina.org/>
- KRDC: <https://apps.kde.org/krdc/>
