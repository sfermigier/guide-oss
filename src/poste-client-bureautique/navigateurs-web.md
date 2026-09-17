# Navigateurs web

Le navigateur est devenu l'application la plus utilisée du poste de travail, et celle qui traite les données les plus sensibles : sessions authentifiées sur les applications métier, moyens de paiement, messagerie, coffre-fort de mots de passe.

Son choix engage l'organisation à trois titres. Sur la **sécurité**, d'abord : c'est la principale surface d'attaque d'un poste bureautique, ce qui fait du rythme de correctifs et de la capacité à les déployer sans intervention de l'utilisateur un critère décisif. Sur la **gouvernance** ensuite : deux moteurs de rendu seulement subsistent réellement, Blink et Gecko, et la disparition du second ferait du web un standard de fait défini par un acteur unique. Sur la **conformité** enfin, car la configuration par défaut de la plupart des navigateurs transmet à leur éditeur des données de navigation qu'une organisation soumise au RGPD doit maîtriser.

Les trois navigateurs présentés ici s'administrent tous par stratégie d'entreprise (fichiers de politiques déployables par GPO, Intune, Ansible ou tout autre outil de gestion de parc), ce qui permet de figer les paramètres sensibles et de pré-installer les extensions autorisées.

## Firefox

Site
: <https://www.firefox.com/>

Porteur
: une fondation (Mozilla Foundation)

Licence
: MPL 2.0

Firefox est un navigateur web libre développé par la Fondation Mozilla et sa filiale, la Mozilla Corporation. Il utilise le moteur de rendu Gecko, qui met en œuvre les normes web actuelles et anticipées. Firefox est disponible pour Windows 10 et les versions ultérieures, macOS et Linux, ainsi que pour Android et iOS.

C'est, avec les navigateurs dérivés de Chromium, l'un des deux seuls moteurs de rendu encore réellement concurrents sur le poste de travail, ce qui en fait un enjeu d'indépendance technologique : tester un site sous Firefox, c'est vérifier qu'il respecte les standards plutôt que les particularités d'une seule implémentation.

Pour un déploiement en entreprise, la version **ESR** (*Extended Support Release*) est celle à retenir : elle conserve la même version majeure pendant environ un an en ne recevant que les correctifs de sécurité, ce qui découple les mises à jour du navigateur des cycles de validation des applications métier. Elle s'administre par le fichier `policies.json` ou par stratégie de groupe, avec plusieurs dizaines de paramètres verrouillables (télémétrie, synchronisation, extensions autorisées, certificats d'entreprise, page d'accueil).

Firefox est écrit en C++, Rust et JavaScript.

## Chromium

Site
: <https://www.chromium.org/>

Porteur
: une communauté, sous la conduite de Google

Licence
: BSD 3-clauses et licences tierces

Chromium est le projet open source dont sont issus Google Chrome, Microsoft Edge, Opera, Brave, Vivaldi et la plupart des navigateurs du marché : son moteur, Blink, équipe aujourd'hui l'écrasante majorité des postes de travail et des terminaux mobiles.

L'intérêt de la version Chromium elle-même, par rapport aux navigateurs commerciaux qui en dérivent, tient à ce qu'elle ne contient pas les services d'intégration et de télémétrie que ceux-ci ajoutent : pas de compte à connecter, pas de remontée d'usage par défaut. Les distributions Linux l'empaquettent directement, ce qui en fait le navigateur Blink le plus simple à maîtriser dans un parc.

Restent deux réserves. La gouvernance du projet reste de fait entre les mains de Google : la Linux Foundation a bien annoncé début 2025 un fonds de soutien aux navigateurs fondés sur Chromium, réunissant plusieurs acteurs de l'industrie, mais il s'agit d'un mécanisme de financement et non d'un transfert de la direction technique. Et le passage au format d'extensions *Manifest V3* a réduit les capacités des bloqueurs de contenu, ce qui a des conséquences pratiques sur la protection des postes.

Chromium est écrit en C++.

## LibreWolf

Site
: <https://librewolf.net/>

Porteur
: une communauté

Licence
: MPL 2.0

LibreWolf est un dérivé de Firefox durci, configuré d'emblée pour la confidentialité : télémétrie et services distants retirés à la compilation, protection renforcée contre le pistage et les empreintes numériques (*fingerprinting*), blocage de contenus intégré, effacement des données à la fermeture.

Sa raison d'être est d'éviter le travail de durcissement manuel, long et fragile, que suppose autrement l'obtention du même résultat. Le revers est assumé : certains sites mal conçus fonctionnent moins bien, la mise à jour suit celle de Firefox avec un léger décalage, et le projet repose sur une équipe réduite. Ces trois points sont à vérifier avant un déploiement à grande échelle.

C'est un bon candidat pour les postes traitant des données sensibles, en complément plutôt qu'en remplacement du navigateur principal du parc.

## Autres

- Ungoogled Chromium, équivalent de LibreWolf côté Blink : Chromium débarrassé de ses liens avec les services de Google: <https://github.com/ungoogled-software/ungoogled-chromium>
- Tor Browser, pour les usages exigeant l'anonymat des connexions: <https://www.torproject.org/>
- Falkon (KDE) et GNOME Web, navigateurs légers intégrés à leur environnement de bureau: <https://www.falkon.org/> et <https://apps.gnome.org/Epiphany/>

Rappelons enfin que Brave, Vivaldi et Opera, souvent cités parmi les alternatives, sont des produits propriétaires bâtis sur une base open source : leur code d'interface n'est pas entièrement publié et leur modèle économique repose sur des partenariats commerciaux qu'il convient d'examiner avant de les recommander dans une organisation.
