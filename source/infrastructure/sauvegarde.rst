Sauvegarde
==========

Les outils de sauvegarde (*backup*), tel que Bacula, permettent l’enregistrement sur différents supports des données importantes pour l’entreprise, ceci à partir de règles évoluées.

Parmi les fonctionnalités que l’on retrouve dans les outils de sauvegarde, on peut citer : la planification des sauvegardes de manière très précise (agenda par exemple), la définition du type de sauvegarde (complète, incrémentale, différentielle), le lieu de stockage, etc. Certains outils vont jusqu’à proposer du multi-streaming, du multi-plexing, de la sauvegarde utilisateur, de la gestion des Pools de sauvegarde, etc.


Bacula
------

:Site: https://www.bacula.org/fr
:Porteur: un éditeur (Bacula Systems)
:Licence: GPL

Bacula est un système de sauvegarde et de restauration très flexible développé en 2000 par Kern Sibbald et maintenant soutenu par la société Bacula Systems.

Bacula permet la planification des sauvegardes de manière très précise aussi bien en termes d'agenda que de type de sauvegarde (complète, incrémentale, différentielle). L'architecture de Bacula repose sur 3 composants essentiels : le Director est le chef d'orchestre (c'est lui qui coordonne de manière centralisée le déroulement des sauvegardes), le File Daemon est l'agent déployé sur chacun des clients chargé de réaliser la sauvegarde sous le contrôle du director, et le Storage Daemon assure le rôle d'interface avec les supports de stockage. Bacula implémente également les fonctionnalités avancées utilisées par toutes les solutions de sauvegarde performantes tel que le multi-streaming, le multi-plexing, la sauvegarde utilisateur, la gestion des Pools de sauvegarde, etc.

Bacula est développé en C/C++. Il s'appuie sur une base de données PostgreSQL ou MySQL.


Autres
------

- Amanda: http://www.amanda.org/
- BackupPC: http://backuppc.sourceforge.net/
- Borg + Borgmatic: https://www.borgbackup.org/ + https://torsion.org/borgmatic/
- Restic: https://restic.net/
- Rclone: https://rclone.org/
- Bareos: https://www.bareos.org/en/
