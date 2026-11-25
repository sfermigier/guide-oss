# Outils de développement

Cette section présente les outils utiles aux développements d’applications, web notamment.

On y trouve des outils de gestion de projet comme Redmine, des forges logicielles comme GitLab, Forgejo ou Tuleap, des gestionnaires de tickets comme MantisBT, des environnements de développement comme Eclipse ou Visual Studio Code et des outils de gestion de sources comme Git.

Comme on le voit, l’open source offre d’excellentes briques de développement pour bâtir des projets ambitieux dans des conditions optimales.

## Forges (plateformes collaboratives de développement) et bug trackers

### Redmine

Site
: <https://www.redmine.org>

Porteur
: une communauté

Licence
: GPL v2

Redmine est un outil collaboratif permettant, à travers une interface web sécurisée, de gérer des projets. Il a été créé par Jean-Philippe Lang en 2006. C'est l'un des rares outils de gestion de projet open source à avoir traversé vingt ans sans rupture, encore très déployé en entreprise.

Redmine offre les fonctionnalités suivantes :

- gestion multi-projets sécurisée
- gestion des utilisateurs, des profils et des droits, en fonction de chaque projet
- gestion de documents, classement par catégorie, propriétaire, titre, date, etc.
- gestion des demandes, de leur statut, de leur priorité et de leur historique, assignation de ces demandes aux acteurs pertinents du projet.
- visualisation de l’actualité du projet sous forme de diagramme de Gantt
- notification par mail ou par flux RSS
- etc.

Redmine a été développé en Ruby sur la base du framework Ruby on Rails.

### Tuleap

Site
: <https://www.tuleap.com/>

Porteur
: un éditeur (Enalean)

Licence
: GPL

Tuleap est une Suite Logicielle open source qui fournit les outils nécessaires aux entreprises pour un développement logiciel et une collaboration efficace. Également appelée Forge Logicielle ou ALM (application life cycle management), Tuleap a été développée par la société Enalean.

Tuleap est un logiciel utilisé par plusieurs dizaines de milliers d'utilisateurs dans le monde pour leurs développements professionnels, dans de grandes entreprises telles que STMicroelectronics, ST-Ericsson ou encore Orange. Tuleap est une suite ALM complète : tracking de bugs, de tests, de risques, etc, gestion de versions, intégration continue, gestion documentaire, outils de collaboration, etc.

L'éditeur de Tuleap, Enalean, est une société française qui a fondé son modèle économique sur le support et les services professionnels.

Tuleap est écrit majoritairement en PHP.

### GitLab Community Edition

Site
: <https://about.gitlab.com/>

Porteur
: un éditeur (GitLab Inc.)

Licence
: MIT pour l'édition communautaire, propriétaire pour le répertoire `ee/` de l'édition Enterprise

Né en 2011, GitLab est la forge auto-hébergeable la plus complète : dépôts Git, revue de code, tickets, wiki, intégration et déploiement continus, registres de paquets et d'images de conteneurs.

L'ensemble est cohérent et couvre à lui seul la chaîne de développement d'une organisation. La contrepartie est le coût d'exploitation : une instance demande au moins 8 Go de mémoire, agrège de nombreux composants (PostgreSQL, Redis, Gitaly, Sidekiq) et doit suivre des versions mensuelles.

GitLab est un cas typique d'*open core*. Le code est public, mais une partie des fonctions (gouvernance, sécurité, gestion de portefeuille) relève des abonnements Premium et Ultimate. L'édition Enterprise est proposée par défaut à l'installation ; pour n'utiliser que du code libre, il faut choisir explicitement les paquets de la Community Edition.

GitLab est écrit principalement en Ruby on Rails, avec des composants en Go et une interface en Vue.js.

### Forgejo

Site
: <https://forgejo.org/>

Porteur
: une communauté, hébergée par une association (Codeberg e.V.)

Licence
: GPL v3+ depuis la version 9 (MIT auparavant)

Forgejo est une forge légère, issue d'un fork de Gitea lancé fin 2022 à la suite du transfert de celui-ci à une société commerciale. Ses noms de domaine sont détenus par l'association allemande Codeberg e.V., dont la plateforme publique codeberg.org l'utilise ; la gouvernance du projet en reste distincte.

Il offre dépôts Git, tickets, demandes de fusion, wiki, registre de paquets et une intégration continue, Forgejo Actions, dont la syntaxe est proche de celle de GitHub Actions. Il se déploie sous la forme d'un binaire unique, avec SQLite, PostgreSQL ou MySQL, ce qui le rend adapté aux petites et moyennes équipes.

Le code est désormais indépendant de celui de Gitea. La migration depuis les versions récentes de ce dernier n'est plus garantie. Forgejo n'a pas d'édition commerciale : le support repose sur la communauté et sur des prestataires.

Forgejo est écrit en Go.

### MantisBT

Site
: <https://www.mantisbt.org>

Porteur
: une communauté

Licence
: GPL v2

MantisBT est un outil web très populaire de suivi de tickets (anomalies, demandes d'évolutions, demandes d'intervention, ...), adapté à tous types de projets. Kenzaburo Ito, initiateur du projet en novembre 2000, est rapidement rejoint en 2002 par Jeroen Latour, Victor Boctor et Julian Fitzell pour constituer le cœur de l'équipe de développement.

