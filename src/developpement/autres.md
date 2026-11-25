# Autres outils de développement { #autres }

Cette page réunit des outils de développement qui ne relèvent d’aucune des autres catégories.

Le principal est Drools, un moteur de règles métier.

## Drools

Site
: <https://kie.apache.org/>

Porteur
: une fondation (Apache)

Licence
: Apache 2.0

Drools (anciennement JBoss Rules) est un système de gestion de règles métier utilisant un moteur d'inférence à chaînage avant.

L'utilisation d'un outil tel que Drools permet de faire évoluer des règles et des contraintes sans modifier le programme qui les applique. L'ensemble comprend le moteur de règles proprement dit, un moteur d'optimisation sous contraintes (OptaPlanner, dont les auteurs poursuivent le développement dans le fork Timefold), un moteur de décision conforme à la norme DMN et un atelier d'édition des règles. Celles-ci peuvent être écrites en syntaxe technique (DRL) ou saisies sous forme de tables de décision, compréhensibles par des utilisateurs fonctionnels.

Le projet a quitté l'écosystème JBoss/Red Hat : Drools et jBPM ont été donnés à la fondation Apache, où ils sont développés depuis 2025 sous le nom d'**Apache KIE** (*Knowledge Is Everything*), encore en incubation. Les anciennes adresses jboss.org/drools et jbpm.org redirigent désormais vers ce projet.

## ESIGate

Site
: <https://github.com/esigate/esigate>

Porteur
: une communauté

Licence
: Apache 2.0

ESIGate assemble à la volée une page à partir de fragments HTML provenant de plusieurs serveurs. Créé par des ingénieurs de la société Smile et écrit en Java, il n'évolue plus : son site est fermé et son dépôt n'a reçu que des mises à jour automatiques de dépendances, la dernière en 2024. Le même besoin se traite aujourd'hui avec les modules ESI de Varnish, de nginx ou de Symfony (HttpCache), ou avec des micro-frontends.
