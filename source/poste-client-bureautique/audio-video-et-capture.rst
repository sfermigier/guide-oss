Audio, vidéo et capture
=======================

La vidéo est devenue un outil de travail courant : tutoriels internes, captations de réunions, webinaires, formation à distance, communication externe. Les organisations qui produisaient une plaquette produisent aujourd'hui une vidéo, et l'outillage correspondant a quitté les services de communication pour se répandre dans les équipes.

Ce domaine est, avec les serveurs web, l'un de ceux où l'open source domine : les bibliothèques qui décodent les formats vidéo, FFmpeg au premier chef, sont utilisées par la quasi-totalité des logiciels du marché, y compris propriétaires, et les outils de diffusion en direct sont devenus des standards professionnels.

Un rappel utile en matière de conformité : la captation d'une réunion ou d'une formation est un traitement de données personnelles, qui suppose information des participants, base légale et durée de conservation définie. Le choix d'un outil auto-hébergé simplifie ce volet, mais ne l'épuise pas.


VLC
---

:Site: https://www.videolan.org/
:Porteur: une association française (VideoLAN)
:Licence: GPL v2 et LGPL v2.1

VLC est le lecteur multimédia le plus déployé au monde, toutes catégories confondues, avec plusieurs milliards de téléchargements. Né en 1996 d'un projet étudiant de l'École centrale Paris, il est aujourd'hui porté par l'association VideoLAN, l'un des plus beaux succès du logiciel libre français.

Sa réputation tient à une qualité simple : il lit à peu près tout, sans installation de codecs supplémentaires, sur à peu près tout : Windows, macOS, Linux, Android, iOS, et jusqu'aux téléviseurs et aux systèmes embarqués. Il assure également la conversion de formats, la capture d'écran, la diffusion en flux sur un réseau et la lecture de flux distants, ce qui en fait aussi un outil d'infrastructure pour la diffusion interne.

La bibliothèque libVLC, sous licence LGPL, permet d'intégrer ces capacités dans une application tierce.

VLC est écrit en C.


FFmpeg
------

:Site: https://ffmpeg.org/
:Porteur: une communauté
:Licence: LGPL v2.1 et GPL v2

FFmpeg est la bibliothèque et la boîte à outils en ligne de commande sur lesquelles repose presque tout le reste : les autres produits de cette section, les plateformes de diffusion, les navigateurs, les logiciels de montage professionnels et les services de vidéo en ligne l'utilisent pour décoder, encoder et transformer les flux audio et vidéo.

Pour une organisation, son intérêt direct est l'automatisation : convertir un lot de captations au format de diffusion, extraire la bande son d'une réunion, normaliser le volume, générer des vignettes ou des sous-titres, redimensionner une vidéothèque. Toutes ces opérations se scriptent en quelques lignes et s'intègrent à une chaîne de traitement.

C'est l'un des projets dont la disparition paralyserait une large part de l'industrie audiovisuelle, ce qui rend d'autant plus notable la modestie de ses moyens : le sujet du financement des briques critiques du logiciel libre y trouve un cas d'école.

FFmpeg est écrit en C.


OBS Studio
----------

:Site: https://obsproject.com/
:Porteur: une communauté (OBS Project)
:Licence: GPL v2

OBS Studio (*Open Broadcaster Software*) est l'outil de référence pour la captation d'écran et la diffusion en direct. Il s'est imposé au point de devenir le standard de fait des plateformes de diffusion, propriétaires comprises.

Son principe est celui d'une régie : on compose des scènes à partir de sources (capture d'écran ou de fenêtre, webcam, image, texte, navigateur, flux distant), on bascule de l'une à l'autre en direct, avec transitions, incrustations, filtres, mixage audio multipiste et contrôle du niveau. Le résultat s'enregistre localement ou se diffuse vers n'importe quel service compatible RTMP.

Ses usages en entreprise vont bien au-delà de la diffusion publique : enregistrement de tutoriels internes, captation d'un poste pour une démonstration, alimentation d'une visioconférence avec une source composée, webinaires. Il est extensible par greffons et scriptable en Lua et Python.

OBS Studio est écrit en C et C++.


Kdenlive
--------

:Site: https://kdenlive.org/
:Porteur: une communauté (projet KDE)
:Licence: GPL v3

Kdenlive est le logiciel de montage vidéo non linéaire du projet KDE, et le plus abouti des monteurs libres multiplateformes.

Il offre ce qu'on attend d'un monteur : pistes vidéo et audio illimitées, montage à trois points, effets et transitions, étalonnage, incrustation sur fond vert, titrage, proxy pour travailler sur des rushes lourds, rendu vers les formats courants. Sa gestion de projet (conservation des chutiers, sauvegarde automatique, récupération après incident) le rend utilisable sur des travaux de plusieurs heures de rushes.

C'est le choix pertinent pour un service communication qui monte régulièrement des vidéos de format court à moyen. Pour la postproduction cinéma, on regardera plutôt du côté de DaVinci Resolve, gratuit mais propriétaire.

Kdenlive est écrit en C++ (Qt) et s'appuie sur le framework MLT.


Audacity
--------

:Site: https://www.audacityteam.org/
:Porteur: une entreprise (Muse Group)
:Licence: GPL v3

Audacity est l'éditeur audio multipiste le plus répandu : enregistrement, découpe, mixage, réduction de bruit, normalisation, export vers les formats courants. C'est l'outil qu'on emploie pour nettoyer une captation de réunion, produire un podcast interne ou préparer une bande son.

Son histoire récente compte avant tout déploiement : après le rachat du projet par Muse Group en 2021, l'annonce de l'ajout de télémétrie et la modification des conditions d'utilisation ont provoqué une rupture avec une partie de la communauté, et la création du fork **Tenacity** (https://tenacityaudio.org/). L'éditeur est largement revenu sur ces décisions, la télémétrie étant désormais optionnelle et désactivée par défaut, mais les organisations sensibles à ce point préféreront Tenacity, qui s'en tient au périmètre historique du logiciel.

Audacity est écrit en C++.


Autres
------

- HandBrake, conversion et compression de fichiers vidéo par lots: https://handbrake.fr/
- Shotcut, monteur vidéo simple et multiplateforme, également fondé sur MLT: https://shotcut.org/
- Ardour, station de travail audio numérique pour l'enregistrement et le mixage professionnels: https://ardour.org/
- Whisper.cpp et WhisperX, pour la transcription et le sous-titrage automatiques de captations: https://github.com/ggml-org/whisper.cpp
