Virtualisation
==============

La virtualisation de serveurs est un ensemble de techniques et d’outils permettant de faire tourner plusieurs systèmes d’exploitation sur un même serveur physique.

Depuis les premières éditions de ce guide, la **conteneurisation** a pris une place au moins aussi importante que la virtualisation : plutôt que d'émuler une machine complète, elle isole des processus qui partagent le noyau de l'hôte, pour un coût très inférieur. Les deux approches sont aujourd'hui complémentaires : machines virtuelles pour l'isolation forte et les systèmes hétérogènes, conteneurs pour le déploiement applicatif. Cette section présente les deux.

Le principe de la virtualisation est donc un principe de partage : les différents systèmes d’exploitation se partagent les ressources du serveur.

Pour être utile de manière opérationnelle, la virtualisation doit respecter deux principes fondamentaux : le cloisonnement (chaque système d’exploitation a un fonctionnement indépendant, et ne peut interférer avec les autres en aucune manière) et la transparence (le fait de fonctionner en mode virtualisé ne change rien au fonctionnement du système d’exploitation et à fortiori des applications).


KVM
---

:Site: https://linux-kvm.org/
:Porteur: une communauté
:Licence: GPL v2

KVM (*Kernel-based Virtual Machine*) est la solution de virtualisation intégrée au noyau Linux depuis 2007. C'est un module du noyau, qui expose les instructions de virtualisation matérielle des processeurs (Intel VT-x, AMD-V) ; QEMU s'appuie sur lui pour l'émulation des périphériques. Les deux projets sont complémentaires.

