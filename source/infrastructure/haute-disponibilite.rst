Haute disponibilité
===================

La haute disponibilité est un terme fréquemment utilisé dans l’univers du Web, à propos d'architectures de systèmes ou de services pour désigner le fait qu’ils soient disponibles un maximum de temps, 100% idéalement.

Dans les entreprises, il est très important de mettre en place des techniques de hautes disponibilité et de résilience tant l’informatique représente souvent le système nerveux de l’organisation. Elles peuvent être mises en œuvre de différentes manières : d’un point de vue physique ou d’un point de vue logique notamment.

Il existe d’excellents outils open source pour s’assurer que les services répondent en permanence. Keepalived par exemple qui fonctionne tel un routeur pour aiguiller les demandes selon l’état des services, ou Linux-HA qui permet la communication entre serveurs pour changer à chaud des configurations selon les états des autres serveurs.


Linux-HA
--------

:Site: https://www.linux-ha.org
:Porteur: une communauté
:Licence: GPL v2

Le projet Linux-HA fournit des composants de haute disponibilité pour les systèmes d'exploitation de type UNIX.

Le composant principal de ce projet est le logiciel de communication Heartbeat, qui permet à un groupe de machines de connaître leur état respectif, et ainsi de déclencher des actions de manière concertée sans avoir besoin d'un serveur tiers. Heartbeat est généralement utilisé avec un logiciel de gestion de cluster, tel que Pacemaker, dont le rôle est de gérer les dépendances entre services et réaliser les opérations de bascule automatiquement. Un gestionnaire de ressources minimal est fourni par Linux-HA, et s'avère très souvent suffisant.

Linux-HA est le système de haute disponibilité le plus répandu, et de nombreux prestataires sont disponibles pour assurer son support. Il remonte à 1999 pour ses premiers composants.

Linux-HA est écrit en C et en Python.

LVS
---

:Site: https://www.linuxvirtualserver.org
:Porteur: une communauté
:Licence: GPL v2

LVS (Linux Virtual Server) est le système d'équilibrage de charge inclus au noyau Linux depuis 1998. Il a écrit écrit par Wensong Zhang.

Il permet de router les connexions réseau entrantes vers un ensemble de machines, en suivant un certain nombre de politiques d'équilibrage de charge classiques (round-robin, weighted round-robin, etc.). Il constitue une simple brique d'un système de load balancing, car il ne prend pas en charge lui-même sa configuration. On utilise un logiciel tiers pour tester l'état des serveurs et mettre à jour la configuration LVS en cas de panne d'un serveur.

Comme le reste des composants de Linux, LVS est disponible sous licence GPL v2 et est supporté par un grand nombre de prestataires.


HAProxy
-------

:Site: http://haproxy.1wt.eu
:Porteur: une communauté
:Licence: GPL

HAProxy est un reverse proxy utilisé pour la répartition de charge. Le projet existe depuis 2001 ; il a été écrit par Willy Tarreau.

Il gère nativement le protocole HTTP ce qui permet de mettre en place de l'affinité de session par cookies. Il dispose de plusieurs mécanismes de vérification d'états afin de détecter les serveurs en panne et de rediriger leur trafic vers les autres serveurs.

HAProxy est supporté officiellement par un petit nombre de sociétés.


Keepalived
----------

:Site: https://www.keepalived.org
:Porteur: une communauté
:Licence: GPL

Keepalived est un composant permettant de configurer LVS. Le projet existe depuis 2001.

LVS étant un système relativement basique et statique, il a besoin d'un logiciel pour maintenir sa configuration. Keepalived permet de faire des tests de disponibilité (par exemple connexion TCP, requête HTTP) d'un service, tient à jour la liste des serveurs utilisables pour LVS. Il gère également un système de bascule IP basé sur VRRP pour sa propre redondance.
