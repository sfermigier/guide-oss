Sécurité
========

Le domaine de la sécurité est très large, de l’antivirus aux systèmes de détection d’intrusion, on trouve de nombreuses solutions open source.

Dans cette rubrique, on présente les vérificateurs d’intégrité, les détecteurs de virus, les détecteurs d’intrusions, les outils d’analyse de problèmes réseaux et des « testeurs » de failles de sécurité.

Tous ces outils sont de précieuses aides pour les administrateurs Systèmes et Réseaux pour garantir l’intégrité de leur parc.


Prelude SIEM
------------

:Site: https://www.prelude-siem.org/
:Porteur: un éditeur (CS)
:Licence: GPL 2.0

Prelude SIEM est un *security information management system* (SIEM), c'est-à-dire un outil de pilotage de la sécurité. Prelude collecte et centralise les informations de sécurité de l'entreprise pour offrir un point central de pilotage. Grâce à l'analyse et la corrélation des journaux et des flux, Prelude SIEM alerte en temps réel des tentatives d'intrusions et des menaces sur le réseau. Prelude SIEM offre plusieurs outils d'investigation et de reporting sur les Big Data permettant d'identifier les signaux faibles qui peuvent préfigurer des menaces persistantes avancées. Enfin, Prelude SIEM dispose de tous les outils d'aide à l'exploitation pour simplifier le travail des opérateurs et la gestion des risques.

Prelude SIEM est l'évolution de Prelude IDS, projet open source de sonde IDS créé en 1998 par Yoann Vandoorselaere.


AIDE
----

:Site: https://github.com/aide/aide
:Porteur: une communauté
:Licence: GPL 2.0

AIDE est un vérificateur d'intégrité pour système UNIX, développé depuis 1999. Rami Lehti and Pablo Virolainen ont initié les développements, suivi entre 2003 et 2010 par Richard van den Berg, puis désormais par Hannes von Haugwitz.

Son but est de calculer une empreinte des fichiers du système au moment de l'installation, et par la suite de valider la conformité du système avec cette empreinte. Ainsi, l'administrateur peut repérer toute modification de fichiers suspecte, généralement signe d'une intrusion sur le système.


ClamAV
------

:Site: https://www.clamav.net
:Porteur: un éditeur (SourceFire)
:Licence: GPL

ClamAV est un détecteur de virus antérieur à 2005.

Contrairement à ses équivalents du monde Windows, il n'est pas utilisé pour protéger la machine sur laquelle il est installé, mais pour scanner les fichiers qui s'y trouvent. On l'utilise ainsi sur les serveurs web, sur les serveurs de fichiers ou encore sur les serveurs mail. ClamAV détecte un grand nombre de menaces couvrant tous les systèmes d'exploitation. L'accès aux mises à jour des signatures est gratuit, alimentées par une communauté investie.

Le moteur antivirus est la bibliothèque libclamav écrite en C.


SNORT
-----

:Site: https://www.snort.org
:Porteur: un éditeur (SourceFire)

SNORT est un détecteur d’intrusion réseau réalisé en 1998 par Martin Roesch.

Souvent utilisé comme sonde, il dispose aussi d'un mode actif qui lui permet, lorsqu'il est installé sur un équipement de routage, de bloquer tout trafic suspect. Il s’agit donc d’un détecteur d’intrusion réseau (NIDS : Network Intrusion Detection System) permettant l’analyse en temps réel du trafic sur un segment de réseau.

Bien que le moteur soit distribué sous licence GPL, il n'est pas utile sans une base de règles. Celle-ci fait l'objet d'une souscription payante auprès de l'éditeur. Cependant, les règles sont mises à disposition gratuitement au bout de 30 jours.


OpenVAS
-------

:Site: https://www.openvas.org
:Porteur: un éditeur (Greenbone)
:Licence: GPL

OpenVAS (Open source Vulnerability Assessment Scanner) est un projet issu du célèbre scanner Nessus dont la première version date de 1998.

Il permet de tester la présence, dans les systèmes à tester, de failles de sécurité. Contrairement à Nessus, OpenVAS est complètement open source et dispose de mises à jours gratuites fournies par la communauté. Des mises à jour payantes, à la disponibilité garantie, et une interface d'administration graphique sont proposées par l'éditeur Greenbone.


WireShark
---------

:Site: https://www.wireshark.org
:Porteur: une fondation (WireShark)
:Licence: GPL

Wireshark (anciennement Ethereal) est un outil d'analyse de trafic réseau qui a vu le jour en 1998. Il fait partie de la famille des « packet sniffer ».

Il est utilisé par grand nombre d'administrateurs pour diagnostiquer des problèmes réseaux complexes. Disponible sous forme d'une application graphique lourde ainsi qu'une interface en mode texte, il est capable de décoder un très grand nombre de protocoles, y compris chiffrés.

Wireshark est multi-plateforme, il fonctionne sous Windows, Mac OS X, Linux, Solaris, ainsi que sous FreeBSD. Wireshark reconnait 759 protocoles.
