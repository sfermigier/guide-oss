Supervision et Métrologie
=========================

Les outils de supervision permettent la surveillance de réseaux, machines, services, etc. Parmi les fonctionnalités que l’on peut trouver, on peut citer : la consultation de l'état des services et des machines supervisés, la métrologie, le reporting, l'accès aux évènements de supervision, la gestion avancée des utilisateurs et des ACL, mais aussi les dépendances, l'escalade de notification, les templates de services et d'hôtes, le support des surveillances actives et passives, etc

La supervision et la métrologie forment un domaine particulièrement bien servi par l'open source. Le paysage s'est toutefois recomposé en profondeur depuis les premières éditions de ce guide : à l'approche historique, centrée sur la vérification périodique d'états par un serveur central (Nagios et ses dérivés), s'est ajoutée une approche fondée sur la collecte massive de métriques et sur leur exploitation (Prometheus, Grafana), issue des environnements *cloud native*. Les deux coexistent, souvent au sein d'une même organisation, la première restant pertinente pour la supervision d'équipements et de services classiques, la seconde pour les applications distribuées.


Nagios
------

:Site: https://www.nagios.org/
:Porteur: un éditeur (Nagios Enterprises)
:Licence: GPL v2 (Nagios Core) et propriétaire (Nagios XI)

Nagios (anciennement Net saint) est un logiciel de supervision de réseaux créé en 1999 par Ethan Galstad. Il est considéré comme étant la référence des solutions de supervision open source.

Nagios dispose de nombreuses fonctionnalités tel que l'héritage multiple, les dépendances, l'escalade de notification, les templates de services et d'hôtes, le support des surveillances actives et passives, etc. Cela en fait un outil très complet pouvant s'adapter à n'importe quel type d'utilisation avec des possibilités de configuration très poussées.

La modularité et la forte communauté (> 250 000) qui gravite autour de Nagios (en participant au développement de nombreux plugins et addons) offrent des possibilités en terme de supervision qui permettent aujourd'hui de pouvoir superviser pratiquement n'importe quelle ressource.

Les plugins sont écrits dans les langages de programmation les plus adaptés à leur tâche : scripts shell (Bash, ksh, etc.), C, C++, Perl, Python, Ruby, PHP, etc.

Il faut cependant noter que Nagios Core n'est plus la référence incontestée qu'il a été : son modèle de configuration par fichiers et son architecture ont conduit à l'apparition de dérivés plus modernes conservant la compatibilité avec ses plugins — Icinga 2, Naemon, Centreon, Shinken — et le projet concentre désormais l'essentiel de ses efforts sur son offre commerciale Nagios XI. Pour un nouveau déploiement, on comparera sérieusement Zabbix, Icinga, Checkmk et Prometheus.


Prometheus
----------

:Site: https://prometheus.io/
:Porteur: une fondation (CNCF)
:Licence: Apache 2.0

Créé en 2012 chez SoundCloud et devenu en 2018 le deuxième projet diplômé de la *Cloud Native Computing Foundation* après Kubernetes, Prometheus est le standard de fait de la métrologie des systèmes modernes.

Son modèle est radicalement différent de celui de Nagios : plutôt que d'exécuter des vérifications qui retournent un état, Prometheus collecte périodiquement (*pull*) des métriques numériques exposées par les applications et par des *exporters*, les stocke dans une base de séries temporelles, et laisse à un langage de requête très expressif (PromQL) le soin de calculer les indicateurs et de déclencher les alertes. La découverte automatique des cibles (Kubernetes, Consul, fichiers) évite d'avoir à déclarer chaque machine.

L'alerte est gérée par un composant distinct, Alertmanager, qui assure le regroupement, l'inhibition et le routage vers les canaux de notification. Pour la conservation longue durée et la mise à l'échelle, on lui adjoint Thanos, Cortex/Mimir ou VictoriaMetrics.

Prometheus est écrit en Go.


Grafana
-------

:Site: https://grafana.com/oss/grafana/
:Porteur: une entreprise (Grafana Labs)
:Licence: AGPL v3

Grafana est l'outil de visualisation devenu indissociable de Prometheus, même s'il sait interroger des dizaines d'autres sources : bases de séries temporelles (InfluxDB, Graphite, VictoriaMetrics), bases relationnelles, Elasticsearch, Zabbix, ClickHouse, services cloud.

Il fournit des tableaux de bord riches et paramétrables, un moteur d'alerte unifié et une gestion fine des droits. L'écosystème s'est élargi à Loki pour les journaux, Tempo pour les traces distribuées et Pyroscope pour le profilage continu, formant une pile d'observabilité complète.

Attention à la licence : Grafana Labs est passé en 2021 de la licence Apache 2.0 à l'AGPL v3 — qui reste une licence libre, mais impose la publication des modifications pour un service exposé en réseau — et une partie des fonctions destinées aux entreprises n'est disponible que dans les éditions commerciales.

Grafana est écrit en Go et TypeScript.


Centreon
--------

:Site: https://www.centreon.com
:Porteur: un éditeur (Centreon)
:Licence: GPL

Centreon a commencé comme interface web de configuration pour Nagios, développée par la société française éponyme (anciennement Merethis). C'est devenu une solution de supervision complète et autonome, dotée de ses propres moteurs de collecte et de traitement (Centreon Engine et Centreon Broker), tout en restant compatible avec l'écosystème de plugins de Nagios.

