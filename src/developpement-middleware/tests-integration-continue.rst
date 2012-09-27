Tests & intégration continue
============================

L’intégration continue est un ensemble de pratiques visant à améliorer la qualité de livraison d’une application en vérifiant à chaque modification de code source, que le résultat des modifications n’entraine pas de régressions (c'est-à-dire d’anomalies supplémentaires liées à l’ajout de code).

Pour mettre en œuvre des plateformes d’intégration continue, il existe de nombreux outils open source de qualité tels que Continiuum ou Hudson. Autour des ces outils, on trouve également des solutions de rendu graphique (affichage des résultats).


Jenkins
-------

:Version: 1.483
:Site: www.jenkins-ci.org
:Porteur: une communauté
:Licence: MIT et Creative Commons.


Jenkins est un outil d'intégration continue, fork du projet Hudson développé à l'origine par Sun.

Jenkins permet d'automatiser la construction de projets et de générer des rapports de tests et de qualité. Jenkins est majoritairement utilisé dans le marché des solutions d'intégration continue. Le grand atout de Jenkins est son écosystème composé de centaines de plugins, ainsi que son interface plus simple et moins austère que celle de Continuum par exemple. Les générations de projets peuvent être initiées par différents moyens (mécanismes de planification similaires au cron, des systèmes de dépendances entre générations, ou par des requêtes sur certaines URL spécifiques).

Jenkins est écrit en Java.


Continiuum
----------

:Version: 1.3.7
:Site: www.continuum.apache.org
:Porteur: une fondation (Apache)
:Licence: Apache

Continuum est l'outil d'intégration continue de la fondation Apache.

Continuum offre toutes les fonctionnalités que l'on attend d'un tel outil. Automatisations configurables bien sûr, mais aussi distribution du build sur des machines esclaves, configuration de différents environnements d'exécution, gestion très fine des droits et reporting intégré pour les résultats des tests unitaires.

La fonctionnalité différenciante de Continuum est la possibilité de regrouper des modules/projets au sein de groupes de projets. Au sein de ces groupes, les différentes configurations et droits sont mutualisés ce qui permet de gérer un ensemble de projets de façon simple même quand ce nombre augmente rapidement.

Continiuum est écrit en Java.


Selenium IDE
------------

:Version: 1.0.4
:Site: http://seleniumhq.org/projects/ide
:Porteur: une communauté
:Licence: Apache

Selenium est un outil de tests d'interfaces. Le projet a débuté en 2004 chez ThoughtWorks à Chicago grâce à Jason Huggins, lequel voulait tester les temps de réponse de diverses applications (Python, Plone, etc.).

Selenium IDE permet d'enregistrer des tests d'interfaces depuis Firefox puis de les sauvegarder afin de les rejouer avec Selenium. Cet outil est très utile pour vérifier qu'une interface est conforme à ce qui est attendu. De plus, il peut être intégré à une plateforme d'intégration continue afin d'automatiser les tests d'interfaces. Selenium IDE n'est pas seulement un outil d'enregistrement : il s'agit d'un environnement de développement intégré (IDE). L'utilisateur peut choisir d'utiliser sa capacité d'enregistrement, ou peut modifier les scripts à la main.


PMD
---

:Version: 4.2.5
:Site: http://pmd.sourceforge.net
:Porteur: une communauté
:Licence: BSD

PMD, connu également sous le nom de "Project Mess Detector", ou de "Project Meets Deadline" est un outil d'analyse statique de code destiné à détecter les erreurs de programmation les plus courantes.

En utilisant un système de règles extensibles, PMD est capable de détecter les try-catch vides, le code mort, code sur-compliqué, copié-collé de code (grâce au plugin CPD). PMD est également capable de calculer la complexité cyclomatique d'un code, indicateur intéressant dans l'évaluation de la qualité logicielle.

PMD analyse le code source Java. Il existe un équivalent en PHP (PHPMD, a.k.a. PHP Mess Detector). Les règles peuvent s'écrire à travers des expressions XPath ou des classes Java (ou PHP pour PHPMD).


Autres
------

Parmi les produits de l’univers Tests et intégration continue, on peut compléter la liste avec les outils ci-dessous :



Nom	URL / Site web

Sonar	http://www.sonarsource.org

Checkstyles	http://checkstyle.sourceforge.net

JUnit	http://www.junit.org

PHPUnit	https://github.com/sebastianbergmann/phpunit

FindBugs	http://findbugs.sourceforge.net

CruseControl	http://cruisecontrol.sourceforge.net

