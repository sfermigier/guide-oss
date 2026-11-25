# Sauvegarde

Les outils de sauvegarde (*backup*) permettent l’enregistrement sur différents supports des données importantes pour l’entreprise, ceci à partir de règles évoluées.

Parmi les fonctionnalités que l’on retrouve dans les outils de sauvegarde, on peut citer : la planification des sauvegardes de manière très précise (agenda par exemple), la définition du type de sauvegarde (complète, incrémentale, différentielle), le lieu de stockage, etc. Certains outils vont jusqu’à proposer du multi-streaming, du multi-plexing, de la sauvegarde utilisateur, de la gestion des Pools de sauvegarde, etc.

## Bacula

Site
: <https://www.bacula.org/fr>

Porteur
: un éditeur (Bacula Systems)

Licence
: GPL

Bacula est un système de sauvegarde et de restauration très flexible développé en 2000 par Kern Sibbald et maintenant soutenu par la société Bacula Systems.

Bacula permet la planification des sauvegardes de manière très précise aussi bien en termes d'agenda que de type de sauvegarde (complète ou partielle, en mode incrémental ou différentiel). L'architecture de Bacula repose sur 3 composants essentiels : le Director est le chef d'orchestre (c'est lui qui coordonne de manière centralisée le déroulement des sauvegardes), le File Daemon est l'agent déployé sur chacun des clients chargé de réaliser la sauvegarde sous le contrôle du director et le Storage Daemon assure le rôle d'interface avec les supports de stockage. Bacula implémente également les fonctionnalités avancées utilisées par toutes les solutions de sauvegarde performantes telles que le multi-streaming, le multi-plexing, la sauvegarde individuelle, la gestion des Pools de sauvegarde, etc.

Bacula est développé en C/C++. Il s'appuie sur une base de données PostgreSQL ou MySQL.

## Bareos

Site
: <https://www.bareos.com/>

Porteur
: un éditeur (Bareos GmbH & Co. KG)

Licence
: AGPL v3

Bareos est un fork de Bacula, développé depuis 2012 par une société allemande. Il en reprend l'architecture : un *director* qui planifie, des agents sur les machines à sauvegarder et des démons de stockage.

Il sauvegarde des serveurs physiques, des machines virtuelles, des bases de données et des applications vers des disques, des bandes ou un stockage S3, avec des greffons pour PostgreSQL, MariaDB, VMware ou Proxmox VE notamment. Une interface web et une API complètent la console. C'est l'une des rares solutions libres adaptées aux bandes et aux parcs hétérogènes.

L'éditeur vend des abonnements donnant accès à des paquets suivis et au support. La configuration, héritée de Bacula, est très paramétrable et demande un apprentissage.

Bareos est écrit en C++ et Python, avec une interface web en PHP et JavaScript.

## BorgBackup

Site
: <https://www.borgbackup.org/>

Porteur
: une communauté

Licence
: BSD 3-clauses

BorgBackup (Borg) est un outil de sauvegarde en ligne de commande, né en 2015 d'un fork d'Attic.

Il découpe les fichiers en blocs dédupliqués, les compresse et les chiffre avant leur envoi. Le dépôt se trouve sur un disque local ou un serveur accessible par SSH, sur lequel Borg est de préférence installé ; un mode d'ajout seul limite les dégâts d'une machine compromise. Les archives peuvent se monter comme un système de fichiers.

Borgmatic (<https://torsion.org/borgmatic/>) y ajoute configuration, rétention et sauvegarde de bases de données. Vorta propose une interface graphique. Un même dépôt partagé par plusieurs machines réduit la déduplication à un accès exclusif : on préfère un dépôt par machine. La perte de la clé ou de la phrase secrète rend les données irrécupérables.

Borg est écrit en Python, avec des parties en Cython et en C.

## Restic

Site
: <https://restic.net/>

Porteur
: une communauté

Licence
: BSD 2-clauses

Restic est un outil de sauvegarde en ligne de commande, distribué sous la forme d'un binaire unique pour Linux, macOS, Windows et les BSD.

Il offre une déduplication et un chiffrement systématiques, vers un disque local, un serveur SFTP, un stockage compatible S3 ou, par l'intermédiaire de Rclone, de nombreux autres services. Plusieurs machines peuvent partager un dépôt. Les instantanés peuvent être montés ou restaurés partiellement.

Restic ne planifie rien : on l'associe à systemd, cron ou un outil comme Backrest. Le serveur REST du projet propose un mode d'ajout seul. Comme avec Borg, le mot de passe du dépôt doit être conservé séparément.

Restic est écrit en Go.

## Autres

Sauvegarde d'entreprise :

- Amanda: <http://www.amanda.org/>
- UrBackup, sauvegarde de postes clients et de serveurs: <https://www.urbackup.org/>
- Proxmox Backup Server, particulièrement adapté aux machines virtuelles et conteneurs, avec déduplication (AGPL v3): <https://pbs.proxmox.com/>

Sauvegarde de fichiers, avec déduplication et chiffrement :

- Plakar, sauvegarde chiffrée et dédupliquée, d'origine française (ISC): <https://plakar.io/>
- Kopia: <https://kopia.io/>
- BackupPC: <https://backuppc.github.io/backuppc/>

Synchronisation et stockage :

- Rclone, pour la copie vers et depuis les stockages objet et services cloud: <https://rclone.org/>
- Velero, pour la sauvegarde des ressources et volumes Kubernetes: <https://velero.io/>

Une sauvegarde n'a de valeur que si la restauration est testée régulièrement. La règle dite « 3-2-1 » (trois copies, deux supports, une hors site) reste le meilleur garde-fou contre les rançongiciels, à condition d'y ajouter une copie immuable ou hors ligne.
