Serveurs http et serveurs d’applications
========================================

Dans cette rubrique, nous présentons les serveurs HTTP et les serveurs d’applications JEE open source du marché.

Les serveurs HTTP (également appelé daemon HTTP ou serveur Web) servent les requêtes (pages, images souvent) des internautes en respectant le protocole http.

Dans l’univers des serveurs HTTP, le serveur Apache domine très largement avec une notoriété exceptionnelle. Il n’est pas difficile de trouver des prestataires pour du conseil ou de l’intégration.

Concernant les serveurs d’applications, même si JBoss AS et Tomcat se partage la vedette, on voit de nombreux noms apparaitre comme Glassfish notamment.



Compte de tenu de la diversité des outils sélectionnés dans cette catégorie, les graphiques suivants ne présentent pas de moyenne.


Apache
------

:Version: 2.2.20
:Site: http://httpd.apache.org
:Porteur: une fondation (Apache)
:Licence: Apache

Apache est le serveur web le plus utilisé au monde. Son développement a commencé en 1995 alors qu’il s'agissait uniquement d'une collection de correctifs et d'additions au serveur NCSA HTTPd 1.3.

Il offre une grande souplesse de configuration et un grand nombre modules pour une couverture fonctionnelle toujours inégalée. La version 2 a notamment apportée le support de plusieurs plateformes (dont Windows), une nouvelle API et le support d’IPv6. En plus de son périmétre initial, Apache est conçu pour être modulaire et permettre l’accueil de fonctionnalités additionnelles comme l’interprétation du language PERL, PHP, Python et Ruby, le support des tags SSI et des CGI, etc.


JBoss AS
--------

:Version: 7.0.1
:Site: www.jboss.org/jbossas
:Porteur: un éditeur (Red Hat)

JBoss AS est le leader mondial des serveurs d'application, avec plus d’un tiers de part de marché. Le premier concepteur du produit fut Marc Fleury. En avril 2006, Red Hat a racheté JBoss Inc.

Certifié Java EE 6 Web Profile, il représente une excellente alternative aux serveurs d’application commerciaux comme WebSphere ou Weblogic. JBoss fournit une interface d'administration claire et simple. Son arborescence est toutefois assez complexe.

JBoss est distribué sous la licence LGPL.

JBoss est écrit en Java.




Tomcat
------

:Version: 7.0.21
:Site: http://tomcat.apache.org
:Porteur: une fondation (Apache)

Apache Tomcat est le conteneur de servlets JEE de la fondation Apache. Le projet Tomcat a été lancé comme implémentation de référence des servlets par James Duncan Davidson, architecte logiciel chez Sun.

Il s'agit du serveur d'application Java le plus utilisé au monde. Son interface d'administration est très sommaire. D’ailleurs, on associe souvent Tomcat à un autre serveur Web plus « généraliste » comme Apache voire JBoss. Dans ce cas, le serveur Web s’occupe de servir les pages web HTML par exemple et délègue à Tomcat les pages faisant appel à Java (Servlet, JSP, etc).

Tomcat est distribué sous la licence Apache.

Tomcat a été écrit en langage Java. Il peut donc s'exécuter via la machine virtuelle Java sur n'importe quel système d'exploitation la supportant.


GlassFish
---------

:Version: 3.0.1
:Site: http://glassfish.java.net/fr
:Porteur: un éditeur (Oracle)

GlassFish est l'implémentation de référence Java EE développé par Oracle. En fait, le projet est né en 2005 de par l’ouverture de Sun Application Server. La première version de GlassFish, la 1.0, date de 2006.

GlassFish possède notamment une interface d'administration très complète et un shell complet permettant d'administrer le serveur en ligne de commande. Au niveau des standards, GlassFish est une implémentation complète de la norme Java EE 6 qui recouvre : EJB 3.1, JPA 2.0, JAX-RS 1.1, JSF 2.0, Servlet 3.0, CDI 1.0, etc.

GlassFish est distribué sous double licence CDDL et GPL v2.

GlassFish est écrit en Java.



Autres
------

Parmi les produits de l’univers Serveurs HTTP et serveurs d’applications, on peut compléter la liste avec les outils ci-dessous :


- EasyBeans:	http://wiki.easybeans.org

- Geronimo:	http://geronimo.apache.org

- JOnAS:	http://wiki.jonas.ow2.org

- Lighttpd:	http://www.lighttpd.net

