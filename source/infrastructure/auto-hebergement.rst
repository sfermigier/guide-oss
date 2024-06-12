Solutions pour l’auto-hébergement (ou self-hosting)
===================================================

L’auto-hébergement, ou *self-hosting*, est la pratique consistant à
héberger ses propres ssolutions informatiques plutôt que de recourir à
des solutions hébergées par des tiers (SaaS ou *software as a service*).

L’auto-hébergement offre un contrôle accru sur les données et les
applications, ce qui peut être particulièrement important pour les
entreprises soucieux de protéger leurs secrets commerciaux ou de
respecter les législations sur les données personnelles, comme le RGPD
en Europe. En gardant les données en interne, les utilisateurs peuvent
mettre en place des mesures de sécurité personnalisées et garantir que
les informations sensibles ne sont accessibles qu’aux personnes
autorisées.

Approches de l’auto-hébergement
-------------------------------

1. Hébergement Sur Site
~~~~~~~~~~~~~~~~~~~~~~~

L’hébergement sur site consiste à installer et à gérer ses propres
serveurs physiques au sein de l’entreprise. Cette approche offre un
contrôle total sur les données et l’infrastructure, mais nécessite des
ressources significatives en termes de matériel, de maintenance et de
sécurité.

2. Hébergement sur serveurs dédiés
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les entreprises peuvent louer des serveurs dédiés auprès de fournisseurs
de services. Bien que l’infrastructure soit externalisée, le contrôle
sur les données et les applications reste prépondérant.

3. Hébergement cloud privé
~~~~~~~~~~~~~~~~~~~~~~~~~~

Les clouds privés, que ce soit sur site ou externalisés chez des
fournisseurs spécialisés, offrent flexibilité et évolutivité tout en
maintenant un haut niveau de contrôle sur les données. Les entreprises
peuvent utiliser des solutions de virtualisation pour gérer efficacement
les ressources.

4. Auto-hébergement sur cloud public
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Il est également possible d’implémenter l’auto-hébergement sur des
infrastructures de cloud public, en utilisant des services IaaS
(Infrastructure as a Service) ou PaaS (Platform as a Service). Cette
approche combine les avantages du cloud en termes d’évolutivité et de
flexibilité avec le contrôle sur les données et les applications.

Avantages de l’auto-hébergement
-------------------------------

1. Protection de la vie privée
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Contrôle total des données
^^^^^^^^^^^^^^^^^^^^^^^^^^

L’auto-hébergement permet aux utilisateurs de garder un contrôle total
sur leurs données, éliminant ainsi les risques associés à la
surveillance et à la collecte de données par des tiers. En conservant
les données en interne, il est plus facile de mettre en œuvre des
politiques de confidentialité strictes et de garantir que les données
sensibles ne sont accessibles qu’aux personnes autorisées.

Sécurisation des communications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Les communications internes et externes peuvent être sécurisées plus
efficacement grâce à des outils de chiffrement personnalisés et des
configurations de réseau robustes. En réduisant le nombre
d’intermédiaires, le risque de compromission des données en transit est
minimisé.

2. Préservation du secret des affaires
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Isolation des informations stratégiques
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L’auto-hébergement permet d’isoler les informations stratégiques de
l’entreprise des infrastructures partagées, réduisant ainsi le risque
d’espionnage industriel et de fuite de données. Les entreprises peuvent
mettre en place des mesures de sécurité adaptées à leurs besoins
spécifiques, comme des pare-feux, des systèmes de détection d’intrusion
et des protocoles d’accès stricts.

Conformité et contrôle juridique
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En hébergeant les données en interne ou sur des serveurs dédiés, les
entreprises peuvent s’assurer que leurs pratiques de gestion des données
sont conformes aux régulations locales et internationales. Cela est
particulièrement pertinent dans des secteurs soumis à des régulations
strictes, comme la santé, la finance et les services juridiques.

3. Personnalisation et Flexibilité
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adaptation aux besoins spécifiques
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L’auto-hébergement offre une grande flexibilité pour personnaliser les
services et les infrastructures en fonction des besoins spécifiques de
l’entreprise. Les entreprises peuvent choisir les technologies, les
outils et les configurations qui répondent le mieux à leurs exigences
opérationnelles et de sécurité.

Évolutivité et résilience
^^^^^^^^^^^^^^^^^^^^^^^^^

Avec des solutions de cloud privé et de virtualisation, les entreprises
peuvent adapter rapidement leurs ressources en fonction de la demande,
assurant ainsi une continuité de service optimale. Les systèmes peuvent
être redondants et résilients, réduisant ainsi le risque de pannes et de
pertes de données.

