VOIP / Téléphonie
=================

La VOIP (« Voix sur IP ») est une technique qui permet de communiquer par la voix sur des réseaux compatible IP. Ce peut être des réseaux privés ou Internet, filaire (câble/ADSL/optique) ou non (satellite, Wifi, GSM).

Cette technologie est notamment utilisée pour supporter le service de téléphonie sur IP (« ToIP » pour Telephony over Internet Protocol).

Les meilleures solutions permettent l’interopérabilité avec des IPBX (système utilisé en entreprise qui assure l'acheminement de tout ou partie des communications) propriétaires  via les protocoles existants (H.323, SIP, IAX, MGCP) et les codecs les plus couramment utilisés (G711, G729ab, iLBC, Speex, GSM, etc.).

Au niveau des solutions open source, Asterisk est l’outil le plus utilisé et le plus complet avec de nombreuses fonctionnalités et une bonne capacité d’intégration à un environnement existant.


Asterisk
--------

:Site: https://www.asterisk.org
:Porteur: un éditeur (Digium)
:Licence: GPL

Asterisk est un autocommutateur téléphonique privé (PABX) open source pour systèmes UNIX. Il permet, entre autres, la messagerie vocale, les files d'attente, les agents d'appels, les musiques d’attente, les mises en garde d'appels, la distribution des appels et la gestion de conférences.

Asterisk implémente les protocoles H.320, H.323 et SIP, ainsi qu'un protocole spécifique nommé IAX (Inter-Asterisk eXchange). Asterisk peut également jouer le rôle de registrar et de passerelle avec les réseaux publics. Il est utilisé par certains opérateurs comme coeur de réseau téléphonique du fait de son intéropérabilité et de sa scalabilité. Associé à SugarCRM ou Vtiger on le retrouve également souvent comme outil de gestion de centre d'appels.

Dans son utilisation classique comme plateforme de téléphonie IP, Asterisk est généralement associé à Freepbx, une IHM permettant de piloter l'ensemble des ses fonctionnalités. On retrouve Asterisk et Freepbx  dans de nombreuses distributions-appliance dont les plus populaires sont Elastix et Trixbox.


Kamailio
--------

:Site: https://www.kamailio.org/
:Porteur: une communauté
:Licence: GPL

Kamailio est un Server SIP open source. Ce fork du projet OpenSER (en 2005) est l'un des PBX les plus complets.

Il supporte des transactions asynchrones TCP, UDP et SCTP, l'encryptage des communications via TLS, la répartition de charge, un mécanisme natif de fail-over, l'authentification sur des backend Radius, Mysql, LDAP ou via transport XMLRCP. Il est utilisé aussi bien par des opérateurs télécoms comme plate-forme de service VoIP que pour les solutions classiques de téléphonie d'entreprise. C'est une alternative à Freeswitch et Asterisk les deux autres poids lourds du domaine.


Kannel
------

:Site: https://www.kannel.org/
:Porteur: une communauté
:Licence: Kannel Software License (basée sur la licence Apache).


Kannel a été développé en 1998 par la société WAPit Ltd qui n’existe plus à ce jour. Le projet est désormais géré par les membres d’un groupe (« The Kannel Group ») qui inclut de grandes entreprises.

Kannel est une Gateway SMS et WAP Open Source Carrier Grade, elle supporte les protocoles des SMSC standard : UCP/EMI, SMPP, HTTP, CIMD. Kannel fournit un ensemble d'API lui permettant d'être utilisée comme front end à des middlewares ou applications Web nécessitant des sorties WAP ou SMS. Intégrée comme brique d'infrastructure, elle sécurise l'accès aux ressources des opérateurs tout en fournissant un support SMS et WAP fiable et robuste.

Kannel est écrit en C.


Autres
------

Parmi les produits de l’univers VOIP/Téléphonie, on peut compléter la liste avec les outils ci-dessous :

- sipXecs: http://www.sipfoundry.org
- Yate: http://www.yate.ro/
- FreeSwitch: http://www.freeswitch.org
