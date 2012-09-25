Frameworks et bibliothèques pour le développement Web
=====================================================

Un framework permet de réduire les temps de développement des applications en répondant de façon efficace aux problèmes les plus courants rencontrés par les développeurs. Il inclut généralement de nombreuses fonctionnalités prêtes à l’emploi dont les implémentations sont bien rodées et utilisent des modèles de conceptions standard et bien implémentés. Le temps ainsi gagné sur les questions génériques pourra être mis à profit sur les parties spécifiques de l’application.

Les frameworks disponibles sont généralement de grande qualité. On en trouve pour tous les langages (Java, Php, Javascript, Python, Ruby, etc.) avec des approches parfois très différentes.

La plupart des applications modernes s’appuie sur des frameworks ou bibliothèques web.




Symfony
-------

:Version: 2.0.0
:Site: www.symfony-project.org
:Porteur: un éditeur (Sensio Labs)

Symfony est un framework Web MVC écrit en PHP. Créé par Fabien Potencier, la première version est sortie en 2005, et la version 2.0, fortement attendue est arrivée en août 2011.

Symfony est un framework dont les principes de fonctionnement sont similaires à Django ou Ruby On Rails. Le respect du protocole HTTP et du paradigme MVC sont au coeur du framework, qui fournit un contexte de développement complet. Le développeur a un accès uniformisé à la base de données (grâce à l'ORM Doctrine), aux contrôleurs, aux vues, etc. Le framework fournit également une large bibliothèque de fonctions utilitaires. Du côté de la sécurité, Symfony fournit des protections contre les attaques classiques sur les applications Web (SQL injection, XSS, CSRF, ...).

Symfony fournit également un ensemble d'outils en ligne de commande permettant de gérer le cache, de générer automatiquement une interface d'administration (admin generator), de générer la structure de la base et les écrans d'éditions pour les objets déclarés (scaffolding), ...

Symfony est distribué sous la licence MIT et développé par Sensio Labs.




Zend Framework
--------------

:Version: 1.11
:Site: http://framework.zend.com
:Porteur: un éditeur (Zend Technologie)

Zend Framework fait partie du couple de tête des frameworks PHP avec Symfony. Il est un des frameworks PHP les plus utilisés, sinon le plus utilisé.

L'approche de Zend est assez différente de Symfony, le couplage des composants étant bien  plus léger. Il peut d'ailleurs être vu comme plus proche d'une bibliothèque de composants qu'un framework complet. Néanmoins, il fournit les composants permettant la création d'une application MVC, avec abstraction de la base de données. A noter cependant que Zend Framework ne fournit pas d'ORM, mais une solution légère de Table Gateway Interface. D'un point de vue général, le panel de composants de Zend Framework est très large. On pourra citer entre autres Zend_Gdata qui permet de communiquer avec les services Google ou Zend_Captcha pour intégrer des captcha à son application.

Zend Framework est distribué sous New BSD license et soutenu par la société Zend Technologies, éditrice également du moteur Zend qui est au cœur de l'interpréteur PHP.

Zend Framework nécessite PHP 5.2 et supporte toute les bases de données gérées par PDO.




Spring
------

:Version: 3.0.6
:Site: www.springsource.org
:Porteur: un éditeur (SpringSource, une entité de VMware)

Spring est un portfolio d'outils et de bibliothèques. Spring propose un stack complet comme une sorte d'alternative à la stack standard Java EE.

Spring s'appuie sur son conteneur léger permettant de gérer les dépendances entre les objets composant l'application. Par dessus ce conteneur léger, il est possible d'utiliser un des nombreux composants du portfolio. Les principaux étant Spring MVC, Spring ORM et Spring AOP. Spring MVC est un framework MVC full-REST et basé sur les annotations. Les classes répondant aux actions utilisateur sont annotées afin d'indiquer la méthode à utiliser ainsi que la vue à retourner. Spring ORM est une bibliothèque d'abstraction des accès aux données. Il fournit une abstraction pour les frameworks usuels de persistence tels que Hibernate, JDO ou EclipseLink. Spring AOP est un framework de programmation orientée aspect. Plus simpliste que AspectJ, Spring AOP offre néanmoins les outils usuels de la POA avec différents types de greffons et différentes manières d'exprimer les points de coupe.

Spring est également utilisé pour charger les différentes configurations de l'application, pour la gestion des transactions ainsi que pour tout un ensemble d'outils utilitaires ce qui le rend incontournable dans l'éco-système Java. Spring est distribué sous la licence Apache.




GWT
---

:Version: 2.4
:Site: http://code.google.com/intl/fr-FR/webtoolkit
:Porteur: un éditeur (Google)

Google Web Toolkit est un framework RIA développé par Google dont la version 1.0 date de du 17 mai 2006.

GWT permet le développement d'applications riches en pur Java qui sera "compilé" en Javascript et HTML. Le résultat est une application riche respectant les standards du web par opposition à des technologies comme Flex ou Silverlight qui nécessitent l’installation d’un plugin spécifique sur les postes Client.

GWT permet un développement rapide grâce à son format XML de description d'interfaces. Toutefois, GWT générant toutes les vues de son interface à partir de XML et de Java, il est paradoxalement très difficile d'intégrer un montage HTML ce qui implique une intégration longue et manuelle consistant en une traduction du montage en XML et en Java.

GWT est distribué selon les termes de la licence Apache.

GWT permet de créer et maintenir des applications web dynamiques mettant en œuvre JavaScript, en utilisant le langage et les outils Java.




JQuery
------

:Version: 1.6.3
:Site: http://jquery.com
:Porteur: une communauté

JQuery est une des principales bibliothèques JavaScript. Créée par John Resig en 2006.

JQuery simplifie les développements JavaScript multi-navigateurs en fournissant une API indépendante de la plateforme sous-jacente. L'objectif de jQuery est de simplifier les manipulations usuelles en javascript : manipulation du DOM, gestion des événements, animation et gestion des appels AJAX. L’implémentation suit une logique objet stricte et peut bénéficier du chainage d'appels pour simplifier l'écriture. JQuery possède également un mode de compatibilité, autorisant son utilisation en même temps qu'une autre bibliothèque JavaScript. Une des forces de jQuery est l'écriture simplifiée de plugins permettant la réutilisation et l'encapsulation fonctionnelle des comportements. La communauté étant très réactive, une multitude de greffons sont disponibles sur le site officiel.

JQuery est distribué sous une double licence MIT ou GPL, permettant de l'intégrer sans contrainte. JQuery a été intégré dans de nombreux projets open source ainsi que dans Microsoft ASP.NET Ajax et Google fournit un CDN pour les fichiers de la bibliothèque.

JQuery est compatible avec la vaste majorité des navigateurs, y compris Internet Explorer 6.




Prototype
---------

:Version: 1.7
:Site: www.prototypejs.org
:Porteur: une communauté

Prototype est une bibliothèque Javascript créée en 2005 par Sam Stephenson, afin d'ajouter le support AJAX au framework Ruby On Rails.

En plus de la simplification du développement cross-navigateurs et orienté Ajax, le but de Prototype est d'enrichir le langage JavaScript ainsi que le DOM en lui rajoutant composants et fonctionnalités supplémentaires. De cette façon, le développement JavaScript à l'aide de Prototype permet de retrouver certains concepts traditionnels de la programmation orientée objet, absent du JavaScript standard (constructeurs, héritage objet, ...). A noter néanmoins que l'enrichissement du DOM pose plusieurs problèmes et est en train d'être retiré de la bibliothèque.

Prototype est distribué sous licence MIT.

Prototype est écrit en JavaScript et est compatible avec la vaste majorité des navigateurs, y compris Internet Explorer 6.




Play !
------

:Version: 1.2.3
:Site: www.playframework.org
:Porteur: un éditeur (Zenexity)

Play! est un framework Java orienté Web créé par Guillaume Bort en 2007.

Le principe de Play! est de réduire la durée du cycle de développement Java, ainsi que limiter la complexité applicative souvent associée aux projets Java. On y trouvera donc la transposition en Java des concepts principaux de frameworks tel que RoR, Django ou encore Symfony : MVC, Convention over Configuration, Don't Repeat Yourself, .... Play! dispose également de son propre gestionnaire technique de projets, permettant la création des interfaces CRUD, et de son propre serveur d'application (même s'il peut se déployer facilement dans un Tomcat), ce qui lui permet par exemple le rechargement transparent et à chaud du code modifié.

Play! est distribué sous licence Apache 2. La société Zenexity contribue au projet et réalise développement et le support sur le produit.

Play! est écrit en Java, les templates en Groovy et le gestionnaire de projets en Python.




Django
------

:Version: 1.3.1
:Site: https://www.djangoproject.com
:Porteur: une fondation (Django Software Foundation)

Django est le framework Web de référence en Python. Il a été créé en 2005 par la société Lawrence Journal-World.

Django est basé sur le paradigme MVC et sur le principe du Don't Repeat Yourself, en fournissant le maximum d'éléments pré-existants, tels qu'une couche d'abstraction à la base, un système de cache, une infrastructure de manipulation des formulaires et de validation des entrées, un moteur de templating, une interface au framework de tests unitaires Python (PyUnit), des outils de créations d'interface CRUD, des systèmes de préventions des attaques Web classiques (XSS, CSRF, injection SQL, etc...). A noter que Django est disponible sur la plateforme Google App Engine. Parmi les sites notables de l'Internet utilisant Django, on peut citer Disqus ou encore Spotify.

Django est distribué sous licence BSD.

Django est développé en Python.




Ruby On Rails
-------------

:Version: 3.1
:Site: http://rubyonrails.org
:Porteur: une communauté

Ruby On Rails est un framework Web. La première version, écrite par David Heinemeier Hansson, est sortie en 2004.

Le framework Ruby On Rails se caractérise par le concept du Don't Repeat Yourself, en fournissant un certain nombre de générateurs de codes et d'interfaces (scaffolding). Ceux-ci évitent au développeur de refaire les mêmes opérations et de recoder des fonctionnalités standards toujours similaires. Dans le même état d'esprit, les couches basses classiques (sécurité, accès aux bases de données, gestion du HTTP, appels Ajax) sont intégrées au framework et permettent au développeur de se concentrer sur la logique métier plutôt que sur les aspects techniques. Parmi les success story de RoR, on peut citer Twitter, même si certaines parties (non liée au front office) ont été ré-écrites en Scala, suite à des problèmes de tenue en charge de l’interpréteur Ruby.

Ruby On Rails est distribué sous licence MIT.

Ruby On Rails est développé en Ruby.




Autres
------

Parmi les produits de l’univers Frameworks et bibliothèques pour le développement Web, on peut compléter la liste avec les outils ci-dessous :



Nom	URL / Site web

CakePHP	http://cakephp.org

Lithium	http://lithify.me

Prado	http://www.pradosoft.com

PHPonTrax	http://www.phpontrax.com

CodeIgniter	http://codeigniter.com

Jelix	http://jelix.org/fr

CXF	http://cxf.apache.org

Yii	http://www.yiiframework.com

Zeta components	http://incubator.apache.org/zetacomponents

