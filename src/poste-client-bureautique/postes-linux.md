# Postes de travail Linux

Passer un parc sous Linux suppose deux choix liés : un environnement de bureau qui définit l’expérience de l’utilisateur et une distribution qui fixe le rythme des mises à jour, la durée de maintenance et le support commercial.

Un projet se joue d’abord sur l’inventaire : logiciels métier sans équivalent, périphériques, macros, authentification. Il se joue ensuite sur l’exploitation : déploiement, configuration, chiffrement et correctifs sont traités dans les parties [Systèmes d’exploitation](../infrastructure/systeme-exploitation-linux-bsd.md) et [Gestion de parc](../infrastructure/gestion-de-parc-et-inventaires.md). La gendarmerie nationale, avec GendBuntu fondé sur Ubuntu, en est l’exemple français le plus ancien.

## GNOME

Site
: <https://www.gnome.org/>

Porteur
: une fondation (GNOME Foundation)

Licence
: GPL v2 et autres licences libres selon les composants

GNOME est l’environnement de bureau par défaut de plusieurs grandes distributions, dont Debian, Fedora et Ubuntu. Son interface repose sur une vue d’ensemble des activités, un dock réduit et un nombre limité de réglages.

La cohérence des applications (fichiers, réglages, visionneuses) et l’accessibilité en font un choix courant pour un parc homogène. Un nouveau cycle est publié tous les six mois.

Les extensions tierces dépendent de la version installée : leur nombre est à limiter sur un poste géré. GNOME est écrit principalement en C, avec une part de JavaScript et de Rust.

## KDE Plasma

Site
: <https://kde.org/plasma-desktop/>

Porteur
: une communauté (KDE, représentée par l’association KDE e.V.)

Licence
: GPL et LGPL selon les composants

Plasma est le bureau du projet KDE. Il s’appuie sur Qt et reprend une organisation familière : barre des tâches, menu, fenêtres classiques, avec de nombreux réglages.

Il convient aux utilisateurs venant de Windows et aux organisations qui veulent configurer finement l’interface. Il s’accompagne des applications KDE, dont [Okular](notes-documents-et-synchronisation.md#okular) et [Kontact](messagerie-agenda-et-contacts.md#kontact).

La richesse des réglages demande de figer un profil commun dans un déploiement. Plasma est écrit en C++ et QML.

## Ubuntu Desktop

Site
: <https://ubuntu.com/desktop>

Porteur
: un éditeur (Canonical)

Licence
: licences libres multiples, selon les paquets

Ubuntu Desktop est la distribution de poste de Canonical, avec GNOME par défaut et des variantes pour d’autres bureaux (Kubuntu pour Plasma). La gendarmerie nationale en a dérivé GendBuntu.

Les versions LTS sont celles à retenir en entreprise. Canonical vend, sous le nom d’Ubuntu Pro, une couverture de sécurité prolongée, un outillage de gestion et un support.

Ses choix propres, notamment le format de paquet Snap, sont à apprécier selon la politique de distribution logicielle.

## Debian

Site
: <https://www.debian.org/>

Porteur
: une communauté (projet Debian)

Licence
: licences libres multiples, conformes aux principes du logiciel libre selon Debian

Debian est la distribution communautaire dont dérivent Ubuntu et Linux Mint. Sa version stable privilégie la prévisibilité : les logiciels y évoluent peu entre deux versions.

Elle convient aux organisations capables d’assurer elles-mêmes l’administration, sans dépendre d’un éditeur et laisse choisir l’environnement de bureau à l’installation. Le support se trouve chez des prestataires.

## Fedora Workstation

Site
: <https://fedoraproject.org/workstation/>

Porteur
: une communauté (parrainée par Red Hat)

Licence
: licences libres multiples, selon les paquets

Fedora Workstation présente rapidement les évolutions de Linux et de GNOME. Elle sert de terrain amont à Red Hat Enterprise Linux.

C’est un bon choix pour les développeurs. Son cycle court, avec deux versions par an, convient moins à un parc qui doit rester stable plusieurs années.

## Autres

- Linux Mint, dérivée d’Ubuntu, avec le bureau Cinnamon : <https://linuxmint.com/>
- openSUSE, en version stable (Leap) ou continue (Tumbleweed) : <https://get.opensuse.org/>
- Xfce, environnement léger pour machines anciennes : <https://www.xfce.org/>
- LXQt, environnement léger en Qt : <https://lxqt-project.org/>
- FOG et Clonezilla, pour le déploiement des postes : voir [Déploiement de postes](../infrastructure/deploiement-postes.md)
