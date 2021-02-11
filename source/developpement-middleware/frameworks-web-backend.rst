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

Django un framework Web en Python qui a été créé en 2005 par le groupe de presse Lawrence Journal-World.

Django est basé sur le paradigme MVC et sur le principe du *Don't Repeat Yourself*, en fournissant le maximum d'éléments pré-existants, tels qu'une couche d'abstraction à la base, un système de cache, une infrastructure de manipulation des formulaires et de validation des entrées, un moteur de templating, une interface au framework de tests unitaires Python (PyUnit), des outils de créations d'interface CRUD, des systèmes de préventions des attaques Web classiques (XSS, CSRF, injection SQL, etc...). A noter que Django est disponible sur la plateforme Google App Engine. Parmi les sites notables de l'Internet utilisant Django, on peut citer Disqus ou encore Spotify.

Django est développé en Python.


Ruby On Rails
-------------

:Site: https://rubyonrails.org/
:Porteur: une communauté
:Licence: MIT

Ruby On Rails est un framework Web. La première version, écrite par David Heinemeier Hansson, est sortie en 2004.

Le framework Ruby On Rails se caractérise par le concept du Don't Repeat Yourself, en fournissant un certain nombre de générateurs de codes et d'interfaces (scaffolding). Ceux-ci évitent au développeur de refaire les mêmes opérations et de recoder des fonctionnalités standards toujours similaires. Dans le même état d'esprit, les couches basses classiques (sécurité, accès aux bases de données, gestion du HTTP, appels Ajax) sont intégrées au framework et permettent au développeur de se concentrer sur la logique métier plutôt que sur les aspects techniques. Parmi les success story de RoR, on peut citer Twitter, même si certaines parties (non liée au front office) ont été ré-écrites en Scala, suite à des problèmes de tenue en charge de l’interpréteur Ruby.

Ruby On Rails est développé en Ruby.


CubicWeb
--------

:Site: https://www.cubicweb.org/
:Porteur: une communauté
:Licence: LGPL

CubicWeb est un framework en Python pour le Web Sémantique qui a été créé en 2001 par la société Logilab.

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

:Site: https://www.symfony-project.org
:Porteur: un éditeur (Sensio Labs)
:Licence: MIT

Symfony est un framework Web MVC écrit en PHP. Créé par Fabien Potencier, la première version est sortie en 2005, et la version 2.0, fortement attendue est arrivée en août 2011.

Symfony est un framework dont les principes de fonctionnement sont similaires à Django ou Ruby On Rails. Le respect du protocole HTTP et du paradigme MVC sont au coeur du framework, qui fournit un contexte de développement complet. Le développeur a un accès uniformisé à la base de données (grâce à l'ORM Doctrine), aux contrôleurs, aux vues, etc. Le framework fournit également une large bibliothèque de fonctions utilitaires. Du côté de la sécurité, Symfony fournit des protections contre les attaques classiques sur les applications Web (SQL injection, XSS, CSRF, ...).

Symfony fournit également un ensemble d'outils en ligne de commande permettant de gérer le cache, de générer automatiquement une interface d'administration (admin generator), de générer la structure de la base et les écrans d'éditions pour les objets déclarés (scaffolding), ...

Symfony est développé par la société française Sensio Labs.


Spring
------

:Site: https://www.springsource.org
:Porteur: un éditeur (SpringSource, une entité de VMware)

Spring est un portfolio d'outils et de bibliothèques. Spring propose un stack complet comme une sorte d'alternative à la stack standard Java EE.

Spring s'appuie sur son conteneur léger permettant de gérer les dépendances entre les objets composant l'application. Par dessus ce conteneur léger, il est possible d'utiliser un des nombreux composants du portfolio. Les principaux étant Spring MVC, Spring ORM et Spring AOP. Spring MVC est un framework MVC full-REST et basé sur les annotations. Les classes répondant aux actions utilisateur sont annotées afin d'indiquer la méthode à utiliser ainsi que la vue à retourner. Spring ORM est une bibliothèque d'abstraction des accès aux données. Il fournit une abstraction pour les frameworks usuels de persistence tels que Hibernate, JDO ou EclipseLink. Spring AOP est un framework de programmation orientée aspect. Plus simpliste que AspectJ, Spring AOP offre néanmoins les outils usuels de la POA avec différents types de greffons et différentes manières d'exprimer les points de coupe.

Spring est également utilisé pour charger les différentes configurations de l'application, pour la gestion des transactions ainsi que pour tout un ensemble d'outils utilitaires ce qui le rend incontournable dans l'éco-système Java. Spring est distribué sous la licence Apache.


Play!
-----

:Site: https://www.playframework.org
:Porteur: un éditeur (Lightbend)
:Licence: Apache

Play! est un framework Java orienté Web créé par Guillaume Bort en 2007.

Le principe de Play! est de réduire la durée du cycle de développement Java, ainsi que limiter la complexité applicative souvent associée aux projets Java. On y trouvera donc la transposition en Java des concepts principaux de frameworks tel que RoR, Django ou encore Symfony : MVC, Convention over Configuration, Don't Repeat Yourself, .... Play! dispose également de son propre gestionnaire technique de projets, permettant la création des interfaces CRUD, et de son propre serveur d'application (même s'il peut se déployer facilement dans un Tomcat), ce qui lui permet par exemple le rechargement transparent et à chaud du code modifié.

Play! a été développé par la société française Zenexity. Le support en est à présent assuré par la société américaine Lightbend.

Play! est écrit en Java et en Scala, les templates en Groovy et le gestionnaire de projets en Python.


Autres
------

Parmi les produits de l’univers Frameworks et bibliothèques pour le développement Web, on peut compléter la liste avec les outils ci-dessous :

- Flask: https://flask.palletsprojects.com/
- CakePHP: https://cakephp.org/
- Lithium: https://lithify.me/
- Jelix: https://jelix.org/fr/
- Apache CXF: https://cxf.apache.org/


