# PKI

Les solutions de type PKI permettent de sécuriser les relations électroniques (email par exemple) en garantissant confidentialité, authentification, intégrité et non-répudiation, que ce soit à travers des certificats de signature (d’e-mail ou d’accès web) ou de chiffrement (cryptage bi-clef).

En sécurisant la gestion des identités, les outils de PKI facilitent le développement des activités transactionnelles, qu’elles soient externes (relations contractuelles et commerciales) ou internes (responsabilisation des collaborateurs).

Parmi les solutions open source disponibles, on peut citer OpenSSL, EJBCA, Dogtag ou step-ca.

Le contexte a beaucoup changé : la généralisation de Let's Encrypt et du protocole ACME a rendu quasi automatique la gestion des certificats destinés au web public, tandis que les autorités de certification internes se concentrent sur les usages d'entreprise : authentification des utilisateurs et des machines, signature, chiffrement, mTLS entre services. Les fiches ci-dessous distinguent ces deux mondes.

## OpenSSL

Site
: <https://openssl-library.org/>

Porteur
: une fondation (OpenSSL Foundation) et une entreprise (OpenSSL Corporation)

Licence
: Apache 2.0 (depuis la version 3.0)

OpenSSL est la bibliothèque open source, quasiment élevée au rang de standard, en ce qui concerne les fonctions cryptographiques. En particulier, elle implémente complètement le standard des PKI, i.e la norme X.509.

En plus d'offrir le chiffrement ainsi que le hachage possible avec les algorithmes courants elle permet également, avec la prise en charge de X.509, d'émettre et de révoquer des certificats ainsi que de parfaitement gérer des chaînes de certification. Elle peut écrire et réécrire les certificats dans les formats les plus courants du marché. Nombre d'outils plus avancés en termes d'utilisabilité sont fondés sur OpenSSL.

Le projet a débuté en 1998, à partir de SSLeay. Les versions antérieures à la 3.0 relevaient d'une double licence OpenSSL et SSLeay.

Développé en C, elle reste la référence dans le domaine Linux et BSD et se retrouve souvent utilisée dans tout contexte nécessitant un chiffrement (allant des protocoles 802.11 aux communications HTTPS, en passant par SSH et FTPS).

## step-ca

Site
: <https://smallstep.com/docs/step-ca/>

Porteur
: une entreprise (Smallstep)

Licence
: Apache 2.0

step-ca est une autorité de certification interne moderne, conçue pour être mise en service en quelques minutes là où les PKI traditionnelles demandent des jours de configuration.

