# Déploiement

Les outils de déploiement permettent de préparer à distance des environnements selon des règles prédéfinies ou selon un état final attendu. Ils facilitent l’administration d’un parc de serveurs et rendent ses changements reproductibles.

Ces outils peuvent être classés en plusieurs sous-catégories:

- **Outils de gestion de configuration** : Ces outils aident à automatiser le processus de configuration des systèmes et des applications dans une infrastructure informatique. Ils permettent aux administrateurs de définir l'état désiré pour les systèmes et les applications, puis travaillent pour amener les systèmes à cet état. Ces outils sont particulièrement utiles dans les environnements avec de nombreux systèmes, où la configuration manuelle de chaque système serait une tâche difficile et sujette à erreurs. Nous présentons plus spécialement:

  > - Ansible
  > - Puppet
  > - Chef
  > - Salt
  > - Rudder

- **Outils de provisionnement d'infrastructure** : ils créent et détruisent les ressources (machines, réseaux, services managés) que les outils précédents configurent ensuite. Nous présentons OpenTofu.

Le clonage de disques et l'installation de postes sont traités à la page [Déploiement de postes](../infrastructure/deploiement-postes.md), l'inventaire à la page [Gestion de parc et inventaires](../infrastructure/gestion-de-parc-et-inventaires.md).

## Cadre conceptuel

Plusieurs des outils cités se fondent sur la théorie des promesses (*Promise Theory*), un cadre conceptuel développé par Mark Burgess, le créateur de CFEngine, pour aider à comprendre et à modéliser des systèmes distribués complexes.

Dans le cadre de la théorie des promesses, un système est compris comme un ensemble d'agents indépendants. Chaque agent peut faire des promesses concernant son propre comportement. Par exemple, dans un système informatique, un agent pourrait être un serveur qui promet de répondre à certaines requêtes, ou un logiciel qui promet de produire certains résultats lorsqu'il reçoit certaines entrées.

Voici quelques principes clés de la théorie des promesses :

- **Autonomie des agents** : Chaque agent est autonome et a le contrôle total sur les promesses qu'il fait. Aucun agent ne peut forcer un autre agent à faire une promesse.
- **Promesses volontaires** : Les agents promettent volontairement. Un agent ne peut pas être contraint de faire une promesse qu'il ne veut pas faire.
- **Promesses comme interface** : Les promesses servent d'interface entre les agents. Elles définissent ce qu'un agent est prêt à faire, mais ne spécifient pas comment l'agent doit accomplir ce qu'il promet.
- **Promesses et observation** : La vérification du respect d'une promesse se fait par l'observation. Si un agent promet de faire quelque chose, les autres agents vérifient cette promesse en observant le comportement de l'agent.

La théorie des promesses offre une manière décentralisée et ascendante de comprendre les systèmes, qui contraste avec les approches descendantes et centralisées. Dans ces dernières, un agent (ou un petit nombre d'agents) tente d'imposer un comportement à l'ensemble du système. En revanche, dans la théorie des promesses, le comportement global du système émerge des interactions entre de nombreux agents indépendants, chacun faisant ses propres promesses.

## Ansible

Site
: <https://www.ansible.com/>

Porteur
: un éditeur (Red Hat)

Licence
: GPL v3 (ansible-core)

Ansible est une plate-forme logicielle open source qui offre des outils pour automatiser la gestion des systèmes et des réseaux. C'est un outil d'automatisation informatique qui permet de gérer à la fois le déploiement de logiciels, l'exécution de tâches ad-hoc (tâches qui ne sont pas nécessairement planifiées ou régulières) et la gestion de la configuration des systèmes.

L'une des principales caractéristiques d'Ansible est sa simplicité d'utilisation. Il utilise le protocole SSH pour se connecter aux différents nœuds ou serveurs, ce qui signifie qu'il n'est pas nécessaire d'installer de logiciel supplémentaire sur les serveurs que vous souhaitez gérer. Cela réduit la complexité et les coûts associés à l'administration des systèmes.

Les « playbooks » sont au cœur d'Ansible. Un playbook est un fichier écrit en YAML (un langage de sérialisation de données lisible par l'homme) qui décrit une série d'étapes à suivre pour accomplir une tâche. Les playbooks peuvent être réutilisés et partagés, ce qui permet une automatisation cohérente et reproductible. Par exemple, vous pouvez avoir un playbook pour configurer un serveur web, un autre pour déployer une application spécifique, etc.

