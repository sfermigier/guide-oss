Haute disponibilité
===================

La haute disponibilité est un terme fréquemment utilisé dans l’univers du Web, à propos d'architectures de systèmes ou de services pour désigner le fait qu’ils soient disponibles un maximum de temps, 100% idéalement.

Dans les entreprises, il est très important de mettre en place des techniques de hautes disponibilité et de résilience tant l’informatique représente souvent le système nerveux de l’organisation. Elles peuvent être mises en œuvre de différentes manières : d’un point de vue physique ou d’un point de vue logique notamment.

Il existe d’excellents outils open source pour s’assurer que les services répondent en permanence : Keepalived, qui fonctionne tel un routeur pour aiguiller les demandes selon l’état des services, ou le couple Pacemaker/Corosync, qui permet aux serveurs d'un cluster de connaître leur état respectif et de basculer les services automatiquement.


ClusterLabs (Pacemaker, Corosync, Heartbeat)
--------------------------------------------

:Site: https://clusterlabs.org/
:Porteur: une communauté
:Licence: GPL v2 et LGPL

Le projet Linux-HA, présenté dans les éditions précédentes de ce guide, fournissait depuis 1999 les composants de haute disponibilité des systèmes de type UNIX, autour du logiciel de communication Heartbeat. Ce projet n'existe plus en tant que tel : son site linux-ha.org n'est plus en service, le développement de Heartbeat s'est arrêté, et l'ensemble de ses fonctions a été repris par la communauté **ClusterLabs**, qui regroupe aujourd'hui Pacemaker (gestionnaire de ressources), Corosync (couche de communication et de quorum) et les agents de ressources associés.

C'est cette pile — largement empaquetée par Red Hat, SUSE et Debian — qui constitue le standard de la haute disponibilité en cluster sous Linux, aussi bien pour les bases de données que pour les systèmes de fichiers partagés, les adresses IP virtuelles ou les applications métier.

Voir les fiches Pacemaker et Corosync ci-dessous.

HAProxy
-------

:Site: https://www.haproxy.org/
:Porteur: une communauté
:Licence: GPL

HAProxy est un reverse proxy utilisé pour la répartition de charge. Le projet existe depuis 2001 ; il a été écrit par Willy Tarreau.

Il gère nativement le protocole HTTP ce qui permet de mettre en place de l'affinité de session par cookies. Il dispose de plusieurs mécanismes de vérification d'états afin de détecter les serveurs en panne et de rediriger leur trafic vers les autres serveurs.

HAProxy est développé et soutenu par la société française HAProxy Technologies, fondée par son auteur, qui en commercialise une édition entreprise et des appliances. C'est aujourd'hui le répartiteur de charge logiciel le plus déployé au monde ; les versions récentes prennent en charge HTTP/2 et HTTP/3, et il existe un contrôleur d'*ingress* pour Kubernetes.


Keepalived
----------

:Site: https://www.keepalived.org/
:Porteur: une communauté
:Licence: GPL

Keepalived est un composant permettant de configurer LVS (LinuxVirtualServer). Le projet existe depuis 2001.

LVS étant un système relativement basique et statique, il a besoin d'un logiciel pour maintenir sa configuration. Keepalived permet de faire des tests de disponibilité (par exemple connexion TCP, requête HTTP) d'un service, tient à jour la liste des serveurs utilisables pour LVS. Il gère également un système de bascule IP basé sur VRRP pour sa propre redondance.


Pacemaker
---------

:Site: https://clusterlabs.org/projects/pacemaker/
:Porteur: une communauté
:Licence: GPL

Pacemaker est un gestionnaire de clusters de haute disponibilité. Il assure la gestion des ressources et les opérations de bascule dans un environnement de cluster. Le projet a débuté en 2004.

Pacemaker fonctionne en conjonction avec Corosync, qui assure la communication entre les nœuds et le calcul du quorum, pour surveiller l'état du cluster et gérer les défaillances. Il gère un large éventail de ressources — systèmes de fichiers, adresses IP, services réseau, bases de données, applications métier — via des agents de ressources standardisés, et prend en charge les mécanismes de *fencing* (STONITH) indispensables pour éviter les scénarios de *split-brain*.

Pacemaker est écrit principalement en C.


Corosync
--------

:Site: https://corosync.github.io/corosync/
:Porteur: une communauté
:Licence: BSD

Corosync est un logiciel de communication et de quorum pour clusters. Il a été initialement lancé en 2008.

Il fournit une bibliothèque de communication pour les nœuds d'un cluster et assure la diffusion des informations de l'état du cluster. Corosync est souvent utilisé en conjonction avec Pacemaker pour créer des environnements de haute disponibilité robustes.

Corosync est écrit en C.


DRBD
----

:Site: https://linbit.com/drbd/
:Porteur: une entreprise autrichienne (LINBIT)
:Licence: GPL

DRBD (Distributed Replicated Block Device) est un système de réplication de données en temps réel. Le projet a commencé en 1999.

Il permet de répliquer des partitions ou des disques entiers entre les nœuds d'un cluster, assurant ainsi la redondance des données. DRBD fonctionne en conjonction avec les autres composants de haute disponibilité comme Pacemaker et Corosync, et son module est intégré au noyau Linux depuis la version 2.6.33. L'éditeur propose également LINSTOR, qui en orchestre le déploiement à l'échelle d'un cluster de stockage.

DRBD est écrit en C.


Autres
------

Selon la couche à rendre hautement disponible, on s'intéressera également aux outils suivants :

- Patroni, pour les clusters PostgreSQL avec bascule automatique: https://patroni.readthedocs.io/
- Galera Cluster, réplication synchrone multi-maître pour MySQL et MariaDB: https://galeracluster.com/
- etcd, entrepôt clé-valeur distribué fondé sur Raft, socle de Kubernetes: https://etcd.io/
- Ceph, stockage distribué (objet, bloc et fichiers) tolérant aux pannes: https://ceph.io/
- Kubernetes, qui intègre nativement le redémarrage et la redistribution des charges applicatives (section :doc:`/infrastructure/virtualisation`)
