Déploiement et sauvegarde
=========================

Les outils de sauvegarde, tel que Bacula, permettent l’enregistrement sur différents supports des données importantes pour l’entreprise, ceci à partir de règles évoluées.

Parmi les fonctionnalités que l’on retrouve dans les outils de sauvegarde, on peut citer : la planification des sauvegardes de manière très précise (agenda par exemple), la définition du type de sauvegarde (complète, incrémentale, différentielle), le lieu de stockage, etc. Certains outils vont jusqu’à proposer du multi-streaming, du multi-plexing, de la sauvegarde utilisateur, de la gestion des Pools de sauvegarde, etc.

Les outils de déploiement, tel que Puppet, permettent de préparer à distance des environnements selon des réglés prédéfinies ou selon un état final attendu. Toutes les grandes entreprises utilisent des logiciels de déploiement pour faciliter l’administration de leur parc.


Bacula
------

:Version: 5.0.3
:Site: www.bacula.org/fr
:Porteur: un éditeur (Bacula Systems)
:Licence: GPL

Bacula est un système de sauvegarde et de restauration très flexible développé en 2000 par Kern Sibbald et maintenant soutenu par la société Bacula Systems.

Bacula permet la planification des sauvegardes de manière très précise aussi bien en termes d'agenda que de type de sauvegarde (complète, incrémentale, différentielle). L'architecture de Bacula repose sur 3 composants essentiels : le Director est le chef d'orchestre (c'est lui qui coordonne de manière centralisée le déroulement des sauvegardes), le File Daemon est l'agent déployé sur chacun des clients chargé de réaliser la sauvegarde sous le contrôle du director, et le Storage Daemon assure le rôle d'interface avec les supports de stockage. Bacula implémente également les fonctionnalités avancées utilisées par toutes les solutions de sauvegarde performantes tel que le multi-streaming, le multi-plexing, la sauvegarde utilisateur, la gestion des Pools de sauvegarde, etc.

Bacula est développé en C/C++. Il s'appuie sur une base de données PostgreSQL ou MySQL.


Puppet
------

:Version: 2.6
:Site: http://puppetlabs.com
:Porteur: un éditeur (Puppet Labs)
:Licence: Apache

Puppet est un outil d'automatisation d'infrastructure.

Au lieu de décrire une suite d'actions à réaliser, comme avec les outils d'administration classiques, l'administrateur saisit l'état qu'il souhaite obtenir (permissions souhaitées, fichiers et logiciels à installer, configurations à appliquer), et puppet se charge automatiquement d'amener le système dans l'état spécifié quelque soit son état de départ. Puppet permet ainsi d'administrer un grand parc hétérogène de façon centralisée.

Puppet bénéficie d'une communauté d'utilisateurs enthousiastes et dynamique, et d'un support professionnel par son éditeur Puppet Labs.

Puppet est réalisé en Ruby.


Autres
------

Parmi les produits de l’univers Déploiement et Sauvegarde, on peut compléter la liste avec les outils ci-dessous :


- Chef: http://www.opscode.com/chef/

- Salt: http://saltstack.com/

- Ansible: http://ansible.cc/

- Kdump	http://lse.sourceforge.net/kdump

- mkCDrec	http://mkcdrec.sourceforge.net

- SIS	http://sourceforge.net/projects/sisuite

- CloneZilla	http://clonezilla.org

- Partimage	http://www.partimage.org

- OCS Inventory NG	http://www.ocsinventory-ng.org

- Amanda	http://www.amanda.org/

- BackupPC	http://backuppc.sourceforge.net/

