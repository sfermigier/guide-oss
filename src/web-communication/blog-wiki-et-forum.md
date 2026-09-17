# Blog, Wiki et Forum

On ne présente plus les blogs, wiki et forums tellement ils sont désormais intégrés à l’entreprise. On dit d’eux qu’ils sont une composante à part entière du Web 2.0.

Un blog est un type de site Web composé de billets (post), c'est-à-dire des notes agglomérées au fil du temps (classement par date).

Un wiki peut également être défini comme un type web mais sa particularité consiste en son ouverture vers les autres. En effet, les pages sont généralement modifiables par les visiteurs afin de permettre des contributions collaboratives.

Un forum est, quant à lui, un espace de discussion publique (généralement) ou les échanges sont archivés par sujet.

## Blogs

### Wordpress

Site
: <https://wordpress.org>

Porteur
: une communauté (WordPress Foundation) et un éditeur (Automattic)

Licence
: GPL v2+

WordPress a été créé en 2003 à la suite d'un fork du logiciel « b2 ». Développé initialement par Matt Mullenweg, il est devenu le logiciel le plus déployé du web : il motorise aujourd'hui une part considérable des sites existants, du blog personnel aux grands sites de médias.

WordPress est un outil de publication très complet, employé bien au-delà du blog pour la construction de sites web de toute nature. La version 3 (2010) avait intégré la gestion multi-sites issue de WordPress MU ; le tournant suivant est l'éditeur de blocs Gutenberg, introduit avec la version 5 (2018), qui a ouvert la voie à l'édition complète du site (*full site editing*) et aux thèmes par blocs. Le rythme de publication reste soutenu, avec plusieurs versions majeures par an.

Deux points appellent la vigilance. D'abord la surface d'attaque : l'immense écosystème d'extensions impose une politique de mise à jour rigoureuse. Ensuite la gouvernance : le projet reste très lié à la société Automattic et à son fondateur, et le conflit ouvert avec l'hébergeur WP Engine en 2024 en a rappelé la fragilité à une partie de la communauté.

WordPress est développé en PHP sur une base MySQL/MariaDB. Il dispose d'API REST et d'un système d'extensions très riche : des dizaines de milliers d'extensions sont disponibles.

### DotClear

Site
: <https://dotclear.org/>

Porteur
: une communauté

Licence
: GPL v2

Dotclear est un logiciel libre de publication web créé en 2002 par Olivier Meunier. C'est une solution conçue avant tout pour ses utilisateurs et recevant des contributions régulières de ceux-ci. Le projet, aujourd'hui animé par une petite équipe de bénévoles, poursuit un développement régulier et reste une alternative française légère à WordPress.

Dotclear dispose d'une richesse fonctionnelle faisant de lui un outil de publication de grande qualité, égalant et allant parfois plus loin que d'autres outils du même ordre. Au-delà des fonctionnalités, Dotclear est conçu pour apporter le maximum de confort à l'utilisateur : une installation automatisée qui ne comprend que 2 étapes. De plus, de nombreux thèmes et plugins sont disponibles pour le personnaliser facilement. Les pages générées ont une structure qui optimise leur référencement naturel.

DotClear2 est développé en PHP5 et supporte les bases PostgreSQL (8.0 minimum), MySQL (4.1 minimum avec InnoDB) et SQLite.

## Forums

### PhpBB

Site
: <https://www.phpbb.com>

Porteur
: une communauté

Licence
: GPL v2

PhpBB est un outil de la famille des forums. En plus des fonctions habituelles, PhpBB permet de créer des sondages, annonces et post-it, ces deux derniers restant en haut de la page pour être plus visibles.

