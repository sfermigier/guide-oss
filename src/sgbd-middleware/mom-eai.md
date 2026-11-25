# MOM et EAI { #mom-eai }

Les Middleware Orientés Messages, ou « MOMs », sont des outils particulièrement précieux pour mettre en œuvre des échanges entre applications de toutes natures.

Un middleware permet à différentes applications d’échanger et d'interopérer. Un middleware permet aux applications d'interopérer y compris lorsqu'elles tournent sur des serveurs différents, interconnectés par un réseau. Le middleware est un outil de haut niveau, puisqu’il offre ses services aux applications, mais les échanges induits s’appuient sur toute une pile de protocoles réseau.

Un middleware est davantage qu'un simple protocole d'appel des services offerts par une application. RPC, RMI ou bien SOAP, tous également synchrones, ne sont pas vraiment considérés comme des middlewares.

Références:

- <https://www.enterpriseintegrationpatterns.com/patterns/messaging/>

## Apache ActiveMQ

Site
: <https://activemq.apache.org>

Porteur
: une fondation (Apache)

Licence
: Apache 2.0

Sorti en 2004, ActiveMQ est le MOM open source de la fondation Apache.

ActiveMQ s’appuie sur quelques autres projets Apache : Apache Camel (pour les *Enterprise Integration Patterns*) et Jetty (Serveur d'application Java intégré à ActiveMQ). Le traitement des messages de ActiveMQ est sans doute son plus célèbre atout, après celui de sa grande connectivité. À l'aide du projet Camel qui est intégré, il a la possibilité de traiter les messages selon les modèles d'intégration d'entreprises (*EIP* ou *Enterprise Integration Patterns*).

ActiveMQ est développé en Java. La diversité des langages et environnements pris en charge côté client est l'un de ses grands atouts : C, C++, .NET, Perl, PHP, Python, Ruby, etc., via les protocoles OpenWire, AMQP, MQTT et STOMP.

Son successeur technique, **Apache Artemis** (<https://artemis.apache.org/>), issu du moteur HornetQ, s'est longtemps appelé ActiveMQ Artemis. Depuis décembre 2025, c'est un projet distinct de la fondation Apache, les deux étant maintenus en parallèle. Artemis, à l'architecture asynchrone, est à étudier en priorité pour un nouveau déploiement.

## JORAM

Site
: <https://joram.ow2.io/>

Porteur
: un consortium (OW2) et un éditeur (ScalAgent)

Licence
: LGPL

JORAM (*Java Open Reliable Asynchronous Messaging*) est un intergiciel à messages écrit en Java, publié en 1999 et hébergé par le consortium OW2. Il met en œuvre JMS et prend en charge AMQP et MQTT. La société française ScalAgent continue de le maintenir, mais son usage est devenu confidentiel et se concentre sur des déploiements industriels existants : pour un nouveau projet, on évaluera plutôt RabbitMQ ou Artemis.

## RabbitMQ

Site
: <https://www.rabbitmq.com>

Porteur
: un éditeur (Broadcom, via VMware Tanzu)

Licence
: MPL 2.0

RabbitMQ est un MOM open source qui implémente le standard AMQP et propose des passerelles vers d'autres protocoles. Son architecture à plugins lui permet d'être étendu par l'ajout de nouvelles fonctionnalités.

RabbitMQ est implémenté en Erlang au-dessus de la plateforme de haute disponibilité OTP, ce qui lui confère une grande robustesse. On peut y accéder côté client dans une grande variété de langages, grâce au protocole standard AMQP, ainsi que via MQTT et STOMP. Les versions récentes ont remplacé les files miroir par les *quorum queues*, fondées sur l'algorithme de consensus Raft et ajouté les *streams* pour les usages de journalisation.

C'est aujourd'hui le courtier de messages généraliste le plus déployé, en particulier comme support de files de tâches pour les applications web (Celery, Sidekiq, Symfony Messenger…).

## Apache Kafka

Site
: <https://kafka.apache.org/>

Porteur
: une fondation (Apache)

Licence
: Apache 2.0

Créé chez LinkedIn en 2011 et confié à la fondation Apache, Kafka est devenu le standard de fait des architectures orientées événements.

Kafka n'est pas un courtier de messages au sens classique : c'est un journal distribué, répliqué et persistant. Les messages y sont conservés pendant une durée configurable et relus à volonté par des consommateurs indépendants, chacun à son rythme. Cette conception autorise des débits de plusieurs millions de messages par seconde et fait de Kafka aussi bien un bus d'intégration temps réel (avec Kafka Connect pour les connecteurs et Kafka Streams pour le traitement en flux) qu'une source de vérité pour des architectures *event sourcing*.

Les versions récentes ont supprimé la dépendance à ZooKeeper (mode KRaft), ce qui simplifie considérablement l'exploitation.

Kafka est écrit en Java et Scala.

## Autres

Parmi les produits de l’univers MOM & EAI, on peut compléter la liste avec les outils ci-dessous :

- NATS, courtier léger et très performant, projet de la CNCF: <https://nats.io/>
- Apache Pulsar, alternative à Kafka avec séparation du calcul et du stockage: <https://pulsar.apache.org/>
- ZeroMQ, bibliothèque de messagerie sans courtier: <https://zeromq.org/>
- Mosquitto, courtier MQTT de référence pour l'IoT: <https://mosquitto.org/>
- Apache Camel, pour l'intégration et le routage (section [ESB](esb.md)): <https://camel.apache.org/>

JBoss Messaging n'existe plus : son moteur a donné naissance à HornetQ, dont le code a été reversé à la fondation Apache et constitue aujourd'hui Apache Artemis.
