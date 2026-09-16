Frameworks mobiles cross-platform
=================================

Les technologies open source jouent un rôle essentiel dans l'écosystème du développement des applications mobiles, en démocratisant l'accès aux outils nécessaires pour créer des applications innovantes et performantes. Ces technologies permettent de construire des applications mobiles en utilisant des langages de programmation et des standards web familiers, réduisant ainsi la barrière d'entrée pour le développement mobile et permettant une plus grande réutilisation du code entre les plateformes.

Apache Cordova
--------------

:Site: https://cordova.apache.org/
:Porteur: Une fondation (Apache Software Foundation)

Apache Cordova (anciennement PhoneGap) est un outil de développement d'applications mobiles multiplateformes qui se distingue par sa capacité à exploiter les standards du web. Créé en 2008 par la société canadienne Nitobi, qui a par la suite été acquise par Adobe, PhoneGap a marqué une évolution significative dans le domaine du développement mobile.

Apache Cordova continue d'offrir aux développeurs la possibilité de créer des applications mobiles en utilisant HTML, CSS et JavaScript, tout en ayant accès aux fonctionnalités matérielles du dispositif à travers une série de plugins. Les applications développées avec Apache Cordova sont des applications web encapsulées dans un conteneur natif, permettant leur déploiement sur diverses plateformes mobiles sans nécessiter plusieurs bases de code.

La transition vers Apache Cordova a également encouragé une plus grande collaboration et innovation au sein de la communauté de développeurs. Avec le soutien de la Apache Software Foundation, Cordova bénéficie d'une gouvernance ouverte et d'une contribution collective, ce qui aide à garantir que la plateforme reste à la pointe du progrès technologique et répond aux besoins changeants des développeurs et des entreprises.

