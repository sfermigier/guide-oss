Messagerie, Emailing & Groupware
================================

Le domaine de la « messagerie » est très large, de la messagerie individuelle à l’envoi de courriels groupés ; on y trouve de nombreuses solutions open source.

Dans cette rubrique, on présente les serveurs de messagerie (SMTP et IMAP), les outils antispam et les interfaces de consultation (groupware). Les antivirus tels que ClamAV sont rangés dans la catégorie :doc:`/infrastructure/securite`, et la messagerie instantanée fait l'objet de la section :doc:`/web-communication/messagerie-instantanee-et-visio`.

Tous ces outils sont de précieuses aides pour mettre en œuvre un système de messagerie complet.


Blue Mind
---------

:Site: https://bluemind.net/
:Porteur: un éditeur (Blue Mind)
:Licence: AGPL v3 / CeCILL v2

Blue Mind est une solution complète de messagerie d’entreprise, d’agendas et de travail collaboratif.

L'ensemble des fonctionnalités est accessible via un navigateur et supporte le mode déconnecté directement dans le navigateur sans installation de logiciels supplémentaire. Blue Mind est aussi accessible via les clients lourds de messagerie classique via les protocoles standard SMTP/POP/IMAP. Pour les logiciels Thunderbird et Outlook, Blue Mind fourni en plus des connecteurs permettant de synchroniser les contacts et calendriers (ou un accès aux calendriers pour Thunderbird). Le support de la synchronisation (push) des Smartphones (Android, Iphone, Ipad, Windows Mobile,..) est natif via le protocole Exchange ActiveSync (EAS).

BlueMind s'appuie sur des logiciels libres préexistants : Postfix, Cyrus IMAP, nginx, PostgreSQL, Elasticsearch/OpenSearch pour l'indexation. Son architecture est fondée sur des services web et un bus de messages. Le produit est l'une des rares alternatives françaises crédibles à Microsoft Exchange et fait l'objet de déploiements dans l'administration française.

Blue Mind est développé et maintenu par la société française éponyme qui travaille avec des revendeurs et des intégrateurs pour déployer la solution chez ses clients.


Postfix
-------

:Site: http://www.postfix.org/
:Porteur: une communauté
:Licence: Eclipse Public License 2.0 et IBM Public License 1.0

Postfix est un serveur de messagerie. La création de postfix remonte à 1997. Il a été développé par Wietse Venema et plusieurs contributeurs. Postfix a tout d'abord été connu sous les noms de VMailer et par la suite IBM Secure Mailer.

Remplaçant de plus en plus Sendmail au sein des infrastructures mail open source, Postfix est un serveur SMTP souple et extensible. Il est capable d'interroger un grand nombre de sources d'informations externes (base de données, annuaires LDAP). Son périmétre est relativement large et parfaitement adapté à une utilisation professionnelle. Postfix permet notamment d’éviter le spam (à partir d’une liste publique anti-spam par exemple).


Cyrus IMAPd
-----------

:Site: https://www.cyrusimap.org/
:Porteur: une communauté
:Licence: BSD

Cyrus est serveur mail extensible disponible à la fois pour un usage personnel ou professionnel. Cyrus s'appuie sur de nombreux standards et propose deux versions téléchargeables. Cyrus IMAPd, quant à lui, est un serveur IMAP libre. Le projet est issu de l'université américaine Carnegie Mellon, et remonte à 1994.

Il supporte des fonctionnalités avancées telles que le push (IDLE), les ACL, les dossiers partagés, les quotas, le filtrage côté serveur (sieve), et un grand nombre de méthodes d'authentification via SASL.


SpamAssassin
------------

:Site: https://spamassassin.apache.org/
:Porteur: une fondation (Apache)
:Licence: Apache

SpamAssassin est un antispam utilisant un grand nombre de techniques différentes. Il date de 1997 et est mené par la Apache Software Foundation, auteur du très célèbre serveur Web Apache HTTP Server.

Il s'agit d'un outil très répandu sur les serveurs de mails, y compris dans les infrastructures des grands fournisseurs. Parmi les techniques utilisées, on retrouve l'analyse Bayesienne, fondée sur l'apprentissage de mots-clés, divers systèmes de listes noires (URIBL, DNSBL), l'analyse du contenu (Razor, DCC), et un certain nombre de critères sur le formatage du message (taux images/texte, absence de version texte, émetteur invalide, etc.).

SpamAssassin est écrit en Perl.


Zimbra
------

:Site: https://www.zimbra.com
:Porteur: un éditeur (Zimbra, Inc.)
:Licence: Zimbra Public License, dérivée de la MPL, et propriétaire

Zimbra est un serveur de messagerie collaborative. Son interface utilisateur entièrement web et fondée sur AJAX est célèbre pour son ergonomie.

