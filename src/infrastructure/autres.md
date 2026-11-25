# Autres outils d’infrastructure { #autres }

Dans cette dernière rubrique de la dimension « Infrastructure » nous présentons d’autres outils open source particulièrement utiles pour des administrateurs Système & Réseaux.

Nous présentons CUPS (un serveur d’impression), Samba (partage de fichiers et contrôleur de domaine) et ProFTPD (un serveur FTP). Les serveurs DNS et DHCP, dont BIND, ont leur propre page : [DNS et DHCP](dns-dhcp.md).

## CUPS

Site
: <https://openprinting.github.io/cups/>

Porteur
: une communauté (OpenPrinting)

Licence
: Apache 2.0

CUPS (*Common Unix Printing System*) est le serveur d'impression de référence des systèmes UNIX. Sa création remonte à 1999, par Michael Sweet et Andrew Senft, fondateurs d'Easy Software Products. Le projet a été racheté par Apple en 2007 ; depuis le départ de son auteur principal en 2019, le développement est assuré par le groupe OpenPrinting de la Linux Foundation, qui publie les versions utilisées par les distributions Linux.

Il est utilisé aussi bien sur les postes de travail que sur les serveurs d'impression dédiés. Il prend en charge un très grand nombre d'imprimantes, offre des capacités d'administration (gestion des files, comptabilité) et la compatibilité avec les protocoles d'impression classiques : IPP, AppSocket, LPD, SMB. L'évolution majeure de ces dernières années est le passage à l'impression « sans pilote » (IPP Everywhere, AirPrint), qui rend inutile l'installation de pilotes pour la plupart des imprimantes récentes.

## Samba

Site
: <https://www.samba.org/>

Porteur
: une communauté

Licence
: GPL v3

Samba est un serveur SMB pour postes de travail Windows. La première version de Samba remonte à 1992. Elle fut écrite par Andrew Tridgell à l'Australian National University.

Sous Windows, le protocole SMB est utilisé pour le partage de fichiers et d'imprimantes. Samba permet d'utiliser un serveur UNIX pour mettre ces ressources à disposition de clients Windows, assurant ainsi la compatibilité entre les deux environnements. Depuis la version 4, Samba est également capable de fonctionner comme contrôleur de domaine Active Directory : c'est la seule implémentation libre de ce rôle, ce qui en fait une brique clé des stratégies de sortie des environnements Microsoft.

## ProFTPD

Site
: <http://www.proftpd.org/>

Porteur
: une communauté

Licence
: GPL v2

ProFTPD est un serveur FTP libre, modulaire, dont la configuration rappelle celle d'Apache Httpd. Il gère les utilisateurs virtuels, les quotas, FTPS et l'authentification par SQL, LDAP ou RADIUS. Un module lui ajoute SFTP. Le protocole FTP, même complété par TLS, est déconseillé pour les échanges nouveaux : on lui préférera SFTP (fourni par OpenSSH), WebDAV ou un [stockage objet](stockage.md) compatible S3.

## Autres

- [BIND](dns-dhcp.md#bind){ #bind }, serveur DNS, désormais présenté à la page DNS et DHCP
- [Stockage](stockage.md), pour les serveurs de fichiers et le stockage objet
