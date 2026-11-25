# Haute disponibilité

La haute disponibilité est un terme fréquemment utilisé dans l’univers du Web, à propos d'architectures de systèmes ou de services pour désigner le fait qu’ils soient disponibles un maximum de temps, 100 % idéalement.

Dans les entreprises, il est très important de mettre en place des techniques de haute disponibilité et de résilience car l’informatique représente souvent le système nerveux de l’entreprise. Elles peuvent être mises en œuvre de différentes manières : d’un point de vue physique ou d’un point de vue logique notamment.

Il existe d’excellents outils open source pour s’assurer que les services répondent en permanence : Keepalived, qui fonctionne tel un routeur pour aiguiller les demandes selon l’état des services, ou le couple Pacemaker/Corosync, qui permet aux serveurs d'un cluster de connaître leur état respectif et de basculer les services automatiquement.

## ClusterLabs (Pacemaker, Corosync, Heartbeat)

Site
: <https://clusterlabs.org/>

Porteur
: une communauté

Licence
: GPL v2 et LGPL v2.1 (Pacemaker), BSD (Corosync)

La communauté ClusterLabs développe la pile de haute disponibilité en cluster la plus répandue sous Linux, empaquetée par Red Hat, SUSE et Debian. Elle a pris la suite du projet Linux-HA et de son logiciel Heartbeat, qui n'est plus développé.

**[Pacemaker](https://clusterlabs.org/projects/pacemaker/)**{ #pacemaker }, commencé en 2004, gère les ressources : systèmes de fichiers, adresses IP virtuelles, services réseau, bases de données, applications métier. Des agents standardisés les démarrent, les surveillent et les basculent d'un nœud à l'autre.

**[Corosync](https://corosync.github.io/corosync/)**{ #corosync }, lancé en 2008, assure la communication entre les nœuds, la détection de leur état et le calcul du quorum, sur lesquels Pacemaker s'appuie.

Un mécanisme de *fencing* (STONITH), qui isole un nœud défaillant, est indispensable pour éviter les scénarios de *split-brain*. Un cluster à deux nœuds appelle en outre un arbitre de quorum.

Pacemaker et Corosync sont écrits en C.

## HAProxy

Site
: <https://www.haproxy.org/>

Porteur
: une communauté, avec le soutien de HAProxy Technologies

Licence
: GPL v2, LGPL v2.1 pour les en-têtes

HAProxy est un reverse proxy utilisé pour la répartition de charge. Le projet existe depuis 2001 ; il a été écrit par Willy Tarreau.

Il gère nativement le protocole HTTP ce qui permet de mettre en place de l'affinité de session par cookies. Il dispose de plusieurs mécanismes de vérification d'états afin de détecter les serveurs en panne et de rediriger leur trafic vers les autres serveurs.

HAProxy est développé et soutenu par la société française HAProxy Technologies, fondée par son auteur, qui en commercialise une édition commerciale et des appliances. C'est aujourd'hui le répartiteur de charge logiciel le plus déployé au monde ; les versions récentes prennent en charge HTTP/2 et HTTP/3. Un contrôleur d'*ingress* existe pour Kubernetes.

## Keepalived

Site
: <https://www.keepalived.org/>

Porteur
: une communauté

Licence
: GPL v2

Keepalived est un composant permettant de configurer LVS (LinuxVirtualServer). Le projet existe depuis 2001.

LVS étant un système relativement basique et statique, il a besoin d'un logiciel pour maintenir sa configuration. Keepalived permet de faire des tests de disponibilité (par exemple connexion TCP, requête HTTP) d'un service, tient à jour la liste des serveurs utilisables pour LVS. Il gère également un système de bascule IP fondé sur VRRP pour sa propre redondance.

## DRBD

Site
: <https://linbit.com/drbd/>

Porteur
: une entreprise (LINBIT)

Licence
: GPL v2

DRBD (Distributed Replicated Block Device) est un système de réplication de données en temps réel. Le projet, porté par une société autrichienne, a commencé en 1999.

Il permet de répliquer des partitions ou des disques entiers entre les nœuds d'un cluster, assurant ainsi la redondance des données. DRBD fonctionne en conjonction avec les autres composants de haute disponibilité comme Pacemaker et Corosync ; son module est intégré au noyau Linux depuis la version 2.6.33. L'éditeur propose également LINSTOR, qui en orchestre le déploiement à l'échelle d'un cluster de stockage.

DRBD est écrit en C.

## Autres

Selon la couche à rendre hautement disponible, on s'intéressera également aux outils suivants :

- Patroni, pour les clusters PostgreSQL avec bascule automatique: <https://patroni.readthedocs.io/>
- Galera Cluster, réplication synchrone multi-maître pour MySQL et MariaDB, désormais développé chez MariaDB plc: <https://mariadb.com/docs/galera-cluster>
- etcd, entrepôt clé-valeur distribué fondé sur Raft, socle de Kubernetes: <https://etcd.io/>
- Ceph, stockage distribué tolérant aux pannes, présenté à la page [Stockage](stockage.md#ceph)
- Kubernetes, qui intègre nativement le redémarrage et la redistribution des charges applicatives (page [Conteneurs et orchestration](conteneurs-orchestration.md))
