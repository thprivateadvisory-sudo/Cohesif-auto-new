(function () {
  'use strict';

  var FORM_ENDPOINT = 'https://formspree.io/f/mzdnndna';

  // Envoie un événement aux outils de mesure s'ils sont installés (GA4, GTM, Plausible).
  function track(name, params) {
    try {
      if (typeof window.gtag === 'function') window.gtag('event', name, params || {});
      if (Array.isArray(window.dataLayer)) window.dataLayer.push(Object.assign({ event: name }, params || {}));
      if (typeof window.plausible === 'function') window.plausible(name, { props: params || {} });
    } catch (e) { /* mesure non bloquante */ }
  }

  document.querySelectorAll('[data-track]').forEach(function (el) {
    el.addEventListener('click', function () { track('cta_click', { cta: el.dataset.track }); });
  });

  // ===== Menu mobile =====
  var menu = document.getElementById('mobileMenu');
  var openBtn = document.getElementById('menuOpen');
  var closeBtn = document.getElementById('menuClose');
  function setMenu(open) {
    menu.classList.toggle('open', open);
    openBtn.setAttribute('aria-expanded', String(open));
    document.body.style.overflow = open ? 'hidden' : '';
  }
  openBtn.addEventListener('click', function () { setMenu(true); });
  closeBtn.addEventListener('click', function () { setMenu(false); });
  menu.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });

  // ===== Formulaire hero en 3 étapes =====
  var lead = document.getElementById('leadForm');
  var steps = lead.querySelectorAll('.form-step');
  var bars = lead.querySelectorAll('.lead-steps span');
  var modeleLabel = document.getElementById('lf-modele-label');
  var modeleInput = document.getElementById('lf-modele');
  var current = 1;

  var stepCopy = {
    "Acheter un véhicule": ['Quel véhicule recherchez-vous ?', 'ex : Audi Q5, Tesla Model Y, Peugeot 3008…'],
    "Importer d'Europe": ['Quel véhicule voulez-vous importer ?', 'ex : BMW M340i Touring, Porsche Macan…'],
    "Flotte entreprise": ['Combien de véhicules, et de quel type ?', 'ex : 4 Renault Trafic, 2 citadines…'],
    "Pièce de collection": ['Quel véhicule et quelle pièce ?', 'ex : Citroën DS 1971, calandre d\'origine']
  };

  function goTo(n) {
    current = n;
    steps.forEach(function (s) { s.classList.toggle('active', Number(s.dataset.step) === n); });
    bars.forEach(function (b, i) { b.classList.toggle('on', i < n); });
    var first = lead.querySelector('.form-step.active input:not([type=radio]), .form-step.active select');
    if (first && n > 1 && window.matchMedia('(min-width: 761px)').matches) first.focus({ preventScroll: true });
  }

  function stepValid(n) {
    var fields = lead.querySelectorAll('.form-step[data-step="' + n + '"] [required]');
    for (var i = 0; i < fields.length; i++) {
      if (!fields[i].checkValidity()) { fields[i].reportValidity(); return false; }
    }
    return true;
  }

  function applyProject(value) {
    var copy = stepCopy[value];
    if (copy) { modeleLabel.textContent = copy[0]; modeleInput.placeholder = copy[1]; }
  }

  lead.querySelectorAll('input[name="projet"]').forEach(function (r) {
    r.addEventListener('change', function () {
      applyProject(r.value);
      track('lead_step', { step: 1, projet: r.value });
      setTimeout(function () { goTo(2); }, 180);
    });
  });
  lead.querySelectorAll('[data-next]').forEach(function (b) {
    b.addEventListener('click', function () {
      if (stepValid(current)) { track('lead_step', { step: current }); goTo(current + 1); }
    });
  });
  lead.querySelectorAll('[data-prev]').forEach(function (b) {
    b.addEventListener('click', function () { goTo(current - 1); });
  });
  modeleInput.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') { e.preventDefault(); if (stepValid(2)) goTo(3); }
  });

  // Les liens "Lancer ma recherche" pré-sélectionnent le projet
  document.querySelectorAll('[data-preset]').forEach(function (a) {
    a.addEventListener('click', function () {
      var radio = lead.querySelector('input[name="projet"][value="' + a.dataset.preset + '"]');
      if (radio) { radio.checked = true; applyProject(radio.value); goTo(2); }
    });
  });

  // ===== Envoi générique des formulaires =====
  function wireForm(form, onSuccess) {
    var card = form.parentElement;
    var success = card.querySelector('.form-success');
    var error = form.querySelector('.form-error');
    var submit = form.querySelector('button[type="submit"]');
    var label = submit.innerHTML;

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      error.classList.remove('show');
      var required = form.querySelectorAll('[required]');
      for (var i = 0; i < required.length; i++) {
        if (!required[i].checkValidity()) { required[i].reportValidity(); return; }
      }

      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = v; });
      data.source = form.dataset.source;
      data._subject = 'Cohesif Auto — ' + (data.projet || 'Demande') + ' — ' + (data.nom || '');
      data._replyto = data.email;

      submit.disabled = true;
      submit.textContent = 'Envoi en cours…';

      fetch(FORM_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(data)
      }).then(function (res) {
        if (!res.ok) throw new Error('HTTP ' + res.status);
        form.style.display = 'none';
        var foot = card.querySelector('.lead-card-foot');
        if (foot) foot.style.display = 'none';
        success.classList.add('show');
        track('generate_lead', { source: form.dataset.source, projet: data.projet || '' });
        if (onSuccess) onSuccess();
      }).catch(function () {
        error.innerHTML = 'L\'envoi n\'a pas abouti. Appelez-nous au <a href="tel:+33756855727"><b>07 56 85 57 27</b></a> ou écrivez-nous sur <a href="https://wa.me/33756855727" target="_blank" rel="noopener"><b>WhatsApp</b></a>.';
        error.classList.add('show');
      }).finally(function () {
        submit.disabled = false;
        submit.innerHTML = label;
      });
    });
  }

  wireForm(lead);
  wireForm(document.getElementById('contactForm'));
  wireForm(document.getElementById('leasingForm'));

  // ===== Simulateur de financement =====
  var amount = document.getElementById('simAmount');
  var amountOut = document.getElementById('simAmountOut');
  var monthlyOut = document.getElementById('simMonthly');
  var durBtns = document.querySelectorAll('.sim-durations button');
  var months = 48;
  var fmt = function (n) { return Math.round(n).toLocaleString('fr-FR') + ' €'; };

  function calc() {
    var p = Number(amount.value), r = 0.039 / 12;
    var m = p * r / (1 - Math.pow(1 + r, -months));
    amountOut.textContent = fmt(p);
    monthlyOut.innerHTML = fmt(Math.ceil(m)) + ' <small>/mois</small>';
    return { prix: p, mois: months, mensualite: Math.ceil(m) };
  }
  amount.addEventListener('input', calc);
  durBtns.forEach(function (b) {
    b.addEventListener('click', function () {
      durBtns.forEach(function (x) { x.classList.remove('on'); });
      b.classList.add('on');
      months = Number(b.dataset.months);
      calc();
    });
  });
  calc();

  // ===== Modal financement =====
  var modal = document.getElementById('leasingModal');
  function openModal() {
    var s = calc();
    var txt = fmt(s.prix) + ' sur ' + s.mois + ' mois ≈ ' + fmt(s.mensualite) + '/mois';
    document.getElementById('leasingRecap').textContent = txt;
    document.getElementById('leasingSimField').value = txt;
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
    track('cta_click', { cta: 'open_leasing' });
    setTimeout(function () { document.getElementById('lm-nom').focus(); }, 50);
  }
  function closeModal() { modal.classList.remove('open'); document.body.style.overflow = ''; }
  document.getElementById('openLeasing').addEventListener('click', openModal);
  modal.addEventListener('click', function (e) { if (e.target === modal || e.target.hasAttribute('data-close')) closeModal(); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { closeModal(); setMenu(false); }
  });

  // ===== Barre de contact mobile : visible après le hero, masquée sur le formulaire de contact =====
  var bar = document.getElementById('mobileBar');
  var hero = document.querySelector('.hero');
  var contact = document.getElementById('contact');
  var heroVisible = true, contactVisible = false;
  function updateBar() { bar.classList.toggle('show', !heroVisible && !contactVisible); }
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (en) { heroVisible = en[0].isIntersecting; updateBar(); }, { threshold: 0.15 }).observe(hero);
    new IntersectionObserver(function (en) { contactVisible = en[0].isIntersecting; updateBar(); }, { threshold: 0.2 }).observe(contact);

    // ===== Apparition douce au scroll =====
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
    bar.classList.add('show');
  }
})();
