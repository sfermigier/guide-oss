# SIEM et WAF

Un SIEM (*Security Information and Event Management*) centralise les journaux et les événements de sécurité, les corrèle et produit des alertes. Un WAF (*Web Application Firewall*) examine les requêtes adressées aux applications web et bloque les attaques reconnaissables, comme les injections. Les sondes réseau, antivirus et outils d'audit sont présentés à la page [Sécurité](securite.md).

Un SIEM n'a de valeur que si ses alertes sont lues. Le travail tient moins à l'installation qu'au choix des sources, au réglage des règles et à l'organisation de l'astreinte ; le volume des journaux et leur durée de conservation déterminent le coût de l'infrastructure. La collecte elle-même est traitée à la page [Journaux et traces](journaux-traces.md).

Un WAF compense provisoirement des applications vulnérables ou non corrigées. Ses règles se mettent en place en mode observation avant le blocage, sous peine d'interrompre des usages légitimes. Il ne remplace pas la correction des applications.

## Wazuh

Site
: <https://wazuh.com/>

Porteur
: un éditeur (Wazuh Inc.)

Licence
: GPL v2 (série 4.x) ; le nouveau moteur d'analyse en développement est sous AGPL v3

Wazuh est une plateforme de détection et de réponse (XDR/SIEM) issue en 2015 d'un fork d'[OSSEC](securite.md#ossec).

Des agents installés sur les postes et serveurs remontent journaux, modifications de fichiers, inventaire et vulnérabilités connues ; un serveur les analyse à l'aide de règles. Un indexeur dérivé d'OpenSearch alimente les tableaux de bord. Des modules suivent la conformité à des référentiels comme PCI DSS ou le RGPD. Des réponses automatiques peuvent être déclenchées.

Le logiciel ne comporte pas d'édition amputée : l'éditeur se rémunère par le support et une offre hébergée. Le réglage initial des règles et le dimensionnement de l'indexeur constituent l'essentiel de l'effort.

Wazuh est écrit en C, C++ et Python, avec une interface en TypeScript.

## Coraza

Site
: <https://www.coraza.io/>

Porteur
: une fondation (OWASP)

Licence
: Apache 2.0

Coraza est un moteur de pare-feu applicatif web, compatible avec le langage de règles de ModSecurity et avec les règles génériques de l'OWASP (*Core Rule Set*, version 4).

Il se présente comme une bibliothèque, que l'on utilise à travers des intégrations : Caddy, nginx, HAProxy (SPOA), Envoy et les proxys compatibles WebAssembly. Il permet de détecter et de bloquer les catégories d'attaques courantes, avec une journalisation d'audit.

C'est une alternative à ModSecurity (<https://modsecurity.org/>), lui aussi confié à l'OWASP et toujours maintenu, dont le module historique vise Apache. La compatibilité entre les deux moteurs est partielle : des règles écrites sur mesure doivent être testées.

Coraza est écrit en Go.

## BunkerWeb

Site
: <https://www.bunkerweb.io/>

Porteur
: une entreprise (Bunkerity)

Licence
: AGPL v3

BunkerWeb est un proxy inverse sécurisé, développé par la société française Bunkerity et construit sur nginx.

Il réunit ModSecurity et le *Core Rule Set*, la gestion des certificats, la limitation de débit, le blocage de robots et de listes d'adresses et l'intégration avec Docker et Kubernetes. Une interface web et un système d'extensions facilitent l'administration.

Il s'adresse à ceux qui préfèrent un produit assemblé à une bibliothèque. Certaines fonctions, comme des rapports avancés, relèvent d'une offre payante.

BunkerWeb est écrit en Python et Lua.

## Autres

- ModSecurity, moteur de pare-feu applicatif historique (Apache 2.0) : <https://modsecurity.org/>
- OWASP Core Rule Set, règles communes à ModSecurity et Coraza (Apache 2.0) : <https://coreruleset.org/>
- OpenSearch Security Analytics, règles de détection au-dessus d'OpenSearch (Apache 2.0) : <https://opensearch.org/>
- DFIR-IRIS, gestion collaborative des incidents (LGPL v3) : <https://www.dfir-iris.org/>
- CrowdSec, MISP et OpenCTI, présentés à la page [Sécurité](securite.md#autres)
