# IaaS et cloud privé

Une plateforme IaaS (*Infrastructure as a Service*) met à disposition des machines virtuelles, des réseaux et des volumes de stockage en libre-service, par un portail ou une API, avec des quotas et une séparation entre locataires. Elle s'appuie sur un hyperviseur, le plus souvent KVM ou Xen, présenté à la page [Virtualisation](virtualisation.md).

La distinction avec une plateforme de virtualisation est une affaire d'usage. Une équipe qui administre elle-même quelques dizaines de machines virtuelles se contentera de Proxmox VE ou de XCP-ng. Un cloud privé se justifie lorsque plusieurs équipes ou clients provisionnent eux-mêmes leurs ressources, que l'on veut automatiser par API, ou que l'on est soi-même hébergeur.

Le critère principal est le coût d'exploitation : nombre de composants, compétences requises, durée de maintenance des versions et procédure de mise à jour. La migration depuis VMware est aujourd'hui un motif de projet fréquent.

## OpenStack

Site
: <https://www.openstack.org/>

Porteur
: une fondation (OpenInfra Foundation)

Licence
: Apache 2.0

OpenStack est né en 2010 d'une initiative commune de la NASA et de Rackspace. Le projet est porté par l'OpenInfra Foundation, rattachée à la Linux Foundation depuis 2025.

Il se compose de services distincts qui communiquent par API : Nova pour le calcul, Neutron pour le réseau, Cinder pour les volumes, Glance pour les images, Keystone pour l'identité, Swift pour les objets, Horizon pour le portail. On n'installe que ceux dont on a besoin. Il équipe des opérateurs de télécommunications, des centres de recherche et des hébergeurs, notamment européens. Il gère de très grands parcs.

Cette modularité se paie en complexité : OpenStack suppose une équipe dédiée ou un prestataire. Il se déploie avec un outil spécialisé (Kolla-Ansible, OpenStack-Ansible) ou une distribution d'éditeur.

OpenStack est écrit en Python.

## Apache CloudStack

Site
: <https://cloudstack.apache.org/>

Porteur
: une fondation (Apache Software Foundation)

Licence
: Apache 2.0

CloudStack a été développé par Cloud.com, rachetée en 2011 par Citrix, qui a confié le projet à la fondation Apache en 2012.

C'est une plateforme intégrée : un serveur de gestion, une base de données, une interface web et une API couvrent le calcul, le réseau, le stockage, les comptes, les quotas et la mesure de la consommation. Elle pilote KVM, VMware et XenServer/XCP-ng, ce qui permet une migration par étapes. Elle sait déployer des clusters Kubernetes.

Elle est employée surtout par des hébergeurs et des opérateurs. Plus simple à installer et à mettre à jour qu'OpenStack, elle offre moins de services complémentaires et un écosystème d'intégrateurs plus restreint.

CloudStack est écrit en Java.

## OpenNebula

Site
: <https://opennebula.io/>

Porteur
: un éditeur (OpenNebula Systems)

Licence
: Apache 2.0 pour l'édition Community, licence commerciale pour les paquets de l'édition Enterprise

OpenNebula est une plateforme de cloud privé et hybride d'origine espagnole, issue d'un projet de recherche lancé en 2005.

Elle gère des machines virtuelles KVM et des conteneurs LXC, les réseaux virtuels, le stockage, les groupes et les quotas, avec un portail unique et un catalogue d'images. Son architecture est légère et convient à des installations de taille moyenne ou réparties sur plusieurs sites.

Le modèle comporte deux éditions : Community (Apache 2.0) et Enterprise, dont les paquets stabilisés, les versions de maintenance et certains outils sont réservés aux abonnés. Les paquets de migration entre versions, restreints pendant plusieurs années, sont de nouveau inclus dans l'édition Community depuis la version 7.0.

OpenNebula est écrit principalement en C++, Ruby et JavaScript.

## XCP-ng

Site
: <https://xcp-ng.org/>

Porteur
: une entreprise (Vates)

Licence
: GPL v2 pour l'essentiel ; AGPL v3 et ISC pour Xen Orchestra

XCP-ng est une plateforme de virtualisation fondée sur l'hyperviseur Xen, créée en 2018 à partir des sources de XenServer par la société française Vates, qui en assure le développement et le support.

Associée à Xen Orchestra, l'interface web du même éditeur, elle couvre la gestion centralisée des hôtes, la migration à chaud, la haute disponibilité, la sauvegarde et la réplication des machines virtuelles, la délégation de droits et l'automatisation par API. Placée entre la virtualisation classique et le cloud privé, elle vise en premier lieu le remplacement de vSphere ou de XenServer.

L'appliance Xen Orchestra prête à l'emploi et le support sont vendus par abonnement ; la construction à partir des sources reste possible, à la charge de l'utilisateur.

XCP-ng réunit des composants en C (Xen, noyau Linux) et OCaml (XAPI) ; Xen Orchestra est écrit en JavaScript et TypeScript.

## Autres

- Proxmox VE et Incus, présentés à la page [Virtualisation](virtualisation.md)
- KubeVirt, machines virtuelles gérées par Kubernetes (Apache 2.0) : <https://kubevirt.io/>
- Harvester, infrastructure hyperconvergée fondée sur Kubernetes et KubeVirt (Apache 2.0) : <https://harvesterhci.io/>
- Ganeti, gestion de clusters de machines virtuelles (BSD) : <https://ganeti.org/>
- oVirt, dont était issu Red Hat Virtualization : <https://www.ovirt.org/>
