Messagerie, Emailing & Groupware
================================

Le domaine de la « messagerie » est très large, de la messagerie individuelle à l’envoi de mailing groupé, on trouve de nombreuses solutions open source.

Dans cette rubrique, on présente les serveurs de messagerie (SMTP et IMAP), les outils Anti-spam et les interfaces de consultation (Groupware). Les anti-virus tels que  CLAV sont rangés dans la catégorie Sécurité.

Tous ces outils sont de précieuses aides pour mettre en œuvre un système de messagerie complet.



Compte de tenu de la diversité des outils sélectionnés dans cette catégorie, les graphiques suivants ne présentent pas de moyenne.






Postfix
-------

:Version: 2.8.5
:Site: www.postfix.org
:Porteur: une communauté

Postfix est un serveur de messagerie. La création de postfix remonte à 1997. Il a été développé par Wietse Venema et plusieurs contributeurs. Postfix a tout d'abord été connu sous les noms de VMailer et par la suite IBM Secure Mailer.

Remplaçant de plus en plus Sendmail au sein des infrastructures mail open source, Postfix est un serveur SMTP souple et extensible. Il est capable d'interroger un grand nombre de sources d'informations externes (base de données, annuaires LDAP). Son périmétre est relativement large et parfaitement adapté à une utilisation professionnelle. Postfix permet notamment d’éviter le spam (à partir d’une liste publique anti-spam par exemple).

Postfix est distribué sous licence IBM.




Cyrus IMAPd
-----------

:Version: 2.4.10
:Site: www.cyrusimap.org
:Porteur: une communauté

Cyrus est serveur mail extensible disponible à la fois pour un usage personnel ou professionnel. Cyrus se base sur de nombreux standards et propose deux versions téléchargeables. Cyrus IMAPd, quant à lui, est un serveur IMAP libre. Le projet est issu de l'université américaine Carnegie Mellon, et remonte à 1994.

Il supporte des fonctionnalités avancées telles que le push (IDLE), les ACL, les dossiers partagés, les quotas, le filtrage côté serveur (sieve), et un grand nombre de méthodes d'authentification via SASL.

Cyrus IMAPd est distribué sous licence BSD.




SpamAssassin
------------

:Version: 3.3.2
:Site: http://spamassassin.apache.org
:Porteur: une communauté

SpamAssassin est un antispam utilisant un grand nombre de techniques différentes. Il date de 1997 et est mené par la Apache Software Foundation, auteur du très célèbre serveur Web Apache HTTP Server.

Il s'agit d'un outil très répandu sur les serveurs de mails, y compris dans les infrastructures des grands fournisseurs. Parmi les techniques utilisées, on retrouve l'analyse Bayesienne, basée sur l'apprentissage de mots-clés, divers systèmes de listes noires (URIBL, DNSBL), l'analyse du contenu (Razor, DCC), et un certains nombre de critères sur le formatage du message (taux images/texte, absence de version texte, émetteur invalide, etc.).

SpamAssassin est disponible sous licence Apache.

SpamAssassin est écrit en Perl.




DSPAM
-----

:Version: 3.10.1
:Site: www.nuclearelephant.com
:Porteur: une communauté

DSPAM est un antispam basé sur le filtrage Bayesien, écrit par Jonathan A. Zdziarski, également auteur du livre Ending Spam.

Ce type de filtrage, basé sur l'apprentissage de mot-clés, s'avère particulièrement efficace après une phase d'entrainement. Le principal intérêt de DSPAM par rapport à ses concurrents réside dans la richesse de son moteur d'analyse, ainsi que dans l'interaction avec l'utilisateur, qui dispose d'une interface web pour gérer la quarantaine, et désigner explicitement un mail comme désirable ou indésirable.

DSPAM est distribué sous licence GPL.




Zimbra
------

:Version: 7.1.1
:Site: www.zimbra.com
:Porteur: un éditeur (WMware)

Zimbra est un serveur de messagerie collaborative. Son interface utilisateur entièrement web et basée sur AJAX est célèbre pour son ergonomie.

