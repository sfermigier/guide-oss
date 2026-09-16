Authentification, fédération et gestion d’identité
==================================================

Dans cette catégorie, nous vous présentons différentes solutions d’authentification, de fédération et de gestion d’identité.

Il s’agit donc d’outils relativement proches, mais aux finalités parfois différentes : fournisseurs d'identité et serveurs de SSO, produits de fédération entre organisations, gestion des identités et des habilitations, authentification forte.

Le domaine a été profondément remodelé par la généralisation des protocoles OAuth 2.0 et OpenID Connect, qui ont largement supplanté les protocoles propriétaires et, pour beaucoup d'usages, SAML — ce dernier restant incontournable dans l'enseignement supérieur et l'interconnexion entre organisations. Keycloak, absent des éditions précédentes de ce guide, s'est imposé comme la solution de référence de la catégorie.

Sont présentés ci-dessous Keycloak, CAS, FusionDirectory, LemonLDAP::NG, LinOTP et Shibboleth.


Keycloak
--------

:Site: https://www.keycloak.org/
:Porteur: une fondation (CNCF), avec le soutien de Red Hat
:Licence: Apache 2.0

Créé par Red Hat en 2014 et accepté en 2023 comme projet en incubation à la *Cloud Native Computing Foundation*, Keycloak est devenu le fournisseur d'identité open source de référence.

Il couvre l'ensemble du besoin dans un produit unique : authentification unique (SSO) sur les applications web et les API, prise en charge d'OpenID Connect, OAuth 2.0 et SAML 2.0, fédération avec des annuaires LDAP et Active Directory existants, délégation vers des fournisseurs d'identité tiers, gestion des utilisateurs, des rôles et des groupes, authentification multifacteur (TOTP, WebAuthn, clés FIDO2), parcours d'authentification personnalisables, et libre-service pour l'inscription et la récupération de mot de passe.

Son adoption massive tient autant à sa couverture fonctionnelle qu'à son mode de déploiement : conteneurisé, configurable de façon déclarative, il s'intègre naturellement aux architectures actuelles. L'offre commerciale correspondante chez Red Hat est *build of Keycloak*.

Keycloak est écrit en Java (Quarkus).


CAS
---

:Site: https://www.apereo.org/projects/cas
:Porteur: une fondation (Apereo)
:Licence: Apache 2.0


*Central Authentication Service* est un système d'authentification unique (SSO) orienté web. Il a été créé au début des années 2000 à l'université Yale, avant de passer sous l'égide du consortium JA-SIG, devenu depuis la **fondation Apereo**. Il reste très implanté dans l'enseignement supérieur et la recherche, en France comme à l'international.

CAS permet de faire de l'authentification unique entre plusieurs sites, y compris dans des domaines différents, à l'aide de jetons à usage unique. Les applications n'ont jamais accès au mot de passe de l'utilisateur et obtiennent son identifiant en interrogeant CAS. Outre son protocole propre, CAS sait aujourd'hui jouer le rôle de fournisseur d'identité SAML 2.0 et OpenID Connect, et transmettre des attributs complémentaires (groupes, nom, prénom, affiliation…). Il prend également en charge l'authentification multifacteur et les délégations vers des fournisseurs externes. CAS peut utiliser différents types de backend en tant que base utilisateur, tels qu'un annuaire LDAP, une base de données relationnelle, des fichiers à plats, etc. CAS fournit également un système de proxy, permettant à une application de transférer l'identification à une autre application, Web ou non, en backend, tel qu'un webservice ou un serveur IMAP.

CAS est écrit en Java, et fournit des clients CAS pour intégrer les applications au SSO, ceci en Java, PHP et .Net. Un module Apache est également disponible.


FusionDirectory
---------------

:Site: https://www.fusiondirectory.org
:Porteur: un editeur, FusionDirectory
:Licence: GPL

Fusiondirectory est une application de gestion des identités, il est issu d'un fork communautaire de GOsa2 en 2010, en 2019, FusionDirectory qui avait déjà le rôle de steward du projet devient officiellement son éditeur.

FusionDirectory fournit une interface simplifiée pour la gestion des identités tout en étant extensible, il compte aujourd'hui plus de 60 plugins dédiés à des besoins particuliers.

FusionDirectory supporte nativement une série norme et d'applicatifs dédiée à l'enseignement supérieur, recherche : Supann, PARTAGE par RENATER et sinaps de l'AMUE.

L'API FusionDirectory vous permet d'écrire de nouveaux plugins pour étendre ses fonctionnalités et répondre à vos besoins.

Le webservice REST de FusionDirectory lui permet de s'intégrer dans des processus complexes de création de comptes et de groupes, entre autres.

FusionDirectory est écrit en PHP


LemonLDAP::NG
--------------

:Site: https://lemonldap-ng.org/
:Porteur: un consortium (OW2) et une communauté
:Licence: GPL v2

LemonLDAP::NG est un système de SSO et de contrôle d'accès Web, initié en 2003 par le Ministère des finances, puis repris par la Gendarmerie Nationale et Linagora. Il intègre le consortium OW2 en 2007. Il nécessite l’utilisation d’un serveur Apache, mais un mode reverse proxy permet de l'utiliser avec des applications fonctionnant sous un autre serveur (IIS, Tomcat, etc.)

