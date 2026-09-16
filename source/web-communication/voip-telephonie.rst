VOIP / Téléphonie
=================

La VOIP (« Voix sur IP ») est une technique qui permet de communiquer par la voix sur des réseaux compatible IP. Ce peut être des réseaux privés ou Internet, filaire (câble/ADSL/optique) ou non (satellite, Wifi, GSM).

Cette technologie est notamment utilisée pour supporter le service de téléphonie sur IP (« ToIP » pour Telephony over Internet Protocol).

Les meilleures solutions permettent l’interopérabilité avec des IPBX (système utilisé en entreprise qui assure l'acheminement de tout ou partie des communications) propriétaires  via les protocoles existants (H.323, SIP, IAX, MGCP) et les codecs les plus couramment utilisés (G711, G729ab, iLBC, Speex, GSM, etc.).

Au niveau des solutions open source, Asterisk est l’outil le plus utilisé et le plus complet avec de nombreuses fonctionnalités et une bonne capacité d’intégration à un environnement existant.


Asterisk
--------

:Site: https://www.asterisk.org
:Porteur: un éditeur (Sangoma)
:Licence: GPL v2

Asterisk est un autocommutateur téléphonique privé (PABX) open source pour systèmes UNIX. Il permet, entre autres, la messagerie vocale, les files d'attente, les agents d'appels, les musiques d’attente, les mises en garde d'appels, la distribution des appels et la gestion de conférences.

Asterisk implémente les protocoles SIP, WebRTC et, pour l'interconnexion avec d'autres instances, le protocole spécifique IAX (*Inter-Asterisk eXchange*) ; la prise en charge de H.323 n'est plus qu'historique. Asterisk peut également jouer le rôle de *registrar* et de passerelle avec les réseaux publics. Il est utilisé par certains opérateurs comme cœur de réseau téléphonique, du fait de son interopérabilité et de sa capacité de montée en charge, et sert fréquemment de socle aux centres d'appels, en liaison avec un CRM.

Le projet, créé par la société Digium, appartient depuis le rachat de celle-ci en 2018 au canadien Sangoma, qui édite également l'interface d'administration FreePBX (https://www.freepbx.org/). Les distributions-appliance citées dans les éditions précédentes de ce guide ont disparu : Trixbox n'est plus maintenue, et Elastix a été rachetée par 3CX en 2016 puis abandonnée en tant que produit open source — son fork communautaire, Issabel (https://www.issabel.org/), en poursuit l'esprit.


Kamailio
--------

:Site: https://www.kamailio.org/
:Porteur: une communauté
:Licence: GPL

Kamailio est un serveur SIP open source, issu du projet SER puis d'OpenSER, dont il a repris le nom en 2008. Ce n'est pas un IPBX mais un serveur SIP de classe opérateur (proxy, *registrar*, *load balancer*), capable de traiter plusieurs milliers d'appels simultanés et généralement placé en frontal d'un IPBX comme Asterisk ou FreeSWITCH.

Il prend en charge les transports UDP, TCP, TLS, SCTP et WebSocket (WebRTC), le chiffrement des communications, la répartition de charge, un mécanisme natif de bascule, ainsi que l'authentification sur des annuaires ou bases RADIUS, MySQL et LDAP. Il est utilisé aussi bien par des opérateurs télécoms comme plateforme de service VoIP que dans des architectures de téléphonie d'entreprise, le plus souvent en complément d'Asterisk ou de FreeSWITCH plutôt qu'à leur place.


FreeSWITCH
----------

:Site: https://signalwire.com/freeswitch
:Porteur: une communauté, soutenue par la société SignalWire
:Licence: MPL 1.1

Créé en 2006 par d'anciens développeurs d'Asterisk, FreeSWITCH est l'autre grande plateforme de téléphonie open source. Sa conception modulaire et son modèle de traitement multi-thread le destinent aux usages exigeants : conférences audio et vidéo de grande taille, transcodage, passerelles opérateur, plateformes de services.

Il prend en charge SIP, WebRTC, la vidéo, les principaux codecs (Opus, G.711, G.722, G.729, VP8, H.264) et s'administre par API (ESL, REST). Là où Asterisk est plus immédiat à mettre en œuvre comme IPBX d'entreprise, FreeSWITCH est souvent préféré comme brique d'infrastructure dans des architectures sur mesure.

FreeSWITCH est écrit en C.


Kannel
------

:Site: https://www.kannel.org/
:Porteur: une communauté
:Licence: Kannel Software License (basée sur la licence Apache).


Kannel a été développé à partir de 1998 par la société WAPit Ltd, qui n'existe plus ; le projet est depuis géré par « The Kannel Group ».

Kannel est une passerelle SMS et WAP de classe opérateur : elle prend en charge les protocoles SMSC standards (UCP/EMI, SMPP, HTTP, CIMD) et fournit un ensemble d'API permettant de l'utiliser comme frontal d'applications web ou de middlewares devant émettre et recevoir des SMS. Le volet WAP n'a plus qu'un intérêt historique, et le développement du projet est aujourd'hui très ralenti ; pour un nouveau projet, on évaluera aussi Jasmin (https://github.com/jookies/jasmin), passerelle SMPP écrite en Python.

Kannel est écrit en C.


Autres
------

Parmi les produits de l’univers VOIP/Téléphonie, on peut compléter la liste avec les outils ci-dessous :

- FreePBX, l'interface d'administration de référence pour Asterisk: https://www.freepbx.org/
- Issabel, distribution IPBX clés en main héritière d'Elastix: https://www.issabel.org/
- Wazo Platform, plateforme française issue du projet XiVO: https://wazo-platform.org/
- OpenSIPS, serveur SIP proche de Kamailio: https://opensips.org/
- Yate: https://yate.ro/

Pour la visioconférence et la messagerie instantanée, qui relèvent désormais du même besoin métier, voir la section :doc:`/web-communication/messagerie-instantanee-et-visio`.
