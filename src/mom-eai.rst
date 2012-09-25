MOM & EAI
=========

Les Middleware Orientés Messages, ou « MOMs », sont des outils particulièrement précieux pour mettre en œuvre des échanges entre applications de toutes natures.

Un middleware permet à différentes applications d’échanger et d'interopérer. Un middleware permet aux applications d'interopérer y compris lorsqu'elles tournent sur des serveurs différents, interconnectés par un réseau. Le middleware est un outil de haut niveau, puisqu’il offre ses services aux applications, mais les échanges induits s’appuient sur toute une pile de protocoles réseau.

Un middleware est davantage qu'un simple protocole d'appel des services offerts par une application, et typiquement RPC, RMI ou bien SOAP, tous également synchrones, ne sont pas vraiment considérés comme des middlewares.




ActiveMQ
--------

:Version: 5.5.0
:Site: http://activemq.apache.org
:Porteur: une fondation (Apache)

Sorti en 2004, ActiveMQ est le MOM open source de la fondation Apache.

ActiveMQ s’appuie sur quelques autres projets Apache : Apache Camel (Implémentation partielle des « Entreprise Integration Patterns ») et Jetty (Serveur d'application Java intégré à ActiveMQ). Et ActiveMQ est à son tour utilisé par quelques autres grands projets : Apache Service Mix, Mule, Geronimo (comme fournisseur JMS par défaut). Le traitement des messages de ActiveMQ est sans doute son plus célèbre atout, après celui de sa grande connectivité. À l'aide du projet Camel qui est intégré, il a la possibilité de traiter les messages selon les modèles d'intégration d'entreprises (EIP).

ActiveMQ est développé en Java. La diversité des langages et environnements supportés est particulièrement grande, et c’est un des grands atouts de Active MQ. Les langages à partir desquels on peut accéder à ActiveMQ sont : C, C++, Ajax, RESTful et SOAP, .Net, Delphi, FreePascal, Perl, PHP, Pike, Python, Ruby, etc.

Il est distribué sous licence Apache 2.0.




JORAM
-----

:Version: 5.7.0
:Site: http://joram.ow2.org
:Porteur: un consortium (OW2) et un éditeur (ScalAgent)

JORAM (« Java Open Reliable Asynchronous Messaging ») est le Middleware de consortium Object Web, sortie en 1999. Object Web est aussi connu pour son serveur d'application Java nommé Jonas auquel est d'ailleurs intégré JORAM.

JORAM a une architecture interne élégante, basée sur le modèle d'agent. Un agent est un composant logiciel répondant à certains événements. Dans le cas de JORAM, les événements sont sous forme de messages. Les queues et les topics sont ainsi représentés par des agents. Un utilisateur connecté à la plateforme est également représenté par un agent dit proxy. Cette approche offre une grande flexibilité car elle permet la création et la suppression d'agents à la volée et sur n'importe quel broker.

Les langages par lesquels ont peut accéder à JORAM sont : Java (via l'interface JMS), C et C++ (à l’aide de JNI permettant ainsi de simuler un environnement JMS).

JORAM est distribué sous licence LGPL depuis mai 2000.




Autres
------

Parmi les produits de l’univers MOM & EAI, on peut compléter la liste avec les outils ci-dessous :



Nom	URL / Site web

JBoss Messaging	http://www.jboss.org/jbossmessaging

