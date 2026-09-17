Portail
=======

Un portail est un site qui réunit différentes ressources, soit autour d’un même thème (portail immobilier, portail d’emploi, …) soit sans thème particulier, c’est un portail généraliste, tel que Yahoo par exemple.

Un portail donne accès à des ressources qui ne lui appartiennent pas toutes : il propose des services relevant d’autres sites, sa valeur ajoutée propre étant dans la sélection et la réunion de ces outils.

Enfin, un portail intègre aussi une dimension de personnalisation, plus ou moins élaborée.

Alliance de contenus et bouquet de services, liens vers des ressources tierces, personnalisation : voilà qui définit généralement un portail.

Des outils open source sont disponibles pour permettre la réalisation de ce type de projet. On peut notamment citer Liferay, eXo Platform ou Silverpeas.

La notion de portail d'entreprise a toutefois beaucoup évolué depuis les premières éditions de ce guide : les portails à base de portlets JSR-168/286 ont largement cédé la place à des intranets construits sur des plateformes collaboratives (Nextcloud, XWiki), sur des CMS généralistes ou sur des applications front-end consommant des API. Les produits présentés ici ont d'ailleurs tous suivi ce mouvement, en se repositionnant sur la *digital workplace*.


eXo Platform
------------

:Site: https://www.exoplatform.com/
:Porteur: un éditeur français (eXo Platform)
:Licence: LGPL v3 et propriétaire

eXo est un éditeur français créé en 2003. L'entreprise possède des bureaux en France, aux États-Unis, au Vietnam et en Tunisie. Elle édite une suite logicielle de travail collaboratif et de gestion de contenus destinée aux entreprises.

Le produit s'est repositionné au fil des versions sur le créneau de la *digital workplace* : réseau social d'entreprise, espaces collaboratifs, gestion documentaire, wiki, agenda, messagerie instantanée et visioconférence, gamification, applications mobiles. Il s'adresse en particulier aux organisations publiques et aux entreprises soucieuses de souveraineté numérique, et fait l'objet de déploiements de grande ampleur dans l'administration française.

eXo Platform est diffusé via un modèle de double licence : le code source et une version packagée (Community) sont librement accessibles sous licence LGPL v3, tandis que l'édition Enterprise est commercialisée par souscription.

eXo Platform est écrit en Java et s'appuie sur un dépôt de contenus conforme à la norme JCR (JSR-170/283).


Silverpeas
----------

:Site: https://www.silverpeas.org/
:Porteur: un éditeur français (Silverpeas)
:Licence: Affero GPL v3

Silverpeas est un portail collaboratif et social. Développé à partir de 2001, la solution a connu une première vie dans le monde des logiciels propriétaires avant de passer en open source en 2011.

Silverpeas se distingue par un apport fonctionnel plutôt riche et une ergonomie d'ensemble assez confortable. Même si la visibilité du produit reste essentiellement nationale pour l'instant, Silverpeas est une alternative très intéressante pour construire rapidement un portail collaboratif simple. SilverPeas n'est pas qu’un portail, ni un CMS, ni un outil de travail collaboratif. En fait, il est à la croisée de tous ces mondes. C'est un portail, car il est capable d'agréger des ressources hétérogènes. C’est un CMS, car il permet de construire simplement des mini-sites avec une interface WYSIWYG simple. C’est un outil collaboratif, car il fournit des outils de gestion de projet avec tâches et visuel Gantt intégré, un agenda partagé, un forum, un blog ou encore un annuaire commun.

Silverpeas est écrit en Java, conforme aux normes JSR 168 et 286.


Liferay
-------

:Site: https://www.liferay.com/
:Porteur: un éditeur (Liferay, Inc)
:Licence: LGPL et propriétaire

Liferay est une solution de portail d'entreprise open source d’un très bon niveau qui permet, entre autres, l'agrégation de contenus et d'informations, le partage des ressources et la collaboration. Liferay a été créé en 2000 à l’origine pour une église américaine.

L’une des forces de Liferay est la facilité de personnalisation par l'utilisateur final. Liferay offre également plus de 60 portlets dont une palette complète d’outils collaboratifs et sociaux (blog, forum, wiki, centre de tâches, notifications, réservation de ressources, …), une gestion intuitive des communautés de pratiques et de l'organisation hiérarchique de l'entité qui l'emploie. Liferay est en outre d'une grande flexibilité pour la gestion des droits ou l’adaptation de l’apparence graphique des pages, et il propose un mécanisme de pré-production (*staging*). Il convient à un portail d'entreprise, où il permet l'intégration standardisée des applicatifs existants.

Liferay est écrit en Java. Historiquement conforme aux normes de portlets (JSR-168, JSR-286, puis JSR-362) et au dépôt de contenus JCR, il s'appuie désormais sur une architecture modulaire OSGi, avec une orientation *headless* (API REST et GraphQL) et un client React. L'édition libre s'appelle Liferay Portal Community Edition (LGPL 2.1), l'édition commerciale Liferay DXP.


Autres
------

Au-delà des produits présentés précédemment, on peut également citer les outils ci-dessous :

- Lutece, le portail open source de la Ville de Paris: https://lutece.paris.fr/
- XWiki, souvent employé comme socle d'intranet collaboratif (section :doc:`/web-communication/blog-wiki-et-forum`): https://www.xwiki.org
- Nextcloud Hub, pour les usages de *digital workplace*: https://nextcloud.com/
- Apache Pluto, implémentation de référence des portlets: https://portals.apache.org/pluto/

JBoss GateIn, cité dans les éditions précédentes, n'est plus maintenu : ses développements ont été absorbés d'un côté par eXo Platform, de l'autre par les produits commerciaux de Red Hat, aujourd'hui abandonnés.

