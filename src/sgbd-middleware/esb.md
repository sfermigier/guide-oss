# ESB

Les ESB (« Enterprise Service Bus ») permettent la communication entres applications qui ne proposent pas, à la base, de services ou d’interfaces prévus pour cela.

Les ESB exploitent différentes techniques : transformation, transfert et routage d’informations, exposition de services web.

La notion d'ESB a beaucoup changé. Le bus central des années 2000, propriétaire du routage et de la transformation, a cédé la place à des approches plus légères : bibliothèques d'intégration embarquées dans les applications (Apache Camel), passerelles d'API, architectures événementielles bâties sur un bus de messages (voir la section [MOM et EAI](mom-eai.md)).

Les ESB interviennent en tant que « médiateur » entre les clients et les fournisseurs de services (applications).

Plus d'infos: <https://fr.wikipedia.org/wiki/Enterprise_service_bus>

## Zato

Site
: <https://zato.io/>

Porteur
: un éditeur (Zato Source)

Licence
: AGPL v3

Zato est une plate-forme middleware et un serveur d'applications open source fondé sur Python. Il a été conçu comme un ESB (Enterprise Service Bus) agile visant à construire des systèmes de systèmes *on premise* ou dans le Cloud. Zato fournit une SOA (*Service Oriented Architecture*), REST (*Representational State Transfer*), des API et une intégration dans le Cloud, ainsi qu'une exposition des services back-end aux clients frontaux.

Zato est une plateforme évolutive qui aide à la fois à créer et à orchestrer des services d'intégration et à améliorer l'intercommunication entre les applications et les sources de données. Elle peut maintenir en ordre toutes les solutions techniques que votre entreprise utilise et ouvrir la voie à de nouvelles opportunités et de nouveaux processus. L'utilisation d'un large éventail de connecteurs, de formats de données et de protocoles permet à Zato d'éviter de restreindre le style architectural ou d'imposer d'autres limites.

## WSO2 EI

Site
: <https://github.com/wso2/product-integrator-mi>

Porteur
: un éditeur (Choreo Labs, anciennement WSO2)

Licence
: Apache 2.0

WSO2 Integrator: MI (Micro Integrator) est le successeur de WSO2 Enterprise Integrator, lui-même issu de WSO2 ESB (2005). C'est un moteur d'intégration léger, conçu pour être déployé en conteneur, avec connecteurs, médiation de messages et exposition d'API.

L'éditeur, WSO2, a pris le nom de Choreo Labs en novembre 2026 et se présente désormais comme un spécialiste de la gouvernance des agents d'IA. Il annonce le maintien des produits, des contrats et des licences open source, les noms devant changer progressivement. Le code reste publié sous licence Apache 2.0 ; l'accès aux correctifs en production passe en revanche par une souscription.

Le produit est écrit en Java.

## NServiceBus

Site
: <https://particular.net/nservicebus>

Porteur
: un éditeur (Particular Software)

Licence
: Reciprocal Public License 1.5

NServiceBus est un framework de messagerie fondé sur .NET. Il permet la création de systèmes distribués évolutifs et fiables. Il prend en charge une variété de modèles de messagerie sur des transports tels que MSMQ, RabbitMQ, Azure, Amazon SQS. Sa conception modulaire lui permet de s'adapter à des choix tels que la mise en file d'attente, le stockage, la sérialisation et les options de journalisation.

## Apache Camel

Site
: <https://camel.apache.org/>

Porteur
: une fondation (Apache)

Licence
: Apache 2.0

Créé en 2007, Apache Camel est devenu la brique d'intégration open source la plus utilisée, au point d'être embarquée par la plupart des ESB du marché, dont ceux présentés ci-dessus.

Camel est une bibliothèque : elle implémente les *Enterprise Integration Patterns* sous forme de routes déclaratives (en Java, XML, YAML ou Kotlin) et fournit plus de trois cents composants de connexion (fichiers, JMS, Kafka, HTTP, bases de données, SaaS, protocoles industriels). L'intégration devient ainsi un morceau d'application ordinaire, versionné, testable et déployable comme le reste du code, ce qui explique en grande partie le recul du bus centralisé.

Les déclinaisons Camel K et Camel Quarkus permettent d'exécuter ces routes directement sur Kubernetes, avec un démarrage quasi instantané.

Camel est écrit en Java.

## Autres

Parmi les produits de l’univers ESB, on peut compléter la liste avec les outils ci-dessous :

- Apache Synapse: <https://synapse.apache.org>
- Apache Karaf, conteneur OSGi fréquemment utilisé comme socle d'exécution: <https://karaf.apache.org/>
- Petals ESB, solution française portée par Linagora: <https://petals.linagora.com/>

JBoss ESB (Red Hat en a arrêté le développement au profit de Camel et de Fuse) et Apache ServiceMix, retiré à l'*Attic* de la fondation Apache, ont disparu.
