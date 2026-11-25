# Serveurs de messagerie

Un service de courriel assemble plusieurs composants : un serveur SMTP qui reçoit et achemine les messages, un serveur IMAP qui donne accès aux boîtes et un filtrage des messages indésirables. Cette page présente ces briques. Les suites complètes, les webmails et les outils d’emailing figurent à la page [Messagerie, emailing et groupware](../web-communication/messagerie-email-groupware.md), les antivirus à la page [Sécurité](securite.md).

Administrer un serveur de courriel demande un suivi régulier : authentification des envois (SPF, DKIM, DMARC), réputation des adresses IP, filtrage, sauvegarde des boîtes.

## Postfix

Site
: <http://www.postfix.org/>

Porteur
: une communauté

Licence
: Eclipse Public License 2.0 et IBM Public License 1.0

Postfix est un serveur de messagerie. La création de Postfix remonte à 1997. Il a été développé par Wietse Venema et plusieurs contributeurs. Postfix a tout d'abord été connu sous les noms de VMailer et par la suite IBM Secure Mailer.

Remplaçant de plus en plus Sendmail au sein des infrastructures mail open source, Postfix est un serveur SMTP souple et extensible. Il est capable d'interroger un grand nombre de sources d'informations externes (base de données, annuaires LDAP). Son périmètre est relativement large et parfaitement adapté à une utilisation professionnelle. Postfix permet notamment d’éviter le spam (à partir d’une liste publique anti-spam par exemple).

## Dovecot

Site
: <https://www.dovecot.org/>

Porteur
: un éditeur (Open-Xchange) et une communauté

Licence
: LGPL v2.1 et MIT pour certaines bibliothèques

Dovecot est un serveur IMAP et POP3 créé en 2002 par Timo Sirainen. C'est le serveur IMAP libre le plus répandu et le compagnon habituel de Postfix, auquel il fournit aussi l'authentification SASL et la remise locale (LMTP).

Il gère les formats de boîtes Maildir, mbox et dbox, l'authentification LDAP, SQL, PAM ou OAuth2, les quotas, les listes de contrôle d'accès et les dossiers partagés. Le projet associé Pigeonhole ajoute le filtrage côté serveur (Sieve). La plupart des distributions de messagerie libres, comme mailcow et Mailu, s'appuient sur lui.

Dovecot est développé par Open-Xchange, qui vend une édition Pro distincte. La version 2.4 de l'édition communautaire a retiré le *director* et la réplication entre serveurs : les architectures qui en dépendaient doivent s'appuyer sur un stockage partagé ou évoluer. La syntaxe de configuration a aussi changé entre les versions 2.3 et 2.4.

Dovecot est écrit en C.

## SpamAssassin

Site
: <https://spamassassin.apache.org/>

Porteur
: une fondation (Apache)

Licence
: Apache

SpamAssassin est un antispam utilisant un grand nombre de techniques différentes. Il date de 1997 et est mené par l'Apache Software Foundation.

Il s'agit d'un outil très répandu sur les serveurs de mails, y compris dans les infrastructures des grands fournisseurs. Parmi les techniques utilisées, on retrouve l'analyse bayésienne, fondée sur l'apprentissage de mots-clés, divers systèmes de listes noires (URIBL, DNSBL), l'analyse du contenu (Razor, DCC) et un certain nombre de critères sur le formatage du message (taux images/texte, absence de version texte, émetteur invalide, etc.).

SpamAssassin est écrit en Perl.

## Autres

- Rspamd, antispam moderne souvent préféré à SpamAssassin pour ses performances: <https://rspamd.com/>
- Mailcow et Mailu, distributions clés en main de serveur de messagerie à base de conteneurs: <https://mailcow.email/> et <https://mailu.io/>
- Stalwart, serveur de messagerie tout-en-un écrit en Rust: <https://stalw.art/>
