PKI
===

Les solutions de type PKI permettent de sécuriser les relations électroniques (email par exemple) en garantissant confidentialité, authentification, intégrité et non-répudiation, que ce soit à travers des certificats de signature (d’e-mail ou d’accès web) ou de chiffrement (cryptage bi-clef).

En sécurisant la gestion des identités, les outils de PKI facilitent le développement des activités transactionnelles, qu’elles soient externes (relations contractuelles et commerciales) ou internes (responsabilisation des collaborateurs).

Parmi les solutions open source disponibles, on peut citer OpenSSL, EJBCA, Dogtag ou step-ca.

Le contexte a beaucoup changé depuis les premières éditions de ce guide : la généralisation de Let's Encrypt et du protocole ACME a rendu quasi automatique la gestion des certificats destinés au web public, tandis que les autorités de certification internes se concentrent sur les usages d'entreprise — authentification des utilisateurs et des machines, signature, chiffrement, mTLS entre services. Les fiches ci-dessous distinguent ces deux mondes.


OpenCA
------

:Site: https://www.openca.org
:Porteur: une communauté
:Licence: BSD

OpenCA PKI est aujourd'hui la composante d'un vaste projet communautaire, visant à définir les standards de développement d'un logiciel de PKI. OpenCA PKI en est la partie dédiée à la gestion des certificats.

D'une conception modulaire, il fournit une interface web pour réaliser aisément la plupart des tâches courantes (révocation et émission de certificats, tests...). Il permet également une restriction des droits. Avec les autres composants du projet PKI tel que le répondeur OCSP, il peut participer à l'établissement d'une solution complète de PKI.

Le développement, entièrement communautaire, a été initié en 2001. Il est aujourd'hui très ralenti : pour une nouvelle mise en œuvre, on lui préférera EJBCA, Dogtag ou step-ca.

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


step-ca
-------

:Site: https://smallstep.com/certificates/
:Porteur: une entreprise (Smallstep)
:Licence: Apache 2.0

step-ca est une autorité de certification interne moderne, conçue pour être mise en service en quelques minutes là où les PKI traditionnelles demandent des jours de configuration.

Elle expose une interface ACME — le même protocole que Let's Encrypt —, ce qui permet d'automatiser l'émission et le renouvellement des certificats internes avec les mêmes outils que ceux du web public (Certbot, acme.sh, Caddy, Traefik, cert-manager). Elle prend également en charge les certificats SSH, l'authentification par fournisseur d'identité OIDC, les jetons à usage unique pour l'enrôlement des machines, et les certificats de courte durée, qui rendent la révocation à peu près superflue.

C'est aujourd'hui l'outil le plus adapté aux architectures de services internes en mTLS.

step-ca est écrit en Go.

*Note :* easyCA, script Bash de gestion de petites autorités de certification présenté dans les éditions précédentes de ce guide, n'est plus maintenu depuis longtemps. Pour un usage ponctuel et manuel, XCA (voir ci-dessous) ou les sous-commandes `openssl ca` restent des options.


EJBCA
-----

:Site: https://www.ejbca.org
:Porteur: un éditeur (Keyfactor, anciennement PrimeKey)
:Licence: LGPL

Développée depuis 2001, EJBCA est une solution open source de gestion de PKI parmi les plus complètes qui soient. Elle est portée par la société suédoise PrimeKey, rachetée en 2021 par l'américain Keyfactor ; l'édition EJBCA Community reste publiée sous licence LGPL, les fonctions les plus avancées et le support relevant de l'édition Enterprise.

A l'instar d'autres solutions de PKI, EJBCA permet non seulement de gérer tous les aspects de la certification courante X509 (émission de certificats, révocations avec CRL, chaînes de certifications) mais fait partie des seuls produits, et c'est là son grand avantage, à implémenter une grande partie des standards liés à la spécification X509 (répondeur OCSP, CMS...) et gère correctement les matériels spécifiques tels que les HSM. Il propose également une interface d'administration complète avec restrictions des droits ainsi qu'un portail client.

Un support commercial est disponible auprès de l'éditeur.

D'un point de vue technique, EJBCA est écrit intégralement en Java et s'exécute sur un serveur d'applications Jakarta EE (WildFly ou Payara). Il prend en charge les protocoles d'enrôlement du marché (ACME, SCEP, CMP, EST) et les modules matériels de sécurité (HSM), ce qui en fait une solution adaptée aux PKI réglementées.

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

cert-manager est écrit en Go. Devenu projet diplômé de la *Cloud Native Computing Foundation*, il est le standard de fait pour la gestion des certificats dans Kubernetes. La société Jetstack, à son origine, a été rachetée par Venafi, elle-même passée chez CyberArk, mais le projet relève désormais de la gouvernance de la CNCF.

Certbot et l'écosystème ACME
----------------------------

:Site: https://certbot.eff.org/
:Porteur: une fondation (Electronic Frontier Foundation)
:Licence: Apache 2.0

Pour les certificats destinés au web public, la question s'est largement simplifiée depuis la création de **Let's Encrypt** (https://letsencrypt.org/) en 2015 : cette autorité de certification, à but non lucratif, délivre gratuitement des certificats de domaine validés automatiquement par le protocole ACME, et a joué un rôle décisif dans la généralisation de HTTPS.

Certbot, développé par l'EFF, en est le client de référence : il obtient, installe et renouvelle automatiquement les certificats, avec des greffons pour les principaux serveurs web et une validation possible par enregistrement DNS (utile pour les certificats génériques). Les alternatives notables sont acme.sh (https://acme.sh/), écrit en shell et très léger, et l'intégration ACME native de Caddy, de Traefik et de step-ca.

*Note :* deux outils présentés dans les éditions précédentes de ce guide ont disparu — TinyCA, interface Perl/GTK de gestion d'une autorité de certification, dont le site n'est plus en service, et Lemur, la solution de gestion de certificats de Netflix, dont le dépôt est archivé.


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
     - Émission et révocation de certificats, répondeur OCSP ; développement très ralenti

   * - OpenSSL
     - https://www.openssl.org
     - une communauté
     - Apache et BSD
     - Avant 1998
     - C
     - Chiffrement, hachage, gestion des certificats X.509, réécriture de certificats

   * - step-ca
     - https://smallstep.com/certificates/
     - une entreprise (Smallstep)
     - Apache 2.0
     - 2018
     - Go
     - Autorité de certification interne avec interface ACME, certificats SSH, certificats de courte durée

   * - EJBCA
     - https://www.ejbca.org
     - Keyfactor (ex-PrimeKey)
     - LGPL
     - 2001
     - Java
     - Émission et révocation de certificats, répondeur OCSP, protocoles ACME/SCEP/CMP/EST, gestion des HSM

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

   * - Certbot
     - https://certbot.eff.org/
     - une fondation (EFF)
     - Apache 2.0
     - 2015
     - Python
     - Client ACME de référence : obtention et renouvellement automatiques des certificats Let's Encrypt
