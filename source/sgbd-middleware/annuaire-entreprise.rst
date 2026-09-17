Annuaire d’entreprise
=====================

Les annuaires d’entreprise, également appélés Annuaire électroniques, sont des bases de données spécialisées destinées à contenir de façon hiérarchique des éléments d’organisation de l’entreprise.

La plupart du temps, on y stocke des personnes (utilisateurs), des groupes et des ressources (imprimantes, etc.). Cependant l’usage d’un annuaire d’entreprise ne se limite pas à des recherches textuelles, on peut également l’utiliser pour constituer des carnets d’adresses, pour authentifier les utilisateurs, pour piloter la politique de sécurité de l’entreprise, etc.

Il existe un standard utilisé dans la plupart des annuaires d’entreprise pour effectuer des requêtes (protocole LDAP).

Dans l’univers de l’open source, la solution OpenLDAP dispose de la plus grande notoriété même si un outil comme 389 Directory server dispose d’un beau périmètre fonctionnel.




389 directory server
--------------------

:Site: https://www.port389.org/
:Porteur: un éditeur (Red Hat) et une communauté
:Licence: GPL v3

389 Directory Server, anciennement Fedora Directory Server, est un serveur LDAP développé par Red Hat au sein de la communauté Fedora. Il est fondé sur le code du vénérable Netscape Directory Server, lui même fondé sur le code de slapd original qui a également donné naissance à OpenLDAP. L'origine remonte donc à 1996, même si la première version de Fedora Directory Server est sortie en 2005.

389 Directory Server implémente le protocole LDAP v3 et se distingue par la réplication multi-maître, qui permet la redondance des accès en lecture comme en écriture. L'ancienne console Java a été remplacée par une console web (Cockpit) et par des outils en ligne de commande. Le serveur constitue par ailleurs le socle de FreeIPA, la solution de gestion d'identité de Red Hat.

389 Directory Server est écrit en C et en Python.




OpenLDAP
--------

:Site: https://www.openldap.org
:Porteur: une communauté
:Licence: OpenLDAP Public License, compatible avec la licence GPL

OpenLDAP est un annuaire d’entreprise libre. Il représente une alternative solide aux annuaires commerciaux. OpenLDAP a été créé en 1998 par Kurt Zeilenga.

OpenLDAP implémente le protocole LDAP dans sa version la plus récente (V3) tout en offrant une architecture extensible par un système d'overlays et de backends. Chaque overlay fournit des fonctionnalités supplémentaires (groupe dynamique, log d'accès, politique de mot de passe, etc.). En outre, les données de l'annuaire peuvent être stockées dans différents backends (proxy ldap, transferts des requêtes à des scripts Perl ou Shell, ou une base de données SQL, ...). OpenLDAP intègre également des mécanismes de réplications et de délégation, permettant par exemple l'implémentation d'un annuaire LDAP distribué sur plusieurs sites, chacun disposant de l'administration de sa propre branche.


OpenLDAP est développé en C et fonctionne sous Linux, sous différentes variantes BSD, sur les OS à base UNIX (Android, AIX, HP UX, Solaris, etc...), ainsi que sous Windows et MacOSX.


Autres
------

Parmi les produits de l’univers Annuaire d’entreprise, on peut compléter la liste avec les outils ci-dessous :

- FreeIPA, qui combine annuaire (389 DS), Kerberos, DNS et autorité de certification pour gérer un domaine UNIX/Linux complet: https://www.freeipa.org/
- Samba Active Directory, seule implémentation libre d'un contrôleur de domaine Active Directory: https://www.samba.org/
- Univention Corporate Server, distribution de gestion d'identité et de parc à base d'OpenLDAP et de Samba: https://www.univention.com/
- Apache Directory (serveur ApacheDS et outil d'administration Apache Directory Studio): https://directory.apache.org/
- LLDAP, annuaire léger pour les petites infrastructures: https://github.com/lldap/lldap
