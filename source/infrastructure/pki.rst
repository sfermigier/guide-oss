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

