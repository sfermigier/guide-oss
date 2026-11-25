# Annuaires d’entreprise { #annuaire-dentreprise }

Les annuaires d’entreprise, également appélés Annuaire électroniques, sont des bases de données spécialisées destinées à décrire de façon hiérarchique la structure de l’entreprise.

La plupart du temps, on y stocke des personnes (utilisateurs), des groupes et des ressources (imprimantes, etc.). Cependant l’usage d’un annuaire d’entreprise ne se limite pas à des recherches textuelles, on peut également l’utiliser pour constituer des carnets d’adresses, pour authentifier les utilisateurs, pour piloter la politique de sécurité de l’entreprise, etc.

Il existe un standard utilisé dans la plupart des annuaires d’entreprise pour effectuer des requêtes (protocole LDAP).

OpenLDAP et 389 Directory Server sont les deux serveurs LDAP libres de référence. Samba et FreeIPA visent un besoin plus large : gérer un domaine, Windows pour le premier, Linux pour le second.

## 389 directory server { #directory-server }

Site
: <https://www.port389.org/>

Porteur
: un éditeur (Red Hat) et une communauté

Licence
: GPL v3

389 Directory Server, anciennement Fedora Directory Server, est un serveur LDAP développé par Red Hat au sein de la communauté Fedora. Il est fondé sur le code du vénérable Netscape Directory Server, lui même fondé sur le code de slapd original qui a également donné naissance à OpenLDAP. L'origine remonte donc à 1996, même si la première version de Fedora Directory Server est sortie en 2005.

389 Directory Server implémente le protocole LDAP v3 et se distingue par la réplication multi-maître, qui permet la redondance des accès en lecture comme en écriture. L'ancienne console Java a été remplacée par une console web (Cockpit) et par des outils en ligne de commande. Le serveur constitue par ailleurs le socle de FreeIPA, la solution de gestion d'identité de Red Hat.

389 Directory Server est écrit en C et en Python.

## OpenLDAP

Site
: <https://www.openldap.org>

Porteur
: une communauté

Licence
: OpenLDAP Public License, compatible avec la licence GPL

OpenLDAP est un annuaire d’entreprise libre. Il représente une alternative solide aux annuaires commerciaux. OpenLDAP a été créé en 1998 par Kurt Zeilenga.

OpenLDAP implémente le protocole LDAP dans sa version la plus récente (V3) tout en offrant une architecture extensible par un système d'overlays et de backends. Chaque overlay fournit des fonctionnalités supplémentaires (groupe dynamique, log d'accès, politique de mot de passe, etc.). En outre, les données de l'annuaire peuvent être stockées dans différents backends (proxy ldap, transferts des requêtes à des scripts Perl ou Shell, ou une base de données SQL, ...). OpenLDAP intègre également des mécanismes de réplications et de délégation, permettant par exemple l'implémentation d'un annuaire LDAP distribué sur plusieurs sites, chacun disposant de l'administration de sa propre branche.

OpenLDAP est développé en C et fonctionne sous Linux, sous différentes variantes BSD, sur les OS à base UNIX (Android, AIX, HP UX, Solaris, etc...), ainsi que sous Windows et MacOSX.

## Samba Active Directory

Site
: <https://gitlab.com/samba-team/samba>

Porteur
: une communauté (Samba Team)

Licence
: GPL v3

Samba implémente les protocoles de partage de fichiers et d'authentification de Windows pour les systèmes Unix. Depuis la version 4, il peut tenir le rôle de contrôleur de domaine Active Directory, avec ses propres services LDAP et Kerberos et un DNS intégré.

Les postes Windows joignent ce domaine comme un domaine Microsoft. Les stratégies de groupe s'administrent avec les outils habituels de Windows (RSAT) ou avec `samba-tool`. C'est le socle de distributions comme Univention Corporate Server et une voie pour se passer de licences Windows Server dans un parc existant.

La compatibilité n'est pas totale et doit être vérifiée avant toute migration. Les niveaux fonctionnels 2012 R2 et 2016, introduits comme options dans la version 4.20, n'y étaient ni complets ni actifs par défaut. Les produits qui étendent le schéma, comme Exchange, demandent une étude particulière. On évitera de faire jouer à la même machine les rôles de contrôleur de domaine et de serveur de fichiers.

Samba est écrit en C et en Python. Son site historique est <https://www.samba.org/>.

## Autres

Parmi les produits de l’univers Annuaire d’entreprise, on peut compléter la liste avec les outils ci-dessous :

- FreeIPA, qui combine annuaire (389 DS), Kerberos, DNS et autorité de certification pour gérer un domaine UNIX/Linux complet: <https://www.freeipa.org/>
- Univention Corporate Server, distribution de gestion d'identité et de parc à base d'OpenLDAP et de Samba: <https://www.univention.com/>
- Apache Directory (serveur ApacheDS et outil d'administration Apache Directory Studio): <https://directory.apache.org/>
- LLDAP, annuaire léger pour les petites infrastructures: <https://github.com/lldap/lldap>
