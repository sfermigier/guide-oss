Authentification, fédération et gestion d’identité
==================================================

Dans cette catégorie, nous vous présentons différentes solutions d’authentification, de fédération et de gestion d’identité.

Il s’agit donc d’outils relativement proches mais avec des finalités parfois différentes. Ainsi par exemple, le système Shibboleth, permet l'authentification unique multi-domaines. Il est ainsi possible d’inclure des applications tierces dans son système de gestion d'identité fédéré afin que les utilisateurs s'identifiant sur leur système unique d'identification puissent avoir accès à l'application en question.

LinOTP est également présenté ; il s’agit d’une solution d’OTP permettant l’utilisation de mots de passe générés à un instant donné, valides pendant une courte durée et utilisables une seule fois.

D’autres solutions open source comme CAS, FederID, LemonLDAP, OpenAM sont présentées.


CAS
---

:Site: https://www.jasig.org/cas
:Porteur: une communauté
:Licence: JA-SIG, de type BSD


Central Authentication Service est un système de Single Sign On orienté Web. Il a été créé au début des années 2000 à l'université de Yale. En 2004, CAS est passé dans le giron du groupement d'intérêts JA-SIG.

CAS permet de faire du Single Sign On entre plusieurs sites, y compris dans des domaines différents, en utilisant des tokens à usage unique. Les applications n'ont jamais accès au mot de passe de l'utilisateur, et obtiennent le login de celui-ci en interrogeant CAS. Le protocole de communication utilisé est le SAML v2, et dans les dernières versions de CAS, il est possible de fournir des informations supplémentaires au login de l'utilisateur (groupes, nom, prénom, etc...). CAS peut utiliser différents types de backend en tant que base utilisateur, tels qu'un annuaire LDAP, une base de données relationnelle, des fichiers à plats, etc. CAS fournit également un système de proxy, permettant à une application de transférer l'identification à une autre application, Web ou non, en backend, tel qu'un webservice ou un serveur IMAP.

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

:Site: http://lemonldap-ng.org
:Porteur: un consortium (OW2)
:Licence: GPL

LemonLDAP::NG est un système de SSO et de contrôle d'accès Web, initié en 2003 par le Ministère des finances, puis repris par la Gendarmerie Nationale et Linagora. Il intègre le consortium OW2 en 2007. Il nécessite l’utilisation d’un serveur Apache, mais un mode reverse proxy permet de l'utiliser avec des applications fonctionnant sous un autre serveur (IIS, Tomcat, etc.)

LemonLDAP::NG permet de baser l'authentification des applications web sur un annuaire LDAP, mais aussi sur de nombreux autres annuaires, bases de données, ainsi que sur d'autres systèmes tels que OpenID et SAML. Il peut également servir de fournisseur CAS, OpenID et SAML. Le contrôle d'accès peut se faire par URL pour chaque application à protéger. LemonLDAP::NG permet aussi la traçabilité des accès. Il propose une interface d'administration Web.

Le produit est réalisé en Perl et est facile à personnaliser, aussi bien en termes de comportement que d'apparence via un moteur de template.


OpenAM
------

:Site: http://forgerock.com/openam.html
:Porteur: un éditeur (ForgeRock)
:Licence: CDDL (Common Development and Distribution License, licence open source créée par Sun Microsystems, basée sur la Mozilla Public License, version 1.1).

OpenAM est une solution complète de gestion d'identités. Suite à la décision de Sun d'arrêter le développement d'OpenSSO, la société ForgeRock a initié une branche qu'elle a nommée OpenAM et qu'elle continue de développer et de maintenir depuis lors. Elle a annoncé qu'elle allait poursuivre la sortie de nouvelles versions d'OpenAM en suivant la feuille de route d'origine de Sun Microsystems.

OpenAM est une brique d'infrastructure permettant d'assurer de façon transparente les fonctions de Single Sign On aussi bien pour des applications WEB que pour des Middleware.  OpenAM fournit une solution permettant un déploiement facilité des projets de gestion des droits d’accès Web : la passerelle universelle.

OpenAM est développée en Java.


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

:Site: http://shibboleth.internet2.edu
:Porteur: une communauté
:Licence: Apache 2.0

Shibboleth a été développé par le consortium Internet2 regroupant universités et centres de recherche (plus de 200) afin de simplifier et sécuriser l'accès à différentes ressources internes et externes. La version 1.0 de Shibboleth a été publiée en 2003.

Shibboleth permet la mise en place d'un système d'authentification centralisé entre plusieurs services ainsi que la propagation d'identités entre ces services. L'objectif de la propagation d'identités est double : déléguer l'authentification à l'établissement d'origine de l'utilisateur et obtenir certains attributs de l'utilisateur (pour gérer le contrôle d'accès ou personnaliser les contenus). A l'instar du module pour Apache HTTP Server, plusieurs extensions ont été développées permettant d'interfacer divers systèmes avec Shibboleth.

Shibboleth est écrit en Java et C++.
