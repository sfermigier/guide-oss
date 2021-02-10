Outils de développement
=======================

Cette section présente les outils utiles aux développements d’applications, web notamment.

On y trouve des outils de gestion de projet comme Redmine ou Maven, des outils d’automatisation comme Ant ou Phing, des environnements de développement comme Eclipse, des gestionnaires de tickets comme MantisBT, des outils de gestion de source comme Subversion ou Git, et des solutions de collaboration et d’ingénierie logicielle comme Tuleap.

Comme on le voit, l’open source offre d’excellentes briques de développement pour bâtir des projets ambitieux dans des conditions optimales.




Acceleo
-------

:Site: http://www.eclipse.org
:Porteur: une fondation (Eclipse)
:Licence: EPL (Eclipse Public License)

Acceleo est un générateur de code qui permet de transformer des modèles vers du code (approche MDA - Model driven Architecture).
Acceleo a l'originalité de laisser à l'utilisateur le choix dans le formalisme de modélisation en entrée, et dans le type de langage et de framework à générer en sortie. Ainsi, de nombreux éditeurs sous Eclipse ont été créés pour simplifier la création de générateurs sur mesure, via une approche basée sur des templates et une syntaxe standardisée.

Acceleo est écrit en Java.



Eclipse IDE
-----------

:Site: www.eclipse.org
:Porteur: une fondation (Eclipse)
:Licence: EPL (Eclipse Public License)

Eclipse est un environnement de développement extensible et polyvalent, initié par IBM en 2001 et porté depuis 2004 par la Fondation Eclipse.

Conçu autour d'une plateforme commune à laquelle s'agrègent des composants dérivatifs, le projet est ainsi constitué de nombreux sous-projets spécifiques aux technologies sous-jacentes. L’object de la solution Eclipse est de fournir des outils favorisant la productivité, mais pas seulement celle qui concerne le codage logiciel. On y trouve des environnements de développement intégré mais également de conception, de modélisation, de tests, de reporting, etc. Eclipse a beau être écrit en Java, il peut être utilisé pour développer sous de très nombreux langages de programmation.

Eclipse est écrit en Java.


MantisBT
--------

:Site: www.mantisbt.org
:Porteur: une communauté
:Licence: GPL v2

MantisBT est un outil web très populaire de suivi de tickets (anomalies, demandes d'évolutions, demandes d'intervention, ...), adapté à tous types de projets. Kenzaburo Ito, initiateur du projet en novembre 2000, est rapidement rejoint en 2002 par Jeroen Latour, Victor Boctor et Julian Fitzell pour constituer le cœur de l'équipe de développement.

MantisBT permet une répartition des tickets par projet. Il est également possible de qualifier les demandes suivant différents critères (type, catégorie, sévérité, priorité, privé/public). L'outil dispose notamment de fonctionnalités comme : un workflow d’enchaînement d'états paramétrables, un système de notification, un formulaire de recherche de tickets avec filtres, une page personnalisée pour chaque utilisateur listant les tickets dont il est l'auteur ainsi que les tickets qui lui sont assignés, une gestion de droits utilisateurs, une rubrique d'administration par projet permettant d'ajouter/supprimer des utilisateurs au projet, la création de sous projets, etc.

MantisBT est développé en PHP et nécessite l'utilisation d'une base de données (MySQL, PostgreSQL, MS SQL ou DB2). Il est principalement testé pour les serveurs Web Apache et IIS.


Maven
-----

:Site: http://maven.apache.org
:Porteur: une fondation (Apache)
:Licence: Apache

Maven est un outil de gestion de projet technique. Son développement est assuré principalement par la fondation Apache.

Maven permet de standardiser la forme d'un projet ainsi que son utilisation. Il permet également de gérer les dépendances d'un projet, d'effectuer une livraison complète et automatique, de déployer une application, et de faciliter le déploiement d'un projet au sein d'une plate-forme d'intégration continue. Maven offre également une intégration poussée de nombreux outils de reporting (Surefire, PMD, CheckStyle, NCSS, etc.). Maven est destiné aux projets Java en général et aux projets Java EE en particulier.

Maven est écrit en Java.


Subversion
----------

:Site: http://subversion.apache.org
:Porteur: une fondation (Apache)
:Licence: Apache et BSD

