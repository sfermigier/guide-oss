Infrastructure
==============

L'infrastructure est le berceau du logiciel libre en entreprise, et la dimension la plus fournie de ce guide : systèmes d'exploitation, virtualisation et conteneurs, réseau et pare-feu, sécurité, gestion d'identité, supervision, sauvegarde, haute disponibilité, gestion de parc.

C'est ici que l'open source s'est imposé le premier, et si complètement que la question ne se pose plus : Linux fait tourner la quasi-totalité des serveurs du monde, des supercalculateurs aux objets connectés, et l'essentiel des briques qui les entourent (serveurs web, DNS, annuaires, hyperviseurs, orchestrateurs) sont libres. Une direction informatique qui refuserait le logiciel libre dans cette dimension n'aurait plus d'offre.

Quatre mouvements structurent la période.

**La reconfiguration de la virtualisation.** Le rachat de VMware par Broadcom, et le bouleversement tarifaire qui a suivi, ont provoqué le plus important mouvement de migration d'infrastructure depuis des années. Proxmox VE, fondé sur KVM et Debian, en est le principal bénéficiaire, aux côtés d'XCP-ng et d'OpenStack pour les grandes installations. C'est aujourd'hui le premier motif de projet dans cette dimension.

**La conteneurisation comme norme.** Docker, Podman et Kubernetes forment désormais le socle ordinaire du déploiement applicatif. Leur adoption a un coût d'exploitation réel, que les distributions allégées comme K3s cherchent à réduire : un cluster Kubernetes pour trois applications reste une mauvaise idée.

**La réglementation devient prescriptive.** La directive NIS 2, transposée en droit français, étend à des milliers d'entités des obligations de sécurité qui relèvent directement de cette dimension : gestion des vulnérabilités, journalisation, sauvegardes éprouvées, continuité d'activité, maîtrise de la chaîne d'approvisionnement. Le règlement sur la cyberrésilience complétera le dispositif côté produits. Les outils présentés ici, de la supervision à la sauvegarde en passant par la PKI et la gestion d'identité, sont les instruments de cette conformité.

**La souveraineté quitte le discours.** Les mêmes causes (dépendance à quelques fournisseurs, législations extraterritoriales, hausses tarifaires subies) poussent administrations et entreprises à reprendre la main sur leur infrastructure. La section :doc:`/infrastructure/auto-hebergement` détaille les approches possibles, du serveur sur site au cloud privé.

Reste une remarque valable pour toute cette dimension : les compétences y comptent autant que les logiciels. Un pare-feu mal configuré, une sauvegarde jamais restaurée ou un cluster que personne ne sait dépanner à trois heures du matin coûtent plus cher que la licence qu'ils ont permis d'économiser.

.. toctree::
    :maxdepth: 1

    systeme-exploitation-linux-bsd.rst
    auto-hebergement.rst
    securite.rst
    pki.rst
    authentification-federation-et-gestion-identite.rst
    firewalls.rst
    vpn.rst
    virtualisation.rst
    supervision-et-metrologie.rst
    controle-de-postes-a-distance.rst
    gestion-de-parc-et-inventaires.rst
    sauvegarde.rst
    haute-disponibilite.rst
    accelerateur-http.rst
    autres.rst