Toutes les fonctionnalités de Zimbra sont accessibles via un navigateur web ou un client lourd. Le Webmail de Zimbra est en effet compatible avec tout navigateur web moderne. La suite Zimbra intègre un client lourd Zimbra Desktop mais reste complètement compatible avec les clients lourds standards tels que Microsoft Outlook, Mozilla Thunderbird, Eudora, etc. Dans sa version commerciale, Zimbra se synchronise également avec la quasi totalité des plateformes mobiles (iPhone OS, Blackberry, Android, Symbian OS, Palm OS).

Cet outil de messagerie s'appuie sur un socle d'infrastructure riche et robuste : LDAP, HTTP(S), SMTP, IMAP, POP3, CalDAV, CardDAV et Exchange ActiveSync. Il fournit une API SOAP/REST permettant le développement d'extensions appelées « Zimlets ».

Zimbra est passé entre de nombreuses mains (VMware en 2010, Telligent puis Synacor en 2013) avant de redevenir en 2022 une société indépendante, Zimbra Inc. Le produit reste décliné en une édition open source (ZCS Open Source Edition) et une édition Network commerciale, cette dernière concentrant les fonctions les plus attendues en entreprise (connecteur Outlook, sauvegarde à chaud, hiérarchisation du stockage). Il faut donc vérifier avec attention le périmètre de l'édition libre avant de s'engager.


Horde
-----

:Site: https://www.horde.org/
:Porteur: une communauté
:Licence: GPL

Horde Groupware Webmail Edition est une solution professionnelle de messagerie collaborative. C'est un groupware (logiciel de groupe de travail) entièrement modulable.

Il permet aux utilisateurs de pouvoir, lire, échanger et organiser leurs emails, organiser et partager leur calendrier, contacts et tâches. Plus qu'un simple agrégat de briques techniques, Horde est une association ergonomique d'applications comme INgo, Turba, IMP, Mnemo dont l'ergonomie d'ensemble fait une messagerie collaborative fiable.

Horde est écrit en PHP.

grommunio (héritier de Zarafa et Kopano)
----------------------------------------

:Site: https://grommunio.com
:Porteur: un éditeur (grommunio GmbH)
:Licence: AGPL v3 et propriétaire

Zarafa, solution néerlandaise de messagerie collaborative connue pour sa prise en charge native du protocole MAPI et son interfaçage direct avec Outlook, a été renommée Kopano en 2016. Le site zarafa.com n'est plus en service et le développement communautaire de Kopano Core s'est arrêté au début des années 2020.

C'est aujourd'hui grommunio, projet austro-allemand lancé en 2020 et largement issu de cette lignée technique, qui reprend le flambeau de l'alternative open source à Microsoft Exchange. Il prend nativement en charge les protocoles MAPI/HTTP, Exchange ActiveSync, EWS, IMAP, CalDAV et CardDAV, connecte Outlook sans connecteur tiers, et fournit un webmail complet, la visioconférence, la messagerie instantanée et des outils de migration depuis Exchange.

grommunio est écrit en C++ et PHP et s'appuie sur MariaDB. Il est publié sous licence AGPL v3, avec une offre de souscription commerciale.

OpenEMM
-------

:Site: https://www.openemm.org/
:Porteur: un éditeur (AGNITAS AG)
:Licence: Common Public Attribution License 1.0 (CPAL)

OpenEMM est une solution d’emaling open source développée depuis 1999 par la société allemande Agintas. OpenEMM est utilisé par de grands groupes tels que BenQ, Siemens, etc.

OpenEMM est utilisé pour gérer les newsletters et les campagnes marketing par email des entreprises. Il existe peu de solutions d’emailing open source disposant d’un périmètre fonctionnel aussi large : une interface entièrement web, disponible en plusieurs langues dont le français et l’anglais, outils de ciblage, statistiques en temps réel, gestion des templates, modules d’importation et d’extraction de masse, bonne documentation, utilisation possible de webservices, gestion des erreurs de retours, etc.

OpenEMM repose sur les langages C, Java et Python. Il utilise la base de données MySQL pour le stockage de ses informations.


Autres
------

Parmi les produits de l’univers Messagerie, Emailing & Groupware, on peut compléter la liste avec les outils ci-dessous :

Webmails et groupware :

- Roundcube, rejoint en 2024 par la société Nextcloud: https://roundcube.net/
- SOGo (groupware français/canadien, CalDAV, CardDAV et ActiveSync): https://www.sogo.nu/
- EGroupware: https://www.egroupware.org/
- Open-Xchange: https://ox.io/
- SnappyMail (webmail léger): https://github.com/the-djmaze/snappymail

Serveurs et filtrage :

- Rspamd, antispam moderne souvent préféré à SpamAssassin pour ses performances: https://rspamd.com/
- Dovecot, serveur IMAP le plus déployé aujourd'hui: https://www.dovecot.org/
- Mailcow et Mailu, distributions clés en main de serveur de messagerie à base de conteneurs: https://mailcow.email/ et https://mailu.io/
- Stalwart, serveur de messagerie tout-en-un écrit en Rust: https://stalw.art/

Emailing :

- Listmonk (gestionnaire de lettres d'information et de campagnes, Go): https://listmonk.app/
- Mautic (automatisation marketing): https://www.mautic.org/