Elle expose une interface ACME (le même protocole que Let's Encrypt), ce qui permet d'automatiser l'émission et le renouvellement des certificats internes avec les mêmes outils que ceux du web public (Certbot, acme.sh, Caddy, Traefik, cert-manager). Elle prend également en charge les certificats SSH, l'authentification par fournisseur d'identité OIDC, les jetons à usage unique pour l'enrôlement des machines et les certificats de courte durée, qui rendent la révocation à peu près superflue.

C'est aujourd'hui l'outil le plus adapté aux architectures de services internes en mTLS.

step-ca est écrit en Go.

Pour un usage ponctuel et manuel, XCA (voir ci-dessous) ou les sous-commandes `openssl ca` restent des options.

## EJBCA

Site
: <https://www.ejbca.org>

Porteur
: un éditeur (Keyfactor, anciennement PrimeKey)

Licence
: LGPL v2.1

Développée depuis 2001, EJBCA est une solution open source de gestion de PKI parmi les plus complètes qui soient. Elle est portée par la société suédoise PrimeKey, rachetée en 2021 par l'américain Keyfactor ; l'édition EJBCA Community reste publiée sous licence LGPL, les fonctions les plus avancées et le support relevant de l'édition Enterprise.

À l'instar d'autres solutions de PKI, EJBCA gère tous les aspects de la certification X.509 courante : émission de certificats, révocations avec CRL, chaînes de certification. Son avantage est d'aller plus loin que la plupart en implémentant une grande partie des standards liés à la spécification X.509 (répondeur OCSP, CMS...) et gère correctement les matériels spécifiques tels que les HSM. Il propose également une interface d'administration complète avec restrictions des droits ainsi qu'un portail client.

Un support commercial est disponible auprès de l'éditeur.

D'un point de vue technique, EJBCA est écrit intégralement en Java et s'exécute sur un serveur d'applications Jakarta EE (WildFly ou Payara). Il prend en charge les protocoles d'enrôlement du marché (ACME, SCEP, CMP, EST) et les modules matériels de sécurité (HSM), ce qui convient aux PKI réglementées.

## Dogtag PKI

Site
: <https://www.dogtagpki.org>

Porteur
: une communauté, avec le soutien de Red Hat

Licence
: GPL v2

Dogtag PKI est une solution complète et open source de gestion de PKI, développée à l'origine par Red Hat et désormais soutenue par une communauté active. Le projet a débuté en 2001.

Dogtag PKI offre un ensemble complet de fonctionnalités pour gérer les certificats numériques, y compris l'émission et la révocation de certificats, la gestion des listes de révocation de certificats (CRL), un répondeur OCSP et une interface web pour l'administration. Il s'intègre également avec les HSM (Hardware Security Modules) pour améliorer la sécurité des clés privées.

Dogtag PKI est écrit en Java et Python et est conçu pour fonctionner sur des systèmes Linux, notamment les distributions fondées sur Red Hat.

## XCA

Site
: <https://hohnstaedt.de/xca/>

Porteur
: une communauté

Licence
: BSD

XCA (X Certificate and Key management) est une application open source permettant de gérer les certificats X.509, les clés privées et les requêtes de signature de certificats (CSR). Le projet a été lancé en 2003.

XCA offre une interface utilisateur graphique qui simplifie la création et la gestion des certificats, des clés privées et des CSR. Il permet également d'importer et d'exporter des certificats et des clés dans différents formats, de gérer des templates de certificats et de générer des CRL.

XCA est écrit en C++ et utilise la bibliothèque Qt pour son interface graphique.

## cert-manager

Site
: <https://cert-manager.io>

Porteur
: une fondation (CNCF)

Licence
: Apache 2.0

cert-manager est une solution open source conçue pour simplifier la gestion des certificats dans les clusters Kubernetes. Le projet a été initialement lancé en 2017.

cert-manager automatise l'émission et le renouvellement des certificats X.509 à partir de diverses autorités de certification (CA), telles que Let's Encrypt, HashiCorp Vault et Venafi. Il utilise les Custom Resource Definitions (CRD) de Kubernetes pour gérer les certificats et les sources de certificats. Il s'intègre facilement avec des services Kubernetes.

cert-manager est écrit en Go. Accepté par la *Cloud Native Computing Foundation* en 2020 et diplômé en 2024, il est le standard de fait pour la gestion des certificats dans Kubernetes. La société Jetstack, à son origine, a été rachetée en 2020 par Venafi, elle-même acquise en 2024 par CyberArk, qui a été rachetée en février 2026 par Palo Alto Networks ; le projet relève de la CNCF.

## Certbot et l'écosystème ACME { #certbot-et-l-ecosysteme-acme }

Site
: <https://certbot.eff.org/>

Porteur
: une fondation (Electronic Frontier Foundation)

Licence
: Apache 2.0

Pour les certificats destinés au web public, la question s'est largement simplifiée depuis la création de **Let's Encrypt** (<https://letsencrypt.org/>) en 2015 : cette autorité de certification, à but non lucratif, délivre gratuitement des certificats de domaine validés automatiquement par le protocole ACME. Elle a joué un rôle décisif dans la généralisation de HTTPS.

Certbot, développé par l'EFF, en est le client de référence : il obtient, installe et renouvelle automatiquement les certificats, avec des greffons pour les principaux serveurs web et une validation possible par enregistrement DNS (utile pour les certificats génériques). Les alternatives notables sont acme.sh (<https://github.com/acmesh-official/acme.sh>), écrit en shell, maintenu par l'autorité de certification ZeroSSL, qu'il utilise par défaut, ainsi que l'intégration ACME native de Caddy, de Traefik et de step-ca.

## Comparatif des solutions PKI open source

| Nom | Site | Porteur | Licence | Année de création | Langage principal | Fonctionnalités clés |
|----|----|----|----|----|----|----|
| OpenSSL | <https://openssl-library.org/> | une fondation et une entreprise | Apache 2.0 | 1998 | C | Chiffrement, hachage, gestion des certificats X.509, réécriture de certificats |
| step-ca | <https://smallstep.com/docs/step-ca/> | une entreprise (Smallstep) | Apache 2.0 | 2018 | Go | Autorité de certification interne avec interface ACME, certificats SSH, certificats de courte durée |
| EJBCA | <https://www.ejbca.org> | un éditeur (Keyfactor, ex-PrimeKey) | LGPL | 2001 | Java | Émission et révocation de certificats, répondeur OCSP, protocoles ACME/SCEP/CMP/EST, gestion des HSM |
| Dogtag PKI | <https://www.dogtagpki.org> | une communauté (soutien de Red Hat) | GPL v2 | 2008 | Java, Python | Émission et révocation de certificats, gestion des CRL, répondeur OCSP, intégration des HSM |
| XCA | <https://hohnstaedt.de/xca/> | une communauté | BSD | 2003 | C++ | Gestion des certificats X.509, clés privées, CSR, interface graphique |
| cert-manager | <https://cert-manager.io> | une fondation (CNCF) | Apache 2.0 | 2017 | Go | Automatisation de l'émission et du renouvellement des certificats dans Kubernetes, intégration avec diverses CA |
| Certbot | <https://certbot.eff.org/> | une fondation (EFF) | Apache 2.0 | 2015 | Python | Client ACME de référence : obtention et renouvellement automatiques des certificats Let's Encrypt |

<span id="openca"></span>
