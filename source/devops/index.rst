Outils pour le DevOps
=====================

Le DevOps est un effort collaboratif et pluridisciplinaire visant à automatiser la livraison continue de nouvelles versions de logiciels, tout en garantissant leur exactitude et leur fiabilité. Cette partie présente l'outillage qui le rend possible : tests et intégration continue d'un côté, déploiement et gestion de configuration de l'autre.

C'est une dimension jeune (elle n'existait pas dans les premières éditions de ce guide) et entièrement bâtie sur du logiciel libre. Elle a connu en quelques années trois recompositions, à connaître avant de choisir ses outils.

**L'intégration continue a émigré vers les forges.** Le serveur d'intégration autonome, dont Jenkins reste l'archétype, cède du terrain aux moteurs intégrés à la forge (GitLab CI, GitHub Actions, Forgejo Actions), qui présentent l'avantage décisif de décrire la chaîne de construction dans le dépôt lui-même, versionnée avec le code qu'elle produit.

**Le déploiement est devenu déclaratif.** On décrit l'état attendu du système, qu'un agent se charge d'atteindre et de maintenir, là où il fallait auparavant écrire la suite des actions à exécuter. Cette idée, formalisée par la théorie des promesses et portée par Ansible, Puppet ou Salt, s'est étendue aux conteneurs sous le nom de GitOps : l'état souhaité du cluster est un dépôt Git, qu'un opérateur applique en continu.

**Les licences ont vacillé.** L'outillage d'infrastructure a été le plus touché par le reflux des licences libres : Terraform est passé sous licence BUSL en 2023, provoquant la création d'OpenTofu ; HashiCorp Vault a connu le même sort avec OpenBao ; Puppet a fermé son développement en 2024, d'où OpenVox. Les trois forks sont hébergés par des fondations et constituent aujourd'hui, pour un usage libre, le choix le plus sûr.

Reste un point de méthode que l'outillage ne résout pas : l'automatisation ne réduit le risque que si elle est testée. Une chaîne de déploiement dont on n'a jamais éprouvé le retour arrière, et une sauvegarde dont on n'a jamais tenté la restauration, appartiennent à la même catégorie d'illusions.

.. toctree::
    :maxdepth: 1

    tests-integration-continue.rst
    deploiement.rst
