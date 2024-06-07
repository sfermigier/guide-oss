PKI
===

Les solutions de type PKI permettent de sécuriser les relations électroniques (email par exemple) en garantissant confidentialité, authentification, intégrité et non-répudiation, que ce soit à travers des certificats de signature (d’e-mail ou d’accès web) ou de chiffrement (cryptage bi-clef).

En sécurisant la gestion des identités, les outils de PKI facilitent le développement des activités transactionnelles, qu’elles soient externes (relations contractuelles et commerciales) ou internes (responsabilisation des collaborateurs).

Parmi les solutions open source disponibles, on peut citer OpenSSL, OpenCA ou encore EJBCA.


OpenCA
------

:Site: https://www.openca.org
:Porteur: une communauté
:Licence: BSD

OpenCA PKI est aujourd'hui la composante d'un vaste projet communautaire, visant à définir les standards de développement d'un logiciel de PKI. OpenCA PKI en est la partie dédiée à la gestion des certificats.

D'une conception modulaire, il fournit une interface web pour réaliser aisément la plupart des tâches courantes (révocation et émission de certificats, tests...). Il permet également une restriction des droits. Avec les autres composants du projet PKI tel que le répondeur OCSP, il peut participer à l'établissement d'une solution complète de PKI.

Le développement, entièrement communautaire, a été initié en 2001 et se poursuit activement.

La solution est très hétérogène mais utilise des standards actuels reconnus : le serveur web est basé sur Apache 2 et l'interface écrite en Perl. Les mécanismes de cryptographie sont basés sur OpenSSL. Enfin, la gestion des certificats est réalisée par OpenLDAP.


OpenSSL
-------

:Site: https://www.openssl.org
:Porteur: une communauté
:Licence: Apache et BSD

OpenSSL est la librairie open source, quasiment élevée au rang de standard, en ce qui concerne les fonctions cryptographiques. En particulier, elle implémente complètement le standard des PKI, i.e la norme X509.

En plus d'offrir le chiffrement ainsi que le hachage possible avec n'importe quel algorithme connu (MD5, AES, blowfish...) elle permet également, avec le support X509, d'émettre et de révoquer des certificats ainsi que de parfaitement gérer des chaînes de certification. Elle peut écrire et réécrire les certificats dans les formats les plus courants du marché, et nombre d'outils plus avancés en terme d'utilisabilité sont basés sur OpenSSL.

Le développement d'OpenSSL est ancien et a débuté avant 1998.

Développé en C, elle reste la référence dans le domaine Linux et BSD et se retrouve souvent utilisée dans tout contexte nécessitant un chiffrement (allant des protocoles 802.11 aux communications HTTPS, en passant par SSH et FTPS).


easyCA
------

:Site: http://sourceforge.net/projects/easyca
:Porteur: une communauté

easyCA permet de gérer très rapidement et sans fioriture une PKI de petite taille. Il a été développé par Ferry Kemps en 2005.

Il permet de s'abstraire quasi-totalement de la complexité relative d'OpenSSL en permettant de créer très vite ses autorités de certification ainsi que ses certificats Client. Il permet en outre la gestion des révocations et propose des options d'export pour sauvegarde.

Sous licence GPL, le développement semble toutefois désormais interrompu. Cependant, le script de base a été repris dans de nombreux projets indépendants et s'est vu compléter par de nouvelles fonctionnalités (OCSP, etc...).

easyCA est écrit en Bash et ne requiert aucune dépendance, hormis OpenSSL. Il est facilement éditable et personnalisable pour les besoins de la plupart des administrateurs système.


EJBCA
-----

:Site: https://www.ejbca.org
:Porteur: un éditeur (Primekey)
:Licence: LGPL

Développée depuis 2001, EJBCA est une solution open-source de gestion PKI, parmi les plus complètes qui soient. Il est actuellement porté et maintenu activement par la société suédoise Primekey.

A l'instar d'autres solutions de PKI, EJBCA permet non seulement de gérer tous les aspects de la certification courante X509 (émission de certificats, révocations avec CRL, chaînes de certifications) mais fait partie des seuls produits, et c'est là son grand avantage, à implémenter une grande partie des standards liés à la spécification X509 (répondeur OCSP, CMS...) et gère correctement les matériels spécifiques tels que les HSM. Il propose également une interface d'administration complète avec restrictions des droits ainsi qu'un portail client.

Un support commercial est contractable auprès de la société éditrice Primekey.

D'un point de vue technique, EJBCA est écrit intégralement en Java et est propulsé par un serveur d'applications JEE, qui peut être aussi bien JBoss que Glassfish. Il fait partie des rares produits respectant intégralement les spécifications Java Beans.

Dogtag PKI
----------

:Site: https://www.dogtagpki.org
:Porteur: une communauté (soutenu par Red Hat)
:Licence: GPL v2

Dogtag PKI est une solution complète et open source de gestion de PKI, développée à l'origine par Red Hat et désormais soutenue par une communauté active. Le projet a débuté en 2001.

Dogtag PKI offre un ensemble complet de fonctionnalités pour gérer les certificats numériques, y compris l'émission et la révocation de certificats, la gestion des listes de révocation de certificats (CRL), un répondeur OCSP, et une interface web pour l'administration. Il supporte également l'intégration avec les HSM (Hardware Security Modules) pour améliorer la sécurité des clés privées.

