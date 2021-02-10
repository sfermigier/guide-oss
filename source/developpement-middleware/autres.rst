Autres
======

Dans cette dernière rubrique de la dimension « Développement et couches intermédiaires » nous présentons d’autres outils open source qui peuvent trouver leur intérêt dans les entreprises même s’il était difficile d’en faire une catégorie à part entière.

Nous présentons notamment Drools (un moteur de règles étonnant) et ESIGate (permettant la construction à la volée de pages à partir de fragments issus de technologies différentes).




Drools
------

:Version: 5.2.0
:Site: www.jboss.org/drools
:Porteur: un éditeur (JBoss)

Drools (ou JBoss Rules) est un système de gestion de règles métier utilisant un moteur d'inférence à chaînage avant.

L’utilisation d’un outil tel que Drools permet de faire évoluer des règles et des contraintes sans modifier un programme informatique. Cela représente un avantage certain. Drools est constitué de plusieurs modules : Guvnor (interface d’administration Web, Expert (moteur de règles), Planner (Moteur de planification automatique) et Flow (Moteur de workflow). Drools Guvnor offre les services suivants : gestion des versions et le déploiement des règles, édition des règles sans développement, hiérarchisation et catégorisation des règles, déploiement automatisé des règles. Les règles peuvent être visualisées de manière technique mais également grâce à un éditeur très simple d’accès et sous forme de tableau de décision parfaitement compréhensible par des utilisateurs fonctionnels.

Drools est distribué sous la licence Apache.




ESIGate
-------

:Version: 2.19
:Site: www.esigate.org
:Porteur: une commaunuté

ESIGate est un agrégateur de contenus web. Il a été créé par plusieurs ingénieurs spécialistes JEE de chez Smile, premier intégrateur français de solutions open source.

ESIGate peut s'interfacer à des serveurs existants, dont il récupère les pages HTML à la volée. Les différentes bribes de contenus ainsi obtenues de différents serveurs sont ensuite assemblées en une page unique, servie à l'internaute. La grande force de cette approche est qu'elle est totalement agnostique technologiquement, capable d'intégrer n'importe quelles applications web, sans demander la moindre modification de l'existant. ESIGate peut aussi être configuré pour extraire des bribes de contenus au sein des pages existantes. Dans ce cas, il est possible d'insérer des commentaires HTML, afin de parfaitement délimiter les blocs à extraire.

ESIGate est distribué sous la licence Apache. ESIGate est écrit en Java et fonctionne en acceptant plusieurs syntaxes, soit à base de taglibs JSP, soit en utilisant les tags de la norme ESI définie par Akamai pour son Content Delivery Network.

