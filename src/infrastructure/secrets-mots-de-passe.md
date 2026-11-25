# Secrets et mots de passe d'équipe

Deux besoins voisins sont réunis ici. Le premier concerne les machines : clés d'API, mots de passe de bases de données, certificats, que les applications doivent obtenir sans qu'ils figurent dans un dépôt Git ou un fichier de configuration. Le second concerne les personnes : les mots de passe partagés au sein d'une équipe, souvent conservés faute de mieux dans un tableur.

Les outils diffèrent. Un gestionnaire de secrets s'adresse aux applications, par API, avec des droits fins, un journal d'audit et des identifiants à durée courte. Un coffre d'équipe s'adresse aux utilisateurs, par une extension de navigateur et une application mobile, avec un chiffrement réalisé sur le poste. Les coffres strictement individuels, comme KeePassXC, sont présentés à la page [Sécurité du poste](../poste-client-bureautique/securite-du-poste.md).

Ces services concentrent les accès les plus sensibles. Leur sauvegarde, la conservation hors ligne des clés de récupération et une procédure de secours testée font partie du projet. L'authentification unique réduit par ailleurs le nombre de mots de passe à gérer : voir [Authentification, fédération et gestion d’identité](authentification-federation-et-gestion-identite.md).

## OpenBao

Site
: <https://openbao.org/>

Porteur
: une fondation (OpenSSF, Linux Foundation)

Licence
: MPL 2.0

OpenBao est le fork communautaire de HashiCorp Vault, lancé à la suite du passage de ce dernier sous licence BUSL en 2023. D'abord hébergé par LF Edge, il a rejoint en juin 2025 l'*Open Source Security Foundation*.

Il stocke des secrets versionnés, délivre à la demande des identifiants temporaires (bases de données, SSH), gère une autorité de certification interne et chiffre à la volée les données des applications. Les clients s'authentifient par jeton, OpenID Connect, LDAP, certificat ou compte de service Kubernetes. Chaque accès est journalisé.

Il conserve une grande compatibilité avec l'API de Vault dans sa version antérieure au changement de licence ; les évolutions ultérieures des deux produits divergent. Le déverrouillage (*unseal*) et la conservation des clés sont à organiser dès le départ.

OpenBao est écrit en Go.

## Vaultwarden

Site
: <https://github.com/dani-garcia/vaultwarden>

Porteur
: une communauté

Licence
: AGPL v3

Vaultwarden est une réimplémentation indépendante de l'API du serveur Bitwarden, compatible avec les applications et extensions officielles de ce dernier.

Beaucoup plus léger que le serveur d'origine, il fonctionne dans un conteneur avec SQLite, MariaDB ou PostgreSQL. Il gère les organisations, les collections partagées, les pièces jointes, la double authentification et l'accès d'urgence. Les données sont chiffrées par les clients.

Le projet n'est pas affilié à Bitwarden et ne fait l'objet d'aucun support de sa part. Une évolution des clients officiels peut imposer une mise à jour du serveur : il faut suivre les versions et ne pas exposer l'interface d'administration.

Vaultwarden est écrit en Rust.

## Passbolt

Site
: <https://www.passbolt.com/>

Porteur
: un éditeur (Passbolt SA)

Licence
: AGPL v3

Passbolt est un gestionnaire de mots de passe conçu pour les équipes, édité par une société luxembourgeoise.

Le chiffrement repose sur OpenPGP : chaque utilisateur possède une paire de clés. Un mot de passe partagé est chiffré pour chacun de ses destinataires. Le partage se règle par personne ou par groupe. Une API permet l'automatisation. Des extensions de navigateur et des applications mobiles sont fournies.

L'éditeur distingue une édition Community gratuite et des éditions payantes qui ajoutent notamment la synchronisation avec l'annuaire, l'authentification unique et des fonctions d'audit. La clé privée de l'utilisateur est nécessaire à l'accès : sa sauvegarde doit faire partie de l'accueil des nouveaux arrivants.

Passbolt est écrit en PHP (CakePHP) et JavaScript.

## Autres

- SOPS, chiffrement de fichiers de secrets versionnés dans Git (MPL 2.0) : <https://getsops.io/>
- External Secrets Operator, synchronisation de secrets vers Kubernetes (Apache 2.0) : <https://external-secrets.io/>
- TeamPass, gestionnaire collaboratif en PHP (GPL v3) : <https://teampass.net/>
- Psono, gestionnaire auto-hébergeable pour équipes (Apache 2.0) : <https://psono.com/>
- Infisical, gestion de secrets pour développeurs (MIT, avec un répertoire `ee/` sous licence commerciale) : <https://infisical.com/>
