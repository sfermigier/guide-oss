# Stockage

Le stockage se présente sous trois formes : en **bloc**, pour les disques des machines virtuelles et des bases de données ; en **fichiers**, pour le partage entre utilisateurs (SMB, NFS) ; en **objets**, pour les sauvegardes, les médias et les applications, le plus souvent par une API compatible avec S3 d'Amazon.

Pour une petite organisation, un serveur de fichiers bien sauvegardé est plus sûr qu'un cluster mal maîtrisé. Le stockage distribué répond au volume ou à la tolérance aux pannes, au prix d'un réseau dimensionné, de plusieurs machines et d'une exploitation suivie. La réplication protège d'une panne matérielle et laisse entier le risque d'effacement ou de rançongiciel : la [sauvegarde](sauvegarde.md) reste nécessaire.

Un changement récent est à connaître : **MinIO**, longtemps le choix courant pour le stockage objet, n'est plus maintenu comme logiciel libre. Son dépôt, sous AGPL v3, est archivé depuis avril 2026, l'éditeur renvoyant vers une offre propriétaire (AIStor). Les installations MinIO existantes sont à migrer vers une des solutions ci-dessous ; la compatibilité S3 n'étant jamais totale, on testera les fonctions réellement utilisées.

## Ceph

Site
: <https://ceph.io/en/>

Porteur
: une fondation (Ceph Foundation, Linux Foundation)

Licence
: LGPL v2.1 ou v3

Ceph est un système de stockage distribué qui fournit à la fois du bloc, du fichier et de l'objet (S3). Né des travaux de thèse de Sage Weil à l'université de Californie à Santa Cruz, il a été développé par Inktank, rachetée par Red Hat en 2014.

Les données sont réparties entre serveurs ordinaires par réplication ou code d'effacement, sans point de défaillance unique, avec une reconstruction automatique. Ceph est la solution de stockage courante d'OpenStack et est intégré à Proxmox VE ; Rook le déploie sur Kubernetes.

Il faut au moins trois nœuds, un réseau rapide et des compétences dédiées. Les performances se jouent sur le choix des disques et sur l'espace libre conservé pour les reconstructions.

Ceph est écrit en C++ et Python.

## Garage

Site
: <https://garagehq.deuxfleurs.fr/>

Porteur
: une association (Deuxfleurs)

Licence
: AGPL v3

Garage est un service de stockage objet compatible S3 développé par l'association française Deuxfleurs, avec des financements européens (NGI, NLnet).

Il est conçu pour de petits clusters dont les nœuds sont répartis sur plusieurs sites, reliés par des connexions ordinaires et constitués de matériel hétérogène. Il tient en un binaire, demande peu de ressources (1 Go de mémoire) et réplique les données entre zones ; il peut aussi servir des sites web statiques.

Son périmètre est restreint : les fonctions S3 avancées ne sont pas toutes présentes. Le code d'effacement n'est pas proposé. La documentation tient à jour la liste des appels pris en charge.

Garage est écrit en Rust.

## SeaweedFS

Site
: <https://github.com/seaweedfs/seaweedfs>

Porteur
: une communauté

Licence
: Apache 2.0

SeaweedFS est un système de fichiers distribué, inspiré à l'origine de Haystack de Facebook et orienté vers les très grands nombres de petits fichiers.

Un serveur maître gère des volumes. Un composant *filer* expose les données par S3, un montage POSIX ou WebDAV. Il propose réplication, code d'effacement et transfert des données froides vers un cloud. Un nœud unique suffit pour débuter.

Le projet est actif, porté par son auteur principal, Chris Lu, qui commercialise aussi une édition Enterprise. Le nombre de composants et d'options demande une lecture attentive de la documentation avant la production.

SeaweedFS est écrit en Go.

## TrueNAS

Site
: <https://www.truenas.com/>

Porteur
: un éditeur (iXsystems)

Licence
: LGPL v3 et GPL pour les principaux composants libres ; édition Enterprise commerciale

TrueNAS est un système de stockage en réseau fondé sur OpenZFS, héritier de FreeNAS. L'édition Community, gratuite, repose aujourd'hui sur Linux.

Il partage des fichiers (SMB, NFS) et des volumes (iSCSI), gère instantanés, réplication, chiffrement et intégration à un annuaire et sait héberger des applications en conteneurs. Son interface web le rend accessible à une petite équipe.

En mars 2026, l'éditeur a déplacé son système de construction dans une infrastructure interne, le dépôt public correspondant étant abandonné. Le code des composants reste publié, mais reproduire une image complète devient plus difficile : c'est un point à considérer pour qui tient à l'auditabilité. OpenMediaVault constitue une alternative communautaire.

TrueNAS est écrit principalement en Python et TypeScript.

## Autres

- OpenMediaVault, serveur de fichiers fondé sur Debian (GPL v3) : <https://www.openmediavault.org/>
- OpenZFS, système de fichiers et gestionnaire de volumes (CDDL) : <https://openzfs.org/>
- Rook, déploiement de Ceph sur Kubernetes (Apache 2.0) : <https://rook.io/>
- Longhorn, stockage en bloc pour Kubernetes (Apache 2.0) : <https://longhorn.io/>
- RustFS, stockage objet compatible S3, projet récent (Apache 2.0) : <https://rustfs.com/>
- Apache Ozone, stockage objet issu de l'écosystème Hadoop (Apache 2.0) : <https://ozone.apache.org/>
- JuiceFS, système de fichiers POSIX au-dessus d'un stockage objet (Apache 2.0) : <https://juicefs.com/>
- DRBD, réplication de blocs, présenté à la page [Haute disponibilité](haute-disponibilite.md#drbd)
- Samba, partage de fichiers, présenté à la page [Autres](autres.md#samba)