LemonLDAP::NG permet de fonder l'authentification des applications web sur un annuaire LDAP, mais aussi sur de nombreux autres annuaires et bases de données, ainsi que sur des fournisseurs externes (SAML, OpenID Connect, CAS, Kerberos). Il peut lui-même jouer le rôle de fournisseur d'identité CAS, SAML 2.0 et OpenID Connect. Le contrôle d'accès s'effectue par URL pour chaque application protégée, et le produit assure la traçabilité des accès ainsi que l'authentification multifacteur. Il propose une interface d'administration web. C'est une solution très implantée dans l'administration française, où elle bénéficie d'un statut de référence.

Le produit est réalisé en Perl et est facile à personnaliser, aussi bien en termes de comportement que d'apparence via un moteur de template.


OpenAM (attention : n'est plus open source chez son éditeur)
------------------------------------------------------------

:Site: https://github.com/OpenIdentityPlatform/OpenAM
:Porteur: une communauté (Open Identity Platform)
:Licence: CDDL

OpenAM était la solution de gestion d'identités et d'accès de la société ForgeRock, issue du code d'OpenSSO abandonné par Sun Microsystems.

La situation a radicalement changé : ForgeRock a cessé de publier son produit en open source au milieu des années 2010, avant d'être rachetée par le fonds Thoma Bravo en 2023 et fusionnée avec Ping Identity ; l'adresse forgerock.com renvoie désormais vers l'offre commerciale de ce dernier. La dernière version libre a été reprise par le collectif **Open Identity Platform**, qui maintient les forks OpenAM, OpenDJ (annuaire), OpenIDM (gestion des identités) et OpenIG (passerelle) sous licence CDDL.

Pour un nouveau projet, on se tournera plutôt vers Keycloak, présenté plus haut.

OpenAM est développé en Java.


LinOTP
------

:Site: https://www.linotp.org
:Porteur: un éditeur (LSE Leading Security Experts GmbH)
:Licence: AGPL v3. Une version Enterprise est également disponible.

LinOTP est une solution d'OTP open source maintenue par la société allemande LSE Leading Security Experts GmbH.

C'est une solution robuste et professionnelle intégrable dans une infrastructure hétérogène. LinOTP s'interface avec tout type de tokens supportant le protocole HMAC-OTP mais également des solutions hybrides telles que les périphériques MOTP. OTP signifie « One-Time Password » : en effet, les OTP sont des mots de passe générés à un instant donné, valides pendant une courte durée et utilisables une seule fois. La génération s'effectue grâce à des matériels adaptés, comme les tokens ou même des smartphones.

D'un point de vue technique, LinOTP est un serveur écrit en langage Python, avec lequel on communique par de simples requêtes HTTP. Il est donc possible de l'administrer via d'autres outils que ceux fournis dans la distribution. On peut imaginer développer une interface web spécifique que l'on inclurait dans une section privilégiée d'un Intranet par exemple.


Shibboleth
----------

:Site: https://www.shibboleth.net/
:Porteur: un consortium (Shibboleth Consortium)
:Licence: Apache 2.0

Shibboleth a été développé par le consortium Internet2 regroupant universités et centres de recherche (plus de 200) afin de simplifier et sécuriser l'accès à différentes ressources internes et externes. La version 1.0 de Shibboleth a été publiée en 2003.

Shibboleth permet la mise en place d'un système d'authentification centralisé entre plusieurs services ainsi que la propagation d'identités entre ces services. L'objectif de la propagation d'identités est double : déléguer l'authentification à l'établissement d'origine de l'utilisateur et obtenir certains attributs de l'utilisateur (pour gérer le contrôle d'accès ou personnaliser les contenus). A l'instar du module pour Apache HTTP Server, plusieurs extensions ont été développées permettant d'interfacer divers systèmes avec Shibboleth.

Shibboleth est écrit en Java et C++. C'est l'implémentation de référence des fédérations d'identité de l'enseignement supérieur et de la recherche — en France, la fédération Éducation-Recherche animée par RENATER — et il reste, à ce titre, incontournable dans ce secteur.


Autres
------

La catégorie s'est enrichie de plusieurs projets qui méritent d'être évalués :

- Authentik, fournisseur d'identité moderne et complet, en Python: https://goauthentik.io/
- Authelia, portail d'authentification léger, conçu pour être placé derrière un proxy inverse: https://www.authelia.com/
- Zitadel, fournisseur d'identité multi-tenant écrit en Go: https://zitadel.com/
- FreeIPA, gestion d'identité intégrée pour les parcs Linux (annuaire, Kerberos, DNS, autorité de certification): https://www.freeipa.org/
- privacyIDEA, gestion de l'authentification multifacteur et des jetons, alternative à LinOTP dont il est issu: https://www.privacyidea.org/
- Ory Hydra et Kratos, briques OAuth 2.0 et gestion des identités pour développeurs: https://www.ory.sh/
