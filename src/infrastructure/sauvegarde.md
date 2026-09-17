# Sauvegarde

Les outils de sauvegarde (*backup*), tel que Bacula, permettent l’enregistrement sur différents supports des données importantes pour l’entreprise, ceci à partir de règles évoluées.

Parmi les fonctionnalités que l’on retrouve dans les outils de sauvegarde, on peut citer : la planification des sauvegardes de manière très précise (agenda par exemple), la définition du type de sauvegarde (complète, incrémentale, différentielle), le lieu de stockage, etc. Certains outils vont jusqu’à proposer du multi-streaming, du multi-plexing, de la sauvegarde utilisateur, de la gestion des Pools de sauvegarde, etc.

## Bacula

Site
: <https://www.bacula.org/fr>

Porteur
: un éditeur (Bacula Systems)

Licence
: GPL

Bacula est un système de sauvegarde et de restauration très flexible développé en 2000 par Kern Sibbald et maintenant soutenu par la société Bacula Systems.

Bacula permet la planification des sauvegardes de manière très précise aussi bien en termes d'agenda que de type de sauvegarde (complète, incrémentale, différentielle). L'architecture de Bacula repose sur 3 composants essentiels : le Director est le chef d'orchestre (c'est lui qui coordonne de manière centralisée le déroulement des sauvegardes), le File Daemon est l'agent déployé sur chacun des clients chargé de réaliser la sauvegarde sous le contrôle du director, et le Storage Daemon assure le rôle d'interface avec les supports de stockage. Bacula implémente également les fonctionnalités avancées utilisées par toutes les solutions de sauvegarde performantes tel que le multi-streaming, le multi-plexing, la sauvegarde utilisateur, la gestion des Pools de sauvegarde, etc.

Bacula est développé en C/C++. Il s'appuie sur une base de données PostgreSQL ou MySQL.

## Autres

Sauvegarde d'entreprise :

- Bareos, fork de Bacula réalisé en 2013, à la communauté plus ouverte et dont l'édition libre est moins restreinte: <https://www.bareos.com/>
- Amanda: <http://www.amanda.org/>
- UrBackup, sauvegarde de postes clients et de serveurs: <https://www.urbackup.org/>
- Proxmox Backup Server, particulièrement adapté aux machines virtuelles et conteneurs, avec déduplication: <https://pbs.proxmox.com/>

Sauvegarde de fichiers, avec déduplication et chiffrement :

- Borg et Borgmatic: <https://www.borgbackup.org/> et <https://torsion.org/borgmatic/>
- Restic: <https://restic.net/>
- Kopia: <https://kopia.io/>
- BackupPC: <https://backuppc.github.io/backuppc/>

Synchronisation et stockage :

- Rclone, pour la copie vers et depuis les stockages objet et services cloud: <https://rclone.org/>
- Velero, pour la sauvegarde des ressources et volumes Kubernetes: <https://velero.io/>

Une sauvegarde n'a de valeur que si la restauration est testée régulièrement, et la règle dite « 3-2-1 » (trois copies, deux supports, une hors site) reste le meilleur garde-fou contre les rançongiciels, à condition d'y ajouter une copie immuable ou hors ligne.
