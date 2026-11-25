# Blogs, wikis et forums { #blog-wiki-et-forum }

Blogs, wikis et forums répondent à trois besoins distincts : publier, documenter à plusieurs et discuter. En entreprise, le blog sert la communication externe ou interne, le wiki la base de connaissances et le forum l’entraide ou le support.

Un blog est un site composé de billets datés, présentés du plus récent au plus ancien.

Un wiki est un site dont les pages sont modifiables par ses lecteurs, avec un historique des versions. Le choix d’un produit engage sur la durée, car la syntaxe et la structure des pages rendent les migrations coûteuses.

Un forum est un espace de discussion où les échanges sont archivés par sujet, donc retrouvables, à la différence d’une messagerie instantanée.

## Blogs

### WordPress

Site
: <https://wordpress.org>

Porteur
: une communauté (WordPress Foundation) et un éditeur (Automattic)

Licence
: GPL v2+

WordPress a été créé en 2003 à la suite d'un fork du logiciel « b2 ». Développé initialement par Matt Mullenweg, il est devenu le logiciel le plus déployé du web : il motorise aujourd'hui une part considérable des sites existants, du blog personnel aux grands sites de médias.

WordPress est un outil de publication très complet, employé bien au-delà du blog pour la construction de sites web de toute nature. La version 3 (2010) avait intégré la gestion multi-sites issue de WordPress MU ; le tournant suivant est l'éditeur de blocs Gutenberg, introduit avec la version 5 (2018), qui a ouvert la voie à l'édition complète du site (*full site editing*) et aux thèmes par blocs. Le rythme de publication reste soutenu, avec plusieurs versions majeures par an.

Deux points appellent la vigilance. D'abord la surface d'attaque : l'immense écosystème d'extensions impose une politique de mise à jour rigoureuse. Ensuite la gouvernance : le projet reste très lié à la société Automattic et à son fondateur. Le conflit ouvert avec l'hébergeur WP Engine en 2024 en a rappelé la fragilité à une partie de la communauté.

WordPress est développé en PHP sur une base MySQL/MariaDB. Il dispose d'API REST et d'un système d'extensions très riche : des dizaines de milliers d'extensions sont disponibles.

### Dotclear

Site
: <https://dotclear.org/>

Porteur
: une association (Association Dotclear)

Licence
: AGPL v3

Dotclear est un moteur de blog créé en 2002 par Olivier Meunier. Le projet est aujourd'hui porté par l'association Dotclear et poursuit un développement régulier.

Il couvre les besoins du blog et s'y tient : multi-blogs et multi-utilisateurs avec gestion des droits, pages statiques, médiathèque, antispam intégré, commentaires, thèmes et plugins, édition en syntaxe wiki, en Markdown ou en WYSIWYG. Sa communauté est surtout francophone et son catalogue d'extensions bien plus réduit que celui de WordPress.

Dotclear est écrit en PHP et fonctionne avec plusieurs types de bases de données.

## Forums

### phpBB

Site
: <https://www.phpbb.com>

Porteur
: une communauté

Licence
: GPL v2

phpBB est un logiciel de forum. Outre les fonctions habituelles (catégories, sujets, modération, messages privés, notifications par courriel), il propose sondages, annonces, sujets épinglés et thèmes graphiques. La mise en forme des messages passe par le BBCode.

phpBB reste, avec SMF, l'un des derniers forums « classiques » largement déployés ; les projets récents lui préfèrent généralement Discourse, Flarum ou NodeBB.

phpBB est écrit en PHP et s'installe sur une pile LAMP.

### Discourse

Site
: <https://www.discourse.org/>

Porteur
: une entreprise (Civilized Discourse Construction Kit, Inc.)

Licence
: GPL v2

Créé en 2013 par Jeff Atwood (cofondateur de Stack Overflow), Discourse est devenu la référence des forums de discussion modernes : c'est le logiciel qui anime les communautés de la plupart des grands projets open source.

Il se distingue des forums classiques par son ergonomie (défilement infini, lecture en fil continu, édition en Markdown, aperçu en direct), par ses mécanismes de modération communautaire et de gestion de la confiance (*trust levels*), par son moteur de recherche intégré et par une intégration poussée au courriel (participation par simple réponse à une notification). Il sert aussi bien de forum public que de support client ou de liste de discussion interne.

Discourse est développé en Ruby on Rails et Ember.js et s'appuie sur PostgreSQL et Redis.

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

XWiki est développé en Java sur une base Hibernate. Les langages de script utilisables au sein du wiki sont Velocity et Groovy. L'extensibilité passe par un dépôt d'extensions bien fourni. Le produit est fréquemment employé comme socle d'intranet ou comme alternative à Confluence. La société XWiki SAS, éditrice du projet, développe également CryptPad, suite collaborative chiffrée de bout en bout.

### MediaWiki

Site
: <https://www.mediawiki.org>

Porteur
: une fondation (Wikimedia Foundation) et une communauté

Licence
: GPL v2+

MediaWiki est le moteur de Wikipédia et des autres projets de la fondation Wikimedia. Il est aussi utilisé par de nombreuses organisations pour leur documentation interne ou publique.

Il gère l'historique des pages, les discussions, les catégories, les modèles et un très grand nombre de langues. Plusieurs centaines d'extensions complètent le noyau, dont l'éditeur visuel et Semantic MediaWiki, qui ajoute des données structurées et interrogeables.

Deux limites sont à connaître. MediaWiki a été conçu pour des contenus ouverts : les droits de lecture par page ne font pas partie de son modèle. Un wiki à confidentialité fine s'appuiera plutôt sur XWiki. Les extensions doivent par ailleurs suivre le rythme des versions ; une version à support long (LTS) paraît tous les deux ans.

MediaWiki est écrit en PHP et s'appuie le plus souvent sur MySQL ou MariaDB.

### PmWiki

Site
: <https://www.pmwiki.net/>

Porteur
: une communauté

Licence
: GPL v2

PmWiki est un moteur de wiki créé par Patrick Michaud, écrit en PHP, qui se passe de base de données. Son noyau est volontairement réduit et s'étend par des recettes (*cookbook*). Il est toujours maintenu, mais son usage est devenu confidentiel : pour un nouveau projet, on évaluera d'abord DokuWiki, qui partage la même approche, ou BookStack.

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

- DokuWiki (sans base de données): <https://www.dokuwiki.org>
- MoinMoin: <https://moinmo.in/>
- BookStack (documentation structurée, PHP/Laravel): <https://www.bookstackapp.com>
- Wiki.js (Node.js): <https://js.wiki>