Subversion (SVN) est un système de gestion de version centralisé. Issu de CVS, son développement est initialisé en 2000 par la société Collabnet. Il est devenu officiellement un projet de la fondation Apache en 2010.

Standard et populaire, il a été choisi par de nombreuses communautés du logiciel libre. De nombreux outils et ressources sont disponibles pour l'exploiter au mieux. Apache Subversion a été écrit pour combler les manques de CVS dont seule l’implémentation avait été remis en cause (et non son concept). Certaines fonctionnalités ont été ajoutées : les répertoires et les métadonnées sont versionnées, les numéros de révision sont globaux pour l’ensemble du dépôt, il est possible de renommer ou de déplacer des fichiers sans perte de l’historique, etc.

Subversion est écrit en C.


Git
---

:Site: http://git-scm.com
:Porteur: une communauté
:Licence: GPL v2

Git est un système de gestion de versionnement décentralisé (DVCS). Il est notamment utilisé pour le noyau Linux ou pour PHP. C'est un logiciel libre créé par Linus Torvalds en 2005.

Git permet notamment de "commiter" localement puis de pousser aux autres développeurs un ensemble de commits locaux. Il permet également d'utiliser un workflow de développement en soumettant par exemple l'envoi de code à l'approbation d'un des développeurs. La faculté de Git à créer des branches facilement ainsi que de permettre leur administration de façon simple en fait un outil de choix dans le cadre de développement de projets open source.

Git est distribué sous la licence GPL v2.

Git est écrit en C, Bourne Shell et Perl.


Redmine
-------

:Site: www.redmine.org
:Porteur: une communauté
:Licence: GPL v2

Redmine est un outil collaboratif permettant, à travers une interface web sécurisée, de gérer des projets. Il a été créé par Jean-Philippe Lang en 2006.

Redmine offre les fonctionnalités suivantes :

- gestion multi-projets sécurisée

- gestion des utilisateurs, des profils et des droits, en fonction de chaque projet

- gestion de documents, classement par catégorie, propriétaire, titre, date, etc.

- gestion des demandes, de leur statut, de leur priorité et de leur historique, assignation de ces demandes aux acteurs pertinents du projet.

- visualisation de l’actualité du projet sous forme de diagramme de Gantt

- notification par mail ou par flux RSS

- etc.

Redmine a été développé en Ruby sur la base du framework Ruby on Rails.


Tuleap
------

:Site: www.enalean.com/produits/tuleap
:Porteur: un éditeur (Enalean)
:Licence: GPL

Tuleap est une Suite Logicielle open source qui fournit les outils nécessaires  aux entreprises pour un développement logiciel et une collaboration efficace. Egalement appelée Forge Logicielle ou ALM (application life cycle management), Tuleap a été développée par la société Enalean.

Tuleap est un logiciel utilisé par plusieurs dizaines de milliers d'utilisateurs dans le monde pour leurs développements professionnels, dans de grandes entreprises telles que STMicroelectronics, ST-Ericsson ou encore Orange. Tuleap est une suite ALM complète : tracking de bugs, de tests, de risques, etc, gestion de versions, intégration continue, gestion documentaire, outils de collaboration, etc.

L'éditeur de Tuleap, Enalean, est une société française qui a fondé son modèle économique sur le support et les services professionnels

Tuleap est écrit majoritairement en PHP.

Mercurial
---------

:Site: https://www.mercurial-scm.org/
:Porteur: une communauté
:Licence: GPL

Mercurial est un logiciel de gestion de versions décentralisé (DVCS) disponible sur la plupart des systèmes Unix, Windows et Mac OS X.

Il a été créé pour s'utiliser via la ligne de commande, mais propose une intégration forte avec le bureau Windows (TortoiseHg), des interfaces graphiques avancées pour l'affichage de l'historique (HgView) et une interface web intégrée.

Ses principales caractéristiques sont sa capacité à gérer les gros projets, son fonctionnement complètement distribué ne nécessitant pas de serveur, sa gestion avancée des branches et des fusions, ainsi que l'ajout récent de la traçabilité de l'évolution de l'historique.

Mercurial est écrit principalement en Python.

Autres
------

Parmi les produits de l’univers Outils de développement, on peut compléter la liste avec les outils ci-dessous :


- gitlab: https://gitlab.com/

- Gforge: https://gforge.org/

- Trac: https://trac.edgewall.org


