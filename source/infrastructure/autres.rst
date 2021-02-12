Autres
======

Dans cette dernière rubrique de la dimension « Infrastructure » nous présentons d’autres outils open source particulièrement utiles pour des administrateurs Système & Réseaux.

Nous présentons notamment CUPS (un serveur d’impression), SAMBA (permettant l’échange de fichiers UNIX sur des postes Windows), ProFTPD (un serveur FTP), et BIND (un serveur DNS).


CUPS
----

:Site: https://www.cups.org/
:Porteur: un éditeur (Apple Inc.)
:Licence: Apache 2.0

CUPS (Common Unix Printing System) est un serveur d'impression populaire pour les systèmes UNIX. Sa création remonte à la fin de l’année 1999 par Michael Sweet et Andrew Senft, propriétaires de Easy Software Products.

Il est utilisé aussi bien sur les postes de travail que sur les serveurs d'impression dédiés. Il offre le support d'un très grand nombre d'imprimantes, des capacités d'administration (gestion des files, comptabilité), et la compatibilité avec les protocoles d'impression classique : IPP, AppSocket, LPD, SMB (Windows).


Samba
-----

:Site: https://www.samba.org/
:Porteur: une communauté
:Licence: GPL

Samba est un serveur SMB pour postes de travail Windows. C’est en 1992 que remonte la première version de Samba. Elle fût écrite par Andrew Tridgell à l'Australian National University.

Sous Windows, le protocole SMB est utilisé pour le partage de fichiers et d'imprimantes. Samba permet l'utilisation d'un serveur UNIX pour la mise à disposition de ces ressources à des clients Windows, permettant ainsi la compatibilité entre les deux environnements. Samba est également capable de fonctionner en contrôleur de domaine sur des petits réseaux.


ProFTPD
-------

:Site: http://www.proftpd.org/
:Porteur: une communauté
:Licence: GPL

ProFTPD est un serveur FTP libre très puissant et bien documenté.

Il dispose de fonctionnalités avancées comme le chroot, les hôtes et utilisateurs virtuels, la comptabilité et les quotas. ProFTPD dispose d’une syntaxe d’accès et de configuration proche de celle du serveur Web Apache. ProFTPD permet d’utiliser une base de données MySQL pour gérer les comptes FTP en lieu et place des utilisateurs de la machine. Son architecture est modulaire, ce qui a permis d'écrire des extensions pour le support de la cryptographie SSL/TLS (protocole FTPS) et l'extension de l'authentification via des bases RADIUS, LDAP ou SQL.


Bind
----

:Site: https://www.isc.org/bind/
:Porteur: un entreprise à but non-lucratif (Internet Systems Consortium, Inc.)
:Licence: BSD

BIND est le serveur DNS de référence. Les origines de BIND remontent aux années 1980 par quatre étudiants de l’Université de Californie.

Édité par l'Internet Systems Consortium, BIND est un serveur DNS permettant aussi bien la résolution des noms auprès de serveurs autoritaires, que l'hébergement de sa propre zone. Il supporte toutes les fonctionnalités avancées, notamment DNSSEC (depuis la réécriture de son code au début des années 2000).