Distribué sous licence Apache, Cordova conserve une communauté active, même si son usage recule : Adobe a mis fin à PhoneGap en 2020, et les nouveaux projets se tournent le plus souvent vers Capacitor (https://capacitorjs.com/), le moteur de plugins natifs développé par l'équipe d'Ionic, qui reprend la même approche avec un outillage plus moderne.


React Native
------------

:Site: https://reactnative.dev/
:Porteur: Meta
:Licence: MIT

React Native est une technologie open source pour le développement d'applications mobiles, créée par Facebook. Elle permet aux développeurs de construire des applications mobiles en utilisant JavaScript et React, offrant ainsi une expérience native tant sur Android que sur iOS. React Native se distingue par sa capacité à traduire le code JavaScript en composants natifs, permettant aux applications de bénéficier de performances optimales et d'une excellente intégration avec les plateformes sous-jacentes.

L'approche de React Native est centrée sur l'efficacité du développement et la réactivité de l'interface utilisateur, en réutilisant le code entre les plateformes mobiles et en accélérant le cycle de développement grâce au rechargement à chaud. La communauté dynamique et l'écosystème riche de React Native offrent une multitude de composants et d'extensions, facilitant l'intégration de fonctionnalités avancées et la personnalisation des applications.

React Native est adapté tant aux jeunes pousses qu'aux grandes entreprises : Meta, Microsoft et Shopify comptent parmi ses principaux utilisateurs et contributeurs. Son modèle de développement fondé sur JavaScript et TypeScript est particulièrement attrayant pour les équipes disposant déjà d'une expertise en développement web. La refonte interne du framework (« nouvelle architecture », avec le moteur Hermes et l'interface JSI) a levé une partie des limites de performance de ses débuts, et la chaîne d'outils Expo (https://expo.dev/) simplifie considérablement la mise en production.

Flutter
-------

:Site: https://flutter.dev/
:Porteur: Google
:Licence: BSD

Flutter est un SDK de développement d'applications mobiles open source créé par Google, qui permet de construire des applications multiplateformes de haute qualité avec une seule base de code. Flutter utilise le langage de programmation Dart, conçu par Google, et offre un système de widgets complet, personnalisable et réactif, ce qui facilite la création d'interfaces utilisateur complexes et attrayantes.

Contrairement à d'autres frameworks qui se reposent sur les composants natifs de la plateforme, Flutter dessine chaque élément de l'interface utilisateur à partir de zéro, garantissant ainsi une cohérence visuelle parfaite sur toutes les plateformes. Cette approche unique permet également une grande flexibilité dans la personnalisation de l'interface utilisateur, donnant aux développeurs le pouvoir de réaliser presque tout ce qu'ils peuvent imaginer.

Flutter s'est rapidement imposé comme un choix populaire pour le développement mobile, grâce à sa performance élevée, son hot reload qui permet des itérations rapides pendant le développement, et sa communauté grandissante. Des entreprises de toutes tailles ont adopté Flutter pour développer leurs applications, y compris des géants technologiques comme Alibaba et Google pour certaines de leurs applications internes.

.NET MAUI (successeur de Xamarin)
---------------------------------

:Site: https://dotnet.microsoft.com/apps/maui
:Porteur: Microsoft
:Licence: MIT

Xamarin, framework open source soutenu par Microsoft, permettait de créer des applications Android et iOS en C# et .NET, avec un fort partage de code entre plateformes. Son support a pris fin le 1er mai 2024 : il est remplacé par .NET MAUI (*Multi-platform App UI*), qui en constitue l'évolution directe.

.NET MAUI conserve le principal atout de son prédécesseur : l'intégration étroite du développement d'applications mobiles dans l'écosystème .NET, avec des outils familiers pour la gestion du code, le débogage et le déploiement. Il unifie dans un projet unique les cibles Android, iOS, macOS et Windows, là où Xamarin.Forms reposait sur des projets séparés, et s'appuie sur les mêmes contrôles natifs.

C'est le choix naturel pour les équipes ayant déjà investi dans les technologies Microsoft ; les projets Xamarin existants doivent en revanche prévoir une migration, celle-ci n'étant pas entièrement transparente.

Ionic
-----

:Site: https://ionicframework.com/
:Porteur: Ionic, filiale d'OutSystems
:Licence: MIT

Ionic est un framework de développement d'applications mobiles open source qui permet aux développeurs de créer des applications mobiles et de bureau de haute qualité en utilisant des technologies web comme HTML, CSS et JavaScript. Ionic se distingue par son approche centrée sur le web, permettant aux développeurs ayant des compétences en développement web de facilement transitionner vers le développement d'applications mobiles. Le framework repose sur une base de composants d'interface utilisateur (UI) optimisés pour le mobile, offrant une expérience similaire à celle des applications natives.

Ionic fonctionne bien avec Apache Cordova pour l'accès aux fonctionnalités du dispositif via des plugins, permettant ainsi aux applications Ionic de tirer parti des capacités matérielles du smartphone, telles que la caméra, le GPS et l'accéléromètre. De plus, Ionic a introduit Capacitor, son propre moteur de plugins natifs, conçu pour offrir une alternative plus moderne à Cordova, avec une meilleure intégration dans les écosystèmes mobiles modernes et un support pour le développement d'applications web progressives (PWA).

Le framework Ionic est particulièrement apprécié pour sa flexibilité et son écosystème riche, qui comprend un large éventail de plugins, outils et services qui facilitent le développement, le test, et le déploiement d'applications. De plus, Ionic offre un système de thèmes et de personnalisation puissant, permettant aux développeurs de créer des interfaces utilisateurs attrayantes et cohérentes sur différentes plateformes sans effort supplémentaire.

Ionic s'adresse aux jeunes pousses, aux entreprises et aux développeurs individuels cherchant à développer rapidement des applications mobiles multiplateformes sans compromettre la qualité de l'expérience utilisateur. Avec son attachement aux standards du web et sa compatibilité avec Angular, React et Vue.js, Ionic continue de jouer un rôle important dans le paysage du développement mobile.

La société Ionic a été rachetée par OutSystems en 2022 et a arrêté la commercialisation de ses produits payants (Appflow, Identity Vault, Portals) début 2025. Les briques open source — Ionic Framework, Capacitor et Stencil — restent publiées sous licence MIT et activement maintenues, Capacitor étant aujourd'hui la partie la plus stratégique de l'ensemble.


Flet
----

:Site: https://flet.dev/
:Porteur: Appveyor Systems Inc

Flet est un framework innovant conçu pour simplifier le développement d'applications en temps réel pour le web, les mobiles et les ordinateurs de bureau. Sa philosophie principale repose sur la facilité d'utilisation et l'accessibilité, permettant aux développeurs de transformer rapidement leurs idées en applications fonctionnelles sans nécessiter une expérience approfondie en développement front-end.

Flet cherche à éliminer la complexité traditionnellement associée à l'architecture des applications modernes, qui requiert souvent une pile technologique composée d'un front-end, d'un back-end, d'API REST, de bases de données et de systèmes de mise en cache. Avec Flet, les développeurs écrivent une application monolithique et à état en utilisant uniquement Python, ce qui simplifie considérablement le processus de développement. Cette approche permet de créer des applications monopages (SPA) temps réel et multi-utilisateurs sans avoir à concevoir ni à déployer des architectures complexes. Flet s'appuie sur Flutter pour le rendu.


Autres
------

Le paysage du développement multiplateforme a beaucoup évolué ces dernières années ; on surveillera également :

- Kotlin Multiplatform et Compose Multiplatform (partage de code et d'interface entre Android, iOS, bureau et web, soutenus par JetBrains et Google): https://kotlinlang.org/multiplatform/
- Capacitor, moteur de plugins natifs successeur de Cordova: https://capacitorjs.com/
- Expo, chaîne d'outils de référence pour React Native: https://expo.dev/
- Tauri, pour les applications de bureau et mobiles légères écrites en Rust et en technologies web: https://tauri.app/
- NativeScript: https://nativescript.org/
