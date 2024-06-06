Haute disponibilité
===================

La haute disponibilité est un terme fréquemment utilisé dans l’univers du Web, à propos d'architectures de systèmes ou de services pour désigner le fait qu’ils soient disponibles un maximum de temps, 100% idéalement.

Dans les entreprises, il est très important de mettre en place des techniques de hautes disponibilité et de résilience tant l’informatique représente souvent le système nerveux de l’organisation. Elles peuvent être mises en œuvre de différentes manières : d’un point de vue physique ou d’un point de vue logique notamment.

Il existe d’excellents outils open source pour s’assurer que les services répondent en permanence. Keepalived par exemple qui fonctionne tel un routeur pour aiguiller les demandes selon l’état des services, ou Linux-HA qui permet la communication entre serveurs pour changer à chaud des configurations selon les états des autres serveurs.


Linux-HA
--------

:Site: http://www.linux-ha.org
:Porteur: une communauté
:Licence: GPL v2

Le projet Linux-HA fournit des composants de haute disponibilité pour les systèmes d'exploitation de type UNIX.

Le composant principal de ce projet est le logiciel de communication Heartbeat, qui permet à un groupe de machines de connaître leur état respectif, et ainsi de déclencher des actions de manière concertée sans avoir besoin d'un serveur tiers. Heartbeat est généralement utilisé avec un logiciel de gestion de cluster, tel que Pacemaker, dont le rôle est de gérer les dépendances entre services et réaliser les opérations de bascule automatiquement. Un gestionnaire de ressources minimal est fourni par Linux-HA, et s'avère très souvent suffisant.

Linux-HA est le système de haute disponibilité le plus répandu, et de nombreux prestataires sont disponibles pour assurer son support. Il remonte à 1999 pour ses premiers composants.

Linux-HA est écrit en C et en Python.

HAProxy
-------

:Site: https://www.haproxy.org/
:Porteur: une communauté
:Licence: GPL

HAProxy est un reverse proxy utilisé pour la répartition de charge. Le projet existe depuis 2001 ; il a été écrit par Willy Tarreau.

Il gère nativement le protocole HTTP ce qui permet de mettre en place de l'affinité de session par cookies. Il dispose de plusieurs mécanismes de vérification d'états afin de détecter les serveurs en panne et de rediriger leur trafic vers les autres serveurs.

HAProxy est supporté officiellement par un petit nombre de sociétés.


Keepalived
----------

:Site: https://www.keepalived.org/
:Porteur: une communauté
:Licence: GPL

Keepalived est un composant permettant de configurer LVS (LinuxVirtualServer). Le projet existe depuis 2001.

LVS étant un système relativement basique et statique, il a besoin d'un logiciel pour maintenir sa configuration. Keepalived permet de faire des tests de disponibilité (par exemple connexion TCP, requête HTTP) d'un service, tient à jour la liste des serveurs utilisables pour LVS. Il gère également un système de bascule IP basé sur VRRP pour sa propre redondance.


Pacemaker
---------

:Site: https://clusterlabs.org/pacemaker/
:Porteur: une communauté
:Licence: GPL

Pacemaker est un gestionnaire de clusters de haute disponibilité. Il assure la gestion des ressources et les opérations de bascule dans un environnement de cluster. Le projet a débuté en 2004.

Pacemaker fonctionne en conjonction avec d'autres composants tels que Corosync ou Heartbeat pour surveiller l'état des nœuds et gérer les défaillances. Il est capable de gérer un large éventail de ressources, y compris les systèmes de fichiers, les services réseau et les applications.

Pacemaker est écrit principalement en C.


Corosync
--------

:Site: https://clusterlabs.org/corosync.html
:Porteur: une communauté
:Licence: BSD

Corosync est un logiciel de communication et de quorum pour clusters. Il a été initialement lancé en 2008.

Il fournit une bibliothèque de communication pour les nœuds d'un cluster et assure la diffusion des informations de l'état du cluster. Corosync est souvent utilisé en conjonction avec Pacemaker pour créer des environnements de haute disponibilité robustes.

Corosync est écrit en C.


DRBD
----

:Site: https://www.linbit.com/en/drbd/
:Porteur: LINBIT
:Licence: GPL

DRBD (Distributed Replicated Block Device) est un système de réplication de données en temps réel. Le projet a commencé en 1999.

Il permet de mirrorer des partitions de disques entiers entre des nœuds d'un cluster, assurant ainsi une redondance des données. DRBD fonctionne en conjonction avec d'autres composants de haute disponibilité comme Pacemaker et Corosync.

DRBD est écrit en C.
