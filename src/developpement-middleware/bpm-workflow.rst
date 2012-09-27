BPM / Workflow
==============

Demande de congés, validation de documents, dématérialisation de la relation client : les processus sont au cœur du système d’informations des entreprises et collectivités.

Les solutions de BPM (Business Process Management) offrent une approche moderne en affranchissant en grande partie les utilisateurs des contraintes techniques pour modéliser, déployer et optimiser leurs processus.

Les solutions de BPM permettent la modélisation graphique des processus, la génération et l’adaptation des formulaires, et le suivi web des demandes.

Dans l’univers de l’open source, des solutions de qualité existent comme Bonita, produit phare du secteur BPM open source.




Bonita
------

:Version: 5.5.2
:Site: http://fr.bonitasoft.com
:Porteur: un éditeur (BonitaSoft)
:Licence: GPL et propriétaire

Développé depuis le début des années 2000 par Bull, le produit est porté depuis 2009 par l'éditeur français open source BonitaSoft, membre d'OW2.

Bonita propose un modeleur graphique de processus extrêmement convivial et qui permet de déployer en quelques clics des applications BPM simples (par exemple diffuser des formulaires de demande de congés sur un intranet). Les formulaires sont générés automatiquement par la solution, ou peuvent être paramétrés de manière avancée. L'accès aux demandes en attente et leur traitement s'effectuent de manière intuitive grâce à l'interface "user XP", très semblable à un client mail. Mais la véritable force de Bonita, c'est son système de connecteurs, proposés par défaut ou développés sur mesure.

La version SP (Pack de Souscription) est soumise à une souscription qui en plus du support, apporte d’autres fonctionnalités.

Bonita est développé en Java, langage également utilisé pour le développement de nouveaux connecteurs. Certains paramétrages avancés s'effectuent en Groovy.


JBPM
----

:Version: 5.1
:Site: www.jboss.org/jbpm
:Porteur: un éditeur (JBoss)
:Licence: LGPL

JBPM est développé par une communauté soutenue par JBoss. Référence du BPM open source depuis plusieurs années, JBPM a été intégré par de nombreux éditeurs à leurs solutions. Le produit souffre toutefois aujourd'hui d'un manque de dynamisme de sa communauté. La dernière version est néanmoins prometteuse et le produit reste incontournable comme brique BPM technique de projets notamment en environnement open source.

JBPM est un excellent moteur BPM, puissant et léger. la version 5 est annoncée compatible avec le langage BPMN 2.0. Utilisé comme brique logicielle c'est une solution technique simple à configurer et bénéficiant d'une API très complète. Des interfaces Eclipse (développeurs) et web (utilisateurs fonctionnels) permettent de gérer les workflows graphiquement, mais pâtissent d'une certaine jeunesse qui les rend inadaptées pour une gestion par des utilisateurs non techniques. De plus, l'interface web n'est disponible que via l'application Drools (moteur de règles) ce qui fait perdre à l'outil son principal avantage : sa simplicité.

JBPM est développé en Java.


Activiti
--------

:Version: 5.7
:Site: www.activiti.org
:Porteur: un éditeur (Alfresco)
:Licence: Apache

Activiti a été publié par l'éditeur d'ECM Alfresco, qui souhaitait développer une alternative à JBPM pour ses propres besoins. En choisissant d’en faire un composant indépendant, Alfresco parie sur le dynamisme de l'open source (le produit a été reversé à la communauté Spring) et souhaite en faire l'outil de référence du BPM open source. Activiti est ainsi techniquement à l'état de l'Art et bénéficie d'un très bon dynamisme grâce à la grande popularité de son porteur.

Activiti est aujourd'hui un moteur BPM léger et robuste. Sa jeunesse le destine plutôt à une fonction de brique BPM intégrée à des projets plus complexes, comme il l’est à Alfresco par exemple. Activiti présente néanmoins des interfaces agréables pour les utilisateurs finaux (dessin de processus) qui permettront aux équipes fonctionnelles et techniques de travailler conjointement sur la modélisation des processus. Sa mise en œuvre à proprement parler nécessitera toutefois impérativement de réelles compétences techniques.

Activiti est développé en Java.


Petals BPM
--------

:Version: 1.0-alpha-3
:Site: http://research.petalslink.org/display/petalsbpm/
:Porteur: LINAGORA (éditeur / SSLL)
:Licence: AGPL

Petals BPM est un outil open source de modélisation de processus métier. Il se présente sous la forme d'une application web, qui permet à travers une interface graphique de créer des diagrammes au standard BPMN 2.0, et à terme, les traduire en processus BPEL exécutables. L’utilisation combinée de Petals BPM, Petals Master (annuaire de
services) et Petals ESB (bus de services) assure ainsi la gestion du cycle de vie complet de vos processus métier à travers une plate-forme cohérente.
C'est un moteur léger, conforme aux standards et ergonomique, qui permettra à terme de créer et importer ses propres modèles grâce à une API. 
Il représente la solution idéale pour concevoir et exéctuer vos processus métiers au sein d'une infrastructure de services, et est activement développé par l'équipe de Petals, désormais intégrée à LINAGORA, leader français de l'édition et prestation de services open source.
Vous pouvez le découvrir sur le site de démonstration : http://bpmneditor.ebmwebsourcing.com/