MantisBT permet une répartition des tickets par projet. Il est également possible de qualifier les demandes suivant différents critères (type, catégorie, sévérité, priorité, privé/public). L'outil dispose notamment de fonctionnalités comme : un workflow d’enchaînement d'états paramétrables, un système de notification, un formulaire de recherche de tickets avec filtres, une page personnalisée pour chaque utilisateur listant les tickets dont il est l'auteur ainsi que les tickets qui lui sont assignés, une gestion de droits utilisateurs, une rubrique d'administration par projet permettant d'ajouter/supprimer des utilisateurs au projet, la création de sous projets, etc.

MantisBT est développé en PHP et nécessite l'utilisation d'une base de données (MySQL, PostgreSQL, MS SQL ou DB2). Il est principalement testé pour les serveurs Web Apache et IIS.

### Autres

- Gitea, forge légère écrite en Go: <https://about.gitea.com/>
- OpenProject (gestion de projet et de portefeuille): <https://www.openproject.org/>
- Trac: <https://trac.edgewall.org/>
- Pagure: <https://pagure.io/pagure>
- SourceHut: <https://sourcehut.org/>

## Gestion de source

### Git

Site
: <https://git-scm.com>

Porteur
: une communauté

Licence
: GPL v2

Git est un système de gestion de versionnement décentralisé (DVCS). Il est notamment utilisé pour le noyau Linux ou pour PHP. C'est un logiciel libre créé par Linus Torvalds en 2005.

Git permet notamment de "commiter" localement puis de pousser aux autres développeurs un ensemble de commits locaux. Il permet également d'utiliser un workflow de développement en soumettant par exemple l'envoi de code à l'approbation d'un des développeurs. La faculté de Git à créer des branches facilement ainsi que de permettre leur administration de façon simple en fait un outil de choix dans le cadre de développement de projets open source.

Git est distribué sous la licence GPL v2.

Git est écrit en C, Bourne Shell et Perl.

### Mercurial

Site
: <https://www.mercurial-scm.org/>

Porteur
: une communauté

Licence
: GPL

Mercurial est un logiciel de gestion de versions décentralisé (DVCS) disponible sur la plupart des systèmes Unix, Windows et Mac OS X.

Il a été créé pour s'utiliser via la ligne de commande, mais propose une intégration forte avec le bureau Windows (TortoiseHg), des interfaces graphiques avancées pour l'affichage de l'historique (HgView) et une interface web intégrée.

Ses principales caractéristiques sont sa capacité à gérer les gros projets, son fonctionnement complètement distribué ne nécessitant pas de serveur, sa gestion avancée des branches et des fusions, ainsi que la traçabilité de l'évolution de l'historique (*changeset evolution*).

Mercurial est écrit principalement en Python. Son usage a toutefois beaucoup reculé face à Git, notamment depuis l'abandon de sa prise en charge par les principaux hébergeurs : Mozilla, longtemps son utilisateur le plus visible, a fait de Git le dépôt de référence de Firefox en 2025. Il reste employé par des organisations attachées à son ergonomie.

## Environnement de développement intégrés

### Eclipse IDE

Site
: <https://www.eclipse.org>

Porteur
: une fondation (Eclipse)

Licence
: EPL (Eclipse Public License)

Eclipse est un environnement de développement extensible et polyvalent, initié par IBM en 2001 et porté depuis 2004 par la Fondation Eclipse.

Conçu autour d'une plateforme commune à laquelle s'agrègent des composants dérivatifs, le projet est ainsi constitué de nombreux sous-projets spécifiques aux technologies sous-jacentes. L’objectif de la solution Eclipse est de fournir des outils favorisant la productivité, mais pas seulement celle qui concerne le codage logiciel. On y trouve des environnements de développement intégré mais également de conception, de modélisation, de tests, de reporting, etc. Eclipse a beau être écrit en Java, il peut être utilisé pour développer sous de très nombreux langages de programmation.

Eclipse est écrit en Java. Le projet reste très vivant dans l'écosystème Java d'entreprise et sert de socle à de nombreux produits (outils de modélisation, BIRT, Jaspersoft Studio), même si, sur le poste des développeurs, la concurrence de Visual Studio Code et des environnements de JetBrains est désormais écrasante.

### Visual Studio Code / VSCodium

Site
: <https://code.visualstudio.com/> et <https://vscodium.com/>

Porteur
: un éditeur (Microsoft) et une communauté (VSCodium)

Licence
: MIT pour le code source

Visual Studio Code est devenu, en une dizaine d'années, l'environnement de développement le plus utilisé au monde, tous langages confondus. Son code source, publié par Microsoft sous licence MIT sous le nom de Code - OSS, en fait un logiciel libre ; les binaires distribués par Microsoft sont en revanche soumis à une licence propriétaire et intègrent de la télémétrie, tout comme la place de marché officielle des extensions, dont les conditions d'utilisation interdisent l'usage par les distributions tierces.

C'est la raison d'être de **VSCodium**, qui fournit des binaires compilés à partir des sources libres, sans télémétrie, s'appuyant sur la place de marché ouverte Open VSX. Les organisations soucieuses de maîtriser leur chaîne d'outils privilégieront cette distribution, ou des alternatives entièrement libres comme Neovim (<https://neovim.io/>) ou Emacs (<https://www.gnu.org/software/emacs/>).

## Génération de code / MDD

### Acceleo

Site
: <https://eclipse.dev/acceleo/>

Porteur
: une fondation (Eclipse)

Licence
: EPL (Eclipse Public License)

Acceleo est un générateur de texte et de code à partir de modèles (approche MDA, *Model Driven Architecture*), écrit en Java et issu de la société française Obeo. Il s'appuie sur les modèles EMF d'Eclipse et sur des gabarits. Le projet est maintenu, mais son usage se limite surtout à l'ingénierie dirigée par les modèles, où il accompagne des outils comme Capella.