KVM est capable d'exécuter des systèmes invités sous tous les systèmes d'exploitation courants en simulant un matériel standardisé, et prend en charge des fonctions avancées telles que la migration à chaud et l'inspection de l'état des machines virtuelles. C'est aujourd'hui l'hyperviseur libre de référence : il constitue le socle d'OpenStack, de Proxmox VE et de l'essentiel des offres IaaS du marché, y compris chez les grands fournisseurs de cloud. On l'administre le plus souvent via la bibliothèque libvirt (https://libvirt.org/) et ses outils (virsh, virt-manager).


QEMU
----

:Site: https://www.qemu.org
:Porteur: une communauté
:Licence: GPL

QEMU est un émulateur de système libre développé à l'origine par Fabrice Bellard et à présent étendu par une large communauté de contributeurs.

QEMU fonctionne sur les plateformes x86, x64, PPC, Sparc et ARM et fonctionne sous les systèmes d'exploitation Linux, FreeBSD, NetBSD, OpenBSD, Mac OS X, Unix et Microsoft Windows. Il sait émuler des systèmes à base de processeurs x86, PowerPC, ARM et SPARC. Du fait de sa versatilité, il est souvent utilisé dans le cadre de travaux de recherche et développement.

Utilisé conjointement à KVM, il permet de virtualiser un système x86 au-dessus d'un processeur x86 avec une perte de performance minimale.


Xen
---

:Site: https://xenproject.org/
:Porteur: une fondation (Linux Foundation)
:Licence: GPL v2

Xen est un hyperviseur gérant la paravirtualisation. Le projet est né en 2003 sous la forme d'un projet de recherche de l'université de Cambridge au Royaume-Uni.

La paravirtualisation désigne la capacité, pour un système de virtualisation, d'interagir avec les systèmes virtualisés, qui en ont conscience : les machines virtuelles sont ainsi plus performantes et mieux administrables. Xen, issu d'un projet de recherche universitaire, a été transféré en 2013 à la Linux Foundation, qui en assure la gouvernance sous le nom de Xen Project. Il reste très présent chez les hébergeurs et dans les usages où l'isolation prime, notamment avec Qubes OS, et sert de base à XenServer (Cloud Software Group) et à XCP-ng (https://xcp-ng.org/), sa déclinaison entièrement open source.


OpenVZ
------

:Site: https://openvz.org
:Porteur: une communauté
:Licence: GPL v2

OpenVZ est une solution de virtualisation légère pour Linux créée en 2005.

Comme toute solution de virtualisation légère, OpenVZ ne permet d'exécuter que des systèmes Linux. En contrepartie, les performances obtenues sont bien plus proches des performances natives que pour tout autre type de virtualisation, en particulier pour les entrées-sorties, avec une consommation de mémoire réduite.

Ses usages ont toutefois été largement absorbés par les mécanismes d'isolation intégrés au noyau Linux (cgroups et espaces de noms), qui sous-tendent Docker, Podman et LXC/Incus. OpenVZ conserve une base installée chez certains hébergeurs de VPS, mais ne constitue plus un choix par défaut.


Oracle VirtualBox
-----------------

:Site: https://www.virtualbox.org
:Porteur: un éditeur (Oracle)
:Licence: GPL v2

VirtualBox est une solution de virtualisation, créée en 2007 et destinée aux postes de travail.

VirtualBox prend en charge un grand nombre de systèmes d'exploitation invités et dispose de fonctionnalités d'interaction avec ces systèmes : partage de fichiers, intégration du pointeur de souris, fusion du bureau avec le bureau hôte. Attention au modèle de licence : le cœur est sous GPL, mais l'*Extension Pack* (USB 2.0/3.0, RDP, démarrage PXE) est soumis à une licence propriétaire dont l'usage professionnel est payant, point régulièrement source de non-conformité en entreprise.


Conteneurs
----------

:Sites: https://www.docker.com/, https://podman.io/, https://kubernetes.io/
:Porteur: un éditeur (Docker Inc.), un éditeur (Red Hat) et une fondation (CNCF)
:Licence: Apache 2.0 pour l'essentiel des composants

Apparu en 2013, **Docker** a popularisé le format d'image et l'expérience d'utilisation qui sont devenus le standard du déploiement applicatif. Le format et l'exécution sont aujourd'hui normalisés par l'*Open Container Initiative*, ce qui garantit l'interopérabilité entre les outils.

**Podman**, développé par Red Hat, offre une interface en ligne de commande compatible avec celle de Docker, sans démon central et avec la possibilité de faire tourner les conteneurs sans privilèges (*rootless*), ce qui en fait une alternative appréciée dans les environnements sensibles.

**Kubernetes**, issu de Google et confié en 2015 à la *Cloud Native Computing Foundation*, est devenu le standard de fait de l'orchestration de conteneurs : ordonnancement sur un parc de machines, redémarrage automatique, montée en charge, réseau et stockage abstraits, déploiements progressifs. Sa richesse a un coût d'exploitation réel, ce qui a fait le succès de distributions allégées comme K3s (https://k3s.io/) ou Talos Linux pour les petites infrastructures et l'informatique de périphérie.


Proxmox VE
----------

:Site: https://www.proxmox.com/en/products/proxmox-virtual-environment/overview
:Porteur: une entreprise autrichienne (Proxmox Server Solutions)
:Licence: AGPL v3

Proxmox Virtual Environment est une plateforme de virtualisation complète, fondée sur Debian, qui combine KVM pour les machines virtuelles et LXC pour les conteneurs système, avec une interface web unifiée.

Elle intègre nativement la gestion de cluster, la haute disponibilité, la migration à chaud, le stockage distribué avec Ceph et la sauvegarde (via Proxmox Backup Server). Entièrement sous licence libre (seuls l'accès au dépôt de paquets « entreprise » et le support sont payants), elle est devenue l'alternative de référence à VMware vSphere pour les PME, les collectivités et les hébergeurs, d'autant que les changements tarifaires opérés par Broadcom après le rachat de VMware ont accéléré les migrations.


Incus et LXC
------------

:Site: https://linuxcontainers.org/incus/
:Porteur: une communauté (Linux Containers)
:Licence: Apache 2.0

LXC fournit depuis 2008 les conteneurs « système » du noyau Linux : des machines complètes, là où Docker isole des processus. LXD, l'outil de gestion développé par Canonical au-dessus de LXC, a fait l'objet en 2023 d'un fork communautaire, **Incus**, à la suite de sa reprise en main par Canonical ; Incus est aujourd'hui la version recommandée par le projet Linux Containers et empaquetée par Debian.

Incus gère indifféremment des conteneurs système et des machines virtuelles, avec la gestion de cluster, les instantanés et la migration à chaud. C'est une solution intermédiaire intéressante entre la virtualisation complète et les conteneurs applicatifs.


