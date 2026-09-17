# Outils de développement

Cette partie présente l'outillage avec lequel on fabrique du logiciel : les frameworks applicatifs, les environnements de développement, les forges, les outils de test et de mesure de charge.

C'est le domaine où la victoire de l'open source est la plus complète, au point qu'elle ne se discute plus. Git, publié en 2005, a éliminé ses concurrents propriétaires en une décennie. Les frameworks qui structurent les applications web (Symfony, Django, Spring, Laravel, Rails) sont tous libres. Les forges, les serveurs d'intégration continue, les analyseurs de code, les bibliothèques de test le sont également. Une équipe de développement contemporaine travaille du matin au soir avec du logiciel libre, souvent sans y penser.

Cette banalisation déplace les questions.

**La dépendance invisible.** Une application moderne agrège des centaines de composants tiers que personne n'a lus. L'inventaire de ces dépendances, la surveillance de leurs vulnérabilités et la production d'une nomenclature logicielle (SBOM) sont devenus des exigences ordinaires, que le règlement européen sur la cyberrésilience rendra obligatoires pour une large part des logiciels mis sur le marché. Les outils correspondants sont présentés dans la partie [Outils pour le DevOps](../devops/index.md).

**Le choix d'un écosystème.** Retenir un framework, c'est s'engager sur dix ans : le recrutement, la formation, la dette technique et la capacité à faire évoluer l'application en dépendront davantage que des différences de performance au banc d'essai. Les critères qui comptent sont la régularité des publications, l'existence d'une version à support long, la qualité de la documentation et la profondeur du marché de compétences, en France notamment.

**La soutenabilité.** Plusieurs des bibliothèques dont dépendent des pans entiers de l'industrie reposent sur quelques mainteneurs bénévoles. Financer ou contribuer à ce dont on dépend relève de la gestion du risque autant que de la réciprocité.

Cette partie recense plus d'une centaine de solutions :

- [Frameworks Web (backend)](frameworks-web-backend.md)
- [Frameworks mobiles cross-platform](frameworks-mobiles-cross-platform.md)
- [Outils de développement](outils-de-developpement.md)
- [Outils de tests de charge](outils-de-tests-de-charge.md)
- [Autres](autres.md)
