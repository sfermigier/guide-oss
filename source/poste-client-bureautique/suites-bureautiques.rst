Suites bureautiques
===================

La suite bureautique installée sur le poste reste le cœur de l'outillage : traitement de texte, tableur, présentation, dessin.

Conformément au périmètre de cette partie, seules les applications qui s'exécutent sur le poste de travail sont traitées ici. L'édition collaborative en ligne, où plusieurs personnes éditent simultanément un document dans leur navigateur, relève d'une plateforme serveur, hors du périmètre du poste client ; les solutions correspondantes sont signalées dans la section :doc:`/applications-generiques/ged-ecm`.

Le critère de choix décisif est la **fidélité de rendu des formats de Microsoft Office**. Sur la richesse fonctionnelle comme sur l'ergonomie, l'écart avec les suites propriétaires s'est considérablement réduit. C'est sur ce point que se jouent les migrations : un document qui se déforme en passant d'un poste à l'autre ruine la confiance des utilisateurs plus sûrement qu'une fonction manquante. Il se teste sur le corpus réel de l'organisation, et sur lui seul : modèles, documents composites, publipostages, classeurs à macros.


LibreOffice
-----------

:Site: https://www.libreoffice.org/
:Porteur: une fondation (The Document Foundation)
:Licence: MPL 2.0

LibreOffice est une suite bureautique libre, issue en 2010 d'un fork d'OpenOffice.org, qui comprend des programmes de traitement de texte (Writer), de création et d'édition de feuilles de calcul (Calc), de diaporamas (Impress), de diagrammes et de dessins (Draw), de travail avec des bases de données (Base) et de composition de formules mathématiques (Math). Elle est disponible dans plus de 100 langues.

Comme format de fichier natif, LibreOffice utilise l'*Open Document Format for Office Applications* (ODF), norme internationale développée conjointement par l'ISO et la CEI. Il gère également les formats de la plupart des autres suites bureautiques, y compris Microsoft Office, grâce à une variété de filtres d'importation et d'exportation.

C'est, à ce jour, la seule suite bureautique libre complète capable de soutenir la comparaison avec l'offre propriétaire sur l'ensemble du périmètre, et la référence de toutes les migrations d'ampleur : administrations, collectivités, armées européennes.

Deux éléments comptent pour un déploiement en entreprise. D'abord le rythme de publication : une branche « Still » conservatrice et une branche « Fresh » plus récente coexistent en permanence, la première étant celle à retenir pour un parc. Ensuite l'écosystème de support professionnel : plusieurs sociétés européennes, dont Collabora et Allotropia, contribuent au code et commercialisent des versions avec engagement de correction, ce qui répond à l'objection la plus fréquente des directions informatiques.

LibreOffice est disponible pour Microsoft Windows, macOS et Linux. Le projet propose également une déclinaison mobile et une version technologique destinée à l'intégration serveur, cette dernière sortant du périmètre de cette partie.


Calligra
--------

:Site: https://calligra.org/
:Porteur: une communauté (projet KDE)
:Licence: GPL v2 et LGPL v2

Calligra est la suite bureautique et graphique du projet KDE, héritière de KOffice. Sa version 4.0, publiée en août 2024, réunit quatre composants : le traitement de texte Words, le tableur Sheets, l'outil de présentation Stage et le logiciel de dessin vectoriel Karbon. Deux applications autrefois incluses, la base de données Kexi et le gestionnaire de projet Plan, suivent désormais leur propre calendrier de publication.

Son intérêt est de proposer une alternative bien plus légère, intégrée au bureau Plasma et construite sur les mêmes bibliothèques : cohérence visuelle, faible empreinte mémoire, démarrage rapide. Ses composants graphiques, Karbon en particulier, témoignent d'une filiation avec Krita, né dans le même ensemble.

C'est un choix à considérer pour des postes modestes, des terminaux légers ou un parc entièrement standardisé sur KDE, en gardant à l'esprit que son rythme de publication est lent et sa communauté restreinte.

Calligra est écrit en C++ (Qt).


Autres
------

Traitements de texte et tableurs autonomes, utiles sur des machines anciennes ou pour des usages ponctuels :

- AbiWord, traitement de texte léger, dont le développement se poursuit sur la forge de GNOME après la disparition de son site historique: https://gitlab.gnome.org/World/AbiWord
- Gnumeric, tableur réputé pour la précision de ses fonctions de calcul: https://www.gnumeric.org/

**Apache OpenOffice**, dont LibreOffice est issu, existe toujours mais n'évolue pratiquement plus : ses publications sont espacées de plusieurs années et sa communauté de développement s'est tarie après la scission de 2010. Les parcs qui en dépendent encore doivent planifier leur migration vers LibreOffice, dont les formats et l'interface leur seront familiers.
