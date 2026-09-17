/* Mesure d'audience Matomo (stats.abilian.com, site 9).
 *
 * Le thème charge les pages en navigation instantanée : le document n'est pas
 * rechargé d'une page à l'autre. L'installation du traceur ne doit donc courir
 * qu'une fois, et c'est l'observable `document$` — qui émet au chargement puis
 * à chaque navigation — qui déclenche le comptage des vues.
 */

var _paq = (window._paq = window._paq || []);

_paq.push(["enableLinkTracking"]);

(function () {
  var u = "//stats.abilian.com/";
  _paq.push(["setTrackerUrl", u + "matomo.php"]);
  _paq.push(["setSiteId", "9"]);

  var d = document;
  var g = d.createElement("script");
  var s = d.getElementsByTagName("script")[0];
  g.async = true;
  g.src = u + "matomo.js";
  s.parentNode.insertBefore(g, s);
})();

document$.subscribe(function () {
  _paq.push(["setCustomUrl", location.href]);
  _paq.push(["setDocumentTitle", document.title]);
  _paq.push(["trackPageView"]);
});
