# Bastions et accès privilégiés

Un bastion est le point de passage obligé des accès d'administration. Il authentifie les administrateurs, limite les cibles accessibles à chacun, enregistre les sessions et évite que les comptes à privilèges des serveurs soient connus de tous. Il répond à une partie des exigences de traçabilité de la directive NIS 2 et des référentiels de sécurité.

Les approches diffèrent. Une passerelle web donne accès à des bureaux et terminaux depuis un navigateur ; un bastion transparent laisse les outils habituels (OpenSSH, client RDP) se connecter à travers lui ; une plateforme d'accès délivre des certificats de courte durée en s'appuyant sur le fournisseur d'identité. Les protocoles à couvrir (SSH, RDP, bases de données, Kubernetes) orientent le choix.

Les licences sont à vérifier dans cette catégorie, où les produits complets sont souvent commerciaux. Un bastion étant par ailleurs un point de défaillance unique, un accès de secours documenté est indispensable.

## Apache Guacamole

Site
: <https://guacamole.apache.org/>

Porteur
: une fondation (Apache Software Foundation)

Licence
: Apache 2.0

Apache Guacamole est une passerelle d'accès distant utilisable depuis un navigateur, sans logiciel client ni greffon, pour RDP, VNC, SSH, Telnet et Kubernetes.

Un service, guacd, traduit ces protocoles. Une application web les présente. Les utilisateurs et les connexions se gèrent dans une base de données ou un annuaire LDAP ; OpenID Connect, SAML, CAS et TOTP sont pris en charge, ainsi que l'enregistrement des sessions.

Il convient au télétravail, aux prestataires et à l'accès à des postes Windows ou Linux. L'audit et la gestion des secrets des comptes cibles y sont plus simples que dans un produit spécialisé. Les outils natifs ne peuvent pas passer par lui.

Guacamole est écrit en C (guacd), Java et JavaScript.

## Warpgate

Site
: <https://warpgate.null.page/>

Porteur
: une communauté

Licence
: Apache 2.0

Warpgate est un bastion transparent pour SSH, HTTPS, Kubernetes, MySQL, PostgreSQL, RDP et VNC, qui ne demande ni client particulier ni agent sur les cibles.

Il se présente sous la forme d'un binaire unique, avec une interface web d'administration. Les droits s'attribuent par rôle et par cible ; les sessions sont enregistrées, consultables en direct ou rejouées. La double authentification (TOTP) et OpenID Connect sont intégrés, ainsi qu'un accès par navigateur.

Le projet est actif et repose sur une équipe restreinte. Sa numérotation reste en 0.x : mises à jour et sauvegarde de la configuration sont à planifier en conséquence.

Warpgate est écrit en Rust.

## The Bastion

Site
: <https://ovh.github.io/the-bastion/>

Porteur
: une entreprise (OVHcloud)

Licence
: Apache 2.0

The Bastion est le bastion SSH qu'OVHcloud a développé pour ses propres équipes et publié en source ouverte.

Il sépare la connexion de l'administrateur au bastion et celle du bastion à la cible, gère des groupes avec délégation, journalise chaque accès et enregistre les terminaux. Il repose sur les outils standards d'un système Linux ou BSD, sans base de données externe. Il peut être déployé en cluster.

Son périmètre est SSH, avec quelques usages associés (scp, sftp, rsync, HTTPS pour des équipements). Il s'administre en ligne de commande et s'adresse à des équipes système à l'aise avec ce mode.

The Bastion est écrit en Perl et Shell.

## Teleport

Site
: <https://goteleport.com/>

Porteur
: un éditeur (Teleport, anciennement Gravitational)

Licence
: AGPL v3 pour le code source ; licence commerciale pour les binaires et images de l'édition Community depuis la version 16

Teleport est une plateforme d'accès à l'infrastructure (SSH, Kubernetes, bases de données, applications web, RDP) qui remplace les clés permanentes par des certificats de courte durée.

Il enregistre les sessions, gère des rôles et des demandes d'accès et maintient un inventaire des ressources. L'authentification unique avec un fournisseur d'identité d'entreprise relève pour l'essentiel de l'édition commerciale.

Le point à connaître est la licence. Depuis la version 16 (juin 2024), les binaires, paquets et images de l'édition Community ne sont utilisables par une entreprise que si elle compte moins de 100 salariés et réalise moins de 10 millions de dollars de revenus annuels. Le code source reste sous AGPL v3 : une entreprise plus grande doit donc compiler elle-même, souscrire, ou choisir une autre solution.

Teleport est écrit en Go et TypeScript, avec des composants en Rust.

## Autres

- JumpServer, bastion web d'origine chinoise (GPL v3, édition Enterprise distincte) : <https://www.jumpserver.com/>
- Redemption, proxy RDP et VNC avec enregistrement des sessions, publié par l'éditeur français WALLIX (GPL v2) : <https://github.com/wallix/redemption>
- OpenSSH, dont la directive `ProxyJump` et les certificats suffisent à un rebond simple : voir [Contrôle de postes à distance](controle-de-postes-a-distance.md#openssh)
