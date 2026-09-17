Frameworks Web (backend)
========================

La plupart des applications modernes s’appuient sur des frameworks ou bibliothèques web.

Un framework permet de réduire les temps de développement des applications en répondant de façon efficace aux problèmes les plus courants rencontrés par les développeurs. Il inclut généralement de nombreuses fonctionnalités prêtes à l’emploi dont les implémentations sont bien rodées et utilisent des modèles de conceptions standards et bien implémentés. Le temps ainsi gagné sur les questions génériques pourra être mis à profit sur les parties spécifiques de l’application.

Les frameworks disponibles sont généralement de grande qualité. On en trouve pour tous les langages (Python, PHP, Javascript, Java, Ruby, etc.) avec des approches parfois très différentes.


Django
------

:Site: https://www.djangoproject.com/
:Porteur: une fondation (Django Software Foundation)
:Licence: BSD

Django est un framework web en Python, créé en 2005 par le groupe de presse Lawrence Journal-World.

Django est fondé sur le paradigme MVC (MVT dans sa terminologie) et sur le principe du *Don't Repeat Yourself*. Il fournit le maximum d'éléments prêts à l'emploi : couche d'abstraction de la base de données (ORM) et système de migrations, système de cache, manipulation des formulaires et validation des entrées, moteur de gabarits, interface d'administration générée automatiquement, intégration au framework de tests unitaires de Python, prévention des attaques web classiques (XSS, CSRF, injection SQL). Les versions récentes y ajoutent la prise en charge de l'asynchrone (ASGI). Parmi les sites notables utilisant Django, on peut citer Instagram, Mozilla ou encore la plateforme data.gouv.fr.

Django est développé en Python.


Ruby On Rails
-------------

:Site: https://rubyonrails.org/
:Porteur: une communauté
:Licence: MIT

Ruby On Rails est un framework Web. La première version, écrite par David Heinemeier Hansson, est sortie en 2004.

Le framework Ruby On Rails se caractérise par les principes *Don't Repeat Yourself* et *convention over configuration*, en fournissant un certain nombre de générateurs de code et d'interfaces (*scaffolding*). Ceux-ci évitent au développeur de recoder des fonctionnalités standards toujours similaires. Dans le même esprit, les couches basses (sécurité, accès aux bases de données, gestion du HTTP, tâches de fond, WebSockets) sont intégrées au framework. Parmi les grands sites bâtis sur Rails, on peut citer GitHub, Shopify ou Basecamp ; les versions récentes mettent l'accent sur la réduction des dépendances JavaScript (Hotwire) et sur la simplification du déploiement (Kamal).

Ruby On Rails est développé en Ruby.


CubicWeb
--------

:Site: https://www.cubicweb.org/
:Porteur: une communauté
:Licence: LGPL

CubicWeb est un framework Python orienté web sémantique, créé en 2001 par la société française Logilab et publié en open source en 2008. Son développement se poursuit, à un rythme modéré et pour une communauté restreinte.

Au-delà des fonctionnalités habituelles de ce genre d'outil (CRUD, sécurité,
RESTful, développement agile, tests unitaires, indépendance vis-à-vis de la base
de données sous-jacente, etc), CubicWeb met l'accent sur la réutilisation et la
fusion de données disponibles sur le Web (Linked Open Data) et leur
visualisation dynamique dans un navigateur, le tout en respectant les standards
du W3C (RDF, OWL, etc). Les applications typiques concernent la publication de
catalogues de plusieurs dizaines de millions d'objets ou des bases dédiées à la
recherche médicale.

CubicWeb est développé en Python.

Symfony
-------

:Site: https://symfony.com
:Porteur: un éditeur (SensioLabs) et une communauté
:Licence: MIT

Symfony est un framework web MVC écrit en PHP. Créé par Fabien Potencier, il est sorti en 2005 ; la réécriture complète de la version 2 (2011) a donné naissance à l'architecture de composants réutilisables qui fait aujourd'hui sa force. Le rythme de publication est très régulier, avec une version majeure tous les deux ans et une version LTS maintenue quatre ans.

