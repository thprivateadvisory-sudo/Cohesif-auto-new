// Paiement du forfait de recherche, directement sur le site (Stripe Embedded Checkout).
(function () {
  // Adresse du Worker Cloudflare qui prépare les paiements (voir tools/paiement-worker).
  // Tant qu'elle est vide, les boutons « Lancer ma recherche » mènent au formulaire de contact.
  var PAIEMENT_URL = '';

  var OFFRES = {
    france:   { nom: 'Recherche en France', prix: '99 €' },
    europe:   { nom: 'Recherche et import Europe', prix: '149 €' },
    prestige: { nom: 'Prestige et collection', prix: '249 €' }
  };

  var modal = document.getElementById('payModal');
  if (!modal || !PAIEMENT_URL) return;
  document.documentElement.classList.add('pay-on');

  var $ = function (s) { return modal.querySelector(s); };
  var consent = $('#payConsent');
  var payBtn = $('#payStart');
  var errBox = $('#payError');
  var offreCourante = null;
  var checkout = null;
  var stripeJs = null;

  function track(name, params) { if (typeof window.gtag === 'function') window.gtag('event', name, params || {}); }

  function etape(nom) {
    ['recap', 'form', 'ok'].forEach(function (n) { $('[data-pay="' + n + '"]').hidden = n !== nom; });
    modal.querySelector('.modal-box').classList.toggle('pay-wide', nom === 'form');
  }

  function chargerStripe() {
    if (stripeJs) return stripeJs;
    stripeJs = new Promise(function (ok, ko) {
      if (window.Stripe) return ok();
      var s = document.createElement('script');
      s.src = 'https://js.stripe.com/v3/';
      s.onload = ok; s.onerror = ko;
      document.head.appendChild(s);
    });
    return stripeJs;
  }

  function erreur(msg) {
    errBox.innerHTML = msg + ' Vous pouvez aussi nous appeler au <a href="tel:+33756855727">07 56 85 57 27</a>.';
    errBox.hidden = false;
  }

  function ouvrir(offre) {
    if (!OFFRES[offre]) return;
    offreCourante = offre;
    var o = OFFRES[offre];
    $('#payOffre').textContent = o.nom;
    $('#payPrix').textContent = o.prix;
    payBtn.querySelector('span').textContent = 'Payer ' + o.prix + ' en toute sécurité';
    var carte = document.querySelector('.plan[data-offre="' + offre + '"] .plan-list');
    $('#payInclus').innerHTML = carte ? carte.innerHTML : '';
    consent.checked = false;
    payBtn.disabled = true;
    errBox.hidden = true;
    etape('recap');
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
    track('pay_open', { offre: offre });
    chargerStripe().catch(function () {});
  }

  function fermer() {
    modal.classList.remove('open');
    document.body.style.overflow = '';
    if (checkout) { checkout.destroy(); checkout = null; }
  }

  consent.addEventListener('change', function () { payBtn.disabled = !consent.checked; });

  payBtn.addEventListener('click', function () {
    if (!consent.checked) return;
    payBtn.disabled = true;
    payBtn.classList.add('loading');
    errBox.hidden = true;
    var offre = offreCourante;
    fetch(PAIEMENT_URL + '/session', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ offre: offre, consentement: true })
    })
      .then(function (r) { return r.json().then(function (d) { if (!r.ok) throw d; return d; }); })
      .then(function (d) {
        return chargerStripe().then(function () {
          var stripe = window.Stripe(d.publishableKey);
          return stripe.initEmbeddedCheckout({
            fetchClientSecret: function () { return Promise.resolve(d.clientSecret); },
            onComplete: function () {
              if (checkout) { checkout.destroy(); checkout = null; }
              etape('ok');
              track('purchase', { offre: offre, currency: 'EUR' });
            }
          });
        });
      })
      .then(function (c) {
        checkout = c;
        etape('form');
        c.mount('#payCheckout');
        track('pay_form', { offre: offre });
      })
      .catch(function () {
        erreur('Le paiement en ligne est momentanément indisponible.');
      })
      .finally(function () {
        payBtn.classList.remove('loading');
        payBtn.disabled = !consent.checked;
      });
  });

  $('#payBack').addEventListener('click', function () {
    if (checkout) { checkout.destroy(); checkout = null; }
    etape('recap');
  });

  modal.addEventListener('click', function (e) {
    if (e.target === modal || e.target.hasAttribute('data-close')) fermer();
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && modal.classList.contains('open')) fermer(); });

  // Boutons des offres
  Array.prototype.forEach.call(document.querySelectorAll('[data-offre-btn]'), function (b) {
    b.addEventListener('click', function (e) { e.preventDefault(); ouvrir(b.getAttribute('data-offre-btn')); });
  });

  // Lien direct à envoyer à un client : cohesifauto.fr/#payer-france (ou -europe, -prestige)
  function depuisAncre() {
    var m = location.hash.match(/^#payer-(france|europe|prestige)$/);
    if (m) ouvrir(m[1]);
  }
  window.addEventListener('hashchange', depuisAncre);
  depuisAncre();

  // Retour après un moyen de paiement avec redirection (PayPal, Klarna…)
  var sid = new URLSearchParams(location.search).get('paiement');
  if (sid) {
    history.replaceState(null, '', location.pathname + '#tarifs');
    fetch(PAIEMENT_URL + '/statut?session_id=' + encodeURIComponent(sid))
      .then(function (r) { return r.json(); })
      .then(function (d) {
        if (d.statut === 'paid') {
          offreCourante = d.offre;
          etape('ok');
          modal.classList.add('open');
          document.body.style.overflow = 'hidden';
        }
      })
      .catch(function () {});
  }
})();
