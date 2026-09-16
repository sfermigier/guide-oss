VPN
===

Un VPN, Réseau Privé Virtuel en français, peut être défini, de manière assez large, comme les différentes techniques permettant d’étendre le Réseau de l’entreprise en préservant la confidentialité des données et en traversant les barrières physiques des réseaux traditionnels.

Les solutions VPN apportent généralement les bénéfices suivants : authentification par clé publique, confidentialité des échanges, confidentialité *a posteriori* en cas de compromission des secrets cryptographiques et transport de paquets à destination d’un réseau privé via un réseau public.

Dans l’univers de l’open source, on compte de nombreuses solutions de qualité, dont WireGuard et OpenVPN, présentées ci-après.


OpenVPN
-------

:Site: https://openvpn.net
:Porteur: un éditeur (OpenVPN Inc.)
:Licence: GPL v2

OpenVPN est le fer de lance d’une catégorie de VPN assez récente : les VPN SSL. Il existe depuis 2002 et a été écrit par James Yonan.

Ces derniers réutilisent les mécanismes du chiffrement SSL pour authentifier et chiffrer les connexions. OpenVPN est basé sur le produit OpenSSL, la principale implémentation libre du protocole SSL, tant en termes de qualité que d’adoption, et s’appuie sur ses routines de chiffrement et de vérification d’identité pour assurer une très bonne sécurisation des données.

Disponible sur l'ensemble des systèmes courants — Linux, BSD, macOS, Windows, Android, iOS —, il offre de nombreuses fonctions de sécurité et de contrôle : authentification par certificats, par mot de passe ou par double facteur, poussée de configuration réseau aux clients, et intégration à un annuaire d'entreprise. La version 2.6 a introduit le mode DCO (*Data Channel Offload*), qui déporte le chiffrement dans le noyau et réduit sensiblement l'écart de performance avec WireGuard.


WireGuard
---------

:Site: https://www.wireguard.com/
:Porteur: une communauté (Jason A. Donenfeld)
:Licence: GPL v2

Créé par Jason A. Donenfeld et intégré au noyau Linux depuis la version 5.6 (2020), WireGuard a profondément renouvelé le domaine du VPN.

Son parti pris est celui de la simplicité radicale : quelques milliers de lignes de code — contre plusieurs centaines de milliers pour les implémentations IPsec ou OpenVPN —, ce qui rend le code auditable ; une cryptographie moderne et non négociable (ChaCha20, Poly1305, Curve25519), qui supprime toute la complexité de négociation des algorithmes ; une configuration réduite à une paire de clés publiques et une liste d'adresses autorisées. Les performances et la rapidité d'établissement des tunnels sont très supérieures à celles des solutions précédentes, et l'itinérance entre réseaux est transparente.

Ses limites sont l'envers de ce choix : pas de gestion d'utilisateurs, pas d'attribution dynamique d'adresses, pas d'authentification par certificats. Ces fonctions sont apportées par des surcouches comme Tailscale/Headscale, NetBird ou Netmaker, qui en font une solution complète pour le télétravail.

WireGuard est disponible sur Linux, BSD, Windows, macOS, Android et iOS.


Libreswan et strongSwan (IPsec)
-------------------------------

:Site: https://libreswan.org/ et https://www.strongswan.org/
:Porteur: des communautés
:Licence: GPL v2

IPsec reste indispensable pour l'interconnexion de sites et l'interopérabilité avec les équipements réseau du marché, où il est le seul protocole universellement pris en charge.

Openswan, l'implémentation présentée dans les éditions précédentes de ce guide et descendante du projet FreeS/WAN (1999), n'est plus activement développée. Deux projets se partagent aujourd'hui ce rôle : **Libreswan**, fork d'Openswan désormais retenu par défaut par Red Hat et Debian, et **strongSwan**, l'autre grande implémentation IKEv2, très employée pour les accès nomades et l'authentification par certificats ou EAP.

Tous deux permettent d'établir des liens IPsec de site à site comme des accès pour clients nomades, et sont compatibles avec la grande majorité des équipements et solutions propriétaires.


Autres
------

- Tailscale et son serveur de coordination libre Headscale, qui simplifient radicalement le déploiement de WireGuard: https://tailscale.com/ et https://github.com/juanfont/headscale
- NetBird, alternative entièrement open source dans le même esprit: https://netbird.io/
- Nebula, réseau maillé chiffré créé par Slack: https://github.com/slackhq/nebula
- OpenVPN Access Server et Pritunl, pour l'administration centralisée d'OpenVPN: https://pritunl.com/

