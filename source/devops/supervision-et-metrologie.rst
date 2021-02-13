Supervision et Métrologie
=========================

Les outils de supervision permettent la surveillance de réseaux, machines, services, etc. Parmi les fonctionnalités que l’on peut trouver, on peut citer : la consultation de l'état des services et des machines supervisés, la métrologie, le reporting, l'accès aux évènements de supervision, la gestion avancée des utilisateurs et des ACL, mais aussi les dépendances, l'escalade de notification, les templates de services et d'hôtes, le support des surveillances actives et passives, etc

La Supervision et métrologie est un domaine bien servi par l’open source avec de nombreux produits de qualité, comme Nagios notamment qui dispose également d’une grande notoriété.


Nagios
------

:Site: https://www.nagios.org/
:Porteur: un éditeur (Nagios Enterprises)
:Licence: GPL

Nagios (anciennement Net saint) est un logiciel de supervision de réseaux créé en 1999 par Ethan Galstad. Il est considéré comme étant la référence des solutions de supervision open source.

Nagios dispose de nombreuses fonctionnalités tel que l'héritage multiple, les dépendances, l'escalade de notification, les templates de services et d'hôtes, le support des surveillances actives et passives, etc. Cela en fait un outil très complet pouvant s'adapter à n'importe quel type d'utilisation avec des possibilités de configuration très poussées.

La modularité et la forte communauté (> 250 000) qui gravite autour de Nagios (en participant au développement de nombreux plugins et addons) offrent des possibilités en terme de supervision qui permettent aujourd'hui de pouvoir superviser pratiquement n'importe quelle ressource.

Les plugins sont écrits dans les langages de programmation les plus adaptés à leur tâche : scripts shell (Bash, ksh, etc.), C++, Perl, Python, Ruby, PHP, C#, etc.


Vigilo NMS
----------

:Site: https://www.vigilo-nms.org/
:Porteur: un éditeur (CS)
:Licence: GPL

Vigilo NMS (Network Monitoring System) est un logiciel de supervision capable de gérer des systèmes hétérogènes (réseau serveurs, applications) de grande taille grâce à une architecture répartie et modulaire. Construit autour de Nagios, Vigilo traite en complément la métrologie, la cartographie, la corrélation et le reporting.


Centreon
--------

:Site: https://www.centreon.com
:Porteur: un éditeur (Centreon)
:Licence: GPL

Centreon est un frontend Web, développé et supporté par la société française éponyme (anciennement Merethis), qui permet de réaliser le paramétrage d'outils de supervision tel que Nagios, Inciga ou Shinken.

Cette interface évoluée apporte, en plus de ses possibilités de configuration, de nombreuses fonctionnalités telles que la consultation de l'état des services et des machines supervisés, la métrologie, le reporting, l'accès aux évènements de supervision, la gestion avancée des utilisateurs et des ACL, etc.

Centreon s’appuie sur les technologies Apache et PHP pour l'interface web, MySQL pour le stockage des données de configuration et de supervision.


Zabbix
------

:Site: https://www.zabbix.com
:Porteur: un éditeur (ZABBIX SIA)
:Licence: GPL

Zabbix est une solution de monitoring complète embarquant un front-end web, un ou plusieurs serveurs distribués, et des agents multi-plateformes précompilés (Windows, Linux, AIX, Solaris, etc).

Zabbix est également capable de faire du monitoring SNMP et IPMI ainsi que de la découverte de réseau. Des vérifications web sont également intégrées permettant de simuler le parcours d'un visiteur sur un serveur web tout en vérifiant le contenu et les temps de réponse des pages. Des graphiques et cartes sont modélisables directement depuis le front-end sur toutes les valeurs supervisées par zabbix et ses agents.

Il repose sur du C/C++, PHP pour la partie front end et MySQL/PostgreSQL/Oracle pour la partie BDD.


OpenNMS
-------

:Site: https://www.opennms.org
:Porteur: un éditeur (OpenNMS group)
:Licence: GPL v3

OpenNMS est à l'open source ce qu'est HP Openview et IBM tivoli au monde propriétaire de la surveillance de réseaux.

OpenNMS a été conçu, dès ses débuts en 1999, pour répondre aux exigences des grandes entreprise telles que la scalabilité, l'automatisation et la flexibilité lui permettant ainsi de surveiller "out-of-the-box" plusieurs dizaines de milliers de ressources. Parmi ses nombreuses fonctionnalités on retrouve : découverte et surveillance automatique des équipements et services, collecte et traitement de données (en SNMP, JMX, XML, nrpe, et autres), gestion avancée d'événements actifs et passifs, alertes et notifications avec escalade et calendrier d'astreinte, génération de rapports, graphiques et cartes réseaux, surveillance en simulation de parcours, compatible multi-sites (remote polling), etc.

OpenNMS est développé en Java et s'appuie sur le moteur WEB Jetty et le SGBD PostgreSQL. Il respecte les standards FCAPS.


Munin
-----

:Site: http://munin-monitoring.org/
:Porteur: une communauté
:Licence: GPL

Le projet existe depuis 2004. Il a été créé par la société Redpill Linpro puis rapidement rejoint par de nombreux autres développeurs. Le projet reste très actif aujourd'hui.

Munin permet de surveiller n'importe quel paramètre des serveurs, et rend l'information disponible sous forme de graphes dans une interface Web. Il permet également d’évaluer n'importe quelle métrique: système, réseau, applications, jusqu'aux limites de votre imagination. Ses principaux atouts sont sa simplicité et le grand nombre de plugins disponibles (par centaines) pour ajouter des graphes supplémentaires.

Munin se repose sur l'excellent outil RRDTool. Il est écrit en Perl, ce qui fait de lui un logiciel totalement multiplateforme (Linux / UNIX / Windows). Les plugins sont des exécutables pouvant être écrits dans n'importe quel langage.


Cacti
-----

:Site: https://www.cacti.net/
:Porteur: une communauté
:Licence: GPL

Cacti est un outil basé sur RRDTool dédié à la métrologie. Il permet de représenter sous forme de graphiques n'importe quelle donnée quantifiable collectée soit par le biais de protocoles réseaux tels que SNMP ou soit par des scripts personnalisés par l'utilisateur.

Il est considéré comme étant le digne successeur de MRTG et apporte une véritable interface à RRDTool en permettant de modifier chacun des aspects des graphiques générés. Les possibilités de configuration très avancées font que celui-ci est souvent utilisé en complément de solutions de supervision tel que Nagios, notamment, pour assurer la partie métrologie lorsque les exigences sont fortes.

De nombreux plugins développés par la communauté permettent d'étendre les fonctionnalités de Cacti et parfois bien même au delà de la simple métrologie.

Il fonctionne grâce à un serveur web équipé d'une base de données et du langage PHP. Cacti utilise aussi un système de scripts (Bash, PHP, Perl, VBs...) pour effectuer des mesures plus complexes.


Autres
------

Parmi les produits de l’univers Supervision et Métrologie, on peut compléter la liste avec les outils ci-dessous :


- Prometheus: https://prometheus.io/
- Logstash: https://www.elastic.co/logstash
- Graylog: https://www.graylog.org/
- Sentry: https://sentry.io/
- MRTG: https://oss.oetiker.ch/mrtg
- Shinken: http://www.shinken-monitoring.org/
- Icinga: https://www.icinga.org/

