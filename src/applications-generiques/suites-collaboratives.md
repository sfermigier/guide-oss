# Suites collaboratives

Une suite collaborative réunit le partage de fichiers, l’édition simultanée de documents et, selon les produits, l’agenda, les discussions ou les formulaires. Elle concurrence directement Microsoft 365 et Google Workspace et concentre une grande partie des données de l’organisation.

Trois questions guident le choix : la fidélité aux formats de bureautique existants, le niveau de confidentialité attendu (un chiffrement de bout en bout limite les traitements possibles sur le serveur) et l’intégration avec l’annuaire, la messagerie et l’archivage. L’éditeur en ligne et l’espace de stockage sont souvent deux logiciels distincts : Nextcloud, par exemple, s’associe à Collabora Online ou à ONLYOFFICE.

Les applications installées sur le poste sont traitées dans [Suites bureautiques](../poste-client-bureautique/suites-bureautiques.md) ; la gestion documentaire l’est dans [GED et ECM](ged-ecm.md).

## Nextcloud

Site
: <https://nextcloud.com/>

Porteur
: un éditeur (Nextcloud GmbH)

Licence
: AGPL v3

Nextcloud a été lancé en juin 2016 par Frank Karlitschek, fondateur d’ownCloud, avec une partie de l’équipe de ce projet. La société éditrice est allemande.

La plateforme couvre la synchronisation et le partage de fichiers, les agendas, les contacts, la visioconférence (Talk) et l’édition en ligne grâce à un moteur tiers. Un catalogue d’applications étend ce périmètre.

L’éditeur vend du support et des services aux entreprises. Le nombre d’applications installées pèse sur les mises à niveau : chaque module se vérifie (mainteneur, compatibilité) avant adoption. Nextcloud est écrit principalement en PHP.

## Collabora Online

Site
: <https://www.collaboraonline.com/>

Porteur
: un éditeur (Collabora Productivity)

Licence
: MPL 2.0

Collabora Online est un éditeur collaboratif dans le navigateur, construit sur la technologie de LibreOffice. Il traite les textes, les tableurs et les présentations aux formats OpenDocument et Microsoft Office.

Il ne stocke pas les fichiers lui-même : il s’intègre, par le protocole WOPI, à une plateforme comme Nextcloud ou à une GED. Le rendu a lieu sur le serveur, ce qui impose de dimensionner la mémoire et le processeur en fonction du nombre de fichiers ouverts.

L’édition de développement (CODE) est destinée à l’essai et aux petits usages ; l’éditeur réserve son support à l’édition commerciale. Le logiciel est écrit en C++ et JavaScript.

## ONLYOFFICE Docs

Site
: <https://www.onlyoffice.com/>

Porteur
: un éditeur (Ascensio System SIA)

Licence
: AGPL v3 (édition Community) et propriétaire

ONLYOFFICE Docs est un éditeur en ligne de textes, tableurs, présentations, formulaires et PDF, conçu autour des formats de Microsoft Office. Il s’intègre à un espace documentaire existant par connecteur.

L’édition Community et les offres commerciales diffèrent par leurs fonctions et leur support. L’éditeur est une société lettonne.

Le projet a fait l’objet en mars 2026 d’un fork, **Euro-Office** (<https://github.com/Euro-Office>, AGPL v3), lancé par plusieurs acteurs européens dont Nextcloud et IONOS. L’éditeur a contesté sa conformité au regard de clauses ajoutées à l’AGPL, que la Free Software Foundation a critiquées. Ce point de gouvernance est à examiner avant d’engager un projet.

## CryptPad

Site
: <https://cryptpad.org/>

Porteur
: une entreprise (XWiki SAS)

Licence
: AGPL v3

CryptPad est une suite collaborative chiffrée de bout en bout, développée à Paris par XWiki SAS. Le serveur ne dispose pas des clés permettant de lire les documents.

Elle propose texte, tableur, présentation, code, tableau Kanban, formulaires et espace de stockage. Son modèle convient aux documents sensibles et aux groupes qui n’accordent pas leur confiance à l’hébergeur.

La contrepartie est que la perte du mot de passe peut entraîner celle des données et que la recherche ou l’indexation côté serveur sont limitées. CryptPad est écrit en JavaScript.

## Docs (La Suite)

Site
: <https://lasuite.numerique.gouv.fr/produits/docs>

Porteur
: une administration (DINUM)

Licence
: MIT

Docs est l’outil de rédaction collaborative de La Suite, l’espace de travail de l’État français porté par la direction interministérielle du numérique. Il privilégie les contenus structurés et le travail à plusieurs dans le navigateur.

Le service est destiné aux agents publics, mais le code (<https://github.com/suitenumerique/docs>) peut être hébergé par d’autres organisations. Docs est orienté notes et pages de travail : il complète une suite bureautique plus qu’il ne reproduit un traitement de texte mis en page.

Avant l’auto-hébergement, il faut prévoir un fournisseur d’identité OpenID Connect et les services associés. Docs est écrit en TypeScript et Python.

## Grist

Site
: <https://www.getgrist.com/>

Porteur
: un éditeur (Grist Labs)

Licence
: Apache 2.0 (grist-core) et propriétaire

Grist réunit tableur et base de données relationnelle : les feuilles deviennent des tables typées, reliées, avec des formules en Python, des vues et des droits d’accès détaillés.

La DINUM et l’ANCT contribuent au code. Grist fait partie des outils de La Suite. Il remplace utilement les classeurs partagés qui servent de petites applications métier.

La société Grist Labs, fondée en 2014, est américaine. Certaines fonctions sont réservées à l’édition commerciale. Grist est écrit en TypeScript et Python.

## Autres

Plateformes complètes :

- openDesk, suite assemblée pour l’administration allemande : <https://www.opendesk.eu/>

Sondages de rendez-vous :

- Framadate, créé par l’association Framasoft : <https://framadate.org/>
- Rallly (AGPL v3) : <https://rallly.co/>