Ansible est écrit en Python, ce qui permet d'étendre ses fonctionnalités en écrivant ses propres modules.

Depuis 2020, le projet est scindé en deux : le moteur `ansible-core` (GPL v3) et les **collections**, qui regroupent modules et rôles par domaine et sont distribuées séparément via Ansible Galaxy. L'offre commerciale de Red Hat s'appelle Ansible Automation Platform. C'est aujourd'hui l'outil de gestion de configuration le plus utilisé, en grande partie grâce à son absence d'agent.

## Puppet

Site
: <https://www.puppet.com/>

Porteur
: un éditeur (Puppet by Perforce)

Licence
: Apache 2.0

Puppet est une plateforme de gestion de configuration qui vous permet d'automatiser l'administration des infrastructures informatiques. Il est particulièrement utile pour gérer des environnements à grande échelle et hétérogènes, où le maintien d'une configuration cohérente à travers de nombreux systèmes peut être un défi.

La particularité de Puppet réside dans son approche de la gestion de configuration fondée sur l'état désiré. Au lieu de scripter une séquence précise d'actions à effectuer sur un système, comme on le ferait avec des outils d'administration traditionnels, avec Puppet, vous définissez l'état final que vous souhaitez pour votre système. Cet état pourrait inclure des aspects tels que les permissions de fichiers, les logiciels à installer, les configurations à appliquer, etc. Puppet se charge ensuite de faire le nécessaire pour que le système atteigne cet état, quel que soit son état de départ.

Cela offre plusieurs avantages. Tout d'abord, cela rend les configurations plus compréhensibles et maintenables : vous décrivez le résultat voulu. Deuxièmement, cela rend l'automatisation plus robuste, car Puppet peut corriger les déviations de l'état désiré qui pourraient survenir au fil du temps.

Puppet est écrit en Ruby, un langage de programmation couramment utilisé pour les applications web et autres outils d'administration. Cela signifie que vous pouvez étendre Puppet avec vos propres modules et intégrations, si vous le souhaitez.

