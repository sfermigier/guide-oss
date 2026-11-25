# Conteneurs et orchestration

La conteneurisation isole des processus qui partagent le noyau de leur hôte, à un coût très inférieur à celui d'une machine virtuelle complète. Une application est livrée sous la forme d'une image qui contient ses dépendances ; la même image sert du poste de développement à la production. Le format des images et leur exécution sont normalisés par l'*Open Container Initiative*, ce qui rend les outils largement interchangeables.

Deux décisions sont à prendre séparément : le moteur qui construit et exécute les conteneurs, puis l'orchestrateur éventuel qui les répartit sur plusieurs machines. Un serveur unique et quelques applications n'appellent pas d'orchestrateur : un fichier Compose, des unités systemd ou une plateforme présentée à la page [PaaS](paas.md) suffisent souvent. Kubernetes se justifie par la taille du parc, la fréquence des déploiements ou l'exigence de disponibilité. Il demande une équipe pour l'administrer.

Restent à traiter, quel que soit le choix, la provenance et la mise à jour des images, la persistance des données et le cloisonnement, un conteneur n'offrant pas l'isolation d'une machine virtuelle. Les conteneurs système (LXC, Incus) sont présentés à la page [Virtualisation](virtualisation.md).

## Docker

Site
: <https://www.docker.com/>

Porteur
: un éditeur (Docker Inc.)

Licence
: Apache 2.0 pour le moteur (projet Moby), licence commerciale pour Docker Desktop

Apparu en 2013, Docker a popularisé le format d'image et l'expérience d'utilisation qui sont devenus le standard du déploiement applicatif. Il comprend un démon, une interface en ligne de commande, l'outil de construction BuildKit et Compose, qui décrit dans un fichier YAML un ensemble de conteneurs liés.

Sur un serveur, le moteur Docker et Compose suffisent à faire tourner des applications sur une machine. L'accès au démon équivaut à un accès administrateur à l'hôte : il doit être réservé, ou l'on doit recourir au mode sans privilèges.

Le point de vigilance concerne Docker Desktop, l'application pour postes de travail, qui n'est pas libre et dont l'usage professionnel est payant au-delà de certains seuils. Le moteur installé sous Linux n'est pas concerné.

Docker est écrit en Go.

## Podman

Site
: <https://podman.io/>

Porteur
: une fondation (CNCF), avec le soutien de Red Hat

Licence
: Apache 2.0

Podman, créé par Red Hat, offre une interface en ligne de commande compatible avec celle de Docker, sans démon central et avec la possibilité de faire tourner les conteneurs sans privilèges (*rootless*). Il forme avec Buildah (construction d'images) et Skopeo (manipulation de registres) un ensemble accepté en janvier 2025 au niveau *sandbox* de la CNCF.

Il s'intègre à systemd, qui peut démarrer et surveiller les conteneurs comme n'importe quel service. Il sait regrouper des conteneurs en *pods* ou exécuter des manifestes Kubernetes simples. C'est l'outil fourni par Red Hat Enterprise Linux et un choix courant dans les environnements où un démon privilégié n'est pas admis.

La compatibilité avec Docker concerne la ligne de commande et l'API ; les projets qui dépendent étroitement de Compose ou du démon sont à tester avant migration.

Podman est écrit en Go.

## Kubernetes

Site
: <https://kubernetes.io/>

Porteur
: une fondation (CNCF)

Licence
: Apache 2.0

Kubernetes, issu de Google et confié en 2015 à la *Cloud Native Computing Foundation*, est le standard de fait de l'orchestration de conteneurs : ordonnancement sur un parc de machines, redémarrage automatique, montée en charge, réseau et stockage abstraits, déploiements progressifs.

L'utilisateur décrit un état souhaité que des contrôleurs s'emploient à atteindre. Ce mécanisme est extensible. Il a donné naissance à un vaste écosystème d'opérateurs (bases de données, certificats, stockage). Le projet est indépendant d'un fournisseur : les mêmes manifestes fonctionnent sur site et chez la plupart des hébergeurs, aux différences de stockage et d'équilibrage de charge près.

Sa richesse a un coût d'exploitation réel : plusieurs versions par an, chacune maintenue pour une durée limitée, des composants tiers à choisir pour le réseau, l'entrée du trafic et la supervision, un modèle de droits à configurer. Les distributions intégrées ou allégées en prennent une partie en charge.

Kubernetes est écrit en Go.

## K3s

Site
: <https://k3s.io/>

Porteur
: une fondation (CNCF), avec le soutien de SUSE

Licence
: Apache 2.0

K3s est une distribution Kubernetes certifiée, réunie dans un unique binaire de moins de 100 Mo. Créée par Rancher, devenu une filiale de SUSE, elle a été acceptée en 2020 au niveau *sandbox* de la CNCF.

Elle s'installe en une commande, remplace par défaut etcd par SQLite sur un serveur unique (etcd embarqué ou une base relationnelle externe restent possibles pour la haute disponibilité) et fournit d'origine un réseau, un contrôleur d'entrée et un stockage local. Elle convient aux petites infrastructures, à l'informatique de périphérie et aux environnements de test.

L'allègement concerne l'installation et l'empreinte mémoire : les concepts à maîtriser, les mises à jour et la sauvegarde du plan de contrôle restent ceux de Kubernetes.

K3s est écrit en Go.

## Autres

- Talos Linux, système d'exploitation minimal et immuable consacré à Kubernetes (MPL 2.0) : <https://www.siderolabs.com/talos-linux>
- OKD, distribution communautaire dont dérive Red Hat OpenShift (Apache 2.0) : <https://okd.io/>
- Rancher, gestion centralisée de plusieurs clusters (Apache 2.0) : <https://www.rancher.com/>
- k0s, distribution Kubernetes en un binaire (Apache 2.0) : <https://k0sproject.io/>
- containerd et CRI-O, moteurs d'exécution utilisés par Kubernetes : <https://containerd.io/> et <https://cri-o.io/>
- Harbor, registre d'images avec contrôle d'accès et analyse de vulnérabilités (Apache 2.0) : <https://goharbor.io/>
- Portainer CE, interface web pour Docker et Kubernetes (licence zlib) : <https://www.portainer.io/>
- Helm, Argo CD et Flux, présentés à la page [Déploiement](../devops/deploiement.md).
