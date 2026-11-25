# Journaux et traces

Les journaux enregistrent ce qui s'est passé, événement par événement ; les traces suivent une requête à travers les services qu'elle traverse. Avec les métriques, présentées à la page [Supervision et métrologie](supervision-et-metrologie.md), ils forment ce que l'on appelle l'observabilité.

Centraliser les journaux répond à plusieurs besoins : diagnostiquer un incident, conserver des preuves après une intrusion, satisfaire à des obligations de traçabilité. Les traces deviennent utiles lorsqu'une application se compose de plusieurs services ; pour une application monolithique, elles apportent moins.

Trois choix structurent un projet : l'instrumentation et la collecte, à confier de préférence à une norme ouverte pour pouvoir changer d'outil ; l'indexation, complète (OpenSearch) ou limitée à des étiquettes (Loki), dont dépendent coût et possibilités de recherche ; la conservation, qui doit respecter le RGPD lorsque les journaux contiennent des données personnelles.

## OpenTelemetry

Site
: <https://opentelemetry.io/>

Porteur
: une fondation (CNCF)

Licence
: Apache 2.0

OpenTelemetry définit un protocole, des conventions et des bibliothèques d'instrumentation communs aux traces, aux métriques et aux journaux. Né en 2019 de la fusion d'OpenTracing et d'OpenCensus, il est projet diplômé de la CNCF depuis mai 2026.

Les bibliothèques couvrent les principaux langages, souvent avec une instrumentation automatique. Le collecteur reçoit les données, les filtre, les échantillonne et les transmet à un ou plusieurs systèmes de stockage.

Il ne stocke ni n'affiche rien : il faut lui associer un outil comme Jaeger, Loki, Prometheus ou OpenSearch. Son intérêt est de rendre l'instrumentation indépendante de cet outil. La maturité varie selon les langages et les types de signaux.

Le collecteur est écrit en Go.

## Grafana Loki

Site
: <https://grafana.com/oss/loki/>

Porteur
: un éditeur (Grafana Labs)

Licence
: AGPL v3

Loki est un système d'agrégation de journaux lancé en 2018, conçu sur le modèle de Prometheus.

Il n'indexe que des étiquettes (service, machine, niveau) et conserve le contenu compressé dans un stockage objet. Le langage LogQL filtre ensuite les lignes et en tire des métriques. La consultation se fait dans Grafana, la collecte par Grafana Alloy ou le collecteur OpenTelemetry.

Ce choix réduit le coût de stockage. Il rend en contrepartie les recherches en plein texte sur de longues périodes plus lentes. Un excès d'étiquettes dégrade les performances.

Loki est écrit en Go.

## OpenSearch

Site
: <https://opensearch.org/>

Porteur
: une fondation (OpenSearch Software Foundation, Linux Foundation)

Licence
: Apache 2.0

OpenSearch, fork d'Elasticsearch lancé en 2021, est présenté comme moteur à la page [Moteurs de recherche](../web-communication/moteurs-de-recherche.md). Associé à OpenSearch Dashboards et à un collecteur (Data Prepper, Fluent Bit, Logstash), il forme une pile complète de gestion de journaux.

L'indexation du contenu autorise des recherches riches, des agrégations et des alertes, ce qui convient aux investigations et aux usages de sécurité. Le cluster demande en retour davantage de mémoire et de stockage que Loki, ainsi qu'une politique de cycle de vie des index.

OpenSearch est écrit en Java.

## Jaeger

Site
: <https://www.jaegertracing.io/>

Porteur
: une fondation (CNCF)

Licence
: Apache 2.0

Jaeger est une plateforme de traçage distribué créée chez Uber, confiée en 2017 à la CNCF et diplômée depuis 2019.

Elle reçoit les traces au format OpenTelemetry, les stocke (Elasticsearch, OpenSearch, Cassandra ou stockage local selon les besoins) et permet de visualiser le parcours d'une requête, ses dépendances et ses latences. Sa version 2 est construite sur le collecteur OpenTelemetry.

Jaeger se limite aux traces et ne remplace pas une solution de métriques ou de journaux. L'échantillonnage est à régler pour maîtriser le volume.

Jaeger est écrit en Go, son interface en TypeScript.

## Autres

- rsyslog et syslog-ng, collecte et routage de journaux système : <https://www.rsyslog.com/> et <https://www.syslog-ng.com/>
- Fluentd et Fluent Bit, collecteurs de la CNCF (Apache 2.0) : <https://www.fluentd.org/> et <https://fluentbit.io/>
- Vector, collecte et transformation (MPL 2.0) : <https://vector.dev/>
- VictoriaLogs, base de journaux (Apache 2.0) : <https://docs.victoriametrics.com/victorialogs/>
- Grafana Tempo, stockage de traces (AGPL v3) : <https://grafana.com/oss/tempo/>
- Zipkin, traçage distribué (Apache 2.0) : <https://zipkin.io/>
- Apache SkyWalking, suivi de performances applicatives (Apache 2.0) : <https://skywalking.apache.org/>
- OpenObserve, journaux, métriques et traces (AGPL v3) : <https://openobserve.ai/>
- SigNoz, observabilité fondée sur OpenTelemetry (MIT, avec des répertoires sous licence commerciale) : <https://signoz.io/>
- GlitchTip, suivi d'erreurs applicatives compatible avec Sentry : <https://glitchtip.com/>
