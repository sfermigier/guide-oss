Autres
======

Dans cette dernière rubrique de la dimension « Infrastructure » nous présentons d’autres outils open source particulièrement utiles pour des administrateurs Système & Réseaux.

Nous présentons notamment CUPS (un serveur d’impression), SAMBA (permettant l’échange de fichiers UNIX sur des postes Windows), ProFTPD (un serveur FTP), et BIND (un serveur DNS).


CUPS
----

:Site: https://openprinting.github.io/cups/
:Porteur: une communauté (OpenPrinting)
:Licence: Apache 2.0

CUPS (*Common Unix Printing System*) est le serveur d'impression de référence des systèmes UNIX. Sa création remonte à 1999, par Michael Sweet et Andrew Senft, fondateurs d'Easy Software Products. Le projet a été racheté par Apple en 2007 ; depuis le départ de son auteur principal en 2019, le développement est assuré par le groupe OpenPrinting de la Linux Foundation, qui publie les versions utilisées par les distributions Linux.

Il est utilisé aussi bien sur les postes de travail que sur les serveurs d'impression dédiés. Il prend en charge un très grand nombre d'imprimantes, offre des capacités d'administration (gestion des files, comptabilité) et la compatibilité avec les protocoles d'impression classiques : IPP, AppSocket, LPD, SMB. L'évolution majeure de ces dernières années est le passage à l'impression « sans pilote » (IPP Everywhere, AirPrint), qui rend inutile l'installation de pilotes pour la plupart des imprimantes récentes.


Samba
-----

:Site: https://www.samba.org/
:Porteur: une communauté
:Licence: GPL v3

Samba est un serveur SMB pour postes de travail Windows. C’est en 1992 que remonte la première version de Samba. Elle fût écrite par Andrew Tridgell à l'Australian National University.

Sous Windows, le protocole SMB est utilisé pour le partage de fichiers et d'imprimantes. Samba permet d'utiliser un serveur UNIX pour mettre ces ressources à disposition de clients Windows, assurant ainsi la compatibilité entre les deux environnements. Depuis la version 4, Samba est également capable de fonctionner comme contrôleur de domaine Active Directory : c'est la seule implémentation libre de ce rôle, ce qui en fait une brique clé des stratégies de sortie des environnements Microsoft.


ProFTPD
-------

:Site: http://www.proftpd.org/
:Porteur: une communauté
:Licence: GPL

ProFTPD est un serveur FTP libre, richement paramétrable et bien documenté. Rappelons toutefois que le protocole FTP, même complété par TLS, est aujourd'hui déconseillé pour les échanges nouveaux : on lui préférera SFTP (fourni par OpenSSH), le partage WebDAV ou un stockage objet compatible S3.

Il dispose de fonctionnalités avancées comme le chroot, les hôtes et utilisateurs virtuels, la comptabilité et les quotas. ProFTPD dispose d’une syntaxe d’accès et de configuration proche de celle du serveur Web Apache. ProFTPD permet d’utiliser une base de données MySQL pour gérer les comptes FTP en lieu et place des utilisateurs de la machine. Son architecture est modulaire, ce qui a permis d'écrire des extensions pour le support de la cryptographie SSL/TLS (protocole FTPS) et l'extension de l'authentification via des bases RADIUS, LDAP ou SQL.


Bind
----

:Site: https://www.isc.org/bind/
:Porteur: un entreprise à but non-lucratif (Internet Systems Consortium, Inc.)
:Licence: BSD

BIND est le serveur DNS de référence. Les origines de BIND remontent aux années 1980 par quatre étudiants de l’Université de Californie.

Édité par l'*Internet Systems Consortium*, BIND 9 est un serveur DNS permettant aussi bien la résolution de noms que l'hébergement de ses propres zones. Il prend en charge l'ensemble des fonctionnalités avancées, notamment DNSSEC, les vues, les zones dynamiques et, plus récemment, le chiffrement du transport (DoT, DoH).

La tendance actuelle est toutefois à la séparation des rôles, chaque fonction étant assurée par un logiciel spécialisé plus petit :

- Unbound, résolveur récursif validant DNSSEC: https://www.nlnetlabs.nl/projects/unbound/about/
- NSD et Knot DNS, serveurs autoritaires: https://www.nlnetlabs.nl/projects/nsd/about/ et https://www.knot-dns.cz/
- PowerDNS, serveur autoritaire et résolveur avec stockage en base de données: https://www.powerdns.com/
- dnsmasq, pour les petits réseaux (DNS, DHCP, TFTP): https://thekelleys.org.uk/dnsmasq/doc.html
- CoreDNS, serveur DNS des clusters Kubernetes: https://coredns.io/
