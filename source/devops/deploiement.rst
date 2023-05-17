Déploiement
===========

Les outils de déploiement permettent de préparer à distance des environnements selon des réglés prédéfinies ou selon un état final attendu. Toutes les grandes entreprises utilisent des logiciels de déploiement pour faciliter l’administration de leur parc.

Ces outils peuvent être classés en plusieurs sous-catégories

- **Outils de gestion de configuration** : Ces outils aident à automatiser le processus de configuration des systèmes et des applications dans une infrastructure informatique. Ils permettent aux administrateurs de définir l'état désiré pour les systèmes et les applications, puis travaillent pour amener les systèmes à cet état. Ces outils sont particulièrement utiles dans les environnements avec de nombreux systèmes, où la configuration manuelle de chaque système serait une tâche difficile et sujette à erreurs. Nous présentons plus spécialement:

	- Ansible
	- Puppet
	- Chef
	- Salt
	- Rudder

- **Outils de sauvegarde et de clonage de disques** : Ces outils permettent de créer une copie exacte d'un disque ou d'une partition, qui peut ensuite être utilisée pour restaurer le disque ou la partition à un état précédent. Ils sont généralement utilisés pour la sauvegarde des données, la restauration du système après un incident, ou le déploiement de systèmes. Nous présentons:

	- Clonezilla
	- Partimage


- **Outils d'inventaire et de suivi des actifs** : Ces outils aident à suivre et à gérer les actifs informatiques dans une organisation. Nous présentons:

	- OCS Inventory NG


Ansible
-------

:Site: https://ansible.com/
:Porteur: un éditeur (Red Hat)
:Licence: GPL v3

Ansible est une plate-forme logicielle open source qui offre des outils pour automatiser la gestion des systèmes et des réseaux. C'est un outil d'automatisation informatique qui permet de gérer à la fois le déploiement de logiciels, l'exécution de tâches ad-hoc (tâches qui ne sont pas nécessairement planifiées ou régulières), et la gestion de la configuration des systèmes.

L'une des principales caractéristiques d'Ansible est sa simplicité d'utilisation. Il utilise le protocole SSH pour se connecter aux différents nœuds ou serveurs, ce qui signifie qu'il n'est pas nécessaire d'installer de logiciel supplémentaire sur les serveurs que vous souhaitez gérer. Cela réduit la complexité et les coûts associés à l'administration des systèmes.