Dogtag PKI est écrit en Java et Python et est conçu pour fonctionner sur des systèmes Linux, notamment les distributions basées sur Red Hat.

XCA
---

:Site: https://hohnstaedt.de/xca/
:Porteur: une communauté
:Licence: BSD

XCA (X Certificate and Key management) est une application open source permettant de gérer les certificats X.509, les clés privées et les requêtes de signature de certificats (CSR). Le projet a été lancé en 2003.

XCA offre une interface utilisateur graphique qui simplifie la création et la gestion des certificats, des clés privées, et des CSR. Il permet également d'importer et d'exporter des certificats et des clés dans différents formats, de gérer des templates de certificats, et de générer des CRL.

XCA est écrit en C++ et utilise la bibliothèque Qt pour son interface graphique.

cert-manager
------------

:Site: https://cert-manager.io
:Porteur: une communauté (soutenu par Jetstack)
:Licence: Apache v2

cert-manager est une solution open source conçue pour simplifier la gestion des certificats dans les clusters Kubernetes. Le projet a été initialement lancé en 2017.

cert-manager automatise l'émission et le renouvellement des certificats X.509 à partir de diverses autorités de certification (CA), telles que Let's Encrypt, HashiCorp Vault, et Venafi. Il utilise les Custom Resource Definitions (CRD) de Kubernetes pour gérer les certificats et les sources de certificats, et s'intègre facilement avec des services Kubernetes.

cert-manager est écrit en Go et est maintenu par une communauté active, avec le soutien de Jetstack.

TinyCA
------

:Site: http://tinyca.sm-zone.net
:Porteur: une communauté
:Licence: GPL v2

TinyCA est une interface graphique simplifiée pour la gestion d'une autorité de certification (CA) open source. Le projet a débuté en 2002.

TinyCA permet de créer et de gérer des certificats, des clés privées, et des CSR. Il est conçu pour être facile à utiliser et offre une interface utilisateur intuitive basée sur GTK. TinyCA supporte également l'exportation et l'importation de certificats et de clés dans différents formats.

TinyCA est écrit en Perl et utilise l'interface graphique GTK pour la gestion des certificats.

Lemur
-----

:Site: https://github.com/Netflix/lemur
:Porteur: une communauté (développé par Netflix)
:Licence: Apache v2

Lemur est une solution open source développée par Netflix pour la gestion des certificats TLS. Le projet a été lancé en 2015.

Lemur facilite la création, le renouvellement, et la distribution des certificats TLS pour les services web. Il intègre des fonctionnalités de gestion centralisée des certificats, de génération de rapports, et de notifications sur les expirations de certificats. Lemur supporte plusieurs CA et peut s'intégrer avec des solutions telles que Let's Encrypt, DigiCert, et Venafi.

Lemur est écrit en Python et utilise une architecture modulaire pour permettre des extensions et des intégrations personnalisées.


Comparatif des solutions PKI open source
----------------------------------------

.. list-table::
   :header-rows: 1

   * - Nom
     - Site
     - Porteur
     - Licence
     - Année de création
     - Langage principal
     - Fonctionnalités clés

   * - OpenCA
     - https://www.openca.org
     - une communauté
     - BSD
     - 2001
     - Perl
     - Émission et révocation de certificats, répondeur OCSP, gestion des certificats via OpenLDAP

   * - OpenSSL
     - https://www.openssl.org
     - une communauté
     - Apache et BSD
     - Avant 1998
     - C
     - Chiffrement, hachage, gestion des certificats X.509, réécriture de certificats

   * - easyCA
     - http://sourceforge.net/projects/easyca
     - une communauté
     - GPL
     - 2005
     - Bash
     - Création d'autorités de certification, émission et révocation de certificats, gestion des révocations

   * - EJBCA
     - https://www.ejbca.org
     - Primekey
     - LGPL
     - 2001
     - Java
     - Émission et révocation de certificats, répondeur OCSP, CMS, gestion des HSM, interface d'administration

   * - Dogtag PKI
     - https://www.dogtagpki.org
     - une communauté (soutenu par Red Hat)
     - GPL v2
     - 2008
     - Java, Python
     - Émission et révocation de certificats, gestion des CRL, répondeur OCSP, support des HSM

   * - XCA
     - https://hohnstaedt.de/xca/
     - une communauté
     - BSD
     - 2003
     - C++
     - Gestion des certificats X.509, clés privées, CSR, interface graphique

   * - cert-manager
     - https://cert-manager.io
     - une communauté (soutenu par Jetstack)
     - Apache v2
     - 2017
     - Go
     - Automatisation de l'émission et du renouvellement des certificats dans Kubernetes, intégration avec diverses CA

   * - TinyCA
     - http://tinyca.sm-zone.net
     - une communauté
     - GPL v2
     - 2002
     - Perl
     - Création et gestion des certificats, clés privées, CSR, interface graphique intuitive

   * - Lemur
     - https://github.com/Netflix/lemur
     - une communauté (développé par Netflix)
     - Apache v2
     - 2015
     - Python
     - Gestion centralisée des certificats TLS, génération de rapports, notifications d'expiration, intégration avec plusieurs CA