4. Avantages de l’auto-hébergement sur le cloud public
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scalabilité et flexibilité
^^^^^^^^^^^^^^^^^^^^^^^^^^

Utiliser des services IaaS ou PaaS permet aux entreprises de bénéficier
de la scalabilité et de la flexibilité des fournisseurs de cloud public
tout en conservant un contrôle significatif sur les applications et les
données. Les ressources peuvent être ajustées dynamiquement en fonction
des besoins, ce qui permet une gestion plus efficace des charges de
travail.

Réduction des coûts initiaux
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L’auto-hébergement sur le cloud public réduit les coûts initiaux
d’acquisition et de maintenance de l’infrastructure matérielle. Les
entreprises peuvent démarrer rapidement avec des investissements
moindres et payer uniquement pour les ressources utilisées, ce qui
améliore l’efficacité économique.

Solutions pour l’auto-hébergement
---------------------------------

Nua
~~~

:Site: https://nua.rocks

:Porteur: une entreprise (Abilian)

:Licence: AGPL-3.0

Nua est une plateforme open source d’auto-hébergement cloud (PaaS -
Platform as a Service) conçue pour couvrir l’ensemble du cycle de vie
des applications web, depuis le développement et le packaging jusqu’au
déploiement et à la maintenance, en passant par la sécurité.

Nua vise particulièrement les organisations (PME, associations, services
publics, etc.) souhaitant ou nécessitant la mise en œuvre d’une
stratégie d’autonomie numérique en privilégiant les logiciels open
source.

D’une conception axée sur la simplicité de déploiement et l’intégration,
Nua utilise des technologies éprouvées telles que le langage Python, les
standards de l’Open Container Initiative (OCI) et la plateforme Docker.
Le projet suit les meilleures pratiques du marché PaaS, notamment la
philosophie des “12 factor apps”, pour faciliter le déploiement des
applications basées sur les principaux frameworks web comme Django,
Rails, et Laravel.

Nua propose une configuration déclarative et des conventions pour
minimiser la duplication des informations, ainsi qu’une chaîne
d’approvisionnement logicielle sécurisée appliquant des pratiques
actuelles telles que la “SBOM” (software bill of material). La
plateforme est extensible via des plugins, permettant l’adoption de
technologies émergentes ou plus confidentielles.

Nua est développé en Python.

Hop3
~~~~

:Site: https://hop3.cloud

:Porteur: une entreprise (Abilian)

:Licence: MIT

Hop3 est un outil pour déployer et gérer des applications web sur un
seul serveur. Il est conçu pour être simple, sécurisé et facile à
utiliser. Hop3 vise à améliorer l’informatique en nuage en mettant
l’accent sur la souveraineté, la sécurité, la durabilité et
l’inclusivité. Il facilite l’accès aux technologies cloud pour une large
gamme d’utilisateurs, notamment les petites et moyennes entreprises
(PME), les associations, les services publics et les développeurs
individuels.

La stack technologique de Hop3 est soigneusement choisie pour soutenir
ses objectifs sans dépendre des outils de conteneurisation
conventionnels comme Docker ou Kubernetes. Elle se concentre sur des
solutions alternatives et légères qui s’alignent sur les principes
d’efficacité et de souveraineté du projet.

Hop3 est développé en Python.

Piku
~~~~

:Site: https://github.com/piku/piku

:Porteur: une communauté

:Licence: MIT

Piku est une plateforme PaaS minimaliste open source qui permet de
déployer des applications en utilisant des commandes Git. Conçu pour
être léger et simple, Piku est idéal pour les petites équipes et les
développeurs individuels qui souhaitent déployer des applications
rapidement sans complexité.

Piku supporte les principaux langages de programmation et frameworks,
notamment Python, Node.js, Ruby, Go, et plus encore. Il permet le
déploiement d’applications en poussant simplement le code vers un dépôt
Git, ce qui déclenche automatiquement le déploiement sur le serveur.

Le développement de Piku est communautaire, favorisant la simplicité et
l’efficacité. Il est conçu pour fonctionner sur des infrastructures
légères, comme des Raspberry Pi ou des serveurs VPS.

Piku est développé en Python.

Dokku
~~~~~

:Site: https://dokku.com

:Porteur: une communauté

:Licence: MIT

Dokku est une plateforme PaaS open source basée sur Docker, permettant
de déployer et de gérer des applications de manière simplifiée. Inspiré
par Heroku, Dokku permet aux utilisateurs de déployer des applications
en poussant leur code vers un dépôt Git.

