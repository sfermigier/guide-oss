Développement et couches intermédiaires
=======================================

Cette dimension réunit les fondations, invisibles depuis l'écran de l'utilisateur : les outils avec lesquels on fabrique le logiciel, les moteurs qui conservent les données et les couches qui font dialoguer les applications entre elles.

C'est le domaine où l'open source ne s'est pas contenté de s'imposer : il a gagné si complètement qu'il faut aujourd'hui chercher pour trouver une alternative propriétaire crédible. Aucune organisation ne développe plus de logiciel sans Git, sans une forge, sans une chaîne d'intégration continue, sans un framework applicatif libre et sans quelques dizaines de milliers de lignes de dépendances publiques. Le débat n'est plus « faut-il adopter l'open source ? » mais « comment gérer ce dont nous dépendons déjà ? ».

Ce basculement déplace les questions à se poser.

La première est celle des **licences**. La quasi-totalité des changements de licence de ces cinq dernières années se sont produits dans cette dimension. Redis, MongoDB, Elasticsearch, Terraform, ArangoDB, HashiCorp Vault, Puppet et Camunda ont quitté, définitivement ou temporairement, le camp des licences reconnues par l'*Open Source Initiative*. Ils ont adopté des licences dites « source-available », qui autorisent la lecture du code tout en restreignant son usage. Chaque fois ou presque, la communauté a répondu par un fork : Valkey, OpenSearch, OpenTofu, OpenBao, OpenVox, CIB seven. Et chaque fois, les organisations concernées ont dû arbitrer dans l'urgence. Les fiches qui suivent signalent systématiquement ces situations : c'est le principal service qu'un guide comme celui-ci peut rendre aujourd'hui.

La deuxième est celle de la **chaîne d'approvisionnement logicielle**. Une application moderne assemble des centaines de composants dont personne, dans l'organisation, n'a lu le code. Les incidents de ces dernières années, de Log4Shell aux prises de contrôle de paquets par ingénierie sociale, ont fait de l'inventaire des dépendances, de la génération d'une nomenclature logicielle (SBOM) et de la veille sur les vulnérabilités des exigences ordinaires. Le règlement européen sur la cyberrésilience les rendra obligatoires pour une large part des produits mis sur le marché européen.

La troisième est celle de la **soutenabilité**. Plusieurs briques critiques de cette dimension reposent sur une poignée de mainteneurs bénévoles. Contribuer, financer ou acheter du support à ceux dont on dépend n'est pas un geste militant : c'est une mesure de gestion du risque, au même titre qu'un contrat de maintenance.

Cette dimension se lit en trois parties : les outils de développement, les bases de données et couches intermédiaires, et l'outillage DevOps qui relie les deux au monde de la production.

.. toctree::
    :maxdepth: 1

    developpement/index.rst
    sgbd-middleware/index.rst
    devops/index.rst
