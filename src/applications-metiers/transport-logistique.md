# Transport et logistique { #transport-logistique }

Le transport et la logistique mêlent plusieurs problèmes : organiser des tournées, calculer des itinéraires, suivre des colis et gérer des stocks. L’offre open source est surtout faite de briques (solveurs, moteurs d’itinéraires, cartographie) à assembler, plus que de progiciels complets.

La qualité du résultat dépend des données : adresses, réseau routier, horaires, capacités des véhicules. OpenStreetMap fournit un fonds cartographique libre, mais les contraintes propres à chaque métier restent à modéliser et à vérifier sur des tournées réelles.

## Mapotempo

Site
: <https://github.com/Mapotempo>

Porteur
: une entreprise (Mapotempo, rattachée à Woop)

Licence
: AGPL v3

Mapotempo est une suite de solutions de gestion d'itinéraires, qui prend en charge l'optimisation, la planification et l'exécution des tournées. Elle permet aux transporteurs et aux entreprises disposant d'une flotte de faire de leurs tournées un axe d'amélioration de la qualité de service et de réduction des coûts d'exploitation.

La société bordelaise Mapotempo a été rachetée par Woop en novembre 2021 : le produit commercial s'appelle désormais Mapo. Les composants libres publiés par Mapotempo, dont *optimizer-api*, n'évoluent plus guère (dernière modification en juin 2023 pour ce dernier). Le dépôt public de Mapotempo Web n'est plus accessible. Cartoway en publie sous AGPL v3 une reprise active, avec *planner-web* (issu du code de Mapotempo Web) et *optimizer-api* : <https://github.com/cartoway>.

## Autres

Parmi les briques open source utiles au transport et à la logistique, on peut également citer :

- Vroom (optimisation de tournées de véhicules): <https://github.com/VROOM-Project/vroom>
- OR-Tools (solveur d'optimisation de Google): <https://developers.google.com/optimization>
- OpenTripPlanner (calcul d'itinéraires multimodaux): <https://www.opentripplanner.org/>
- OSRM (calcul d'itinéraires routiers sur données OpenStreetMap): <https://project-osrm.org/>
- Odoo et Dolibarr, qui disposent de modules de gestion des stocks et des expéditions (section [ERP / PGI](../applications-generiques/erp-pgi.md))