**Point de vigilance important.** Perforce, qui a racheté Puppet en 2022, a annoncé en 2024 le transfert du développement vers des dépôts internes et l'arrêt de la publication d'une version open source entretenue. La communauté a répondu en créant **OpenVox** (<https://openvox.org/>), fork maintenu par le collectif Vox Pupuli, dont les versions sont fonctionnellement équivalentes à celles de Puppet et publiées depuis janvier 2025. Les organisations qui déploient Puppet aujourd'hui doivent donc arbitrer entre l'offre commerciale de Perforce et la filière communautaire OpenVox, laquelle constitue, pour un usage libre, le choix le plus sûr.

## Rudder

Site
: <https://www.rudder.io/>

Porteur
: un éditeur (Normation)

Licence
: GPL v3

Rudder est un outil d'automatisation et de gestion de configuration de serveurs open source. Conçu pour être facile à utiliser, il offre une interface web qui facilite la gestion de votre infrastructure informatique.

Rudder fonctionne sur la base d'un modèle dirigé par les rôles, ce qui signifie que vous pouvez définir des configurations fondées sur le rôle d'un serveur dans votre infrastructure. Par exemple, vous pouvez avoir des rôles pour les serveurs web, les bases de données, les serveurs d'application, etc.. Chaque rôle peut avoir une configuration spécifique qui lui est associée.

Rudder nécessite l'installation d'un agent léger sur chaque machine que vous souhaitez gérer. Cet agent communique avec le serveur Rudder pour recevoir les configurations à appliquer. L'utilisation d'agents locaux permet à Rudder de gérer efficacement la configuration même lorsque la connectivité réseau est interrompue ou limitée.

Rudder est développé par la société française Normation, qui offre également un support professionnel pour le logiciel. Cela signifie que vous pouvez obtenir de l'aide pour résoudre les problèmes ou développer de nouvelles fonctionnalités si nécessaire.

En termes de technologie, Rudder est développé en Scala pour la partie serveur, un langage de programmation moderne qui combine la programmation orientée objet et fonctionnelle. L'agent de configuration, qui est installé sur les machines gérées, est écrit en C, un langage de programmation largement utilisé pour les systèmes à bas niveau.

## Chef

Site
: <https://www.chef.io/>

Porteur
: un éditeur (Progress Software)

Licence
: Apache 2.0 pour le code source, licence commerciale pour les binaires distribués par l'éditeur

Chef est un outil d'automatisation et de gestion de configuration qui permet aux développeurs et aux administrateurs système de gérer et de contrôler leurs infrastructures informatiques.

Chef adopte une approche fondée sur le code pour la gestion de configuration, ce qui signifie que les configurations des serveurs et des systèmes sont définies en code (appelé recettes dans Chef). Ces recettes sont écrites en Ruby, un langage orienté objet à la syntaxe concise et lisible. Ces recettes décrivent les ressources nécessaires et l'état désiré pour chaque ressource.

L'une des principales caractéristiques de Chef est son modèle fondé sur le client-serveur. Le serveur Chef (ou Chef Server) est le point central de communication et de stockage des configurations. Les clients Chef, qui sont installés sur chaque nœud que vous souhaitez gérer, communiquent avec le serveur pour obtenir leurs configurations. Ensuite, ils appliquent ces configurations localement, permettant ainsi de garantir que les systèmes sont dans l'état désiré.

Chef permet également l'intégration avec les principales plateformes cloud, comme AWS, Google Cloud Platform et Microsoft Azure, rendant la gestion des ressources dans ces environnements aussi simple que la gestion des ressources sur site.

Chef possède une communauté d'utilisateurs et de contributeurs qui ont créé un grand nombre de recettes prêtes à l'emploi pour diverses tâches de configuration.

Deux points sont à connaître avant de s'engager. La société Chef Software a été rachetée en 2020 par Progress Software. Par ailleurs, si le code reste sous licence Apache 2.0, les binaires officiels sont soumis depuis 2019 à une licence commerciale au-delà d'un certain périmètre d'usage. Le projet **Cinc** (<https://cinc.sh/>) fournit des binaires reconstruits à partir des sources libres, sans cette restriction.

## Salt

Site
: <https://saltproject.io/>

Porteur
: un éditeur (Broadcom, via VMware Tanzu) et une communauté

Licence
: Apache 2.0

Salt, aussi appelé SaltStack, est un outil d'automatisation et de gestion de configuration qui vise à rendre la gestion des infrastructures informatiques aussi efficace et automatisée que possible.

Salt adopte une approche fondée sur le modèle "maître-minion" (ou "maître-agent"). Le maître Salt, c'est-à-dire le serveur central, envoie des commandes aux minions, les noeuds gérés. Ces minions peuvent être des serveurs, des conteneurs ou tout autre type de dispositif dans une infrastructure informatique. L'agent Salt (le minion) est installé sur chaque nœud et communique avec le serveur maître pour recevoir ses instructions.

Une des particularités de Salt est sa rapidité et son efficacité, grâce à son architecture fondée sur le modèle de communication asynchrone ZeroMQ. Cela permet à Salt d'envoyer des commandes à des milliers de systèmes en un rien de temps.

Salt utilise le langage de données YAML pour la création de ses configurations, appelées "states". Les states décrivent l'état désiré pour un système et peuvent spécifier des choses comme les packages à installer, les services à exécuter, les fichiers à écrire, etc.

Salt est écrit en Python, un langage de programmation populaire pour son accessibilité et sa facilité d'utilisation. Cela signifie qu'il est relativement facile d'écrire de nouvelles fonctionnalités pour Salt si vous avez des besoins spécifiques non couverts par les fonctionnalités de base.

En outre, Salt est capable de gérer des environnements hétérogènes, ce qui le rend très souple pour les organisations qui utilisent une variété de systèmes d'exploitation et de plateformes. Le projet, racheté avec SaltStack par VMware en 2020, relève depuis 2023 de Broadcom ; il conserve une gouvernance communautaire (*Salt Project*) et une licence Apache 2.0.

## OpenTofu

Site
: <https://opentofu.org/>

Porteur
: une fondation (Linux Foundation, CNCF)

Licence
: MPL 2.0

OpenTofu est un outil d'infrastructure décrite par le code, issu du fork de Terraform que la communauté a lancé après le passage de ce dernier sous licence BUSL, en août 2023. Hébergé par la Linux Foundation, il a été accepté en avril 2025 au niveau *sandbox* de la CNCF.

On décrit dans des fichiers HCL les ressources souhaitées : machines, réseaux, enregistrements DNS, bases managées. OpenTofu compare cette description à l'état connu, présente un plan, puis l'applique à travers des fournisseurs (*providers*) qui couvrent les principaux clouds, OpenStack, Proxmox VE ou Kubernetes. Il complète les outils de gestion de configuration, qui interviennent une fois la machine créée.

Il reprend les configurations de Terraform antérieures à la séparation, mais les deux produits évoluent désormais différemment : le chiffrement du fichier d'état, par exemple, est une fonction d'OpenTofu. Ce fichier d'état, qui peut contenir des secrets, doit être partagé, verrouillé et protégé dès qu'une équipe est concernée.

OpenTofu est écrit en Go. Le même changement de licence a donné naissance à [OpenBao](../infrastructure/secrets-mots-de-passe.md#openbao), fork de Vault.

## Autres outils

Gestion de configuration :

- **CFEngine** : C'est l'un des premiers outils de gestion de configuration. Il est connu pour sa vitesse et sa capacité à gérer des milliers de nœuds.
- **Juju** : C'est un outil développé par Canonical (la société derrière Ubuntu) qui se concentre sur le déploiement et la gestion des services au-dessus du niveau du système d'exploitation.
- **pyinfra** : Il s'agit d'un outil de déploiement de serveurs et d'outil de gestion de configuration écrit en Python. Il fonctionne en générant et en exécutant des commandes SSH sur les serveurs cibles. pyinfra est conçu pour être rapide (temps de déploiement minimal) et pour fonctionner avec toute configuration de serveur, que vous ayez un seul serveur ou des milliers. Il offre également une API Python, ce qui signifie que vous pouvez intégrer pyinfra dans d'autres scripts ou outils Python.
- **BundleWrap** : Est également un outil de gestion de configuration fondé sur Python. Comme pyinfra, il utilise SSH pour communiquer avec les serveurs cibles. BundleWrap se distingue par son approche de la gestion de configuration : chaque nœud a un bundle qui décrit l'état désiré pour ce nœud. BundleWrap travaille pour amener le nœud à cet état. Il est conçu pour être simple à comprendre et à utiliser, avec un système de fichiers en texte brut et un ensemble minimal de concepts à apprendre.

Déploiement applicatif et conteneurs :

- **Docker**, **Podman** et **Kubernetes** constituent aujourd'hui le socle dominant du déploiement applicatif ; ils sont présentés dans la section [Conteneurs et orchestration](../infrastructure/conteneurs-orchestration.md).
- **Argo CD** (<https://argo-cd.readthedocs.io/>) et **Flux** (<https://fluxcd.io/>) mettent en œuvre l'approche GitOps, où l'état souhaité du système est décrit dans un dépôt Git et appliqué en continu par un agent : transposition directe, à l'échelle des conteneurs, de la logique d'état désiré décrite plus haut.
- **Helm** (<https://helm.sh/>) pour l'empaquetage des applications Kubernetes.

Présentés ailleurs :

- [OCS Inventory NG](../infrastructure/gestion-de-parc-et-inventaires.md#ocs-inventory-ng){ #ocs-inventory-ng }, inventaire de parc
- [Clonezilla](../infrastructure/deploiement-postes.md#clonezilla){ #clonezilla } et [Partimage](../infrastructure/deploiement-postes.md#partimage){ #partimage }, clonage de disques
