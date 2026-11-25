# Déploiement de postes

Le déploiement de postes consiste à installer un système sur des machines, puis à y distribuer logiciels et mises à jour. Deux méthodes coexistent : le **clonage** d'une image de référence, rapide et fidèle mais lié au matériel et à entretenir ; l'**installation automatisée** depuis le réseau, plus souple, complétée par un outil de gestion de configuration.

Le démarrage par le réseau (PXE) est commun à la plupart des solutions et suppose de maîtriser le service [DHCP](dns-dhcp.md). L'inventaire du parc est traité à la page [Gestion de parc et inventaires](gestion-de-parc-et-inventaires.md), la configuration des serveurs à la page [Déploiement](../devops/deploiement.md).

Une image de poste n'est pas une sauvegarde : pour les données des utilisateurs, on se reportera à la page [Sauvegarde](sauvegarde.md).

## Clonezilla

Site
: <https://clonezilla.org>

Porteur
: une communauté

Licence
: GPL v2

Clonezilla est un outil de clonage et d'imagerie de disque. Il copie un disque ou une partition vers un autre, ou vers une image conservée pour un usage ultérieur.

Clonezilla Live démarre depuis une clé USB ou le réseau et traite une machine à la fois ; les éditions serveur restaurent une image sur de nombreuses machines simultanément, en multidiffusion. Les systèmes de fichiers courants de Linux, Windows et macOS sont reconnus et seuls les blocs utilisés sont copiés. Le démarrage UEFI est pris en charge.

L'interface, en mode texte, s'adresse à des techniciens. La cible doit en général être au moins aussi grande que la source. Un système Windows cloné à plusieurs exemplaires doit être généralisé au préalable (Sysprep).

Clonezilla est écrit principalement en Shell et s'appuie sur Partclone.

## FOG Project

Site
: <https://fogproject.org/>

Porteur
: une communauté

Licence
: GPL v3

FOG est un serveur d'imagerie de postes par le réseau.

À partir d'une interface web, on enregistre les machines, on capture une image et on la déploie à un ou plusieurs postes démarrés par PXE, en multidiffusion si nécessaire. Un agent optionnel assure le renommage, la jonction au domaine, l'installation de logiciels et des tâches planifiées. Windows est la cible principale ; Linux et macOS sont possibles.

Le serveur s'installe sous Linux. L'isolation du réseau de déploiement et la protection des images, qui peuvent contenir des secrets, sont à prévoir, de même que le comportement des postes avec Secure Boot.

FOG est écrit en PHP, Shell et C#.

## Partimage

Site
: <https://www.partimage.org>

Porteur
: une communauté

Licence
: GPL v2

Partimage sauvegarde une partition dans une image. Sa dernière version date de 2010 ; il ne gère ni ext4 ni les systèmes de fichiers récents. Il est mentionné pour mémoire : utilisez Clonezilla.

## Autres

- opsi, gestion de postes Windows, Linux et macOS, d'origine allemande (cœur libre, extensions payantes) : <https://opsi.org/>
- Foreman, installation et cycle de vie des machines (GPL v3) : <https://theforeman.org/>
- Cobbler, serveur d'installation automatisée de Linux (GPL v2) : <https://cobbler.github.io/>
- MAAS, installation de serveurs physiques, édité par Canonical (AGPL v3) : <https://canonical.com/maas>
- Rescuezilla, clonage de disque avec interface graphique (GPL v3) : <https://rescuezilla.com/>
- Ventoy, clé USB amorçable contenant plusieurs images ISO (GPL v3) : <https://www.ventoy.net/>
- netboot.xyz, menu pour installer des systèmes par le réseau (Apache 2.0) : <https://netboot.xyz/>
- Munki, distribution de logiciels sur macOS (Apache 2.0) : <https://www.munki.org/munki/>
- **dd** (copie bas niveau) et **rsync** (synchronisation de fichiers), pour les cas simples