Toutes les fonctionnalités de Zimbra sont accessibles via un navigateur web ou un client lourd. Le Webmail de Zimbra est en effet compatible avec tout navigateur web moderne. La suite Zimbra intègre un client lourd Zimbra Desktop mais reste complètement compatible avec les clients lourds standards tels que Microsoft Outlook, Mozilla Thunderbird, Eudora, etc. Dans sa version commerciale, Zimbra se synchronise également avec la quasi totalité des plateformes mobiles (iPhone OS, Blackberry, Android, Symbian OS, Palm OS).

Zimbra est publié sous la licence « Zimbra Public License », dérivé de MPL.

Cet outil de messagerie s'appuie sur un socle infrastructure riche et robuste : WebDAV (XML), LDAP, iCal, HTTP(S), SMTP, IMAP, POP3 et CalDAV. Il fournit un socle SOAP permettant le développement de plugins appelés "Zimlets" assurant l'extension libre de son périmètre fonctionnel. Il est ainsi possible de l'interfacer avec une solution de téléphonie comme Asterisk ou un outil de CRM tel que SugarCRM. Zimbra est aujourd'hui une référence incontournable de la messagerie collaborative d'entreprise.




Horde
-----

:Version: 4.0.8
:Site: www.horde.org
:Porteur: une communauté

Horde Groupware Webmail Edition est une solution professionnelle de messagerie collaborative. C'est un groupware (logiciel de groupe de travail) entièrement modulable.

Il permet aux utilisateurs de pouvoir, lire, échanger et organiser leurs emails, organiser et partager leur calendrier, contacts et tâches. Plus qu'un simple agrégat de briques techniques, Horde est une association ergonomique d'applications comme INgo, Turba, IMP, Mnemo dont l'ergonomie en fait une solution incontournable et fiable de messagerie collaborative.

Horde est distribué sous la licence GPL.

Horde est écrit en PHP.




Zarafa
------

:Version: 7.0.1
:Site: www.zarafa.com
:Porteur: un éditeur (Zarafa)

Zarafa est une solution de messagerie collaborative supportant nativement le protocole MAPI. Elle est originaire des Pays-bas.

Son Webmail (entièrement accessible en Web et utilisant de l’Ajax) et son interfaçage direct avec Outlook le désigne, fonctionnellement, comme l'alternative open source la plus proche de Microsoft Exchange. Depuis 2007, le moteur de la version entreprise de Zarafa embarque le protocole Z-push assurant une compatibilité quasi totale avec les smartphones et Pocket PC du marché.

Zarafa est distribué sous la licence Affero GPL v3.

Zarafa utilise la base de données MySQL pour le stockage de ses données. Le webmail est basé sur l’Ajax avec des traitements en PHP (avec l’extension MAPI PHP).




OpenEMM
-------

:Version: OpenEMM 2011
:Site: www.openemm.org
:Porteur: un éditeur (AGNITAS AG)

OpenEMM est une solution d’emaling open source développée depuis 1999 par la société allemande Agintas. OpenEMM est utilisé par de grands groupes tels que BenQ, Siemens, etc.

OpenEMM est utilisé pour gérer les newsletters et les campagnes marketing par email des entreprises. Il existe peu de solutions d’emailing open source disposant d’un large périmètre ce pourquoi, OpenEMM a toute sa place dans ce guide open source. D’un point de vue fonctionnel, l’outil est relativement riche. Citons par exemple : une interface entièrement web, disponible en plusieurs langues dont le français et l’anglais, outils de ciblage, statistiques en temps réel, gestion des templates, modules d’importation et d’extraction de masse, bonne documentation, utilisation possible de webservices, gestion des erreurs de retours, etc.

OpenEMM est distribué sous la licence « Common Public Attribution License » 1.0 (CPAL).

OpenEMM repose sur les langages C, Java et Python. Il utilise la base de données MySQL pour le stockage de ses informations.Autres

Parmi les produits de l’univers Messagerie, Emailing & Groupware, on peut compléter la liste avec les outils ci-dessous :



Nom	URL / Site web

RoundCube	http://roundcube.net

EGroupware	http://www.egroupware.org

OBM	http://obm.org

Open-Xchange	http://www.open-xchange.com

