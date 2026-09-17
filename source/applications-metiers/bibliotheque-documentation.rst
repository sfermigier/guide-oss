Bibliothèque & Documentation
============================

Adossés à l’univers de la gestion documentaire, des outils open source de gestion bibliothécaire et de documentation ont vu le jour ces dernières années.

On peut notamment citer Koha ou PMB. À ces SIGB s'ajoutent, pour la valorisation de collections numériques et d'archives, des outils comme Omeka S (https://omeka.org/s/) ou AtoM (https://accesstomemory.org/).

Parmi les principales fonctionnalités de ces outils, on peut citer : import de notices et catalogage UNIMARC, gestion des lecteurs, prêts/retours avec amendes, périodiques et commandes, OPAC, Client et Serveur Z3950, serveur OAI-PMH, gestion de thesaurus, OPAC (interface de consultation à destination des utilisateurs), DSI (diffusion selon centres d'intérêt), gestion des périodiques et des achats, etc..


Koha
----

:Site: https://koha-community.org/
:Porteur: une communauté
:Licence: GPL v3

Ce SIGB (système intégré de gestion de bibliothèque) a été créé en 1999 par un consortium de quatre bibliothèques néo-zélandaises. Koha s'adresse surtout aux bibliothèques souhaitant respecter le standard de catalogage UNIMARC.

Parmi les principales fonctionnalités de Koha, on peut citer : import de notices et catalogage UNIMARC, gestion des lecteurs, prêts/retours avec amendes, périodiques et commandes, OPAC, Client et Serveur Z3950, serveur OAI-PMH. A l'exception de la récupération d'une vignette, Koha ne propose pas de fonctions de GED. Il est conseillé de remplacer l'OPAC de consultation par un CMS (un connecteur Drupal existe par exemple) pour disposer d'une ergonomie plus agréable.

Koha est maintenu par une communauté internationale, avec deux versions majeures par an. Attention au site officiel : le domaine koha.org appartient à une société commerciale éditrice d'un fork ; celui du projet communautaire est koha-community.org. Plusieurs sociétés françaises (BibLibre, Tamil…) fournissent de l'hébergement, du support et des développements spécifiques.

Koha est développé en Perl et tourne principalement sous Debian, mais peut également s'installer sous d'autres systèmes UNIX. Le moteur de base de données est MariaDB (ou MySQL) ; l'indexation et la recherche s'appuient sur Zebra ou, plus récemment, sur Elasticsearch/OpenSearch.


PMB
---

:Site: https://www.sigb.net/
:Porteur: un éditeur (PMB Services)
:Licence: CeCILL

Créé en 2003 par la société française PMB Services, ce SIGB très complet s'adresse plutôt aux centres de ressources documentaires et bibliothèques spécialisées qui n'ont pas besoin de cataloguer en Unimarc.

Parmi les principales fonctionnalités de PMB, on peut citer : catalogage de tout type de document (textuel, multimédia, web) avec attachement de fichiers, indexation plein texte, import de notices (Unimarc, CSV, etc.), gestion de thésaurus, OPAC (interface de consultation à destination des utilisateurs), DSI (diffusion selon centres d'intérêt), gestion des lecteurs, gestion des prêts et des retours, gestion des périodiques et des achats, client Z39.50, portail documentaire.

Le support et les développements sont assurés pour l'essentiel par la société éditrice, PMB Services, et par un petit nombre de partenaires.

PMB a été développé autour d’une plateforme LAMP/WAMP (plateforme Apache, PHP, MySQL), qui peut donc fonctionner sous Linux, Mac OS X ou Microsoft Windows.

