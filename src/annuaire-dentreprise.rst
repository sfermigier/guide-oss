Annuaire d’entreprise
=====================

Les annuaires d’entreprise, également appélés Annuaire électroniques correspondent à un type de base de données spécialisées destinées à contenir de façon hiérarchique des éléments d’organisation de l’entreprise.

La plupart du temps, on y stocke des personnes (utilisateurs) et/ou des ressources (imprimantes, etc.).  Cependant l’usage d’un annuaire d’entreprise ne se limite pas à des recherches textuelles, on peut également l’utiliser pour constituer des carnets d’adresses, pour authentifier les utilisateurs, pour définir la politique de sécurité de l’entreprise, etc.

Il existe un standard utilisé dans la plupart des annuaires d’entreprise pour effectuer des requêtes (protocole LDAP).

Dans l’univers de l’open source, la solution OpenLDAP dispose de la plus grande notoriété même si des outils comme 389 Directory server dispose d’un beau périmètre fonctionnel.




389 directory server
--------------------

:Version: 1.2.9.9
:Site: http://directory.fedoraproject.org
:Porteur: un éditeur (Red Hat)

389 Directory Server, anciennement Fedora Directory Server, est un serveur LDAP développé par Red Hat au sein de la communauté Fedora. Il est basé sur le code du vénérable Netscape Directory Server, lui même basé sur le code de slapd original qui a également donné naissance à OpenLDAP. L'origine remonte donc à 1996, même si la première version de Fedora Directory Server est sortie en 2005.

389 Directory Server implémente le protocole LDAP v3, se distingue de ses concurrents par une interface graphique d'administration écrite en Java ainsi que le support de la réplication master-master, permettant ainsi la redondance des accès lectures et écritures. A noter également que 389 directory server peut servir de solution de remplacement à SunONE/JES Directory Server, la base de code étant très proche, et SunONE semblant ne pas être poursuivi depuis le rachat par Oracle.

389 Directory Server est distribué sous licence GPL.

389 Directory Server est écrit en majeure partie en C, avec certaines parties telles que le GUI en Java.




OpenLDAP
--------

:Version: 2.4.26
:Site: www.openldap.org
:Porteur: une communauté

OpenLDAP est un annuaire d’entreprise libre. Il représente une alternative solide aux annuaires commerciaux. OpenLDAP a été créé en 1998 par Kurt Zeilenga.

OpenLDAP implémente le protocole LDAP dans sa version la plus récente (V3) tout en fournissant une architecture extensible à travers un système d'overlay et backend. Chaque overlay fournit des fonctionnalités supplémentaires (groupe dynamique, log d'accès, politique de mot de passe, etc.). En outre, les données de l'annuaire peuvent être stockées dans différents backends (proxy ldap, transferts des requêtes à des scripts Perl ou Shell, ou une base de données SQL, ...). OpenLDAP intègre également des mécanismes de réplications et de délégation, permettant par exemple l'implémentation d'un annuaire LDAP distribué sur plusieurs sites, chacun disposant de l'administration de sa propre branche.

OpenLDAP est distribué sous licence OpenLDAP Public License, compatible avec la licence GPL et validé par la Free Software Fundation.

OpenLDAP est développé en C et fonctionne sous Linux, sous différentes variantes BSD, sur les OS à base UNIX (Android, AIX, HP UX, Solaris, etc...), ainsi que sous Windows et MacOSX.


Autres
------

Parmi les produits de l’univers Annuaire d’entreprise, on peut compléter la liste avec les outils ci-dessous :



Nom	URL / Site web

Apache Directory	http://directory.apache.org

OpenDS	http://www.opends.org

