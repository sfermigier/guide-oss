# Portails { #portail }

Un portail réunit, derrière une page d’accueil personnalisée, des contenus et des services provenant de plusieurs applications : actualités internes, annuaire, outils métiers, démarches, documents.

L'enjeu est double : offrir un point d'entrée unique, avec une authentification et des droits cohérents et éviter de redévelopper ce que les applications agrégées font déjà.

Les portails à base de portlets (normes Java JSR-168 et JSR-286) ont largement cédé la place à des intranets construits sur des plateformes collaboratives (Nextcloud, XWiki), sur des CMS généralistes ou sur des applications front-end consommant des API. Les produits présentés ici ont tous suivi ce mouvement, en se repositionnant sur l'espace de travail numérique.

## eXo Platform

Site
: <https://www.exoplatform.com/>

Porteur
: un éditeur (eXo Platform)

Licence
: LGPL v3 et propriétaire

eXo est un éditeur français créé en 2003. L'entreprise possède des bureaux en France, aux États-Unis, au Vietnam et en Tunisie. Elle édite une suite logicielle de travail collaboratif et de gestion de contenus destinée aux entreprises.

Le produit s'est repositionné au fil des versions sur le créneau de l'espace de travail numérique : réseau social d'entreprise, espaces collaboratifs, gestion documentaire, wiki, agenda, messagerie instantanée et visioconférence, gamification, applications mobiles. Il s'adresse en particulier aux organisations publiques et aux entreprises soucieuses de souveraineté numérique. Il fait l'objet de déploiements de grande ampleur dans l'administration française.

eXo Platform est diffusé via un modèle de double licence : le code source et une version packagée (Community) sont librement accessibles sous licence LGPL v3, tandis que l'édition Enterprise est commercialisée par souscription.

eXo Platform est écrit en Java et s'appuie sur un dépôt de contenus conforme à la norme JCR (JSR-170/283).

## Silverpeas

Site
: <https://www.silverpeas.org/>

Porteur
: un éditeur (Silverpeas)

Licence
: Affero GPL v3

Silverpeas est un portail collaboratif et social. Développé à partir de 2001, la solution a connu une première vie dans le monde des logiciels propriétaires avant de passer en open source en 2011.

Silverpeas réunit les fonctions d'un portail (agrégation de ressources hétérogènes), d'un CMS (construction de mini-sites) et d'un outil collaboratif : gestion de projet avec diagramme de Gantt, agenda partagé, forum, blog, gestion documentaire et annuaire. Sa diffusion est essentiellement française.

Silverpeas est écrit en Java.

## Liferay

Site
: <https://www.liferay.com/>

Porteur
: un éditeur (Liferay, Inc)

Licence
: LGPL et propriétaire

Liferay est une solution de portail d'entreprise open source d’un très bon niveau qui permet, entre autres, l'agrégation de contenus et d'informations, le partage des ressources et la collaboration. Liferay a été créé en 2000 à l’origine pour une église américaine.

Liferay propose une palette d’outils collaboratifs (blog, forum, wiki, notifications), une gestion des communautés et de l'organisation hiérarchique, des droits fins, la personnalisation des pages et un mécanisme de pré-production (*staging*). Il convient à un portail interne, où il permet l'intégration standardisée des applicatifs existants.

Liferay est écrit en Java. Issu du monde des portlets, il s'appuie désormais sur une architecture modulaire OSGi, avec une orientation *headless* (API REST et GraphQL) et un client React. L'édition libre s'appelle Liferay Portal Community Edition (LGPL 2.1), l'édition commerciale Liferay DXP.

## Autres

Au-delà des produits présentés précédemment, on peut également citer les outils ci-dessous :

- Lutece, le portail open source de la Ville de Paris: <https://lutece.paris.fr/>
- XWiki, souvent employé comme socle d'intranet collaboratif (section [Blogs, wikis et forums](blog-wiki-et-forum.md)): <https://www.xwiki.org>
- Nextcloud Hub, pour les usages d'espace de travail numérique: <https://nextcloud.com/>

JBoss GateIn n'est plus maintenu. Le projet Apache Portals (Pluto, Jetspeed) a été retiré à l'*Attic* de la fondation Apache.