Cette interface évoluée apporte, en plus de ses possibilités de configuration, de nombreuses fonctionnalités telles que la consultation de l'état des services et des machines supervisés, la métrologie, le reporting, l'accès aux évènements de supervision, la gestion avancée des utilisateurs et des ACL, etc.

Centreon s'appuie sur PHP pour l'interface web et sur MariaDB pour le stockage des données de configuration et de supervision. L'édition communautaire (Centreon OSS) est publiée sous licence GPL v2 ; les modules avancés (cartographie, business intelligence, haute disponibilité, connecteurs) relèvent des éditions commerciales, ce qu'il convient de vérifier avant de dimensionner un projet.


Zabbix
------

:Site: https://www.zabbix.com
:Porteur: un éditeur (Zabbix SIA)
:Licence: AGPL v3 depuis la version 7.0 (GPL v2 auparavant)

Zabbix est une solution de monitoring complète embarquant un front-end web, un ou plusieurs serveurs distribués, et des agents multi-plateformes précompilés (Windows, Linux, AIX, Solaris, etc).

Zabbix est également capable de faire du monitoring SNMP et IPMI ainsi que de la découverte de réseau. Des vérifications web sont également intégrées permettant de simuler le parcours d'un visiteur sur un serveur web tout en vérifiant le contenu et les temps de réponse des pages. Des graphiques et cartes sont modélisables directement depuis le front-end sur toutes les valeurs supervisées par zabbix et ses agents.

Il repose sur C/C++ pour les serveurs et les agents, PHP pour l'interface web, et MySQL/MariaDB, PostgreSQL ou TimescaleDB pour le stockage. Sa particularité la plus appréciable est qu'il n'existe pas d'édition commerciale amputant les fonctionnalités : tout est dans le produit libre, l'éditeur letton se rémunérant sur le support et les services. À noter le changement de licence intervenu avec la version 7.0 (juin 2024), qui fait passer le projet de la GPL v2 à l'AGPL v3.


OpenNMS
-------

:Site: https://www.opennms.com/
:Porteur: un éditeur (The OpenNMS Group, filiale de NantHealth)
:Licence: AGPL v3

OpenNMS occupe, dans le monde open source, la place que tenaient HP OpenView et IBM Tivoli parmi les solutions propriétaires de supervision de réseaux. Le projet est porté par The OpenNMS Group, racheté en 2021 par NantHealth, et reste publié sous licence libre.

OpenNMS a été conçu, dès ses débuts en 1999, pour répondre aux exigences des grandes entreprise telles que la scalabilité, l'automatisation et la flexibilité lui permettant ainsi de surveiller "out-of-the-box" plusieurs dizaines de milliers de ressources. Parmi ses nombreuses fonctionnalités on retrouve : découverte et surveillance automatique des équipements et services, collecte et traitement de données (en SNMP, JMX, XML, nrpe, et autres), gestion avancée d'événements actifs et passifs, alertes et notifications avec escalade et calendrier d'astreinte, génération de rapports, graphiques et cartes réseaux, surveillance en simulation de parcours, compatible multi-sites (remote polling), etc.

OpenNMS est développé en Java et s'appuie sur le moteur WEB Jetty et le SGBD PostgreSQL. Il respecte les standards FCAPS.


Munin
-----

:Site: http://munin-monitoring.org/
:Porteur: une communauté
:Licence: GPL

Le projet existe depuis 2004. Il a été créé par la société Redpill Linpro, puis rapidement rejoint par de nombreux autres développeurs. Son développement se poursuit aujourd'hui à un rythme modéré : Munin conserve tout son intérêt pour de petits parcs, grâce à sa simplicité de mise en œuvre, mais les infrastructures importantes lui préfèrent désormais Prometheus ou Zabbix.

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

Supervision d'états :

- Icinga 2, fork de Nagios devenu un produit à part entière: https://icinga.com/
- Checkmk, édition Raw sous licence GPL, réputée pour sa facilité de mise en œuvre: https://checkmk.com/
- Naemon, autre fork de Nagios: http://www.naemon.io/
- Uptime Kuma, supervision légère de disponibilité, très populaire en auto-hébergement: https://uptime.kuma.pet/
- Shinken, fork Python de Nagios, dont le développement est aujourd'hui à l'arrêt et dont le site n'est plus en service: https://github.com/shinken-solutions/shinken

Métriques et observabilité :

- Netdata, collecte à la seconde avec tableaux de bord immédiats: https://www.netdata.cloud/
- VictoriaMetrics, base de séries temporelles compatible Prometheus: https://victoriametrics.com/
- OpenTelemetry, norme de la CNCF pour l'instrumentation (métriques, traces, journaux): https://opentelemetry.io/
- MRTG, historique mais toujours utilisé: https://oss.oetiker.ch/mrtg

Journaux et erreurs applicatives :

- Grafana Loki, indexation de journaux économe en ressources: https://grafana.com/oss/loki/
- Graylog Open, gestion centralisée des journaux (licence SSPL, non libre au sens de l'OSI): https://www.graylog.org/
- OpenSearch et sa pile d'ingestion, alternative sous licence Apache à la suite Elastic (section :doc:`/web-communication/moteurs-de-recherche`): https://opensearch.org/
- Sentry, suivi des erreurs applicatives, publié sous *Functional Source License*, source-available et non libre: https://sentry.io/ — son fork libre est GlitchTip (https://glitchtip.com/)

La solution française Vigilo NMS, éditée par CS Group et présentée dans les éditions précédentes de ce guide, ne fait plus l'objet d'une distribution publique : son site n'est plus en service.

