Serveurs d’applications
=======================

Dans cette rubrique, nous présentons les principaux serveurs d’applications Java (Jakarta EE) open source du marché.

Le contexte a toutefois changé en profondeur : le modèle du serveur d'applications dans lequel on déploie des archives applicatives a largement cédé la place à celui de l'application autonome embarquant son propre serveur (Spring Boot, Quarkus, Micronaut, Helidon), plus simple à conteneuriser et à déployer. Les serveurs présentés ci-dessous restent néanmoins en production dans de nombreux systèmes d'information, et Tomcat comme Jetty sont, de fait, les moteurs embarqués par ces mêmes frameworks.


WildFly
-------

:Site: https://www.wildfly.org/
:Porteur: un éditeur (Red Hat) et une communauté
:Licence: Apache 2.0

WildFly est le nouveau nom, depuis 2013, de JBoss AS, le serveur d'applications Java EE initialement conçu par Marc Fleury et dont l'éditeur, JBoss Inc., a été racheté par Red Hat en 2006.

Le serveur est certifié Jakarta EE et propose un mode *bootable jar* ainsi que des images conçues pour Kubernetes (via l'opérateur WildFly), qui répondent aux usages conteneurisés. L'édition commerciale correspondante est Red Hat JBoss EAP. Le projet a par ailleurs quitté la licence LGPL pour la licence Apache 2.0.

WildFly est écrit en Java.


Apache Tomcat
-------------

:Site: https://tomcat.apache.org/
:Porteur: une fondation (Apache)
:Licence: Apache 2.0

Apache Tomcat est le conteneur de servlets JEE de la fondation Apache. Le projet Tomcat a été lancé comme implémentation de référence des servlets par James Duncan Davidson, architecte logiciel chez Sun.

Il s'agit du serveur d'applications Java le plus utilisé au monde, d'autant qu'il est embarqué par défaut par Spring Boot. Son interface d'administration est très sommaire : on l'associe souvent à un serveur web ou à un proxy inverse plus généraliste (Apache httpd, nginx), qui sert les contenus statiques et lui délègue les traitements Java (servlets, JSP).

Tomcat est distribué sous la licence Apache.

Tomcat a été écrit en langage Java. Il peut donc s'exécuter via la machine virtuelle Java sur n'importe quel système d'exploitation qui l'accueille.


Eclipse GlassFish
-----------------

:Site: https://projects.eclipse.org/projects/ee4j.glassfish
:Porteur: une fondation (Eclipse)

GlassFish était l'implémentation de référence Java EE développée par Sun Microsystems puis par Oracle. La première version date de 2006. Oracle a transféré Java EE à la fondation Eclipse en 2017, ce qui a donné naissance à Jakarta EE : GlassFish y est désormais maintenu comme implémentation de référence de la norme.

GlassFish est distribué sous licences EPL 2.0 et GPL v2 avec *classpath exception*.

GlassFish est écrit en Java.


Autres
------

- Eclipse Jetty, serveur léger très utilisé en embarqué: https://jetty.org/
- Payara Server, dérivé de GlassFish avec un support commercial et un rythme de publication soutenu: https://www.payara.fish/
- Open Liberty, serveur d'IBM sous licence EPL, certifié Jakarta EE et MicroProfile: https://openliberty.io/
- Apache TomEE, Tomcat enrichi des API Jakarta EE: https://tomee.apache.org/
- Quarkus, pour les architectures conteneurisées (section :doc:`/developpement/frameworks-web-backend`): https://quarkus.io/

Apache Geronimo, cité dans les éditions précédentes, n'est plus maintenu : le projet indique lui-même que le serveur d'applications n'est plus développé.

