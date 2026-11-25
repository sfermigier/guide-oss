# DNS et DHCP

Le DNS traduit les noms en adresses ; le DHCP distribue les adresses et les paramètres réseau aux postes. Ces deux services sont discrets, mais leur arrêt rend le système d'information inutilisable : ils se déploient en redondance et leur configuration se sauvegarde.

Deux rôles du DNS sont à distinguer. Un serveur **autoritaire** publie les zones dont l'organisation est responsable ; un **résolveur récursif** répond aux postes internes en interrogeant l'arborescence publique. La pratique actuelle les sépare, chacun étant confié à un logiciel spécialisé. La validation DNSSEC, le chiffrement du transport (DoT, DoH) et le filtrage des domaines malveillants se décident surtout au niveau du résolveur.

En France et en Europe, la maîtrise du résolveur est aussi un sujet de confidentialité, puisqu'il voit l'ensemble des noms consultés. Tous les logiciels présentés ici peuvent être exploités sur site.

## BIND { #bind }

Site
: <https://www.isc.org/bind/>

Porteur
: une association à but non lucratif (Internet Systems Consortium)

Licence
: MPL 2.0

BIND est le serveur DNS historique, dont les origines remontent à l'université de Californie à Berkeley dans les années 1980.

Édité par l'*Internet Systems Consortium*, BIND 9 assure aussi bien la résolution de noms que l'hébergement de zones. Il prend en charge l'ensemble des fonctionnalités avancées, notamment DNSSEC, les vues, les zones dynamiques et le chiffrement du transport (DoT, DoH).

Sa polyvalence explique son statut de référence documentaire du domaine. Elle implique aussi une surface d'exposition large et des correctifs de sécurité réguliers à suivre ; l'éditeur vend un support professionnel.

BIND est écrit en C.

## Unbound

Site
: <https://www.nlnetlabs.nl/projects/unbound/about/>

Porteur
: une fondation (NLnet Labs)

Licence
: BSD 3-clauses

Unbound est un résolveur récursif validant DNSSEC, développé par l'organisme néerlandais à but non lucratif NLnet Labs.

Il assure le cache, la validation, le chiffrement des requêtes (DoT, DoH), la minimisation des noms transmis et le filtrage par listes de réponses (RPZ). Il sait servir quelques enregistrements locaux, mais n'a pas vocation à publier des zones, rôle de NSD chez le même porteur.

C'est le résolveur fourni par OpenBSD, FreeBSD, OPNsense et pfSense. C'est aussi un choix courant pour remplacer la fonction récursive de BIND.

Unbound est écrit en C.

## PowerDNS

Site
: <https://www.powerdns.com/>

Porteur
: un éditeur (PowerDNS, groupe Open-Xchange)

Licence
: GPL v2

PowerDNS réunit trois logiciels distincts, d'origine néerlandaise : un serveur autoritaire, un résolveur récursif et dnsdist, répartiteur de charge et filtre pour le trafic DNS.

Le serveur autoritaire lit ses zones dans une base de données (PostgreSQL, MySQL, SQLite), dans des fichiers ou par d'autres greffons. Il s'administre par API HTTP. C'est ce qui le rend commode pour les hébergeurs et pour les organisations qui automatisent la gestion de nombreuses zones.

L'éditeur commercialise support et offres complémentaires pour opérateurs. L'interface web la plus répandue, PowerDNS-Admin, est un projet tiers dont l'état de maintenance est à contrôler.

PowerDNS est écrit en C++.

## Knot DNS

Site
: <https://www.knot-dns.cz/>

Porteur
: une association (CZ.NIC)

Licence
: GPL v2 ou ultérieure

Knot DNS est un serveur autoritaire développé par CZ.NIC, l'association qui gère le domaine national tchèque.

Il vise la performance et l'automatisation : signature DNSSEC et rotation des clés, transferts incrémentaux, mises à jour dynamiques, limitation du débit des réponses, reconfiguration à chaud. Il convient aux registres, aux hébergeurs et à tout gestionnaire de zones signées.

Le même porteur développe Knot Resolver, résolveur récursif distinct (<https://www.knot-resolver.cz/>).

Knot DNS est écrit en C.

## Kea

Site
: <https://www.isc.org/kea/>

Porteur
: une association à but non lucratif (Internet Systems Consortium)

Licence
: MPL 2.0 ; quelques extensions sous licence commerciale

Kea est le serveur DHCP de l'*Internet Systems Consortium*, successeur d'ISC DHCP, dont la maintenance a pris fin en 2022.

Il sépare les services DHCPv4, DHCPv6 et la mise à jour dynamique du DNS, se configure en JSON et se pilote par une API. Les baux et les réservations peuvent résider dans MySQL ou PostgreSQL ; la haute disponibilité est prise en charge. Stork, projet associé, fournit un tableau de bord.

La version 3.0 a placé sous MPL 2.0 douze extensions auparavant payantes. Deux restent réservées aux abonnés, dont le contrôle d'accès par rôle.

Kea est écrit en C++.

## Autres

- NSD, serveur autoritaire de NLnet Labs (BSD) : <https://www.nlnetlabs.nl/projects/nsd/about/>
- dnsmasq, DNS, DHCP et TFTP pour les petits réseaux : <https://thekelleys.org.uk/dnsmasq/doc.html>
- CoreDNS, serveur DNS des clusters Kubernetes (Apache 2.0) : <https://coredns.io/>
- Technitium DNS Server, résolveur et serveur autoritaire avec interface web (GPL v3) : <https://technitium.com/dns/>
- Pi-hole et AdGuard Home, résolveurs filtrants pour petits réseaux : <https://pi-hole.net/> et <https://adguard.com/adguard-home/overview.html>
- NetBox, référentiel d'adressage, présenté à la page [Gestion de parc et inventaires](gestion-de-parc-et-inventaires.md)
