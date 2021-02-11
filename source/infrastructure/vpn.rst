VPN
===

Un VPN, Réseau Privé Virtuel en français, peut être défini, de manière assez large, comme les différentes techniques permettant d’étendre le Réseau de l’entreprise en préservant la confidentialité des données et en traversant les barrières physiques des réseaux traditionnels.

Les solutions VPN apportent généralement les bénéfices suivants : authentification par clé publique, confidentialité des échanges, confidentialité *a posteriori* en cas de compromission des secrets cryptographiques et transport de paquets à destination d’un réseau privé via un réseau public.

Dans l’univers de l’open source, on compte de nombreuses solutions de qualité dont OpenVPN et OpenSWAN présentés ci-après.


OpenVPN
-------

:Site: http://openvpn.net
:Porteur: un éditeur (OpenVPN Technologies)
:Licence: GPL v2

OpenVPN est le fer de lance d’une catégorie de VPN assez récente : les VPN SSL. Il existe depuis 2002 et a été écrit par James Yonan.

Ces derniers réutilisent les mécanismes du chiffrement SSL pour authentifier et chiffrer les connexions. OpenVPN est basé sur le produit OpenSSL, la principale implémentation libre du protocole SSL, tant en termes de qualité que d’adoption, et s’appuie sur ses routines de chiffrement et de vérification d’identité pour assurer une très bonne sécurisation des données.

Disponible sous Solaris, Linux, OpenBSD, FreeBSD, NetBSD, Mac OS X, Windows 2000, XP, Vista et 7, il offre aussi de nombreuses fonctions de sécurité et de contrôle.


OpenSwan
--------

:Site: https://www.openswan.org
:Porteur: une communauté
:Licence: GPL

Openswan est une implémentation IPsec pour Linux, descendante du projet FreeS/WAN (remontant à 1999).

OpenSwan permet la mise en place de liens IPsec entre machines, mais également de tunnels VPN, et ce, aussi bien entre réseaux d'entreprises que pour des clients nomades. Il est compatible avec un grand nombre de systèmes d’exploitation et de solutions propriétaires.

