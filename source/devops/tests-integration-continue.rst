Tests & intégration continue
============================

L’intégration continue est un ensemble de pratiques visant à améliorer la qualité de livraison d’une application en vérifiant à chaque modification de code source, que le résultat des modifications n’entraine pas de régressions (c'est-à-dire d’anomalies supplémentaires liées à l’ajout de code).

Pour mettre en œuvre des plateformes d’intégration continue, il existe de nombreux outils open source de qualité. Le paysage s'est toutefois recomposé : les serveurs d'intégration continue autonomes de la génération précédente (Apache Continuum et Hudson, tous deux retirés à l'*Attic* d'Apache et de la fondation Eclipse) ont disparu, et Jenkins lui-même est de plus en plus concurrencé par les moteurs intégrés aux forges — GitLab CI, GitHub Actions, Forgejo Actions — qui présentent l'avantage de décrire la chaîne de construction dans le dépôt lui-même.


Tests
~~~~~

Selenium
--------

:Site: https://www.selenium.dev/
:Porteur: une communauté (Software Freedom Conservancy)
:Licence: Apache 2.0

Selenium est l'outil historique de test d'interfaces web. Le projet a débuté en 2004 chez ThoughtWorks, à l'initiative de Jason Huggins.

Son cœur est aujourd'hui **WebDriver**, devenu une recommandation du W3C et implémenté nativement par tous les navigateurs : les tests, écrits en Java, Python, JavaScript, C# ou Ruby, pilotent le navigateur comme le ferait un utilisateur. Selenium Grid permet de répartir leur exécution sur un parc de navigateurs et de systèmes. Selenium IDE, l'enregistreur de scénarios présenté dans les éditions précédentes de ce guide, existe toujours, mais sous la forme d'une extension pour navigateurs, l'ancienne version limitée à Firefox ayant disparu avec les anciennes extensions XUL.

Pour les nouveaux projets, on comparera Selenium à **Playwright** (https://playwright.dev/), développé par Microsoft, et à **Cypress** (https://www.cypress.io/), qui offrent une expérience de développement plus moderne (attente automatique, capture de traces, exécution parallèle) et se sont imposés sur les applications web récentes.


Squash
------

:Site: https://www.squashtm.com/
:Porteur: un éditeur français (Henix)
:Licence: LGPL v3 et propriétaire

La suite Squash se compose de plusieurs outils dédiés à l'industrialisation des tests fonctionnels, développés par la société française Henix.

Squash TM est un outil open source de gestion de référentiels de tests. Nativement multi-projets, il permet de gérer l'ensemble des étapes d'une recette, de la gestion des exigences à l'exécution des campagnes de test, et s'intègre aux outils de suivi de tickets (Jira, Redmine, GitLab).

Le volet automatisation a évolué : Squash TA a laissé place à **Squash AUTOM** et à l'orchestrateur Squash Orchestrator, qui pilotent l'exécution de tests écrits avec les automates du marché (Selenium, Cypress, Playwright, Robot Framework, JMeter…) plutôt que de fournir leur propre langage de scénarios.


Autres
------

- JUnit: https://junit.org/
- PHPUnit: https://phpunit.de/
- pytest (Python): https://docs.pytest.org/
- Robot Framework (tests fonctionnels pilotés par mots-clés): https://robotframework.org/
- Testcontainers (dépendances réelles jetables dans les tests d'intégration): https://testcontainers.com/



Integration continue
~~~~~~~~~~~~~~~~~~~~

Jenkins
-------

:Site: https://www.jenkins.io
:Porteur: une communauté
:Licence: MIT et Creative Commons.


Jenkins est un outil d'intégration continue, fork du projet Hudson développé à l'origine par Sun.

Jenkins permet d'automatiser la construction de projets et de générer des rapports de tests et de qualité. Jenkins est majoritairement utilisé dans le marché des solutions d'intégration continue. Le grand atout de Jenkins est son écosystème composé de centaines de plugins, ainsi que son interface plus simple et moins austère que celle de Continuum par exemple. Les générations de projets peuvent être initiées par différents moyens (mécanismes de planification similaires au cron, des systèmes de dépendances entre générations, ou par des requêtes sur certaines URL spécifiques).

Jenkins est écrit en Java. Son principal atout — un écosystème de plus de mille huit cents extensions — est aussi sa principale charge d'exploitation : maintenir un Jenkins à jour et sûr demande un travail réel, ce qui pousse nombre d'équipes vers les moteurs intégrés à leur forge.


Autres
------

- GitLab CI/CD, intégré à la forge GitLab: https://docs.gitlab.com/ci/
- Forgejo Actions et Gitea Actions, compatibles avec la syntaxe de GitHub Actions: https://forgejo.org/docs/latest/user/actions/
- Woodpecker CI, moteur léger issu de Drone: https://woodpecker-ci.org/
- Tekton, chaînes de construction natives Kubernetes: https://tekton.dev/
- Argo CD, pour le volet déploiement continu (GitOps): https://argo-cd.readthedocs.io/
- Buildbot: https://buildbot.net/
- Tox (matrices de tests Python): https://tox.wiki/


Analyse statique de code
~~~~~~~~~~~~~~~~~~~~~~~~

PMD
---

:Site: https://pmd.github.io/
:Porteur: une communauté
:Licence: BSD

PMD, connu également sous le nom de "Project Mess Detector", ou de "Project Meets Deadline" est un outil d'analyse statique de code destiné à détecter les erreurs de programmation les plus courantes.

En utilisant un système de règles extensibles, PMD est capable de détecter les try-catch vides, le code mort, code sur-compliqué, copié-collé de code (grâce au plugin CPD). PMD est également capable de calculer la complexité cyclomatique d'un code, indicateur intéressant dans l'évaluation de la qualité logicielle.

PMD analyse le code source Java, mais prend également en charge une vingtaine d'autres langages (Apex, JavaScript, Kotlin, Swift…). Il existe un équivalent en PHP (PHPMD, *PHP Mess Detector*). Les règles peuvent s'écrire sous forme d'expressions XPath ou de classes Java.


Autres
------

- SonarQube Community Build, plateforme d'analyse continue de la qualité et de la sécurité du code: https://www.sonarsource.com/products/sonarqube/
- Checkstyle (conventions de codage Java): https://checkstyle.org/
- SpotBugs, successeur de FindBugs, dont le développement s'est arrêté en 2015: https://spotbugs.github.io/
- Ruff, analyseur et formateur Python en Rust, qui a largement remplacé Flake8 et isort par sa rapidité: https://docs.astral.sh/ruff/
- Pylint: https://pylint.readthedocs.io/
- mypy et Pyright, vérificateurs de types Python: https://mypy-lang.org/ et https://microsoft.github.io/pyright/
- ESLint (JavaScript et TypeScript): https://eslint.org/
- Semgrep, analyse statique orientée sécurité, multi-langages: https://semgrep.dev/
- Trivy, analyse des dépendances, des images de conteneurs et des configurations d'infrastructure: https://trivy.dev/
