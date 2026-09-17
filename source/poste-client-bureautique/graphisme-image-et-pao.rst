Graphisme, image et PAO
=======================

Les métiers de la création graphique sont, avec la finance, ceux où la dépendance aux logiciels propriétaires est la plus forte et la mieux installée : la suite d'Adobe y tient lieu de standard de fait ; son passage à l'abonnement a transformé cette dépendance en coût récurrent.

L'offre open source du domaine a pourtant changé de nature ces dernières années. Longtemps cantonnée à l'amateur éclairé, elle est aujourd'hui employée en production dans l'animation, l'édition et l'illustration, avec un critère de maturité qui ne trompe pas : la gestion de la chaîne colorimétrique, des espaces CMJN et des profils ICC, sans laquelle aucun travail destiné à l'impression n'est possible.

Reste une règle de prudence : ces outils s'évaluent poste par poste et métier par métier, jamais en bloc. Un studio peut très bien retenir Blender pour la 3D et conserver un logiciel propriétaire pour la retouche photo, sans que la cohérence de sa chaîne de production en souffre.


GIMP
----

:Site: https://www.gimp.org/
:Porteur: une communauté (projet GNU)
:Licence: GPL v3

GIMP (*GNU Image Manipulation Program*) est le logiciel de retouche et de composition d'images matricielles de référence du monde libre, développé depuis 1995.

Il couvre l'essentiel de ce qu'on attend d'un tel outil : calques et masques, détourage, correction colorimétrique, filtres, retouche locale, scriptage (Script-Fu, Python-Fu) et traitement par lots, avec une bibliothèque d'extensions fournie.

La version 3.0, publiée en 2025 après une décennie de réécriture, marque un tournant : passage à GTK3, édition non destructive par effets de calque, meilleure gestion des espaces colorimétriques et des images en haute profondeur de bits, prise en charge améliorée des fichiers PSD. Les reproches qui lui étaient adressés (interface datée, absence d'édition non destructive) perdent une bonne partie de leur objet, même si l'ergonomie reste déroutante pour qui vient d'un autre outil.

GIMP est écrit en C.


Inkscape
--------

:Site: https://inkscape.org/
:Porteur: une communauté (Inkscape Project, projet membre de Software Freedom Conservancy)
:Licence: GPL v3

Inkscape est l'éditeur de dessin vectoriel libre de référence. Il travaille nativement au format **SVG**, standard du W3C, ce qui garantit la lisibilité des fichiers produits par n'importe quel outil conforme et leur intégration directe dans une page web.

Sa couverture fonctionnelle (chemins de Bézier, opérations booléennes, effets de chemin dynamiques, typographie avancée, traçage d'images matricielles, clones et motifs) le rend apte à la production d'illustrations, de logos, de schémas techniques et de documents de communication. La gestion des couleurs CMJN, longtemps son point faible pour l'impression, a progressé avec les versions 1.x.

Il occupe une place particulière dans les organisations : c'est souvent le premier logiciel libre adopté par des équipes de communication, parce que le format SVG s'est imposé indépendamment de lui.

Inkscape est écrit en C++.


Krita
-----

:Site: https://krita.org/
:Porteur: une fondation (Krita Foundation) et la communauté KDE
:Licence: GPL v3

Krita est un atelier de peinture numérique et d'illustration. Sa vocation est le dessin, là où GIMP sert la retouche photographique : les deux outils coexistent sur un même poste.

Il propose des centaines de brosses paramétrables, la gestion de la pression et de l'inclinaison des stylets, les calques de groupe et de filtre, les masques, les assistants de perspective, la peinture symétrique, la gestion colorimétrique complète et un module d'animation image par image.

Il est employé en production par des illustrateurs et des studios d'animation, et son financement (dons, vente sur les boutiques d'applications, subventions) a permis d'entretenir une équipe de développeurs à plein temps, ce qui est rare dans cette catégorie.

Krita est écrit en C++ (Qt).


Scribus
-------

:Site: https://www.scribus.net/
:Porteur: une communauté
:Licence: GPL v2

Scribus est le logiciel de publication assistée par ordinateur du monde libre : mise en page de documents destinés à l'impression professionnelle, du dépliant au magazine.

C'est sur la sortie qu'il se juge. Il y tient ses promesses : séparation CMJN, gestion des profils ICC, tons directs, défonce et surimpression, export PDF/X aux normes des imprimeurs, contrôle en amont (*preflight*) qui signale les images sous-résolues ou les polices manquantes avant l'envoi.

Son interface a vieilli et son rythme de publication est lent : la branche stable évolue peu, l'essentiel du travail se concentrant sur une version 1.7 en développement prolongé. C'est néanmoins la seule solution libre crédible pour la PAO destinée à l'imprimerie ; des collectivités et des associations l'emploient pour leurs publications périodiques.

Scribus est écrit en C++ (Qt).


darktable
---------

:Site: https://www.darktable.org/
:Porteur: une communauté
:Licence: GPL v3

darktable est un logiciel de développement de fichiers RAW et de gestion de flux photographique : catalogage, tri, développement non destructif, exportation.

Le traitement y est entièrement non destructif : le fichier d'origine n'est jamais modifié, seules les opérations sont enregistrées. Il s'appuie sur un pipeline colorimétrique moderne (modules « scene-referred ») qui produit des résultats de qualité professionnelle. L'accélération par GPU via OpenCL permet de travailler sans attente sur des fichiers de grande taille.

Il s'adresse aux photographes et aux services communication qui produisent leurs propres images. Son apprentissage est exigeant : la contrepartie d'une chaîne de traitement entièrement paramétrable.

darktable est écrit en C.


Blender
-------

:Site: https://www.blender.org/
:Porteur: une fondation néerlandaise (Blender Foundation)
:Licence: GPL

Blender est la grande réussite du logiciel libre dans le domaine de la création : suite complète de création 3D (modélisation, sculpture, texturation, animation, simulation physique, rendu, montage vidéo, compositing) employée aujourd'hui dans la publicité, le jeu vidéo, l'architecture et le cinéma d'animation.

Son modèle de financement fait école : le *Development Fund* de la fondation réunit des contributions d'entreprises, dont plusieurs grands studios et fabricants de matériel, et finance une équipe permanente. Le projet est ainsi passé en une décennie du statut d'outil marginal à celui de standard reconnu, avec des films d'animation produits intégralement sous Blender.

Pour une organisation, c'est aussi un outil de production de contenus de communication : visuels 3D, animations de présentation, visualisations de produits ou de bâtiments.

Blender est écrit en C, C++ et Python.


Autres
------

- RawTherapee, autre développeur de fichiers RAW, complémentaire de darktable: https://www.rawtherapee.com/
- digiKam, gestion de photothèque à grande échelle: https://www.digikam.org/
- ImageMagick et GraphicsMagick, pour le traitement d'images en ligne de commande et par lots: https://imagemagick.org/
- FreeCAD et LibreCAD, pour la conception assistée par ordinateur: https://www.freecad.org/ et https://librecad.org/