Symfony est un framework dont les principes de fonctionnement sont similaires à ceux de Django ou de Ruby On Rails. Le respect du protocole HTTP et du paradigme MVC sont au cœur du framework, qui fournit un contexte de développement complet. Le développeur a un accès uniformisé à la base de données (grâce à l'ORM Doctrine), aux contrôleurs, aux vues, etc. Du côté de la sécurité, Symfony fournit des protections contre les attaques classiques sur les applications web (injection SQL, XSS, CSRF…).

Son influence dépasse largement son propre périmètre : ses composants constituent le socle de Drupal, de Laravel, d'Ibexa, de TYPO3 et de nombreux autres produits présentés dans ce guide.

Symfony fournit également un ensemble d'outils en ligne de commande permettant de gérer le cache, de générer le code de départ des contrôleurs et des entités, d'appliquer les migrations de base de données, etc. L'écosystème s'est enrichi d'API Platform pour la création d'API REST et GraphQL, et de Symfony UX pour l'intégration des composants front-end.

Symfony est développé par la société française SensioLabs et par une très large communauté.


Spring
------

:Site: https://spring.io
:Porteur: un éditeur (Broadcom, via VMware Tanzu) et une communauté
:Licence: Apache 2.0

Spring est un portefeuille d'outils et de bibliothèques qui propose une pile complète, alternative à la pile standard Jakarta EE. Le projet, né chez Interface21 puis passé chez SpringSource, VMware et enfin Broadcom (qui a racheté VMware en 2023), est devenu le standard de fait du développement Java d'entreprise.

Spring s'appuie sur son conteneur léger permettant de gérer les dépendances entre les objets composant l'application. Par dessus ce conteneur léger, il est possible d'utiliser un des nombreux composants du portfolio. Les principaux étant Spring MVC, Spring ORM et Spring AOP. Spring MVC est un framework MVC full-REST et fondé sur les annotations. Les classes répondant aux actions utilisateur sont annotées afin d'indiquer la méthode à utiliser ainsi que la vue à retourner. Spring ORM est une bibliothèque d'abstraction des accès aux données. Il abstrait les frameworks de persistance usuels, Hibernate, JDO ou EclipseLink. Spring AOP est un framework de programmation orientée aspect. Plus simpliste que AspectJ, Spring AOP offre néanmoins les outils usuels de la POA avec différents types de greffons et différentes manières d'exprimer les points de coupe.

Spring est également utilisé pour charger les différentes configurations de l'application, pour la gestion des transactions ainsi que pour tout un ensemble d'outils utilitaires, ce qui en fait une pièce centrale de l'écosystème Java.

C'est aujourd'hui **Spring Boot** qui constitue le point d'entrée du portefeuille : il assemble et configure automatiquement les composants Spring, embarque un serveur d'application (Tomcat, Jetty ou Undertow) et produit un exécutable autonome, ce qui a largement contribué au déclin des serveurs d'applications JEE traditionnels. Spring est distribué sous licence Apache 2.0.


Play!
-----

:Site: https://www.playframework.com
:Porteur: une communauté
:Licence: Apache 2.0

Play! est un framework Java orienté Web créé par Guillaume Bort en 2007.

Le principe de Play! est de réduire la durée du cycle de développement Java, ainsi que limiter la complexité applicative souvent associée aux projets Java. On y trouvera donc la transposition en Java des concepts principaux de frameworks tel que RoR, Django ou encore Symfony : MVC, Convention over Configuration, Don't Repeat Yourself, .... Play! dispose également de son propre gestionnaire technique de projets, permettant la création des interfaces CRUD, et de son propre serveur d'application (même s'il peut se déployer facilement dans un Tomcat), ce qui lui permet par exemple le rechargement transparent et à chaud du code modifié.

Play! a été développé à l'origine par la société française Zenexity, puis porté par l'américaine Lightbend (devenue Akka). Celle-ci s'étant désengagée, le framework est aujourd'hui maintenu par sa communauté.

Play! est écrit en Scala et en Java ; depuis la version 2, les gabarits sont écrits en Scala et la compilation s'appuie sur sbt.


Autres
------

Parmi les produits de l’univers Frameworks et bibliothèques pour le développement Web, on peut compléter la liste avec les outils ci-dessous :

Python :

- FastAPI (API REST modernes, asynchrones, documentation OpenAPI générée): https://fastapi.tiangolo.com/
- Flask: https://flask.palletsprojects.com/
- Litestar: https://litestar.dev/

PHP :

- Laravel, aujourd'hui le framework PHP le plus utilisé au monde: https://laravel.com/
- CakePHP: https://cakephp.org/
- Laminas (successeur de Zend Framework): https://getlaminas.org/

Java et JVM :

- Spring Boot (voir ci-dessus): https://spring.io/projects/spring-boot
- Quarkus, orienté conteneurs et démarrage instantané: https://quarkus.io/
- Micronaut: https://micronaut.io/
- Apache CXF (services web): https://cxf.apache.org/

JavaScript et TypeScript :

- Express: https://expressjs.com/
- NestJS: https://nestjs.com/
- Fastify: https://fastify.dev/

Autres langages :

- ASP.NET Core (C#, MIT): https://dotnet.microsoft.com/apps/aspnet
- Axum et Actix Web (Rust): https://github.com/tokio-rs/axum et https://actix.rs/
- Echo et Gin (Go): https://echo.labstack.com/ et https://gin-gonic.com/


