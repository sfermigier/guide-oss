Messagerie instantanée et visioconférence
=========================================

La messagerie d’équipe et la visioconférence sont devenues, en quelques années, le système nerveux du travail quotidien. Elles ont largement remplacé le courriel pour les échanges courts et la réunion physique pour la coordination à distance.

C’est aussi la catégorie où la dépendance à quelques fournisseurs américains est la plus forte — Slack, Microsoft Teams, Zoom, Google Meet — et où elle est la plus problématique : ces outils transportent l’essentiel des échanges informels d’une organisation, c’est-à-dire ce qu’elle a de plus sensible et de moins formalisé. Les questions de conformité au RGPD, de confidentialité des délibérations et de réversibilité s’y posent donc avec une acuité particulière, ce qui explique l’intérêt marqué du secteur public européen pour les solutions présentées ici.

Trois familles de protocoles structurent l’offre open source :

- **Matrix**, protocole de communication fédérée et chiffrée de bout en bout, conçu dès l’origine pour l’interopérabilité entre organisations ;
- **XMPP**, plus ancien, plus léger, toujours très présent dans les usages d’infrastructure et l’internet des objets ;
- **WebRTC**, qui n’est pas un protocole de messagerie mais la brique de transport audio et vidéo temps réel des navigateurs, sur laquelle reposent toutes les solutions de visioconférence de cette section.

La frontière entre les deux domaines s’estompe : les messageries intègrent l’appel vidéo, les outils de visioconférence intègrent le fil de discussion. Nous les traitons néanmoins séparément, parce que les critères de choix restent distincts — la conversation écrite se juge sur la durée et l’organisation de la mémoire collective, la visioconférence sur la qualité de service et la capacité de montée en charge.


Messagerie d’équipe
~~~~~~~~~~~~~~~~~~~

Element et Matrix
-----------------

:Site: https://matrix.org/ et https://element.io/
:Porteur: une fondation (The Matrix.org Foundation) et un éditeur (Element)
:Licence: Apache 2.0 pour la spécification, AGPL v3 pour Synapse et pour les clients Element

Matrix est un protocole ouvert de communication décentralisée, créé en 2014 et normalisé par la fondation Matrix.org. Sa particularité est la fédération : à l’image du courriel, chaque organisation héberge son propre serveur et les utilisateurs de serveurs différents conversent sans passer par une plateforme centrale. Le chiffrement de bout en bout est actif par défaut, y compris pour les conversations de groupe.

L’implémentation de référence du serveur est **Synapse**, écrite en Python ; Dendrite et Continuwuity en proposent des alternatives plus légères. Le client de référence est **Element**, disponible en web, bureau, Android et iOS, édité par la société britannique éponyme (ex-New Vector), qui commercialise par ailleurs une distribution clés en main, Element Server Suite.

L’écosystème de passerelles (*bridges*) est un atout décisif en phase de transition : il permet de relier un salon Matrix à Slack, Teams, WhatsApp, IRC ou XMPP, et donc de migrer progressivement sans couper les échanges avec l’extérieur. La visioconférence est assurée par Element Call, fondé sur MatrixRTC et LiveKit.

