Sécurité
========

Le domaine de la sécurité est très large, de l’antivirus aux systèmes de détection d’intrusion, on trouve de nombreuses solutions open source.

Dans cette rubrique, on présente les vérificateurs d’intégrité, les détecteurs de virus, les détecteurs d’intrusions, les outils d’analyse de problèmes réseaux et des « testeurs » de failles de sécurité. Les anti-spam tels que  SpamAssassin ou DSPAM sont rangés dans la catégorie Messagerie, Emailing & Groupware.

Tous ces outils sont de précieuses aides pour les administrateurs Systèmes et Réseaux pour garantir l’intégrité de leur parc.


AIDE
----

:Site: aide.sourceforge.net
:Porteur: une communauté
:Licence: GPL

AIDE est un vérificateur d'intégrité pour système UNIX, développé depuis 1999. Rami Lehti and Pablo Virolainen ont initié les développements, suivi entre 2003 et 2010 par Richard van den Berg, puis désormais par Hannes von Haugwitz.

Son but est de calculer une empreinte des fichiers du système au moment de l'installation, et par la suite de valider la conformité du système avec cette empreinte. Ainsi, l'administrateur peut repérer toute modification de fichiers suspecte, généralement signe d'une intrusion sur le système.


ClamAV
------

:Site: www.clamav.net
:Porteur: un éditeur (SourceFire)
:Licence: GPL

ClamAV est un détecteur de virus antérieur à 2005.

Contrairement à ses équivalents du monde Windows, il n'est pas utilisé pour protéger la machine sur laquelle il est installé, mais pour scanner les fichiers qui s'y trouvent. On l'utilise ainsi sur les serveurs web, sur les serveurs de fichiers ou encore sur les serveurs mail. ClamAV détecte un grand nombre de menaces couvrant tous les systèmes d'exploitation. L'accès aux mises à jour des signatures est gratuit, alimentées par une communauté investie.

Le moteur antivirus est la bibliothèque libclamav écrite en C.


SNORT
-----

:Site: www.snort.org
:Porteur: un éditeur (SourceFire)

SNORT est un détecteur d’intrusion réseau réalisé en 1998 par Martin Roesch.

Souvent utilisé comme sonde, il dispose aussi d'un mode actif qui lui permet, lorsqu'il est installé sur un équipement de routage, de bloquer tout trafic suspect. Il s’agit donc d’un détecteur d’intrusion réseau (NIDS : Network Intrusion Detection System) permettant l’analyse en temps réel du trafic sur un segment de réseau.

Bien que le moteur soit distribué sous licence GPL, il n'est pas utile sans une base de règles. Celle-ci fait l'objet d'une souscription payante auprès de l'éditeur. Cependant, les règles sont mises à disposition gratuitement au bout de 30 jours.


OpenVAS
-------

:Site: www.openvas.org
:Porteur: un éditeur (Greenbone)
:Licence: GPL

OpenVAS (Open source Vulnerability Assessment Scanner) est un projet issu du célèbre scanner Nessus dont la première version date de 1998.

Il permet de tester la présence, dans les systèmes à tester, de failles de sécurité. Contrairement à Nessus, OpenVAS est complètement open source et dispose de mises à jours gratuites fournies par la communauté. Des mises à jour payantes, à la disponibilité garantie, et une interface d'administration graphique sont proposées par l'éditeur Greenbone.



WireShark
---------

:Site: www.wireshark.org
:Porteur: une fondation (WireShark)
:Licence: GPL

Wireshark (anciennement Ethereal, changement pour des raisons de copyright essentiellement) est un outil d'analyse de trafic réseau qui a vu le jour en 1998. Il fait partie de la famille des « packet sniffer ».

Il est utilisé par grand nombre d'administrateurs pour diagnostiquer des problèmes réseaux complexes. Disponible sous forme d'une application graphique lourde ainsi qu'une interface en mode texte, il est capable de décoder un très grand nombre de protocoles, y compris chiffrés.

Wireshark est multi-plateforme, il fonctionne sous Windows, Mac OS X, Linux, Solaris, ainsi que sous FreeBSD. Wireshark reconnait 759 protocoles.



LinShare
--------

:Site: www.linshare.org
:Porteur: un éditeur (LINAGORA)
:Licence: GNU Affero GPL v3

LinShare est une application de partage de fichiers volumineux et sécurisés créée en 2008, qui se focalise sur la traçabilité, la confidentialité et l’intégrité des données.

Cette application propose plusieurs interfaces d’utilisation telles que : une interface web, des plugins (Outlook, Thunderbird, OBM), une API REST. Elle est utilisée dans l’entreprise pour déposer des fichiers dans son espace personnel (tel qu’un coffre-fort) et partager des fichiers avec des utilisateurs internes ou externes, ou des invités ponctuels.

Les points forts de LinShare sont : la sécurité des échanges (horodatage, signature et chiffrement), la traçabilité des échanges (notifications, historique, journaux, reporting, etc.), l’utilisation et la configuration par multi-domaines.

LinShare est une application Java JEE multi-plateformes (GNU/Linux, Windows, etc.). Elle fonctionne dans un conteneur applicatif (Tomcat, Jetty) et s’appuie sur une base de données (PostgreSQL, MySQL) et un annuaire (LDAP, Active Directory).


LinSign
-------

:Site: www.linsign.org
:Porteur: un éditeur (LINAGORA)
:Licence: GNU Affero GPL v3

LinSign est une application de signature électronique de documents créée en 2008, multi-documents et multi-signatures.

Spécialement conçue pour signer électroniquement des documents, des contrats et des données sensibles, LinSign garantit l’authentification du signataire, l’intégrité, la non-répudiation et l’invariance sémantique des données signées. Nombreux formats de documents à signer (PDF, OpenDocument, XML, etc.), de signatures (PDF, XAdES, XML-Dsig) et supporte divers types de magasins de certificats (PKCS #12, carte à puce, token USB, navigateur web).

LinSign peut être : soit installée sur le poste de travail, soit installée sur un serveur web, soit intégrée dans une autre application web (e.g. une GED). Elle s’appuie sur un système de politiques de signature pour signer des documents avec des certificats numériques X.509 qui peuvent être stockés sur des cartes à puce.

LinSign est une application Java JEE multi-plateformes (GNU/Linux, Windows, etc.).

LinSign est conforme au Profil de protection Application de création de signature électronique, et est en cours de certification ANSSI-CSPN (Certification de sécurité de premier niveau).




Autres
------

Parmi les produits de l’univers Sécurité, on peut compléter la liste avec les outils ci-dessous :

- Bastille:	http://bastille-linux.sourceforge.net

- OpenSIMS:	http://opensims.sourceforge.net

- RadicalSpam:	http://www.radical-spam.org