Les émoticônes permettent de rendre plus visuel le contenu. Il gère un système d'avertissement optionnel par courriel de l'apparition d'une réponse au(x) sujet(s) que l'on choisit de surveiller. Si on accepte les cookies dans le navigateur, on peut voir rapidement où sont les nouveaux messages (c'est-à-dire ceux publiés depuis la dernière consultation de la page). Pour aller plus loin, un système de messages privés entre les utilisateurs, permet d'éviter la publication des adresses électroniques personnelles. Il permet l’utilisation du BBCode (code voisin du HTML) dans les messages pour une mise en forme enrichie. Graphiquement, le support de différents thèmes visuels est complet : la partie graphique est totalement séparée du logiciel en lui-même, et est donc personnalisable à volonté.

PhpBB repose sur une architecture LAMP. Il est écrit en PHP.

phpBB reste, avec SMF, l'un des derniers forums « classiques » largement déployés ; les projets récents lui préfèrent généralement Discourse, Flarum ou NodeBB.

### Discourse

Site
: <https://www.discourse.org/>

Porteur
: une entreprise (Civilized Discourse Construction Kit, Inc.)

Licence
: GPL v2

Créé en 2013 par Jeff Atwood (cofondateur de Stack Overflow), Discourse est devenu la référence des forums de discussion modernes : c'est le logiciel qui anime les communautés de la plupart des grands projets open source.

Il se distingue des forums classiques par son ergonomie (défilement infini, lecture en fil continu, édition en Markdown, aperçu en direct), par ses mécanismes de modération communautaire et de gestion de la confiance (*trust levels*), par son moteur de recherche intégré et par une intégration poussée au courriel (participation par simple réponse à une notification). Il sert aussi bien de forum public que de support client ou de liste de discussion interne.

Discourse est développé en Ruby on Rails et Ember.js, et s'appuie sur PostgreSQL et Redis.

### Autres

- Flarum (forum léger, PHP): <https://flarum.org>
- NodeBB (forum temps réel, Node.js): <https://nodebb.org>
- SMF (Simple Machines Forum): <https://www.simplemachines.org>
- PunBB: <https://punbb.informer.com>

## Wikis

### XWiki

Site
: <https://www.xwiki.org>

Porteur
: un éditeur (XWiki SAS)

Licence
: LGPL

La solution XWiki a été créée en 2004 par Ludovic Dubost. Elle est aujourd’hui essentiellement portée par la société XWiki.

Wiki applicatif de seconde génération, XWiki est utilisé pour du travail collaboratif, du partage d'informations, ou encore la mise en ligne de contenu structuré ou non. En plus des fonctionnalités wiki usuelles (mise-en-forme facilitée, gestion des droits d'accès, édition collaborative...), il offre la possibilité de programmer au sein même des pages du wiki. C'est ce qui en fait un wiki applicatif, c'est-à-dire capable d'évoluer en fonction des besoins de ses utilisateurs.

XWiki est développé en Java sur une base Hibernate. Les langages de script utilisables au sein du wiki sont Velocity et Groovy, et l'extensibilité passe par un dépôt d'extensions bien fourni. Le produit est fréquemment employé comme socle d'intranet ou comme alternative à Confluence. La société XWiki SAS, éditrice du projet, développe également CryptPad, suite collaborative chiffrée de bout en bout.

### PmWiki

Site
: <http://www.pmwiki.org/>

Porteur
: Une communauté

Licence
: GPL v2

PmWiki est un moteur de wiki libre programmé par Patrick Michaud. Il utilise le language PHP et ne nécessite pas de base de données.

L'approche de PmWiki est d'être centré sur les rédacteurs plutôt que les lecteurs, ce qui implique certaines limites aux documents rédigés, notamment dans leur présentation. PmWiki se concentre également sur un nombre de fonctionnalités répondant à des besoins bien spécifiques plutôt que des choses identifiées comme "pouvant être utiles". Ce ce fait, PmWiki dispose d'un champ fonctionnel réduit mais extremement pointu. L'approche modulaire de PmWiki permet également à chacun de se créer et de partager une fonctionnalité qu'il trouve intéressante.

### Foswiki (issu de TWiki)

Site
: <https://foswiki.org>

Porteur
: une communauté

Licence
: GPL v3

TWiki, wiki d'entreprise écrit en Perl, a connu en 2008 une scission : l'essentiel de ses développeurs a quitté le projet, à la suite d'un désaccord sur sa gouvernance, pour fonder Foswiki. C'est ce dernier qui poursuit aujourd'hui le développement ; TWiki n'évolue pratiquement plus.

Foswiki peut être utilisé comme espace de travail collaboratif, base documentaire ou application de gestion structurée : sa force reste la définition de formulaires et de données structurées directement dans les pages, interrogeables ensuite comme une base de données.

Foswiki est composé de scripts Perl. Les contenus sont stockés dans des fichiers texte versionnés et mis en forme à la volée.

### Autres

- MediaWiki, le moteur de Wikipédia: <https://www.mediawiki.org>
- DokuWiki (sans base de données): <https://www.dokuwiki.org>
- MoinMoin: <https://moinmo.in/>
- BookStack (documentation structurée, PHP/Laravel): <https://www.bookstackapp.com>
- Wiki.js (Node.js): <https://js.wiki>
- Outline (base de connaissances en Markdown): <https://www.getoutline.com>