Dokku supporte une large gamme de langages et frameworks, grâce à
l’utilisation de buildpacks. Il offre des fonctionnalités de gestion des
bases de données, des certificats SSL, et des configurations
environnementales, facilitant le déploiement et la gestion des
applications.

Le développement de Dokku est communautaire, avec une forte emphase sur
la facilité d’utilisation et la flexibilité. Il permet aux développeurs
de créer des environnements de production fiables sur des serveurs
auto-hébergés.

Dokku est développé en Shell script et utilise Docker pour l’isolation
des applications.

YunoHost
~~~~~~~~

:Site: https://yunohost.org

:Porteur: une communauté

:Licence: GPL-3.0

YunoHost est une distribution basée sur Debian qui vise à simplifier le
processus d’auto-hébergement. Il fournit une interface web intuitive
pour installer, configurer et gérer divers services.

D’une conception modulaire, YunoHost permet l’installation facile
d’applications comme Nextcloud, WordPress, Roundcube, et Jitsi Meet via
une interface web. Il propose également une gestion simplifiée des
utilisateurs et des groupes ainsi que des fonctionnalités de sécurité
comme les certificats SSL/TLS, le pare-feu et les mises à jour
automatiques.

Le développement est entièrement communautaire, permettant une
contribution active et continue à l’amélioration de la plateforme.

YunoHost est basé sur des standards reconnus et utilise des technologies
comme NGINX pour le serveur web, Python pour l’interface et OpenLDAP
pour la gestion des utilisateurs.

Sandstorm
~~~~~~~~~

:Site: https://sandstorm.io

:Porteur: une communauté

:Licence: Apache 2.0

Sandstorm est une plateforme open source qui permet de déployer des
applications web de manière sécurisée et isolée.

Chaque application fonctionne dans un environnement sécurisé et isolé,
offrant une protection accrue contre les vulnérabilités. Sandstorm
propose une interface utilisateur simplifiée pour installer et gérer des
applications, avec un App Store riche en applications open source.

Le développement est communautaire et vise à fournir une solution
sécurisée et facile à utiliser pour l’auto-hébergement.

Sandstorm utilise des conteneurs pour l’isolation des applications et
supporte des technologies comme Node.js et MongoDB pour le backend.

CasaOS
~~~~~~

:Site: https://www.casaos.io

:Porteur: une entreprise (X-NODE Space)

:Licence: Apache 2.0

CasaOS est une solution open source conçue pour être une plateforme
domestique unifiée, simplifiant le déploiement et la gestion de diverses
applications.

Avec une interface utilisateur conviviale, CasaOS permet de gérer
facilement des applications populaires comme Plex, Nextcloud, et Home
Assistant. Il supporte également Docker pour étendre les capacités de la
plateforme.

CasaOS est soutenu par une communauté active, qui contribue au
développement et à l’amélioration continue du projet.

Il fonctionne sur divers systèmes, y compris les Raspberry Pi, et
utilise Docker pour l’isolation et la gestion des applications.

CasaOS est développé en Go.

HomelabOS
~~~~~~~~~

:Site: https://homelabos.com

:Porteur: une communauté

:Licence: MIT

HomelabOS est un ensemble de scripts Ansible pour configurer et gérer
une variété de services auto-hébergés.

L’automatisation via Ansible permet une configuration rapide et efficace
des services comme Nextcloud, Plex, GitLab, et plus encore. Il offre des
fonctionnalités de sécurité intégrées comme le chiffrement SSL/TLS et la
gestion des utilisateurs.

Le projet est communautaire, avec des contributions ouvertes pour
l’ajout de nouvelles fonctionnalités et l’amélioration des existantes.

HomelabOS est conçu pour être facile à configurer et à utiliser, avec
des fichiers YAML pour la gestion des configurations.

HomelabOS est développé en Python (+ Ansible).

FreedomBox
~~~~~~~~~~

:Site: https://freedombox.org

:Porteur: une communauté

:Licence: AGPL-3.0

FreedomBox est une solution basée sur Debian, destinée à rendre
l’auto-hébergement accessible à tous, en mettant l’accent sur la vie
privée et la sécurité.

Elle propose une interface web simple pour l’installation et la gestion
des applications, avec un accent particulier sur les applications
orientées vie privée comme Tor, OpenVPN, et Syncthing.

Le développement est conduit par une communauté active, visant à fournir
une solution de serveur personnel facile à utiliser et sécurisée.

FreedomBox supporte divers matériels, y compris des mini-PC et des
routeurs, et utilise des technologies standard comme Apache et OpenLDAP
pour ses services.

FreedomBox est développé en Python (+ Django).
