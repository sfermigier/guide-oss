Déploiement et sauvegarde
=========================

Les outils de déploiement, tel que Andible ou Puppet, permettent de préparer à distance des environnements selon des réglés prédéfinies ou selon un état final attendu. Toutes les grandes entreprises utilisent des logiciels de déploiement pour faciliter l’administration de leur parc.


Ansible
-------

:Site: https://ansible.com/
:Porteur: un éditeur (Red Hat)
:Licence: GPL v3

Ansible est une plate-forme logicielle libre pour la configuration et la gestion des ordinateurs. Elle combine le déploiement de logiciels (en) multi-nœuds, l'exécution des tâches ad-hoc, et la gestion de configuration. Elle se connecte aux différents nœuds à l'aide du protocole SSH et ne nécessite l'installation d'aucun logiciel supplémentaire sur ceux-ci.

Le système utilise YAML pour exprimer des descriptions réutilisables de systèmes, appelées playbook.

Ansible est écrit en Python.


Puppet
------

:Site: https://puppetlabs.com/
:Porteur: un éditeur (Puppet Labs)
:Licence: Apache

Puppet est un outil d'automatisation d'infrastructure.

Au lieu de décrire une suite d'actions à réaliser, comme avec les outils d'administration classiques, l'administrateur saisit l'état qu'il souhaite obtenir (permissions souhaitées, fichiers et logiciels à installer, configurations à appliquer), et puppet se charge automatiquement d'amener le système dans l'état spécifié quelque soit son état de départ. Puppet permet ainsi d'administrer un grand parc hétérogène de façon centralisée.

Puppet bénéficie d'une communauté d'utilisateurs enthousiastes et dynamique, et d'un support professionnel par son éditeur Puppet Labs.

Puppet est réalisé en Ruby.


Rudder
------

:Site: https://rudder.io/
:Porteur: un éditeur français (Normation)
:Licence: GPL v3

Rudder est un logiciel libre de configuration automatique de serveurs (ou gestion de parc informatique). Il se veut simple d'utilisation, orienté web et applique un raisonnement dirigé par les rôles. Il s'appuie sur des agents légers installés localement sur chaque machine gérée.

Rudder est développé par un éditeur français, Normation.

Rudder est développé en Scala côté serveur, et son agent de configuration en C.


Autres
------

- Chef: http://www.opscode.com/chef/
- Salt: http://saltstack.com/
- OCS Inventory NG: http://www.ocsinventory-ng.org/
- CloneZilla: http://clonezilla.org
- Partimage: http://www.partimage.org
