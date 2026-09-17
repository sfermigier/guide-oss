MOM & EAI
=========

Les Middleware Orientés Messages, ou « MOMs », sont des outils particulièrement précieux pour mettre en œuvre des échanges entre applications de toutes natures.

Un middleware permet à différentes applications d’échanger et d'interopérer. Un middleware permet aux applications d'interopérer y compris lorsqu'elles tournent sur des serveurs différents, interconnectés par un réseau. Le middleware est un outil de haut niveau, puisqu’il offre ses services aux applications, mais les échanges induits s’appuient sur toute une pile de protocoles réseau.

Un middleware est davantage qu'un simple protocole d'appel des services offerts par une application, et typiquement RPC, RMI ou bien SOAP, tous également synchrones, ne sont pas vraiment considérés comme des middlewares.

Références:

- https://www.enterpriseintegrationpatterns.com/patterns/messaging/



Apache ActiveMQ
---------------

:Site: https://activemq.apache.org
:Porteur: une fondation (Apache)
:Licence: Apache 2.0

Sorti en 2004, ActiveMQ est le MOM open source de la fondation Apache.

ActiveMQ s’appuie sur quelques autres projets Apache : Apache Camel (Implémentation partielle des « Entreprise Integration Patterns ») et Jetty (Serveur d'application Java intégré à ActiveMQ). Et ActiveMQ est à son tour utilisé par quelques autres grands projets : Apache Service Mix, Mule, Geronimo (comme fournisseur JMS par défaut). Le traitement des messages de ActiveMQ est sans doute son plus célèbre atout, après celui de sa grande connectivité. À l'aide du projet Camel qui est intégré, il a la possibilité de traiter les messages selon les modèles d'intégration d'entreprises (*EIP* ou *Enterprise Integration Patterns*).

ActiveMQ est développé en Java. La diversité des langages et environnements pris en charge côté client est l'un de ses grands atouts : C, C++, .NET, Perl, PHP, Python, Ruby, etc., via les protocoles OpenWire, AMQP, MQTT et STOMP.

Le projet se décline aujourd'hui en deux implémentations : ActiveMQ « Classic », la version historique, et **ActiveMQ Artemis**, issue du moteur HornetQ et devenue la branche recommandée pour les nouveaux déploiements, plus performante et plus économe en ressources.


JORAM
-----

:Site: https://joram.ow2.io/
:Porteur: un consortium (OW2) et un éditeur (ScalAgent)
:Licence: LGPL

JORAM (« Java Open Reliable Asynchronous Messaging ») est le Middleware de consortium Object Web, sortie en 1999. Object Web est aussi connu pour son serveur d'application Java nommé Jonas auquel est d'ailleurs intégré JORAM.

JORAM a une architecture interne élégante, fondée sur le modèle d'agent. Un agent est un composant logiciel répondant à certains événements. Dans le cas de JORAM, les événements sont sous forme de messages. Les queues et les topics sont ainsi représentés par des agents. Un utilisateur connecté à la plateforme est également représenté par un agent dit proxy. Cette approche offre une grande flexibilité car elle permet la création et la suppression d'agents à la volée et sur n'importe quel broker.

Les langages par lesquels on peut accéder à JORAM sont Java (via l'interface JMS), C et C++ (à l'aide de JNI, ce qui permet de simuler un environnement JMS). Le projet, très lié à l'écosystème OW2 et au serveur JOnAS, n'évolue plus guère ; il reste employé dans des systèmes embarqués et des déploiements industriels existants.


RabbitMQ
--------

:Site: https://www.rabbitmq.com
:Porteur: un éditeur (Broadcom, via VMware Tanzu)
:Licence: MPL 2.0

RabbitMQ est un MOM open source qui implémente le standard AMQP et propose des passerelles vers d'autres protocoles. Son architecture à plugins lui permet d'être étendu par l'ajout de nouvelles fonctionnalités.

RabbitMQ est implémenté en Erlang au-dessus de la plateforme de haute disponibilité OTP, ce qui lui confère une grande robustesse. On peut y accéder côté client dans une grande variété de langages, grâce au protocole standard AMQP, ainsi que via MQTT et STOMP. Les versions récentes ont remplacé les files miroir par les *quorum queues*, fondées sur l'algorithme de consensus Raft, et ajouté les *streams* pour les usages de journalisation.

C'est aujourd'hui le courtier de messages généraliste le plus déployé, en particulier comme support de files de tâches pour les applications web (Celery, Sidekiq, Symfony Messenger…).


Apache Kafka
------------

:Site: https://kafka.apache.org/
:Porteur: une fondation (Apache)
:Licence: Apache 2.0

Créé chez LinkedIn en 2011 et confié à la fondation Apache, Kafka est devenu le standard de fait des architectures orientées événements. Son absence des éditions précédentes de ce guide était la lacune la plus criante.

Kafka n'est pas un courtier de messages au sens classique : c'est un journal distribué, répliqué et persistant. Les messages y sont conservés pendant une durée configurable et relus à volonté par des consommateurs indépendants, chacun à son rythme. Cette conception autorise des débits de plusieurs millions de messages par seconde et fait de Kafka aussi bien un bus d'intégration temps réel (avec Kafka Connect pour les connecteurs et Kafka Streams pour le traitement en flux) qu'une source de vérité pour des architectures *event sourcing*.

Les versions récentes ont supprimé la dépendance à ZooKeeper (mode KRaft), ce qui simplifie considérablement l'exploitation.

Kafka est écrit en Java et Scala. Redpanda (https://www.redpanda.com/), réimplémentation en C++ compatible avec son protocole, en constitue une alternative notable, sous licence source-available.


Autres
------

Parmi les produits de l’univers MOM & EAI, on peut compléter la liste avec les outils ci-dessous :

- NATS, courtier léger et très performant, projet de la CNCF: https://nats.io/
- Apache Pulsar, alternative à Kafka avec séparation du calcul et du stockage: https://pulsar.apache.org/
- ZeroMQ, bibliothèque de messagerie sans courtier: https://zeromq.org/
- Mosquitto, courtier MQTT de référence pour l'IoT: https://mosquitto.org/
- Apache Camel, pour l'intégration et le routage (section :doc:`/sgbd-middleware/esb`): https://camel.apache.org/

JBoss Messaging, cité dans les éditions précédentes, n'existe plus : son moteur a donné naissance à HornetQ, dont le code a été reversé à la fondation Apache et constitue aujourd'hui ActiveMQ Artemis.
