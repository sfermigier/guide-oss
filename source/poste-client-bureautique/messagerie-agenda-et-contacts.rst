Messagerie, agenda et contacts
==============================

Cette section traite des clients installés sur le poste de travail. Les serveurs correspondants (SMTP, IMAP, groupware, antispam) font l'objet de la section :doc:`/web-communication/messagerie-email-groupware`, et la messagerie instantanée de la section :doc:`/web-communication/messagerie-instantanee-et-visio`.

Le client lourd n'a pas disparu au profit du webmail, pour trois raisons persistantes : le travail hors connexion, la manipulation d'archives volumineuses que les interfaces web traitent mal, et le chiffrement de bout en bout, qui suppose que les clés restent sur le poste.

Le point d'attention d'un déploiement est presque toujours le même : la connexion à un serveur Exchange ou à Microsoft 365. Les protocoles ouverts (IMAP, CalDAV, CardDAV) ne suffisent pas toujours, et l'authentification moderne par OAuth 2.0, désormais imposée par Microsoft, exige un client à jour et un enregistrement d'application côté annuaire. C'est à vérifier avant tout engagement.


Thunderbird
-----------

:Site: https://www.thunderbird.net/
:Porteur: une fondation (Mozilla Foundation, via MZLA Technologies)
:Licence: MPL 2.0

Mozilla Thunderbird est un client de messagerie électronique, un gestionnaire d'informations personnelles, un client NNTP, un client RSS et un client de discussion, publié sous licence libre. Son développement est assuré depuis 2020 par MZLA Technologies Corporation, filiale de la Fondation Mozilla, et financé par les dons des utilisateurs.

Après plusieurs années de stagnation, le projet a repris un rythme de publication soutenu : refonte complète de l'interface, gestion native des comptes Exchange sans connecteur tiers, prise en charge d'OAuth 2.0, moteur de recherche revu, et déclinaison mobile Thunderbird for Android issue du projet K-9 Mail.

C'est le client de référence pour un parc hétérogène : il fonctionne à l'identique sous Windows, macOS et Linux, s'administre par stratégies d'entreprise comme Firefox, gère le chiffrement OpenPGP nativement et S/MIME par certificats, et importe les archives des clients qu'il remplace. Les versions ESR conviennent aux déploiements qui doivent figer une version majeure.

Thunderbird est écrit en C++ et JavaScript.


Evolution
---------

:Site: https://wiki.gnome.org/Apps/Evolution
:Porteur: une communauté (projet GNOME), avec le soutien de Red Hat
:Licence: LGPL v2 et GPL v2

Evolution est le gestionnaire d'informations personnelles du bureau GNOME : messagerie, agenda, carnet d'adresses, tâches et mémos dans une interface unique.

Son principal atout en entreprise est le connecteur **EWS** (*Exchange Web Services*), qui lui donne accès à un serveur Exchange ou à Microsoft 365 avec les fonctions attendues d'un client natif : dossiers partagés, disponibilité des participants lors de l'organisation d'une réunion, délégation de boîte, carnet d'adresses global. C'est, de longue date, la réponse la plus complète du monde libre à cette contrainte d'intégration, ce qui en fait le choix par défaut des migrations de postes vers Linux en environnement Microsoft.

Son intégration étroite au bureau GNOME est aussi sa limite : l'expérience est moins homogène sous Windows, où Thunderbird reste préférable.

Evolution est écrit en C.


Kontact
-------

:Site: https://kontact.kde.org/
:Porteur: une communauté (projet KDE)
:Licence: GPL v2

Kontact est la suite de communication du bureau KDE Plasma, qui réunit le client de messagerie KMail, l'agenda KOrganizer, le carnet d'adresses KAddressBook et le lecteur de flux Akregator.

Elle se distingue par la finesse de son paramétrage (règles de filtrage, identités multiples, gestion avancée du chiffrement OpenPGP et S/MIME) et par son moteur de stockage Akonadi, qui mutualise l'accès aux données entre les applications du bureau. La contrepartie est une mise en œuvre plus exigeante, Akonadi étant réputé sensible aux configurations inhabituelles.

C'est le choix cohérent pour un parc standardisé sur KDE Plasma, notamment dans les administrations et les universités européennes qui ont retenu cet environnement.


Betterbird
----------

:Site: https://www.betterbird.eu/
:Porteur: une communauté
:Licence: MPL 2.0

Betterbird est un dérivé de Thunderbird qui ajoute des correctifs et des fonctionnalités que le projet amont n'a pas retenus ou n'a pas encore intégrés : affichage des dossiers, gestion des fils de discussion, options d'impression, corrections d'anomalies anciennes.

Il suit de près les versions de Thunderbird et importe les profils existants sans conversion, ce qui en fait un recours commode lorsqu'une régression de la branche principale bloque un usage précis. C'est un recours ciblé, à réserver aux utilisateurs qui en expriment le besoin.


Autres
------

- Claws Mail, client léger et très configurable, adapté aux machines modestes: https://www.claws-mail.org/
- Geary, client épuré du bureau GNOME: https://wiki.gnome.org/Apps/Geary
- DavMail, passerelle qui expose un serveur Exchange en IMAP, SMTP et CalDAV pour les clients qui ne savent pas s'y connecter directement: https://davmail.sourceforge.net/
