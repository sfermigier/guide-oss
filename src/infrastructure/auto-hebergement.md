# Auto-hébergement (self-hosting) { #solutions-pour-lauto-hebergement-ou-self-hosting }

L’auto-hébergement, ou *self-hosting*, est la pratique consistant à héberger ses propres solutions informatiques plutôt que de recourir à des solutions hébergées par des tiers (SaaS ou *software as a service*).

Il donne la maîtrise des données et des applications, ce qui importe pour protéger des secrets d’affaires, respecter le RGPD ou réduire une dépendance. Il transfère en retour à l’organisation ce que le prestataire assurait : mises à jour, sauvegardes testées, surveillance, réponse aux incidents. La question à trancher est donc d’abord celle des compétences disponibles.

Cette page présente les distributions et plateformes qui permettent d’installer un catalogue d’applications sur un serveur. Les outils destinés à déployer ses propres applications sont à la page [PaaS](paas.md), les infrastructures de plus grande taille à la page [IaaS et cloud privé](iaas-cloud-prive.md).

## Approches de l’auto-hébergement

- **Sur site**{ #hebergement-sur-site } : des machines dans ses locaux. Contrôle maximal, mais matériel, alimentation, réseau et sécurité physique sont à sa charge.
- **Sur serveurs dédiés**{ #hebergement-sur-serveurs-dedies } loués à un hébergeur, qui fournit le matériel et le réseau, l’organisation administrant le reste.
- **Sur un cloud privé**{ #hebergement-cloud-prive }, interne ou opéré par un prestataire, qui ajoute élasticité et libre-service.
- **Sur un cloud public**{ #auto-hebergement-sur-cloud-public }, avec ses propres logiciels sur des machines virtuelles louées. L’investissement initial est faible, mais le fournisseur et le droit dont il relève restent à examiner.

## Avantages de l’auto-hébergement

- **Vie privée**{ #protection-de-la-vie-privee } : le *contrôle des données*{ #controle-total-des-donnees } et la *sécurisation des communications*{ #securisation-des-communications } ne dépendent plus d’un fournisseur de service.
- **Secret des affaires**{ #preservation-du-secret-des-affaires } : l’*isolation des informations stratégiques*{ #isolation-des-informations-strategiques } et la *conformité*{ #conformite-et-controle-juridique } se règlent en interne, y compris dans les secteurs réglementés.
- **Personnalisation**{ #personnalisation-et-flexibilite } : l’*adaptation aux besoins*{ #adaptation-aux-besoins-specifiques } est libre ; l’*évolutivité et la résilience*{ #evolutivite-et-resilience } dépendent des moyens que l’on y consacre.
- **Cloud public**{ #avantages-de-lauto-hebergement-sur-le-cloud-public } : on y gagne la *souplesse des ressources*{ #scalabilite-et-flexibilite } et la *réduction des coûts initiaux*{ #reduction-des-couts-initiaux }, en conservant le choix des logiciels.

## Solutions pour l’auto-hébergement

### YunoHost

Site
: <https://yunohost.org>

Porteur
: une communauté

Licence
: AGPL v3

YunoHost est une distribution d'origine française, fondée sur Debian, qui simplifie l'administration d'un serveur. Une interface web permet d'installer des centaines d'applications (Nextcloud, WordPress, Roundcube…), de gérer les utilisateurs, les domaines, les certificats, le courriel, le pare-feu et les sauvegardes.

Son point fort est l'intégration : un annuaire LDAP et un portail d'authentification unique sont partagés par les applications qui le permettent. Celles-ci étant installées directement sur le système, l'empaquetage dépend de bénévoles et sa qualité varie ; chaque application affiche son niveau. YunoHost convient aux particuliers, aux associations et aux petites structures.

YunoHost est écrit principalement en Python et Shell.

### Sandstorm

Site
: <https://sandstorm.org>

Porteur
: une communauté

Licence
: Apache 2.0

Sandstorm isole chaque document ou instance d'application dans son propre bac à sable, une idée toujours originale. La société fondatrice a cessé son activité en 2017 ; une petite communauté entretient le projet, dont le catalogue a vieilli. On le réservera aux installations existantes et à l'expérimentation.

### CasaOS

Site
: <https://casaos.zimaspace.com/>

Porteur
: une entreprise (IceWhale Technology, marque ZimaSpace)

Licence
: Apache 2.0

CasaOS ajoute à un système Debian, Ubuntu ou Raspberry Pi OS un tableau de bord web pour gérer fichiers et applications Docker, choisies dans un catalogue ou définies par l'utilisateur.

Il vise le serveur domestique : il n'offre ni annuaire partagé ni authentification unique. Il n'a pas vocation à être exposé directement sur Internet.

CasaOS est écrit en Go.

### HomelabOS

Site
: <https://homelabos.com>

Porteur
: une communauté

Licence
: MIT

HomelabOS est un ensemble de scripts Ansible qui déploie plus d'une centaine de services Docker sur un serveur, à partir de fichiers YAML. Il gère les certificats, les sauvegardes et, en option, un relais WireGuard. Il s'adresse à des administrateurs à l'aise avec Ansible et la ligne de commande.

### FreedomBox

Site
: <https://freedombox.org>

Porteur
: une communauté, avec le soutien d'une fondation (FreedomBox Foundation)

Licence
: AGPL v3

FreedomBox est un serveur personnel fondé sur Debian, dont il fait partie intégrante : on peut l'installer depuis les dépôts de la distribution ou sous forme d'image pour mini-PC et cartes ARM.

Une interface web installe et configure des applications tournées vers la vie privée : partage de fichiers, messagerie instantanée, VPN, Tor, synchronisation avec Syncthing. Le catalogue, limité aux paquets de Debian, est plus restreint que celui de YunoHost, mais bénéficie de son suivi de sécurité.

FreedomBox est écrit en Python (Django).

### Autres

- Proxmox VE, pour la couche de virtualisation sous-jacente (section [Virtualisation](virtualisation.md))
- [Hop3](paas.md#hop3){ #hop3 }, [Nua](paas.md#nua){ #nua }, [Piku](paas.md#piku){ #piku } et [Dokku](paas.md#dokku){ #dokku }, ainsi que Coolify et CapRover, présentés à la page PaaS
