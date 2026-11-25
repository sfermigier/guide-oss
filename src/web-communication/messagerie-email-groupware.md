# Messagerie, emailing et groupware { #messagerie-emailing-groupware }

Le domaine de la « messagerie » est très large, de la messagerie individuelle à l’envoi de courriels groupés ; on y trouve de nombreuses solutions open source.

Cette page présente les suites de messagerie collaborative, les webmails et les outils d’envoi de courriels groupés. Les serveurs SMTP et IMAP et les antispams sont traités à la page [Serveurs de messagerie](../infrastructure/serveurs-messagerie.md), la messagerie instantanée à la page [Messagerie instantanée et visioconférence](messagerie-instantanee-et-visio.md).

## BlueMind { #blue-mind }

Site
: <https://bluemind.net/>

Porteur
: un éditeur (BlueMind)

Licence
: AGPL v3

BlueMind est une solution complète de messagerie d’entreprise, d’agendas et de travail collaboratif, développée par l’éditeur français du même nom et déployée notamment dans l'administration.

Elle s'utilise depuis un navigateur, depuis Thunderbird et depuis Outlook. La version 5 prend ce dernier en charge sans extension, par l'implémentation des protocoles Exchange (MAPI) côté serveur. Les mobiles se synchronisent par les protocoles standard du domaine.

BlueMind s'appuie sur des logiciels libres préexistants (Postfix, nginx, PostgreSQL). Jusqu'à la version 4, le stockage du courrier reposait sur Cyrus IMAP ; la version 5 l'a remplacé par un composant propre, capable de placer les messages sur un stockage objet. Le code est publié sous AGPL v3, l'éditeur commercialisant souscriptions et services avec un réseau d'intégrateurs : on vérifiera les conditions d'accès aux binaires et aux outils de mise à jour.

## Zimbra

Site
: <https://www.zimbra.com>

Porteur
: un éditeur (Synacor)

Licence
: GPL v2 pour le serveur, CPAL 1.0 pour le client web, propriétaire pour l'édition Network

Zimbra est une suite de messagerie collaborative apparue en 2005 : courriel, agendas, carnets d'adresses, tâches et partage de fichiers, derrière un webmail. Elle est compatible avec les clients IMAP, CalDAV et CardDAV ; l'édition commerciale y ajoute la synchronisation mobile et un connecteur Outlook. Son API SOAP/REST permet d'écrire des extensions, les « Zimlets ».

Passé par Yahoo!, VMware puis Telligent, Zimbra a été racheté en 2015 par l'américain Synacor. L'éditeur présente l'édition open source comme en fin de vie, sans mises à jour ni support. Elle n'est plus distribuée sous forme de binaires officiels depuis la fin de la branche 8.8.15 : il faut la compiler à partir du dépôt zm-build (<https://github.com/Zimbra/zm-build>) ou recourir à des paquets tiers. Ce point, joint à la fréquence des failles de sécurité exploitées sur le produit, doit peser dans le choix d'un nouveau déploiement.

Zimbra est écrit en Java pour l'essentiel du serveur.

## Horde

Site
: <https://www.horde.org/>

Porteur
: une communauté

Licence
: GPL

Horde Groupware Webmail Edition est une solution professionnelle de messagerie collaborative. C'est un groupware (logiciel de groupe de travail) entièrement modulable.

Il permet aux utilisateurs de pouvoir, lire, échanger et organiser leurs emails, organiser et partager leur calendrier, contacts et tâches. Plus qu'un simple agrégat de briques techniques, Horde est une association ergonomique d'applications comme INgo, Turba, IMP, Mnemo dont l'ergonomie d'ensemble fait une messagerie collaborative fiable.

Horde est écrit en PHP.

## grommunio (héritier de Zarafa et Kopano)

Site
: <https://grommunio.com>

Porteur
: un éditeur (grommunio GmbH)

Licence
: AGPL v3 (souscription commerciale pour le support)

Zarafa, solution néerlandaise de messagerie collaborative connue pour sa prise en charge native du protocole MAPI et son interfaçage direct avec Outlook, a été renommée Kopano en 2016. Le site zarafa.com n'est plus en service et le développement communautaire de Kopano Core s'est arrêté au début des années 2020.

C'est aujourd'hui grommunio, projet austro-allemand lancé en 2020 et largement issu de cette lignée technique, qui reprend le flambeau de l'alternative open source à Microsoft Exchange. Il prend nativement en charge les protocoles MAPI/HTTP, Exchange ActiveSync, EWS, IMAP, CalDAV et CardDAV et connecte Outlook sans connecteur tiers. Il fournit un webmail complet, la visioconférence, la messagerie instantanée et des outils de migration depuis Exchange.

grommunio est écrit en C++ et PHP et s'appuie sur MariaDB. Il est publié sous licence AGPL v3, avec une offre de souscription commerciale.

## OpenEMM

Site
: <https://www.agnitas.de/en/e-marketing_manager/email-marketing-software-variants/openemm/>

Porteur
: un éditeur (AGNITAS AG)

Licence
: AGPL v3

OpenEMM est une solution d’emailing développée par la société allemande AGNITAS. C'est l'édition libre de son produit commercial E-Marketing Manager.

Elle gère les lettres d'information et les campagnes : interface web multilingue, ciblage, statistiques, gabarits, import et export de destinataires, services web, traitement des retours en erreur.

OpenEMM est écrit principalement en Java, avec des composants en C et en Python. Il s'appuie sur une base MySQL ou MariaDB.

<span id="cyrus-imapd"></span>

## Autres

Parmi les produits de l’univers Messagerie, Emailing & Groupware, on peut compléter la liste avec les outils ci-dessous :

Webmails et groupware :

- Roundcube, rejoint en 2024 par la société Nextcloud: <https://roundcube.net/>
- SOGo (groupware français/canadien, CalDAV, CardDAV et ActiveSync): <https://www.sogo.nu/>
- EGroupware: <https://www.egroupware.org/>
- Open-Xchange: <https://ox.io/>
- SnappyMail (webmail léger): <https://github.com/the-djmaze/snappymail>

Serveurs et filtrage (page [Serveurs de messagerie](../infrastructure/serveurs-messagerie.md)) :

- [Postfix](../infrastructure/serveurs-messagerie.md#postfix){ #postfix }
- [Dovecot](../infrastructure/serveurs-messagerie.md#dovecot){ #dovecot }
- [SpamAssassin](../infrastructure/serveurs-messagerie.md#spamassassin){ #spamassassin }

Emailing :

- Listmonk (gestionnaire de lettres d'information et de campagnes, Go): <https://listmonk.app/>
- Mautic (automatisation marketing): <https://www.mautic.org/>
