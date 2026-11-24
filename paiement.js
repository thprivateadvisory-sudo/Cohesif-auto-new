// Paiement du forfait de recherche, directement sur le site, avec le formulaire Cohesif Auto.
(function () {
  // Adresse du Worker Cloudflare qui crée les paiements (voir tools/paiement-worker).
  // Vide = boutons « Lancer ma recherche » vers le formulaire de contact.
  var PAIEMENT_URL = 'https://cohesif-paiement.muddy-fog-dddb.workers.dev';

  var OFFRES = {
    france:   { nom: 'Recherche en France', prix: '99 €', montant: 9900 },
    europe:   { nom: 'Recherche et import Europe', prix: '149 €', montant: 14900 },
    prestige: { nom: 'Prestige et collection', prix: '249 €', montant: 24900 }
  };

  var modal = document.getElementById('payModal');
  if (!modal || !PAIEMENT_URL) return;

  var $ = function (s) { return modal.querySelector(s); };
  var consent = $('#payConsent');
  var nextBtn = $('#payStart');
  var form = $('#payForm');
  var submitBtn = $('#paySubmit');
  var err1 = $('#payError');
  var err2 = $('#payError2');
  var offre = null;
  var stripe = null, elements = null, paymentEl = null;
  var pret = null;

  function track(name, params) { if (typeof window.gtag === 'function') window.gtag('event', name, params || {}); }

  function etape(nom) {
    ['recap', 'form', 'ok'].forEach(function (n) { $('[data-pay="' + n + '"]').hidden = n !== nom; });
    $('.modal-box').scrollTop = 0;
  }
  function montrer(box, msg) {
    box.innerHTML = msg + ' Vous pouvez aussi nous appeler au <a href="tel:+33756855727">07 56 85 57 27</a>.';
    box.hidden = false;
  }

  // Chargement du module de paiement sécurisé (une seule fois)
  function preparer() {
    if (pret) return pret;
    pret = Promise.all([
      new Promise(function (ok, ko) {
        if (window.Stripe) return ok();
        var s = document.createElement('script');
        s.src = 'https://js.stripe.com/v3/';
        s.onload = ok; s.onerror = ko;
        document.head.appendChild(s);
      }),
      fetch(PAIEMENT_URL + '/config').then(function (r) { return r.json(); })
    ]).then(function (res) {
      stripe = window.Stripe(res[1].publishableKey, { locale: 'fr' });
    });
    pret.catch(function () { pret = null; });
    return pret;
  }

  function monterPaiement() {
    var o = OFFRES[offre];
    if (paymentEl) { paymentEl.destroy(); paymentEl = null; }
    elements = stripe.elements({
      mode: 'payment',
      amount: o.montant,
      currency: 'eur',
      paymentMethodTypes: ['card'],
      locale: 'fr',
      fonts: [{ cssSrc: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap' }],
      appearance: {
        theme: 'stripe',
        variables: {
          colorPrimary: '#1d4fb0',
          colorText: '#0b1220',
          colorDanger: '#b91c1c',
          fontFamily: 'Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif',
          fontSizeBase: '15px',
          borderRadius: '10px',
          spacingUnit: '4px'
        },
        rules: {
          '.Input': { border: '1.5px solid #d7dce5', boxShadow: 'none', padding: '12px 14px' },
          '.Input:focus': { borderColor: '#1d4fb0', boxShadow: '0 0 0 4px rgba(37,99,235,.14)' },
          '.Label': { fontWeight: '600', color: '#2a3446' },
          '.Tab': { border: '1.5px solid #d7dce5', boxShadow: 'none' },
          '.Tab--selected': { borderColor: '#1d4fb0', boxShadow: '0 0 0 1px #1d4fb0' }
        }
      }
    });
    paymentEl = elements.create('payment', {
      layout: { type: 'tabs' },
      defaultValues: { billingDetails: { address: { country: 'FR' } } },
      fields: { billingDetails: { name: 'never', email: 'never', phone: 'never', address: { country: 'never' } } },
      wallets: { applePay: 'auto', googlePay: 'auto', link: 'never' },
      terms: { card: 'never' }
    });
    $('#payElement').innerHTML = '';
    paymentEl.mount('#payElement');
  }

  function ouvrir(o) {
    if (!OFFRES[o]) return;
    offre = o;
    var d = OFFRES[o];
    $('#payOffre').textContent = d.nom;
    $('#payPrix').textContent = d.prix;
    $('#payOffre2').textContent = d.nom;
    $('#payPrix2').textContent = d.prix;
    submitBtn.querySelector('span').textContent = 'Payer ' + d.prix;
    var carte = document.querySelector('.plan[data-offre="' + o + '"] .plan-list');
    $('#payInclus').innerHTML = carte ? carte.innerHTML : '';
    consent.checked = false;
    nextBtn.disabled = true;
    err1.hidden = true; err2.hidden = true;
    etape('recap');
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
    track('pay_open', { offre: o });
    preparer();
  }

  function fermer() {
    modal.classList.remove('open');
    document.body.style.overflow = '';
  }

  consent.addEventListener('change', function () { nextBtn.disabled = !consent.checked; });

  nextBtn.addEventListener('click', function () {
    if (!consent.checked) return;
    nextBtn.disabled = true;
    nextBtn.classList.add('loading');
    err1.hidden = true;
    preparer()
      .then(function () {
        etape('form');
        monterPaiement();
        track('pay_form', { offre: offre });
        setTimeout(function () { $('#pf-nom').focus(); }, 60);
      })
      .catch(function () { montrer(err1, 'Le paiement en ligne est momentanément indisponible.'); })
      .finally(function () { nextBtn.classList.remove('loading'); nextBtn.disabled = !consent.checked; });
  });

  $('#payBack').addEventListener('click', function () { etape('recap'); });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    err2.hidden = true;
    var nom = $('#pf-nom').value.trim();
    var email = $('#pf-email').value.trim();
    var tel = $('#pf-tel').value.trim();
    var champs = [['#pf-nom', !!nom], ['#pf-email', /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)], ['#pf-tel', tel.replace(/\D/g, '').length >= 9]];
    var premier = null;
    champs.forEach(function (c) {
      var el = $(c[0]); el.closest('.field').classList.toggle('invalid', !c[1]);
      if (!c[1] && !premier) premier = el;
    });
    if (premier) { premier.focus(); err2.textContent = 'Merci de renseigner votre nom, un email et un téléphone valides.'; err2.hidden = false; return; }

    submitBtn.disabled = true;
    submitBtn.classList.add('loading');
    var label = submitBtn.querySelector('span');
    var labelInit = label.textContent;
    label.textContent = 'Paiement en cours…';

    elements.submit()
      .then(function (r) {
        if (r.error) throw { stripe: r.error };
        return fetch(PAIEMENT_URL + '/paiement', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ offre: offre, consentement: true, nom: nom, email: email, telephone: tel, recherche: $('#pf-rech').value })
        }).then(function (r) { return r.json().then(function (d) { if (!r.ok) throw d; return d; }); });
      })
      .then(function (d) {
        return stripe.confirmPayment({
          elements: elements,
          clientSecret: d.clientSecret,
          redirect: 'if_required',
          confirmParams: {
            return_url: 'https://cohesifauto.fr/?paiement=ok#tarifs',
            receipt_email: email,
            payment_method_data: { billing_details: { name: nom, email: email, phone: tel, address: { country: 'FR' } } }
          }
        });
      })
      .then(function (r) {
        if (r.error) throw { stripe: r.error };
        etape('ok');
        track('purchase', { offre: offre, currency: 'EUR', value: OFFRES[offre].montant / 100 });
      })
      .catch(function (e) {
        if (e && e.stripe && (e.stripe.type === 'card_error' || e.stripe.type === 'validation_error')) {
          err2.textContent = e.stripe.message; err2.hidden = false;
        } else {
          montrer(err2, 'Le paiement n\'a pas pu aboutir. Aucun montant n\'a été prélevé.');
        }
      })
      .finally(function () {
        submitBtn.disabled = false;
        submitBtn.classList.remove('loading');
        label.textContent = labelInit;
      });
  });

  modal.addEventListener('click', function (e) {
    if (e.target === modal || e.target.hasAttribute('data-close')) fermer();
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && modal.classList.contains('open')) fermer(); });

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

  // Retour après une validation bancaire avec redirection (rare)
  var q = new URLSearchParams(location.search);
  var cs = q.get('payment_intent_client_secret');
  if (q.get('paiement') === 'ok' && cs) {
    history.replaceState(null, '', location.pathname + '#tarifs');
    preparer().then(function () { return stripe.retrievePaymentIntent(cs); }).then(function (r) {
      if (r.paymentIntent && r.paymentIntent.status === 'succeeded') {
        etape('ok'); modal.classList.add('open'); document.body.style.overflow = 'hidden';
      }
    }).catch(function () {});
  }
})();
