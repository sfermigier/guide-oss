# Frameworks web (frontend)

Un framework frontend structure le code exécuté dans le navigateur : composants, état de l’interface, navigation, échanges avec le serveur. Il s’utilise le plus souvent avec TypeScript et un outil de construction.

Le choix engage sur plusieurs années, par les compétences, l’écosystème de composants et les migrations. La première question est celle du besoin : une application métier très interactive justifie un framework, alors qu’un site de contenu ou un formulaire peut se contenter de HTML rendu par le serveur, complété par une bibliothèque légère.

Les frameworks qui produisent le HTML côté serveur sont traités dans [Frameworks web (backend)](frameworks-web-backend.md) ; le mobile l’est dans [Frameworks mobiles](frameworks-mobiles-cross-platform.md).

## React

Site
: <https://react.dev/>

Porteur
: une fondation (React Foundation, Linux Foundation)

Licence
: MIT

React, bibliothèque d’interfaces créée chez Facebook, est passée en février 2026 sous la React Foundation, hébergée par la Linux Foundation. Meta n’en est plus propriétaire, mais compte parmi les membres fondateurs.

Elle décrit l’interface sous forme de composants et laisse à d’autres bibliothèques le routage, les données ou le rendu serveur. Son écosystème et le marché des compétences sont les plus larges de la catégorie.

Cette liberté oblige l’équipe à choisir et à maintenir un assemblage de dépendances, souvent à travers un framework comme Next.js. React est écrit en JavaScript.

## Vue

Site
: <https://vuejs.org/>

Porteur
: une communauté (projet d’Evan You)

Licence
: MIT

Vue est un framework progressif : on peut l’ajouter à une page existante ou construire une application complète avec ses outils officiels de routage et d’état.

Sa syntaxe proche du HTML facilite la prise en main et la reprise d’un code par des intégrateurs. Nuxt apporte le rendu serveur.

Vue est financé par des dons et des partenaires, sans entreprise dominante au capital du projet. Il est écrit en TypeScript.

## Angular

Site
: <https://angular.dev/>

Porteur
: une entreprise (Google)

Licence
: MIT

Angular est un framework complet de Google : composants, injection de dépendances, formulaires, routage et outillage sont fournis ensemble.

Il s’adresse aux grandes applications d’entreprise, où l’homogénéité entre équipes compte. Les versions majeures paraissent à un rythme régulier. Un outil automatise une partie des migrations.

La gouvernance et la feuille de route dépendent de Google. Angular est écrit en TypeScript.

## Svelte

Site
: <https://svelte.dev/>

Porteur
: une communauté

Licence
: MIT

Svelte compile les composants en JavaScript : le navigateur reçoit peu de code d’exécution. SvelteKit ajoute le routage et le rendu serveur.

Il convient aux équipes qui recherchent une syntaxe concise et un faible poids de page. Son écosystème de composants est plus réduit que celui de React. Svelte est écrit en JavaScript et TypeScript.

## htmx

Site
: <https://htmx.org/>

Porteur
: une communauté (projet Big Sky Software)

Licence
: Zero-Clause BSD

htmx permet d’échanger des fragments HTML avec le serveur à partir d’attributs placés sur les balises. La logique reste sur le serveur, dans le langage de l’équipe, sans étape de construction.

Il accompagne bien Django, Rails ou Symfony pour une application de gestion. Les interfaces qui travaillent hors ligne ou avec un état local riche lui conviennent moins. htmx est écrit en JavaScript.

## Autres

- Preact, variante légère de React (MIT) : <https://preactjs.com/>
- SolidJS, framework réactif sans DOM virtuel (MIT) : <https://www.solidjs.com/>
- Alpine.js, comportements dans le HTML (MIT) : <https://alpinejs.dev/>
- Lit, composants web (BSD 3-clauses) : <https://lit.dev/>
- Ember.js (MIT) : <https://emberjs.com/>
