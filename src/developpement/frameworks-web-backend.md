# Frameworks web (backend)

La plupart des applications modernes s’appuient sur des frameworks ou bibliothèques web.

Un framework permet de réduire les temps de développement des applications en répondant de façon efficace aux problèmes les plus courants rencontrés par les développeurs. Il inclut généralement de nombreuses fonctionnalités prêtes à l’emploi dont les implémentations sont bien rodées et utilisent des modèles de conceptions standards et bien implémentés. Le temps ainsi gagné sur les questions génériques pourra être mis à profit sur les parties spécifiques de l’application.

Les frameworks disponibles sont généralement de grande qualité. On en trouve pour tous les langages (Python, PHP, Javascript, Java, Ruby, etc.) avec des approches parfois très différentes.

## Django

Site
: <https://www.djangoproject.com/>

Porteur
: une fondation (Django Software Foundation)

Licence
: BSD

Django est un framework web en Python, créé en 2005 par le groupe de presse Lawrence Journal-World.

Django est fondé sur le paradigme MVC (MVT dans sa terminologie) et sur le principe du *Don't Repeat Yourself*. Il fournit le maximum d'éléments prêts à l'emploi : couche d'abstraction de la base de données (ORM) et système de migrations, système de cache, manipulation des formulaires et validation des entrées, moteur de gabarits, interface d'administration générée automatiquement, intégration au framework de tests unitaires de Python, prévention des attaques web classiques (XSS, CSRF, injection SQL). Les versions récentes y ajoutent la prise en charge de l'asynchrone (ASGI). Parmi les sites notables utilisant Django, on peut citer Instagram, Mozilla ou encore la plateforme data.gouv.fr.

Django est développé en Python.

## Ruby On Rails

Site
: <https://rubyonrails.org/>

Porteur
: une communauté

Licence
: MIT

Ruby On Rails est un framework Web. La première version, écrite par David Heinemeier Hansson, est sortie en 2004.

Le framework Ruby On Rails se caractérise par les principes *Don't Repeat Yourself* et *convention over configuration*, en fournissant un certain nombre de générateurs de code et d'interfaces (*scaffolding*). Ceux-ci évitent au développeur de recoder des fonctionnalités standards toujours similaires. Dans le même esprit, les couches basses (sécurité, accès aux bases de données, gestion du HTTP, tâches de fond, WebSockets) sont intégrées au framework. Parmi les grands sites bâtis sur Rails, on peut citer GitHub, Shopify ou Basecamp ; les versions récentes mettent l'accent sur la réduction des dépendances JavaScript (Hotwire) et sur la simplification du déploiement (Kamal).

Ruby On Rails est développé en Ruby.

## FastAPI

Site
: <https://fastapi.tiangolo.com/>

Porteur
: une communauté (projet initié par Sebastián Ramírez)

Licence
: MIT

Publié en 2018 par Sebastián Ramírez, FastAPI est l'un des frameworks Python les plus utilisés pour écrire des API HTTP, en particulier autour des services d'IA et de données.

Les annotations de type de Python y décrivent les paramètres et les corps de requête ; le framework en déduit la validation (Pydantic) et une documentation OpenAPI consultable dans le navigateur. Il repose sur Starlette, donc sur le standard asynchrone ASGI. Il intègre un mécanisme d'injection de dépendances. À la différence de Django, il n'impose ni ORM ni interface d'administration.

Deux points sont à considérer : le projet reste en version 0.x, ce qui impose de suivre les notes de version. Sa conduite dépend beaucoup de son auteur, qui a fondé FastAPI Labs pour commercialiser une offre d'hébergement.

FastAPI est écrit en Python.

## CubicWeb

Site
: <https://www.cubicweb.org/>

Porteur
: une communauté

Licence
: LGPL

CubicWeb est un framework Python orienté web sémantique, créé en 2001 par la société française Logilab et publié en open source en 2008. Il décrit une application par son schéma de données, expose les standards RDF et OWL et sert à publier des catalogues liés (*Linked Open Data*). Son développement se poursuit pour une communauté restreinte, sur des usages de niche comme la publication de grands catalogues de données.

## Symfony

Site
: <https://symfony.com>

Porteur
: un éditeur (Symfony SAS) et une communauté

Licence
: MIT

Symfony est un framework web MVC écrit en PHP. Créé par Fabien Potencier, il est sorti en 2005 ; la réécriture complète de la version 2 (2011) a donné naissance à l'architecture de composants réutilisables qui fait aujourd'hui sa force. Le rythme de publication est très régulier, avec une version majeure tous les deux ans et une version LTS maintenue quatre ans.

