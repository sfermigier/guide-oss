Messagerie, Emailing & Groupware
================================

Le domaine de la « messagerie » est très large, de la messagerie individuelle à l’envoi de mailing groupé, on trouve de nombreuses solutions open source.

Dans cette rubrique, on présente les serveurs de messagerie (SMTP et IMAP), les outils Anti-spam et les interfaces de consultation (Groupware). Les anti-virus tels que  CLAV sont rangés dans la catégorie Sécurité.

Tous ces outils sont de précieuses aides pour mettre en œuvre un système de messagerie complet.


Blue Mind
---------

:Site: https://www.blue-mind.net/
:Porteur: un éditeur (Blue Mind)
:Licence: AGPL v3 / CeCILL v2

Blue Mind est une solution complète de messagerie d’entreprise, d’agendas et de travail collaboratif.

L'ensemble des fonctionnalités est accessible via un navigateur et supporte le mode déconnecté directement dans le navigateur sans installation de logiciels supplémentaire. Blue Mind est aussi accessible via les clients lourds de messagerie classique via les protocoles standard SMTP/POP/IMAP. Pour les logiciels Thunderbird et Outlook, Blue Mind fourni en plus des connecteurs permettant de synchroniser les contacts et calendriers (ou un accès aux calendriers pour Thunderbird). Le support de la synchronisation (push) des Smartphones (Android, Iphone, Ipad, Windows Mobile,..) est natif via le protocole Exchange ActiveSync (EAS).

Blue Mind s'appuie sur les logiciels libres préexistants: Postfix, cyrus IMAP, Roundcube, Apache, Tomcat, Nginx, HornetQ, PostgreSQL. L'interface utilisateur est entièrement fondée sur Ajax avec le framework Javascript Closure développé par Google. L'architecture de Blue Mind est basée sur des web services et un bus de messages.

Blue Mind est développé et supporté par la société française éponyme qui travaille avec des revendeurs et des intégrateurs pour déployer la solution chez ses clients.


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

Cyrus est serveur mail extensible disponible à la fois pour un usage personnel ou professionnel. Cyrus se base sur de nombreux standards et propose deux versions téléchargeables. Cyrus IMAPd, quant à lui, est un serveur IMAP libre. Le projet est issu de l'université américaine Carnegie Mellon, et remonte à 1994.

Il supporte des fonctionnalités avancées telles que le push (IDLE), les ACL, les dossiers partagés, les quotas, le filtrage côté serveur (sieve), et un grand nombre de méthodes d'authentification via SASL.


SpamAssassin
------------

:Site: https://spamassassin.apache.org/
:Porteur: une fondation (Apache)
:Licence: Apache

SpamAssassin est un antispam utilisant un grand nombre de techniques différentes. Il date de 1997 et est mené par la Apache Software Foundation, auteur du très célèbre serveur Web Apache HTTP Server.

Il s'agit d'un outil très répandu sur les serveurs de mails, y compris dans les infrastructures des grands fournisseurs. Parmi les techniques utilisées, on retrouve l'analyse Bayesienne, basée sur l'apprentissage de mots-clés, divers systèmes de listes noires (URIBL, DNSBL), l'analyse du contenu (Razor, DCC), et un certain nombre de critères sur le formatage du message (taux images/texte, absence de version texte, émetteur invalide, etc.).

SpamAssassin est écrit en Perl.


Zimbra
------

:Site: https://www.zimbra.com
:Porteur: un éditeur (WMware)
:Licence: Zimbra Public License, dérivée de MPL

Zimbra est un serveur de messagerie collaborative. Son interface utilisateur entièrement web et basée sur AJAX est célèbre pour son ergonomie.

Toutes les fonctionnalités de Zimbra sont accessibles via un navigateur web ou un client lourd. Le Webmail de Zimbra est en effet compatible avec tout navigateur web moderne. La suite Zimbra intègre un client lourd Zimbra Desktop mais reste complètement compatible avec les clients lourds standards tels que Microsoft Outlook, Mozilla Thunderbird, Eudora, etc. Dans sa version commerciale, Zimbra se synchronise également avec la quasi totalité des plateformes mobiles (iPhone OS, Blackberry, Android, Symbian OS, Palm OS).

Cet outil de messagerie s'appuie sur un socle infrastructure riche et robuste : WebDAV (XML), LDAP, iCal, HTTP(S), SMTP, IMAP, POP3 et CalDAV. Il fournit un socle SOAP permettant le développement de plugins appelés "Zimlets" assurant l'extension libre de son périmètre fonctionnel. Il est ainsi possible de l'interfacer avec une solution de téléphonie comme Asterisk ou un outil de CRM tel que SugarCRM. Zimbra est aujourd'hui une référence incontournable de la messagerie collaborative d'entreprise.


Horde
-----

:Site: https://www.horde.org/
:Porteur: une communauté
:Licence: GPL

Horde Groupware Webmail Edition est une solution professionnelle de messagerie collaborative. C'est un groupware (logiciel de groupe de travail) entièrement modulable.

Il permet aux utilisateurs de pouvoir, lire, échanger et organiser leurs emails, organiser et partager leur calendrier, contacts et tâches. Plus qu'un simple agrégat de briques techniques, Horde est une association ergonomique d'applications comme INgo, Turba, IMP, Mnemo dont l'ergonomie en fait une solution incontournable et fiable de messagerie collaborative.

Horde est écrit en PHP.

Zarafa
------

:Site: https://www.zarafa.com/
:Porteur: un éditeur (Zarafa)
:Licence: Affero GPL v3


Zarafa est une solution de messagerie collaborative supportant nativement le protocole MAPI. Elle est originaire des Pays-bas.

Son Webmail (entièrement accessible en Web et utilisant de l’Ajax) et son interfaçage direct avec Outlook le désigne, fonctionnellement, comme l'alternative open source la plus proche de Microsoft Exchange. Depuis 2007, le moteur de la version entreprise de Zarafa embarque le protocole Z-push assurant une compatibilité quasi totale avec les smartphones et Pocket PC du marché.

Zarafa utilise la base de données MySQL pour le stockage de ses données. Le webmail est basé sur l’Ajax avec des traitements en PHP (avec l’extension MAPI PHP).

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

- RoundCube: http://roundcube.net/
- EGroupware: http://www.egroupware.org/
- Open-Xchange: http://www.open-xchange.com/

