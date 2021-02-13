BPM / Workflow
==============

Demande de congés, validation de documents, dématérialisation de la relation client : les processus sont au cœur du système d’informations des entreprises et collectivités.

Les solutions de BPM (Business Process Management) offrent une approche moderne en affranchissant en grande partie les utilisateurs des contraintes techniques pour modéliser, déployer et optimiser leurs processus.

Les solutions de BPM permettent la modélisation graphique des processus, la génération et l’adaptation des formulaires, et le suivi web des demandes.


Bonita
------

:Site: http://fr.bonitasoft.com
:Porteur: un éditeur (BonitaSoft)
:Licence: GPL et propriétaire

Développé depuis le début des années 2000 par Bull, le produit est porté depuis 2009 par l'éditeur français open source BonitaSoft, membre d'OW2.

Bonita propose un modeleur graphique de processus extrêmement convivial et qui permet de déployer en quelques clics des applications BPM simples (par exemple diffuser des formulaires de demande de congés sur un intranet). Les formulaires sont générés automatiquement par la solution, ou peuvent être paramétrés de manière avancée. L'accès aux demandes en attente et leur traitement s'effectuent de manière intuitive grâce à l'interface "user XP", très semblable à un client mail. Mais la véritable force de Bonita, c'est son système de connecteurs, proposés par défaut ou développés sur mesure.

La version SP (Pack de Souscription) est soumise à une souscription qui en plus du support, apporte d’autres fonctionnalités.

Bonita est développé en Java, langage également utilisé pour le développement de nouveaux connecteurs. Certains paramétrages avancés s'effectuent en Groovy.


jBPM
----

:Site: https://www.jbpm.org/
:Porteur: un éditeur (Red Hat)
:Licence: LGPL

jBPM est développé par une communauté soutenue par JBoss. Référence du BPM open source depuis plusieurs années, jBPM a été intégré par de nombreux éditeurs à leurs solutions. Le produit souffre toutefois aujourd'hui d'un manque de dynamisme de sa communauté.

jBPM supporte les standards suivants:

- business processes (BPMN2)
- case management (BPMN2 and CMMN)
- decision management (DMN)
- business rules (DRL)
- business optimisation (Solver)

JBPM est un excellent moteur BPM, puissant et léger. Utilisé comme brique logicielle c'est une solution technique simple à configurer et bénéficiant d'une API très complète.

JBPM est développé en Java.


Activiti
--------

:Site: https://www.activiti.org/
:Porteur: un éditeur (Alfresco)
:Licence: Apache

Activiti a été publié par l'éditeur d'ECM Alfresco, qui souhaitait développer une alternative à jBPM pour ses propres besoins. En choisissant d’en faire un composant indépendant, Alfresco parie sur le dynamisme de l'open source (le produit a été reversé à la communauté Spring) et souhaite en faire l'outil de référence du BPM open source. Activiti est ainsi techniquement à l'état de l'Art et bénéficie d'un très bon dynamisme grâce à la grande popularité de son porteur.

Activiti est aujourd'hui un moteur BPM léger et robuste. Sa jeunesse le destine plutôt à une fonction de brique BPM intégrée à des projets plus complexes, comme il l’est à Alfresco par exemple. Activiti présente néanmoins des interfaces agréables pour les utilisateurs finaux (conception de processus) qui permettront aux équipes fonctionnelles et techniques de travailler conjointement sur la modélisation des processus. Sa mise en œuvre à proprement parler nécessitera toutefois impérativement de réelles compétences techniques.

Activiti est développé en Java.


Autres
------

- SpiffWorkflow (Python): https://github.com/knipknap/SpiffWorkflow
- ViewFlow (Python): http://viewflow.io/
- Adhesive (Python): https://germaniumhq.com/adhesive/
- Camunda (Java): https://github.com/camunda/camunda-bpm-platform
- Flor (Ruby): https://github.com/floraison/flor

