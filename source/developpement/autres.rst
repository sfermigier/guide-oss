Autres
======

Dans cette dernière rubrique de la dimension « Développement et couches intermédiaires » nous présentons d’autres outils open source qui peuvent trouver leur intérêt dans les entreprises même s’il était difficile d’en faire une catégorie à part entière.

Nous présentons notamment Drools (un moteur de règles métier) et ESIGate (permettant la construction à la volée de pages à partir de fragments issus de technologies différentes).


Drools
------

:Site: https://kie.apache.org/
:Porteur: une fondation (Apache)
:Licence: Apache 2.0

Drools (anciennement JBoss Rules) est un système de gestion de règles métier utilisant un moteur d'inférence à chaînage avant.

L'utilisation d'un outil tel que Drools permet de faire évoluer des règles et des contraintes sans modifier le programme qui les applique. L'ensemble comprend le moteur de règles proprement dit, un moteur d'optimisation sous contraintes (OptaPlanner, devenu Timefold), un moteur de décision conforme à la norme DMN et un atelier d'édition des règles. Celles-ci peuvent être écrites en syntaxe technique (DRL) ou saisies sous forme de tables de décision, compréhensibles par des utilisateurs fonctionnels.

Le projet a quitté l'écosystème JBoss/Red Hat : Drools et jBPM ont été donnés à la fondation Apache, où ils sont développés depuis 2025 sous le nom d'**Apache KIE** (*Knowledge Is Everything*). Les anciennes adresses jboss.org/drools et jbpm.org redirigent désormais vers ce projet.


ESIGate
-------

:Site: https://github.com/esigate/esigate
:Porteur: une communauté
:Licence: Apache 2.0

ESIGate est un agrégateur de contenus web. Il a été créé par plusieurs ingénieurs spécialistes JEE de la société Smile. Son site esigate.org n'est plus en service et le projet n'évolue plus : la fiche est conservée pour mémoire, l'approche restant pertinente et pouvant être obtenue aujourd'hui via les modules ESI de Varnish, de nginx ou de Symfony (HttpCache), ou via les architectures de micro-frontends.

ESIGate peut s'interfacer à des serveurs existants, dont il récupère les pages HTML à la volée. Les différentes bribes de contenus ainsi obtenues de différents serveurs sont ensuite assemblées en une page unique, servie à l'internaute. La grande force de cette approche est qu'elle est totalement agnostique technologiquement, capable d'intégrer n'importe quelles applications web, sans demander la moindre modification de l'existant. ESIGate peut aussi être configuré pour extraire des bribes de contenus au sein des pages existantes. Dans ce cas, il est possible d'insérer des commentaires HTML, afin de parfaitement délimiter les blocs à extraire.

ESIGate est distribué sous la licence Apache. ESIGate est écrit en Java et fonctionne en acceptant plusieurs syntaxes, soit à base de taglibs JSP, soit en utilisant les tags de la norme ESI définie par Akamai pour son Content Delivery Network.

