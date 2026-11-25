# Autres applicatifs métiers { #autres }

Cette rubrique réunit des applications propres à un métier : santé, géomatique, associations, collectivités et industrie. Elle ne prétend pas couvrir chaque secteur : elle signale des solutions actives et les points à examiner.

Les critères de la partie s’y appliquent sans réserve : conformité réglementaire, prestataires en mesure d’intervenir et nombre d’organisations comparables en production. Un logiciel de santé ou de télétransmission suppose un dossier de conformité que la seule licence ne fournit pas.

## Santé

### GNU Health

Site
: <https://www.gnuhealth.org/>

Porteur
: une association (GNU Solidario)

Licence
: GPL v3 ou ultérieure

GNU Health est un système d’information hospitalier et de santé publique créé par Luis Falcón et publié pour la première fois en 2008. Paquet officiel du projet GNU, il est porté par l’organisation à but non lucratif GNU Solidario.

Il couvre le dossier patient, la gestion hospitalière, le laboratoire et la médecine sociale. Il repose sur le framework [Tryton](../applications-generiques/erp-pgi.md#tryton).

Son usage en France exige une étude de conformité : hébergement de données de santé, identité nationale de santé, facturation à l’assurance maladie. Il est écrit en Python.

### OpenEMR

Site
: <https://www.open-emr.org/>

Porteur
: une communauté

Licence
: GPL v3

OpenEMR est un dossier médical informatisé et un outil de gestion de cabinet. Il dispose aux États-Unis de la certification ONC.

Il comprend le dossier, les rendez-vous, les ordonnances et la facturation. La facturation américaine est centrale dans l’outil : l’adaptation au contexte français représente un projet à part entière.

OpenEMR est écrit en PHP.

## Systèmes d’information géographique

### GeoServer

Site
: <https://geoserver.org/>

Porteur
: une fondation (OSGeo)

Licence
: GPL v2

GeoServer publie des données géographiques selon les standards de l’Open Geospatial Consortium (WMS, WFS, WCS, WMTS). Il lit de nombreuses sources, dont PostGIS, des fichiers et des images.

Il sert de brique d’infrastructure à une infrastructure de données géographiques, en complément de [PostGIS](../sgbd-middleware/bases-de-donnees.md#postgis) et de [QGIS](../applications-generiques/autres.md#quantum-gis) sur le poste.

Un service exposé sur internet doit être tenu à jour et restreint aux couches et opérations utiles. GeoServer est écrit en Java.

### GeoNode

Site
: <https://geonode.org/>

Porteur
: une fondation (OSGeo)

Licence
: GPL v3

GeoNode est un gestionnaire de contenus géographiques : catalogue, métadonnées, cartes en ligne, droits et partage. C’est un projet communautaire de l’OSGeo.

Il s’appuie sur GeoServer pour publier les couches et permet à des agents non spécialistes de déposer et de consulter des données. L’assemblage est plus lourd à administrer qu’un simple serveur de cartes.

GeoNode est écrit en Python (Django).

## Associations

### Galette

Site
: <https://galette.eu/>

Porteur
: une communauté

Licence
: GPL v3

Galette gère les adhérents et les cotisations d’une association depuis un navigateur : fiches, contributions, reçus et envois. Son périmètre ciblé le rend simple à installer et à transmettre.

Elle ne remplace pas une comptabilité. Galette est écrit en PHP.

### Paheko

Site
: <https://paheko.cloud/>

Porteur
: une communauté

Licence
: AGPL v3

Paheko (anciennement Garradin), développé depuis 2012, réunit adhérents, cotisations, comptabilité en partie double, documents, site web et temps bénévole.

Il convient aux petites associations qui veulent un seul outil. Une offre hébergée finance le projet. Son développement a lieu sur <https://fossil.kd2.org/paheko/>.

## Collectivités

### Pastell

Site
: <https://www.libriciel.fr/logiciels/pastell/>

Porteur
: une entreprise (Libriciel SCOP)

Licence
: AGPL v3

Pastell (*Plate-forme Adullact Sécurisée Transactionnelle d’Échanges en Logiciel Libre*) orchestre les échanges dématérialisés d’une administration entre ses applications métier, sa signature, la télétransmission et l’archivage.

Le code est publié sur la forge de l’[ADULLACT](https://adullact.org/). La coopérative Libriciel SCOP en assure l’édition, l’intégration et le support. Pastell est écrit en PHP.

### S²LOW

Site
: <https://gitlab.adullact.net/Libriciel/s2low>

Porteur
: une entreprise (Libriciel SCOP)

Licence
: AGPL v3

S²LOW est une plateforme de télétransmission des documents échangés entre les collectivités et leurs partenaires, dont les actes administratifs et les flux comptables (Hélios).

Son usage dépend des certificats, des habilitations et des raccordements de chaque collectivité, qui s’organisent avec l’opérateur retenu. L’ADULLACT maintient aussi PubliS²LOW, qui publie les actes sur un site web (AGPL v3).

## Industrie

### InvenTree

Site
: <https://inventree.org/>

Porteur
: une communauté

Licence
: MIT

InvenTree gère les pièces, les stocks et les nomenclatures multiniveaux d’un atelier ou d’un bureau d’études. Il couvre les commandes, les fabrications et l’étiquetage. Des greffons l’étendent.

Son périmètre s’arrête à la pièce et au stock ; la comptabilité et les ventes relèvent d’un [ERP](../applications-generiques/erp-pgi.md). InvenTree est écrit en Python (Django) et React.

### frePPLe

Site
: <https://frepple.com/>

Porteur
: un éditeur (frePPLe)

Licence
: MIT (édition communautaire) et propriétaire

frePPLe planifie la production et prévoit la demande, sous contrainte de matières et de capacité. Il peut s’intégrer à Odoo.

L’éditeur belge distribue le produit sous double licence : la comparaison entre l’édition communautaire et l’édition commerciale se fait sur le besoin réel de planification. frePPLe est écrit en C++ et Python.

## Voir également

Les fiches suivantes sont désormais dans [Applications génériques, Autres](../applications-generiques/autres.md) :

- [QGIS](../applications-generiques/autres.md#quantum-gis){ #quantum-gis }
- [Revive Adserver (ex-OpenX Source)](../applications-generiques/autres.md#revive-adserver-ex-openx-source){ #revive-adserver-ex-openx-source }
- [LimeSurvey](../applications-generiques/autres.md#limesurvey){ #limesurvey }
