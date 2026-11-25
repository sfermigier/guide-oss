# Signature électronique

Une plateforme de signature prépare un document, le soumet aux signataires, recueille leur accord et conserve une preuve : journal, horodatage, empreinte du document. Héberger ce service permet de garder les contrats hors des plateformes américaines.

Le règlement européen eIDAS (n° 910/2014, article 25) dispose qu’une signature électronique ne peut être privée d’effet juridique ni refusée comme preuve au seul motif de sa forme électronique ou parce qu’elle n’est pas qualifiée. Seule la signature **qualifiée** a, dans toute l’Union, le même effet juridique qu’une signature manuscrite.

Les logiciels présentés ici fournissent un parcours de signature. Le niveau juridique obtenu dépend du certificat, du mode d’identification et du prestataire de confiance retenus, qui restent à choisir et à documenter.

## Documenso

Site
: <https://documenso.com/>

Porteur
: un éditeur (Documenso, Inc.)

Licence
: AGPL v3

Documenso se présente comme une alternative ouverte à DocuSign, avec modèles de documents, destinataires multiples, suivi et API.

L’édition auto-hébergée convient aux organisations qui veulent intégrer la signature à leurs propres outils. L’éditeur vend un service hébergé et une offre commerciale.

Il faut fournir son propre certificat de signature et vérifier la recevabilité du niveau obtenu pour chaque type d’acte. Documenso est écrit en TypeScript.

## DocuSeal

Site
: <https://www.docuseal.com/>

Porteur
: un éditeur (DocuSeal)

Licence
: AGPL v3, avec clause d’attribution

DocuSeal permet de construire un formulaire à partir d’un PDF, de le faire remplir et signer, puis d’en conserver la trace. Il s’installe comme une application unique et s’intègre à d’autres outils par API.

Son usage va du bon de commande au dossier d’embauche. L’éditeur propose une offre hébergée et des fonctions commerciales.

La licence comporte des conditions additionnelles au titre de l’article 7(b) de l’AGPL : l’attribution à DocuSeal doit rester visible dans l’interface interactive. DocuSeal est écrit en Ruby (Rails).

## Autres

- LibreSign, application de signature pour Nextcloud (AGPL v3) : <https://libresign.coop/>
- OpenSign (AGPL v3, hors une partie réservée au service hébergé) : <https://www.opensignlabs.com/>
- DSS, bibliothèque Java de la Commission européenne pour créer et valider des signatures (LGPL v2.1) : <https://github.com/esig/dss>
- [Pastell](../applications-metiers/autres.md#pastell) et [S²LOW](../applications-metiers/autres.md#s2low), pour la dématérialisation dans les collectivités