Symfony est un framework dont les principes de fonctionnement sont similaires à ceux de Django ou de Ruby On Rails. Le respect du protocole HTTP et du paradigme MVC sont au cœur du framework, qui fournit un contexte de développement complet. Le développeur a un accès uniformisé à la base de données (grâce à l'ORM Doctrine), aux contrôleurs, aux vues, etc. Du côté de la sécurité, Symfony fournit des protections contre les attaques classiques sur les applications web (injection SQL, XSS, CSRF…).

Son influence dépasse largement son propre périmètre : ses composants constituent le socle de Drupal, de Laravel, d'Ibexa, de TYPO3 et de nombreux autres produits présentés dans ce guide.

Symfony comprend également un ensemble d'outils en ligne de commande permettant de gérer le cache, de générer le code de départ des contrôleurs et des entités, d'appliquer les migrations de base de données, etc. L'écosystème s'est enrichi d'API Platform pour la création d'API REST et GraphQL et de Symfony UX pour l'intégration des composants front-end.

Symfony est porté par la société Symfony SAS (titulaire de la marque) et par une très large communauté. SensioLabs, la société d'origine de Fabien Potencier, en est distincte depuis 2018 ; elle appartient au groupe Smile et propose services et formations. Le logiciel est écrit en PHP.

## Laravel

Site
: <https://laravel.com/>

Porteur
: un éditeur (Laravel) et une communauté

Licence
: MIT

Créé par Taylor Otwell en 2011, Laravel est l'un des frameworks PHP les plus utilisés. Il s'appuie sur plusieurs composants Symfony.

Il couvre l'ensemble d'une application web : routage, ORM Eloquent et migrations, gabarits Blade, files de tâches, notifications, planification, authentification et tests. Des bibliothèques officielles prolongent le cœur (Livewire et Inertia sont les deux voies courantes pour les interfaces interactives).

Le framework est libre, mais une partie de son écosystème ne l'est pas : l'éditeur vit d'outils et de services commerciaux (Nova, Forge, Cloud). Il a levé 57 millions de dollars auprès d'Accel en 2024. On veillera à distinguer, dans un projet, ce qui relève du framework et ce qui crée une dépendance à ces services.

Laravel est écrit en PHP.

## Spring

Site
: <https://spring.io>

Porteur
: un éditeur (Broadcom, via VMware Tanzu) et une communauté

Licence
: Apache 2.0

Spring est un portefeuille d'outils et de bibliothèques qui propose une pile complète, alternative à la pile standard Jakarta EE. Le projet, né chez Interface21 puis passé chez SpringSource, VMware et enfin Broadcom (qui a racheté VMware en 2023), est devenu la référence du développement Java d'entreprise.

Spring s'appuie sur son conteneur léger permettant de gérer les dépendances entre les objets composant l'application. Par dessus ce conteneur léger, il est possible d'utiliser un des nombreux composants du portfolio. Les principaux étant Spring MVC, Spring ORM et Spring AOP. Spring MVC est un framework MVC full-REST et fondé sur les annotations. Les classes répondant aux actions utilisateur sont annotées afin d'indiquer la méthode à utiliser ainsi que la vue à retourner. Spring ORM est une bibliothèque d'abstraction des accès aux données. Il abstrait les frameworks de persistance usuels, Hibernate, JDO ou EclipseLink. Spring AOP est un framework de programmation orientée aspect. Plus simpliste que AspectJ, Spring AOP offre néanmoins les outils usuels de la POA avec différents types de greffons et différentes manières d'exprimer les points de coupe.

Spring est également utilisé pour charger les différentes configurations de l'application, pour la gestion des transactions ainsi que pour tout un ensemble d'outils utilitaires, ce qui en fait une pièce centrale de l'écosystème Java.

C'est aujourd'hui **Spring Boot** qui constitue le point d'entrée du portefeuille : il assemble et configure automatiquement les composants Spring, embarque un serveur d'application (Tomcat, Jetty ou Undertow) et produit un exécutable autonome, ce qui a largement contribué au déclin des serveurs d'applications JEE traditionnels. Spring est distribué sous licence Apache 2.0.

## Play!

Site
: <https://www.playframework.com>

Porteur
: une communauté

Licence
: Apache 2.0

Play! est un framework Java orienté Web créé par Guillaume Bort en 2007.

Le principe de Play! est de réduire la durée du cycle de développement Java, ainsi que limiter la complexité applicative souvent associée aux projets Java. On y trouvera donc la transposition en Java des concepts principaux de frameworks tel que RoR, Django ou encore Symfony : MVC, Convention over Configuration, Don't Repeat Yourself, .... Play! dispose également de son propre gestionnaire technique de projets (création des interfaces CRUD) et de son propre serveur d'application (même s'il peut se déployer facilement dans un Tomcat), ce qui lui permet par exemple le rechargement transparent et à chaud du code modifié.

Play! a été développé à l'origine par la société française Zenexity, puis porté par l'américaine Lightbend (devenue Akka). Celle-ci s'étant désengagée, le framework est aujourd'hui maintenu par sa communauté.

Play! est écrit en Scala et en Java ; depuis la version 2, les gabarits sont écrits en Scala et la compilation s'appuie sur sbt.

## Autres

Parmi les produits de l’univers Frameworks et bibliothèques pour le développement Web, on peut compléter la liste avec les outils ci-dessous :

Python :

- Flask: <https://flask.palletsprojects.com/>
- Litestar: <https://litestar.dev/>

PHP :

- CakePHP: <https://cakephp.org/>
- Laminas (successeur de Zend Framework): <https://getlaminas.org/>

Java et JVM :

- Spring Boot (voir ci-dessus): <https://spring.io/projects/spring-boot>
- Quarkus, orienté conteneurs et démarrage instantané: <https://quarkus.io/>
- Micronaut: <https://micronaut.io/>
- Apache CXF (services web): <https://cxf.apache.org/>

JavaScript et TypeScript :

- Express: <https://expressjs.com/>
- NestJS: <https://nestjs.com/>
- Fastify: <https://fastify.dev/>

Autres langages :

- ASP.NET Core (C#, MIT): <https://dotnet.microsoft.com/apps/aspnet>
- Axum et Actix Web (Rust): <https://github.com/tokio-rs/axum> et <https://actix.rs/>
- Echo et Gin (Go): <https://echo.labstack.com/> et <https://gin-gonic.com/>