Les "playbooks" sont au cœur de la façon dont Ansible fonctionne. Un playbook est un fichier écrit en YAML (un langage de sérialisation de données lisible par l'homme) qui décrit une série d'étapes à suivre pour accomplir une tâche. Les playbooks peuvent être réutilisés et partagés, ce qui permet une automatisation cohérente et reproductible. Par exemple, vous pouvez avoir un playbook pour configurer un serveur web, un autre pour déployer une application spécifique, etc.

Ansible est écrit en Python, ce qui signifie que vous pouvez étendre ses fonctionnalités en écrivant vos propres modules si vous le souhaitez. Python est un langage de programmation populaire et largement utilisé, ce qui signifie qu'il y a une grande communauté de développeurs qui peuvent aider à résoudre les problèmes ou à développer de nouvelles fonctionnalités.


Puppet
------

:Site: https://puppetlabs.com/
:Porteur: un éditeur (Puppet Labs)
:Licence: Apache

Puppet est une plateforme de gestion de configuration qui vous permet d'automatiser l'administration des infrastructures informatiques. Il est particulièrement utile pour gérer des environnements à grande échelle et hétérogènes, où le maintien d'une configuration cohérente à travers de nombreux systèmes peut être un défi.

La particularité de Puppet réside dans son approche de la gestion de configuration basée sur l'état désiré. Au lieu de scripter une séquence précise d'actions à effectuer sur un système, comme on le ferait avec des outils d'administration traditionnels, avec Puppet, vous définissez l'état final que vous souhaitez pour votre système. Cet état pourrait inclure des aspects tels que les permissions de fichiers, les logiciels à installer, les configurations à appliquer, etc. Puppet se charge ensuite de faire le nécessaire pour que le système atteigne cet état, quel que soit son état de départ.

Cela offre plusieurs avantages. Tout d'abord, cela rend les configurations plus compréhensibles et maintenables, car vous décrivez ce que vous voulez, et non comment l'obtenir. Deuxièmement, cela rend l'automatisation plus robuste, car Puppet peut corriger les déviations de l'état désiré qui pourraient survenir au fil du temps.

Puppet est écrit en Ruby, un langage de programmation couramment utilisé pour les applications web et autres outils d'administration. Cela signifie que vous pouvez étendre Puppet avec vos propres modules et intégrations, si vous le souhaitez.

Enfin, Puppet bénéficie d'une communauté d'utilisateurs actifs et passionnés, qui contribuent régulièrement à son développement et à son amélioration. Puppet Labs, l'entreprise qui développe Puppet, offre également un support professionnel, ce qui peut être un atout pour les organisations qui ont besoin d'un niveau supplémentaire de support pour leur infrastructure.


Rudder
------

:Site: https://rudder.io/
:Porteur: un éditeur français (Normation)
:Licence: GPL v3

Rudder est un outil d'automatisation et de gestion de configuration de serveurs open source. Conçu pour être facile à utiliser, il offre une interface web qui facilite la gestion de votre infrastructure informatique.

Rudder fonctionne sur la base d'un modèle dirigé par les rôles, ce qui signifie que vous pouvez définir des configurations basées sur le rôle d'un serveur dans votre infrastructure. Par exemple, vous pouvez avoir des rôles pour les serveurs web, les bases de données, les serveurs d'application, etc., et chaque rôle peut avoir une configuration spécifique qui lui est associée.

Rudder nécessite l'installation d'un agent léger sur chaque machine que vous souhaitez gérer. Cet agent communique avec le serveur Rudder pour recevoir les configurations à appliquer. L'utilisation d'agents locaux permet à Rudder de gérer efficacement la configuration même lorsque la connectivité réseau est interrompue ou limitée.

Rudder est développé par la société française Normation, qui offre également un support professionnel pour le logiciel. Cela signifie que vous pouvez obtenir de l'aide pour résoudre les problèmes ou développer de nouvelles fonctionnalités si nécessaire.

En termes de technologie, Rudder est développé en Scala pour la partie serveur, un langage de programmation moderne qui combine la programmation orientée objet et fonctionnelle. L'agent de configuration, qui est installé sur les machines gérées, est écrit en C, un langage de programmation largement utilisé pour les systèmes à bas niveau.


Chef
----

:Site: https://www.opscode.com/chef/


Chef est un outil d'automatisation et de gestion de configuration puissant qui permet aux développeurs et aux administrateurs système de gérer et de contrôler leurs infrastructures informatiques.

Chef adopte une approche basée sur le code pour la gestion de configuration, ce qui signifie que les configurations des serveurs et des systèmes sont définies en code (appelé recettes dans Chef). Ces recettes sont écrites en Ruby, un langage de programmation orienté objet qui est à la fois puissant et facile à lire. Ces recettes décrivent les ressources nécessaires et l'état désiré pour chaque ressource.

L'une des principales caractéristiques de Chef est son modèle basé sur le client-serveur. Le serveur Chef (ou Chef Server) est le point central de communication et de stockage des configurations. Les clients Chef, qui sont installés sur chaque nœud que vous souhaitez gérer, communiquent avec le serveur pour obtenir leurs configurations. Ensuite, ils appliquent ces configurations localement, permettant ainsi de garantir que les systèmes sont dans l'état désiré.

Chef permet également l'intégration avec les principales plateformes cloud, comme AWS, Google Cloud Platform et Microsoft Azure, rendant la gestion des ressources dans ces environnements aussi simple que la gestion des ressources sur site.

Chef possède une forte communauté d'utilisateurs et de contributeurs qui ont créé un grand nombre de recettes prêtes à l'emploi pour diverses tâches de configuration. Cela signifie que vous pouvez souvent trouver une recette existante qui fait ce que vous voulez, ce qui peut considérablement accélérer le processus de mise en place et de configuration de votre infrastructure.

Salt
----

:Site: https://saltstack.com/

Salt, aussi appelé SaltStack, est un outil d'automatisation et de gestion de configuration qui vise à rendre la gestion des infrastructures informatiques aussi efficace et automatisée que possible.

Salt adopte une approche basée sur le modèle "maître-minion" (ou "maître-agent"). Le maître Salt, c'est-à-dire le serveur central, envoie des commandes aux minions, les noeuds gérés. Ces minions peuvent être des serveurs, des conteneurs ou tout autre type de dispositif dans une infrastructure informatique. L'agent Salt (le minion) est installé sur chaque nœud et communique avec le serveur maître pour recevoir ses instructions.

Une des particularités de Salt est sa rapidité et son efficacité, grâce à son architecture basée sur le modèle de communication asynchrone ZeroMQ. Cela permet à Salt d'envoyer des commandes à des milliers de systèmes en un rien de temps.

Salt utilise le langage de données YAML pour la création de ses configurations, appelées "states". Les states décrivent l'état désiré pour un système et peuvent spécifier des choses comme les packages à installer, les services à exécuter, les fichiers à écrire, etc.

Salt est écrit en Python, un langage de programmation populaire pour son accessibilité et sa facilité d'utilisation. Cela signifie qu'il est relativement facile d'écrire de nouvelles fonctionnalités pour Salt si vous avez des besoins spécifiques non couverts par les fonctionnalités de base.

En outre, Salt est capable de gérer des environnements mixtes, ce qui le rend très flexible pour les organisations qui utilisent une variété de systèmes d'exploitation et de plateformes.


OCS Inventory NG
----------------

:Site: http://www.ocsinventory-ng.org/

OCS Inventory NG (Open Computers and Software Inventory Next Generation) est un outil d'inventaire informatique open source qui aide à faire un suivi et à gérer les actifs informatiques au sein d'une organisation.

L'outil fonctionne en installant un agent sur chaque poste de travail ou serveur, qui collecte des informations sur le matériel et les logiciels installés, puis envoie ces informations à un serveur central OCS. Les données collectées peuvent inclure des informations telles que la configuration matérielle, le système d'exploitation, les logiciels installés, les logiciels en cours d'exécution, les mises à jour de logiciels, les adresses IP et bien d'autres.

OCS Inventory NG est très utile pour les grandes organisations avec de nombreux postes de travail et serveurs, où le suivi manuel des actifs informatiques serait une tâche énorme. Il permet aux administrateurs système de voir rapidement et facilement quels actifs ils ont, où ils se trouvent, et comment ils sont configurés.

Un autre avantage d'OCS Inventory NG est sa capacité à intégrer avec d'autres outils de gestion informatique, comme GLPI (Gestion Libre de Parc Informatique). Cette intégration peut permettre des fonctionnalités supplémentaires, comme le suivi des incidents, la gestion des demandes de service, la planification des changements, et bien d'autres.

OCS Inventory NG est écrit en Perl pour la partie agent, et utilise PHP pour l'interface web du serveur. Il est compatible avec de nombreux systèmes d'exploitation, y compris Linux, Windows et MacOS.

CloneZilla
----------

:Site: http://clonezilla.org

Clonezilla est un outil de clonage et d'imagerie de disque open source qui permet de copier, cloner et restaurer des systèmes d'exploitation et des données sur des disques durs. Il est souvent utilisé pour la sauvegarde, la restauration et le déploiement de systèmes dans des environnements informatiques.

Clonezilla est capable de cloner un disque ou une partition individuelle à un autre disque ou partition, ou de créer une image d'un disque ou d'une partition qui peut être stockée pour une utilisation ultérieure. Cette image peut ensuite être utilisée pour restaurer le système sur le même disque ou sur un autre disque, ce qui peut être utile pour la récupération de données ou le déploiement de systèmes.

Clonezilla supporte une variété de systèmes de fichiers, y compris ceux couramment utilisés dans les environnements Windows (NTFS, FAT), Linux (ext2, ext3, ext4, xfs, btrfs) et MacOS (HFS+). Il peut également cloner des disques avec des partitions de démarrage UEFI, ce qui est de plus en plus courant dans les systèmes modernes.

L'un des principaux avantages de Clonezilla est son efficacité. Il n'effectue la copie que des blocs de données utilisés sur le disque, ce qui permet de gagner du temps et de l'espace de stockage lors du clonage ou de la création d'images de disques qui ne sont pas entièrement utilisés.

Clonezilla est généralement utilisé via une interface en ligne de commande, mais il existe aussi une version avec une interface graphique appelée Clonezilla Live. Clonezilla Live est un système d'exploitation autonome qui peut être démarré à partir d'un CD, d'une clé USB ou d'un réseau PXE, et qui peut être utilisé pour cloner ou restaurer des disques sans avoir besoin d'un système d'exploitation existant sur la machine.


Partimage
---------

:Site: http://www.partimage.org


Partimage, qui signifie Partition Image, est un outil open-source de sauvegarde de disque et de partition. Il est spécifiquement conçu pour sauvegarder des partitions de disque en créant une image de la partition, ce qui peut ensuite être utilisé pour restaurer la partition à un état précédent.

Partimage fonctionne en lisant une partition de disque bloc par bloc et en écrivant ces blocs dans un fichier image. Cette image peut ensuite être stockée sur un autre disque ou sur un serveur de réseau pour une utilisation future. Lorsque vous avez besoin de restaurer la partition, vous pouvez utiliser Partimage pour lire l'image et écrire les blocs de données sur la partition cible.

L'un des avantages de Partimage est qu'il ne copie que les blocs de données utilisés sur la partition, ce qui signifie que les fichiers supprimés ou l'espace non utilisé sur la partition ne sont pas inclus dans l'image. Cela rend les images de sauvegarde plus petites et plus rapides à créer et à restaurer que si vous copiez simplement tous les blocs de la partition.

Partimage supporte une variété de systèmes de fichiers, y compris ceux couramment utilisés dans les environnements Linux (comme ext2, ext3, ext4, ReiserFS, XFS) et Windows (FAT16, FAT32, NTFS). Cependant, il est à noter que le support de certains systèmes de fichiers peut être limité, et pour les systèmes de fichiers non pris en charge, Partimage peut seulement effectuer une copie de l'ensemble du disque.

Partimage est généralement utilisé via une interface en ligne de commande, bien qu'il existe une interface graphique disponible appelée Partimage Is Not Ghost (PING), qui offre une interface utilisateur plus conviviale.


Autres outils
-------------

Gestion de configuration :

- **CFEngine** : C'est l'un des premiers outils de gestion de configuration. Il est connu pour sa vitesse et sa capacité à gérer des milliers de noeuds.
- **Terraform** : C'est un outil de gestion de configuration qui se concentre sur l'infrastructure en tant que code (IaC). Il est largement utilisé pour la gestion de l'infrastructure dans le cloud.
- **Juju** : C'est un outil développé par Canonical (la société derrière Ubuntu) qui se concentre sur le déploiement et la gestion des services au-dessus du niveau du système d'exploitation.

Clonage de disques :

- **dd** : C'est un outil de ligne de commande Unix qui peut être utilisé pour copier et convertir des données à un niveau très bas. Il est souvent utilisé pour cloner des disques entiers.
- **rsync** : C'est un outil de synchronisation de fichiers extrêmement puissant et flexible. Bien qu'il ne clone pas les disques à proprement parler, il est souvent utilisé pour la sauvegarde de données.

Inventaire et suivi des actifs :

- **GLPI** : C'est un système d'information de gestion des ressources informatiques (ITSM) qui gère non seulement l'inventaire des actifs informatiques, mais aussi de nombreuses autres fonctions de gestion informatique.
- **FusionInventory** : C'est un outil d'inventaire qui peut être utilisé seul ou en tandem avec GLPI pour fournir une solution d'inventaire et de gestion des actifs plus complète.
- **RackTables** : C'est une solution de gestion de centre de données et de réseau qui aide à gérer le matériel, les emplacements, les adresses IP, les câbles et d'autres actifs.

