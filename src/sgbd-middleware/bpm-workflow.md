# BPM / Workflow

Demande de congés, validation de documents, dématérialisation de la relation client : les processus sont au cœur du système d’informations des entreprises et collectivités.

Les solutions de BPM (Business Process Management) offrent une approche moderne en affranchissant en grande partie les utilisateurs des contraintes techniques pour modéliser, déployer et optimiser leurs processus.

Les solutions de BPM permettent la modélisation graphique des processus, la génération et l’adaptation des formulaires, et le suivi web des demandes.

## Bonita

Site
: <https://www.ofelia.com/downloads>

Porteur
: un éditeur français (Ofelia, anciennement Bonitasoft)

Licence
: GPL et propriétaire

Développé depuis le début des années 2000 par Bull, le produit est porté depuis 2009 par l'éditeur français Bonitasoft, membre d'OW2. Attention au changement de nom : la société s'est rebaptisée **Ofelia** en 2026, en réorientant une partie de son activité vers l'orchestration d'agents d'IA ; le site bonitasoft.com renvoie désormais vers ofelia.com. Bonita BPM reste commercialisé et maintenu, avec son édition communautaire.

Bonita propose un modeleur graphique de processus extrêmement convivial et qui permet de déployer en quelques clics des applications BPM simples (par exemple diffuser des formulaires de demande de congés sur un intranet). Les formulaires sont générés automatiquement par la solution, ou peuvent être paramétrés de manière avancée. L'accès aux demandes en attente et leur traitement s'effectuent de manière intuitive grâce à l'interface "user XP", très semblable à un client mail. La force de Bonita est son système de connecteurs, proposés par défaut ou développés sur mesure.

La version SP (Pack de Souscription) est soumise à une souscription qui en plus du support, apporte d’autres fonctionnalités.

Bonita est développé en Java, langage également utilisé pour le développement de nouveaux connecteurs. Certains paramétrages avancés s'effectuent en Groovy.

## jBPM

Site
: <https://kie.apache.org/>

Porteur
: une fondation (Apache)

Licence
: Apache 2.0

jBPM a longtemps été la référence du BPM open source en Java et a été intégré par de nombreux éditeurs à leurs solutions. Développé au sein de l'écosystème JBoss puis de Red Hat, le projet a été donné à la fondation Apache : il y est développé depuis 2025, avec Drools, sous le nom d'**Apache KIE**. L'adresse jbpm.org redirige désormais vers ce projet.

jBPM met en œuvre les standards suivants :

- business processes (BPMN2)
- case management (BPMN2 and CMMN)
- decision management (DMN)
- business rules (DRL)
- business optimisation (Solver)

jBPM est un moteur BPM léger. Utilisé comme brique logicielle, c'est une solution simple à configurer et dotée d'une API très complète.

jBPM est développé en Java.

## Activiti

Site
: <https://www.activiti.org/>

Porteur
: une communauté (dans l'orbite d'Alfresco/Hyland)

Licence
: Apache 2.0

Activiti a été publié par l'éditeur d'ECM Alfresco, qui souhaitait développer une alternative à jBPM pour ses propres besoins, avant d'en faire un composant indépendant.

Le projet a connu en 2016 une scission décisive : ses principaux auteurs l'ont quitté pour créer **Flowable** (<https://www.flowable.com/>), qui est depuis lors la branche la plus active et la plus complète des deux, avec la prise en charge des normes BPMN 2.0, CMMN et DMN et une édition open source sous licence Apache 2.0. Activiti poursuit son développement sous la forme d'Activiti Cloud, orienté conteneurs et Kubernetes, mais avec une communauté plus restreinte.

Pour une nouvelle mise en œuvre, on comparera donc en priorité Flowable et Apache KIE (jBPM). Ces moteurs restent des briques techniques : ils supposent de réelles compétences de développement, même s'ils proposent des interfaces de modélisation utilisables par les équipes fonctionnelles.

Activiti est développé en Java.

## Autres

- Flowable (Java), fork d'Activiti par ses auteurs d'origine: <https://www.flowable.com/>
- SpiffWorkflow (Python), moteur BPMN 2.0: <https://github.com/sartography/SpiffWorkflow>
- Viewflow (Python/Django): <https://viewflow.io/>
- Temporal (orchestration de workflows durables, plutôt orientée développeurs): <https://temporal.io/>
- Windmill (plateforme de workflows et de scripts, alternative libre aux outils d'automatisation SaaS): <https://www.windmill.dev/>
- Flor (Ruby): <https://github.com/floraison/flor>

**Le cas Camunda.** Camunda 7, longtemps l'une des références du BPM open source (Apache 2.0), a atteint sa fin de vie en octobre 2025 : le dépôt de l'édition communautaire est archivé et ne reçoit plus de correctifs, y compris de sécurité. Son successeur, Camunda 8, n'est plus open source : depuis octobre 2024, ses composants sont publiés sous Camunda License 1.0, qui autorise la lecture du code et l'usage en développement, mais exige une licence commerciale en production. Les utilisateurs de Camunda 7 souhaitant rester en open source se tournent vers le fork **CIB seven** (<https://cibseven.org/>), vers Flowable ou vers Apache KIE.
