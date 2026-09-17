Notes, documents et synchronisation
===================================

Cette dernière section réunit les outils du travail personnel : prendre des notes, lire et annoter des documents, gérer une bibliographie, synchroniser ses fichiers entre plusieurs machines.

Ce sont les usages où le poste de travail s'échappe le plus facilement du système d'information : quand l'organisation ne fournit rien, chacun installe ce qu'il connaît, et des documents professionnels se retrouvent dans des services grand public dont personne n'a validé les conditions d'utilisation. Proposer un outil, même modeste, vaut mieux que constater l'essaimage.

Le critère commun à ces produits est la maîtrise du format et du lieu de stockage : des notes en Markdown dans un dossier synchronisé restent lisibles dans dix ans et migrables vers n'importe quel autre outil, ce qui n'est le cas d'aucune base propriétaire.


Joplin
------

:Site: https://joplinapp.org/
:Porteur: une communauté
:Licence: AGPL v3

Joplin est un gestionnaire de notes et de tâches organisé en carnets, avec des notes rédigées en **Markdown**, éventuellement chiffrées de bout en bout.

Sa force est la liberté de synchronisation : les notes se répliquent entre le poste, le téléphone et la tablette via Nextcloud, WebDAV, un partage de fichiers, S3 ou le service payant de l'éditeur : l'organisation choisit où atterrissent les données. Le greffon de capture web permet d'archiver une page complète dans un carnet, et l'import depuis Evernote ou depuis un dossier Markdown se fait sans perte.

Les applications existent pour Windows, macOS, Linux, Android et iOS, plus une interface en ligne de commande pour les usages scriptés.

Joplin est écrit en TypeScript.


Zotero
------

:Site: https://www.zotero.org/
:Porteur: une organisation à but non lucratif (Corporation for Digital Scholarship)
:Licence: AGPL v3

Zotero est le gestionnaire de références bibliographiques de référence dans le monde académique, et le seul de sa catégorie à être entièrement libre.

Il capture une référence depuis une page web, un PDF ou un identifiant (DOI, ISBN) en un clic, en extrait les métadonnées, stocke le document associé, permet de l'annoter, et génère citations et bibliographies dans plusieurs milliers de styles éditoriaux, avec des greffons pour LibreOffice Writer et Microsoft Word. Les bibliothèques de groupe permettent le travail collaboratif sur un corpus commun.

Son intérêt dépasse la recherche universitaire : tout service qui produit des rapports documentés (bureau d'études, veille réglementaire, cabinet de conseil, service juridique) y trouve un outil de gestion de sources et de citations sans équivalent libre.

Zotero est écrit en JavaScript.


Syncthing
---------

:Site: https://syncthing.net/
:Porteur: une communauté
:Licence: MPL 2.0

Syncthing synchronise des dossiers entre plusieurs machines **sans serveur central** : les appareils s'authentifient mutuellement par certificat et échangent en pair-à-pair, les données transitant chiffrées et ne séjournant sur aucune infrastructure tierce.

C'est la réponse adaptée aux cas où l'on veut la commodité de la synchronisation sans en accepter la centralisation : postes d'une même équipe, machine de bureau et portable d'un même utilisateur, sauvegarde croisée entre deux sites. Le versionnage des fichiers, la synchronisation sélective et la gestion des conflits en font un outil de travail et non un simple utilitaire.

Il ne remplace pas une plateforme collaborative comme Nextcloud (pas de partage par lien, d'édition en ligne ni de gestion centralisée des droits), mais il en est un excellent complément, et il fonctionne sur Windows, macOS, Linux, BSD et Android.

Syncthing est écrit en Go.


Okular
------

:Site: https://okular.kde.org/
:Porteur: une communauté (projet KDE)
:Licence: GPL v2

Okular est un lecteur de documents universel : PDF, mais aussi PostScript, DjVu, CHM, EPUB, ouvrages numérisés et images.

Sa fonction distinctive est l'annotation : surlignages, notes, tampons, formes géométriques et signatures, enregistrés soit dans le PDF lui-même, soit dans un fichier séparé qui laisse l'original intact. La distinction est précieuse pour annoter un document contractuel sans le modifier. Il gère également les formulaires PDF, les signatures numériques et leur vérification.

C'est un choix utile pour les postes Linux, où le lecteur PDF par défaut se limite souvent à l'affichage. Il fonctionne aussi sous Windows.

Okular est écrit en C++ (Qt).


Autres
------

- Logseq et Obsidian, pour la prise de notes en réseau ; le premier est libre (AGPL), le second gratuit mais propriétaire: https://logseq.com/
- PDF Arranger, pour réorganiser, pivoter et assembler des pages PDF: https://github.com/pdfarranger/pdfarranger
- OCRmyPDF, pour rendre cherchables des documents numérisés: https://ocrmypdf.readthedocs.io/
- Rclone, pour synchroniser avec à peu près n'importe quel stockage distant (section :doc:`/infrastructure/sauvegarde`): https://rclone.org/

Les plateformes collaboratives présentées en :doc:`/applications-generiques/ged-ecm` fournissent par ailleurs leurs propres clients de synchronisation pour le poste de travail.
