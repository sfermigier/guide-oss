Sécurité
========

Le domaine de la sécurité est très large, de l’antivirus aux systèmes de détection d’intrusion, on trouve de nombreuses solutions open source.

Dans cette rubrique, on présente les vérificateurs d’intégrité, les détecteurs de virus, les détecteurs d’intrusions, les outils d’analyse de problèmes réseaux et les « testeurs » de failles de sécurité. Les briques de gestion des identités et des certificats font l'objet des sections :doc:`/infrastructure/authentification-federation-et-gestion-identite` et :doc:`/infrastructure/pki`.

Tous ces outils sont de précieuses aides pour les administrateurs Systèmes et Réseaux pour garantir l’intégrité de leur parc.


Prelude SIEM
------------

:Site: https://www.prelude-siem.org/
:Porteur: un éditeur (CS)
:Licence: GPL 2.0

Prelude SIEM est un *security information management system* (SIEM), c'est-à-dire un outil de pilotage de la sécurité. Prelude collecte et centralise les informations de sécurité de l'entreprise pour offrir un point central de pilotage. Grâce à l'analyse et la corrélation des journaux et des flux, Prelude SIEM alerte en temps réel des tentatives d'intrusions et des menaces sur le réseau. Prelude SIEM offre plusieurs outils d'investigation et de reporting sur les Big Data permettant d'identifier les signaux faibles qui peuvent préfigurer des menaces persistantes avancées. Enfin, Prelude SIEM dispose de tous les outils d'aide à l'exploitation pour simplifier le travail des opérateurs et la gestion des risques.

Prelude SIEM est l'évolution de Prelude IDS, projet open source de sonde IDS créé en 1998 par Yoann Vandoorselaere, et repris par CS Group. Attention au modèle de diffusion : seule la version « Prelude OSS », aux performances volontairement limitées, est librement disponible, l'essentiel des capacités relevant de l'offre commerciale.


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
:Porteur: un éditeur (Cisco)
:Licence: GPL v2

ClamAV est un antivirus créé en 2002, passé chez Sourcefire en 2007 puis chez Cisco, qui a racheté cette dernière en 2013.

Contrairement à ses équivalents du monde Windows, il n'est pas utilisé pour protéger la machine sur laquelle il est installé, mais pour scanner les fichiers qui s'y trouvent. On l'utilise ainsi sur les serveurs web, sur les serveurs de fichiers ou encore sur les serveurs mail. ClamAV détecte un grand nombre de menaces couvrant tous les systèmes d'exploitation. L'accès aux mises à jour des signatures est gratuit, alimentées par une communauté investie.

Le moteur antivirus est la bibliothèque libclamav écrite en C.


SNORT
-----

:Site: https://www.snort.org
:Porteur: un éditeur (Cisco)
:Licence: GPL v2

SNORT est un détecteur d’intrusion réseau réalisé en 1998 par Martin Roesch.

Souvent utilisé comme sonde, il dispose aussi d'un mode actif qui lui permet, lorsqu'il est installé sur un équipement de routage, de bloquer tout trafic suspect. Il s’agit donc d’un détecteur d’intrusion réseau (NIDS : Network Intrusion Detection System) permettant l’analyse en temps réel du trafic sur un segment de réseau.

Bien que le moteur soit distribué sous licence GPL, il n'est guère utile sans base de règles. Celle-ci fait l'objet d'une souscription payante auprès de l'éditeur, les règles étant mises à disposition gratuitement au bout de trente jours ; il existe par ailleurs des jeux de règles communautaires (Emerging Threats). La version 3 de Snort, sortie en 2021, a profondément revu l'architecture du moteur pour tirer parti des processeurs multicœurs, point sur lequel Suricata (voir ci-dessous) avait pris l'avantage.


OpenVAS
-------

:Site: https://www.greenbone.net/
:Porteur: un éditeur (Greenbone)
:Licence: GPL v2

OpenVAS (*Open Vulnerability Assessment Scanner*) est un projet né en 2005 du dernier code libre de Nessus, devenu propriétaire. Il est aujourd'hui intégré dans un ensemble plus large, la **Greenbone Community Edition** (anciennement GVM, *Greenbone Vulnerability Management*), qui regroupe le scanner, le gestionnaire de vulnérabilités et l'interface web.

Il permet de tester la présence de failles de sécurité sur les systèmes audités. Le flux de tests communautaire est gratuit ; l'éditeur allemand Greenbone propose en complément un flux d'entreprise, garanti et plus rapidement mis à jour, ainsi que des appliances.


WireShark
---------

:Site: https://www.wireshark.org
:Porteur: une fondation (WireShark)
:Licence: GPL

Wireshark (anciennement Ethereal) est un outil d'analyse de trafic réseau qui a vu le jour en 1998. Il fait partie de la famille des « packet sniffer ».

Il est utilisé par grand nombre d'administrateurs pour diagnostiquer des problèmes réseaux complexes. Disponible sous forme d'une application graphique lourde ainsi qu'une interface en mode texte, il est capable de décoder un très grand nombre de protocoles, y compris chiffrés.

Wireshark est multiplateforme : il fonctionne sous Windows, macOS, Linux et les systèmes BSD, et reconnaît plusieurs milliers de protocoles. Le projet est porté depuis 2023 par la Wireshark Foundation, qui en assure la gouvernance et le financement.


OSSEC
-----

:Site: https://www.ossec.net
:Porteur: une communauté
:Licence: GPL 2.0