C’est la solution retenue par plusieurs administrations européennes pour leur messagerie interne, dont l’État français avec **Tchap** (https://tchap.gouv.fr/), une déclinaison de Synapse et d’Element dont les dépôts sont publics et publiés sous AGPL v3.

Un point d’attention pour les intégrateurs : Synapse et les clients Element sont passés de la licence Apache 2.0 à l’AGPL v3 fin 2023, ce qui change les obligations en cas de réutilisation dans un produit tiers.


Mattermost
----------

:Site: https://mattermost.com/
:Porteur: un éditeur (Mattermost, Inc.)
:Licence: AGPL v3 pour le code source, à l’exception des modules « enterprise » sous licence propriétaire ; binaires officiels sous MIT

Lancé en 2015, Mattermost est l’une des alternatives à Slack les plus déployées en entreprise, en particulier dans les environnements soumis à de fortes contraintes de sécurité : administrations, défense, industrie, équipes de développement travaillant sur des réseaux isolés.

Son périmètre dépasse la conversation : canaux publics et privés, fils de discussion, recherche, applications mobiles et bureau, intégrations avec les forges et les chaînes d’intégration continue, et surtout les *playbooks*, qui permettent de dérouler des procédures d’exploitation (gestion d’incident, revue de sécurité) directement dans l’outil. L’extensibilité passe par un système de greffons et une API REST complète.

Le modèle de diffusion mérite d’être lu attentivement : l’édition Team, gratuite, couvre les usages courants, tandis que la conformité avancée, la haute disponibilité et l’authentification unique relèvent des éditions payantes.

Mattermost est écrit en Go pour le serveur et en React pour l’interface, et s’appuie sur PostgreSQL.


Rocket.Chat
-----------

:Site: https://www.rocket.chat/
:Porteur: un éditeur (Rocket.Chat Technologies)
:Licence: MIT, à l’exception des répertoires de l’édition entreprise

Créé en 2015, Rocket.Chat se distingue de ses concurrents par son orientation **omnicanale** : au-delà de la messagerie interne, il agrège les conversations venues du site web de l’organisation, de WhatsApp, de Facebook Messenger, du courriel ou du SMS dans une même interface d’agent. C’est donc autant un outil de relation client qu’une messagerie d’équipe.

Il propose les fonctions attendues du domaine (canaux, fils, messages vocaux, partage de fichiers, applications mobiles), une place de marché d’applications, la fédération via Matrix, et une visioconférence intégrée qui s’appuie sur Jitsi.

Rocket.Chat est écrit en JavaScript (Node.js, Meteor) et s’appuie sur MongoDB.


Zulip
-----

:Site: https://zulip.com/
:Porteur: une entreprise (Kandra Labs)
:Licence: Apache 2.0

Zulip, né en 2012 et libéré en 2015 après son rachat par Dropbox, repose sur un parti pris d’organisation qui le rend difficilement comparable aux autres : la conversation y est structurée en **flux et sujets**, chaque message appartenant à un sujet nommé au sein d’un canal.

Ce qui ressemble à un détail change tout à l’usage. Là où un canal Slack ou Mattermost très actif devient illisible dès qu’on s’en absente quelques heures, un canal Zulip se relit sujet par sujet, comme une série de fils courts. C’est le choix le plus pertinent pour les équipes réparties sur plusieurs fuseaux horaires, pour les organisations qui travaillent en asynchrone et pour les grandes communautés open source, nombreuses à l’avoir adopté.

Autre différence notable, le modèle économique : il n’existe pas d’édition communautaire amputée, l’intégralité des fonctionnalités est publiée sous licence Apache 2.0, l’éditeur se rémunérant sur l’offre hébergée et le support.

Zulip est écrit en Python (Django) et s’appuie sur PostgreSQL.


Autres
------

Messageries fondées sur XMPP, protocole plus ancien mais toujours pertinent, notamment lorsque la légèreté prime :

- ejabberd, serveur XMPP de classe opérateur édité par la société française ProcessOne: https://www.ejabberd.im/
- Prosody, serveur XMPP réputé pour sa simplicité de configuration: https://prosody.im/
- Openfire, serveur XMPP Java de la fondation Ignite Realtime: https://www.igniterealtime.org/projects/openfire/

À signaler également :

- Nextcloud Talk, lorsque la messagerie doit s’intégrer à une suite collaborative existante: https://nextcloud.com/talk/
- Zulip, Mattermost et Rocket.Chat proposent tous une offre hébergée en Europe, ce qui constitue une étape intermédiaire pour les organisations qui ne souhaitent pas exploiter le service elles-mêmes.


Visioconférence
~~~~~~~~~~~~~~~

Jitsi Meet
----------

:Site: https://jitsi.org/
:Porteur: un éditeur (8x8)
:Licence: Apache 2.0

Héritier du client SIP Communicator lancé en 2003, Jitsi est passé chez Atlassian en 2015 puis chez l’américain 8x8 en 2018, qui continue d’en publier l’intégralité du code sous licence Apache 2.0.

Jitsi Meet est la solution de visioconférence open source la plus répandue, et la plus immédiate à mettre en œuvre : aucune installation ni création de compte n’est nécessaire côté participant, un lien suffit. Le serveur de mixage (Jitsi Videobridge) fonctionne en mode SFU, ce qui lui permet de tenir des réunions de plusieurs dizaines de participants sur un matériel modeste ; le composant Jibri assure l’enregistrement et la diffusion en direct.

Son autre force est son intégration : Nextcloud, Rocket.Chat, Moodle et de nombreux autres produits proposent un connecteur Jitsi natif. C’est également la brique retenue par de nombreuses instances publiques de visioconférence libre, dans l’enseignement supérieur comme dans le milieu associatif.

Jitsi est écrit en Java pour le serveur et en JavaScript pour le client web.


BigBlueButton
-------------

:Site: https://bigbluebutton.org/
:Porteur: une entreprise canadienne (Blindside Networks) et une communauté
:Licence: LGPL v3

Développé depuis 2007, BigBlueButton n’est pas un outil de réunion généraliste mais une **plateforme de classe virtuelle**, et cette spécialisation fait toute sa valeur dans le contexte pédagogique.

On y trouve ce que les outils de réunion classiques ne proposent pas : tableau blanc collaboratif, partage de documents annotables par les participants, sondages et quiz, salles de sous-commission, prise de notes partagée, suivi de présence et statistiques d’engagement, enregistrement intégral rejouable. L’intégration aux plateformes d’apprentissage se fait par le standard LTI ou par des connecteurs dédiés pour Moodle, Chamilo ou Canvas, et l’interface d’administration Greenlight permet une utilisation autonome.

La contrepartie de cette richesse est une installation plus exigeante que celle de Jitsi, historiquement liée à une version précise d’Ubuntu Server. Plusieurs établissements d’enseignement et services publics français s’appuient sur cette solution.

BigBlueButton est écrit en Java, Scala et JavaScript.


La Suite Meet
-------------

:Site: https://github.com/suitenumerique/meet
:Porteur: une administration (DINUM, La Suite numérique)
:Licence: MIT

La Suite Meet est l’outil de visioconférence développé par la Direction interministérielle du numérique française dans le cadre de La Suite numérique, l’ensemble d’outils de travail de l’État — qui comprend également Docs pour l’édition collaborative et Drive pour le partage de fichiers.

Le produit s’appuie sur **LiveKit** pour le transport temps réel et vise explicitement le niveau de qualité des solutions propriétaires du marché : accès depuis le navigateur sans installation, salles persistantes, partage d’écran, sous-titrage et transcription. Son intérêt pour les organisations françaises est double : le code est publié sous licence MIT, donc réutilisable sans contrainte, et le produit est conçu et exploité par une administration soumise aux mêmes obligations que ses utilisateurs publics.

La Suite Meet est écrit en Python (Django) et en React.


Galène
------

:Site: https://galene.org/
:Porteur: une communauté (projet initié par Juliusz Chroboczek)
:Licence: MIT

Galène est un serveur de visioconférence écrit en Go, né à l’Université Paris Cité pendant la période des cours à distance, avec un objectif rare : fonctionner correctement sur un serveur modeste et sur des connexions médiocres.

Le pari est tenu — quelques dizaines de mégaoctets de mémoire suffisent là où les solutions concurrentes en réclament plusieurs gigaoctets — et le projet couvre les usages essentiels : salles avec droits différenciés (présentateur, opérateur, spectateur), partage d’écran, discussion écrite, enregistrement, diffusion vers un large public. L’installation se résume à un binaire et à un fichier de configuration.

C’est le choix à considérer pour une association, un laboratoire ou un établissement d’enseignement qui souhaite héberger sa propre visioconférence sans y consacrer d’infrastructure notable.


Autres
------

Briques d’infrastructure temps réel, à retenir pour bâtir une solution sur mesure plutôt que pour un déploiement clés en main :

- LiveKit, serveur SFU et jeu de SDK sous licence Apache 2.0, socle de La Suite Meet et d’Element Call: https://livekit.io/
- Janus, serveur WebRTC modulaire édité par l’italien Meetecho: https://janus.conf.meetecho.com/
- mediasoup, bibliothèque SFU pour Node.js: https://mediasoup.org/
- OpenVidu, plateforme complète bâtie au-dessus de LiveKit et de Kurento: https://openvidu.io/

Solutions intégrées à une suite collaborative :

- Nextcloud Talk, qui gère les petites réunions en pair-à-pair et s’appuie sur un serveur dédié (*High Performance Back-end*) au-delà: https://nextcloud.com/talk/
- Element Call, la visioconférence chiffrée de bout en bout de l’écosystème Matrix: https://element.io/

Voir également les sections :doc:`/web-communication/voip-telephonie` pour la téléphonie sur IP, :doc:`/web-communication/messagerie-email-groupware` pour la messagerie électronique et le travail collaboratif, et :doc:`/web-communication/reseaux-sociaux-entreprise-rse` pour les plateformes sociales d’entreprise.