OSSEC est un système de détection d'intrusion basé sur l'hôte (HIDS, *Host Intrusion Detection System*), créé en 2004 par Daniel B. Cid. Il surveille en temps réel les journaux système, les modifications de fichiers et la base de registre Windows, et détecte les rootkits. Il permet une analyse approfondie de la sécurité du système grâce à des règles configurables, et dispose d'une fonction d'alerte par courriel.

À noter : **Wazuh** (https://wazuh.com/), fork d'OSSEC créé en 2015, a largement dépassé le projet d'origine. Il en conserve l'agent et les règles, mais y ajoute une interface web complète, la gestion des vulnérabilités, le suivi de conformité (PCI-DSS, RGPD, NIS 2), l'inventaire et l'intégration à OpenSearch, ce qui en fait une plateforme XDR/SIEM complète sous licence AGPL v3. C'est aujourd'hui la solution à évaluer en priorité dans cette catégorie.

Suricata
--------

:Site: https://suricata.io
:Porteur: une fondation (OISF - Open Information Security Foundation)
:Licence: GPL 2.0

Suricata est un moteur de détection et de prévention des intrusions réseau (NIDS/NIPS) open source. Développé par la fondation OISF, il est conçu pour être une alternative et un complément à SNORT. Suricata offre des capacités avancées d'analyse de trafic, incluant la détection de menaces, l'inspection approfondie de paquets (DPI), et la prise en charge des formats de fichiers multiples pour l'analyse des fichiers capturés. Sa compatibilité avec les règles SNORT et son support pour les systèmes multi-thread en font un outil puissant pour les administrateurs réseau et les analystes de sécurité.

Metasploit Framework
--------------------

:Site: https://www.metasploit.com
:Porteur: un éditeur (Rapid7)
:Licence: BSD

Metasploit Framework est un outil de test d'intrusion créé en 2003 par H.D. Moore. Il est devenu l'un des outils les plus utilisés pour les tests de pénétration et l'exploitation des vulnérabilités. Metasploit permet aux administrateurs et aux chercheurs en sécurité de découvrir, valider et exploiter des failles dans les systèmes informatiques. Le framework inclut une large base de données d'exploits, de payloads et de modules auxiliaires pour divers types d'attaques et de tests. Il est utilisé pour automatiser les tests de sécurité, évaluer les systèmes pour les vulnérabilités et améliorer la posture de sécurité globale.

Zeek
----

:Site: https://zeek.org
:Porteur: une fondation (Zeek)
:Licence: BSD

Zeek (anciennement connu sous le nom de Bro) est un framework de surveillance du réseau et de détection des intrusions réseau (NIDS) open source. Créé en 1995 par Vern Paxson, Zeek est conçu pour capturer et analyser le trafic réseau en profondeur. Il permet d'extraire des métadonnées détaillées et de détecter des activités anormales grâce à un langage de script puissant. Zeek est largement utilisé dans les environnements de recherche et de production pour son efficacité à fournir des informations contextuelles et des capacités de détection avancées.

Nmap
----

:Site: https://nmap.org
:Porteur: une communauté
:Licence: GPL 2.0

Nmap (Network Mapper) est un scanner de sécurité réseau open source, créé par Gordon Lyon (Fyodor) en 1997. Il est utilisé pour découvrir les hôtes et les services sur un réseau informatique, créant ainsi une "carte" du réseau. Nmap offre une variété de fonctionnalités pour explorer les réseaux, incluant la découverte d'hôtes, la détection de services, l'identification de versions, et la détection de vulnérabilités. Nmap est essentiel pour les audits de sécurité, les tests de pénétration, et la gestion des inventaires réseau.

OpenSCAP
--------

:Site: https://www.open-scap.org
:Porteur: une communauté
:Licence: GPL 2.0

OpenSCAP est une suite d'outils open source pour l'audit de sécurité des systèmes d'information. Basé sur les standards de sécurité développés par NIST, OpenSCAP permet l'évaluation de la conformité, la détection des vulnérabilités et la remédiation des configurations non conformes. Il est largement utilisé dans les environnements conformes aux réglementations comme PCI-DSS et HIPAA. OpenSCAP comprend un scanner de conformité, un éditeur de profils et divers outils d'analyse, permettant aux administrateurs de maintenir et de renforcer la sécurité de leurs systèmes.


Autres
------

Le domaine s'est considérablement étoffé ces dernières années ; parmi les projets à connaître :

- CrowdSec, solution française de détection et de blocage comportemental, fondée sur le partage communautaire des adresses malveillantes: https://www.crowdsec.net/
- Fail2ban, l'outil historique de bannissement d'adresses IP sur la base des journaux: https://github.com/fail2ban/fail2ban
- OpenCTI, plateforme de renseignement sur les menaces développée par la société française Filigran avec le soutien de l'ANSSI: https://filigran.io/products/opencti
- MISP, plateforme de partage d'indicateurs de compromission: https://www.misp-project.org/
- Falco, détection d'anomalies à l'exécution dans les conteneurs et Kubernetes (projet CNCF): https://falco.org/
- Trivy, analyse de vulnérabilités des images, dépendances et configurations: https://trivy.dev/
- Lynis, audit de durcissement des systèmes UNIX: https://cisofy.com/lynis/
- OpenBao, gestion des secrets, fork libre de HashiCorp Vault (section :doc:`/infrastructure/pki`): https://openbao.org/

