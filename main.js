(function () {
  'use strict';

  var FORM_ENDPOINT = 'https://formspree.io/f/mzdnndna';
  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };

  // Envoie un événement aux outils de mesure s'ils sont installés (GA4, GTM, Plausible).
  function track(name, params) {
    try {
      if (typeof window.gtag === 'function') window.gtag('event', name, params || {});
      if (Array.isArray(window.dataLayer)) window.dataLayer.push(Object.assign({ event: name }, params || {}));
      if (typeof window.plausible === 'function') window.plausible(name, { props: params || {} });
    } catch (e) { /* mesure non bloquante */ }
  }

  $$('[data-track]').forEach(function (el) {
    el.addEventListener('click', function () { track('cta_click', { cta: el.dataset.track, page: location.pathname }); });
  });
  $$('a[href^="tel:"]').forEach(function (a) {
    a.addEventListener('click', function () { track('phone_click', { page: location.pathname }); });
  });
  $$('a[href*="wa.me"]').forEach(function (a) {
    a.addEventListener('click', function () { track('whatsapp_click', { page: location.pathname }); });
  });

  // ===== Menu mobile =====
  var menu = $('#mobileMenu');
  var openBtn = $('#menuOpen');
  var closeBtn = $('#menuClose');
  function setMenu(open) {
    if (!menu) return;
    menu.classList.toggle('open', open);
    if (openBtn) openBtn.setAttribute('aria-expanded', String(open));
    document.body.style.overflow = open ? 'hidden' : '';
  }
  if (menu && openBtn && closeBtn) {
    openBtn.addEventListener('click', function () { setMenu(true); });
    closeBtn.addEventListener('click', function () { setMenu(false); });
    $$('a', menu).forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
  }

  // ===== Formulaire en 3 étapes (accueil) =====
  var lead = $('#leadForm');
  var goTo = function () {};
  var applyProject = function () {};
  if (lead) {
    var steps = $$('.form-step', lead);
    var bars = $$('.lead-steps span', lead);
    var modeleLabel = $('#lf-modele-label');
    var modeleInput = $('#lf-modele');
    var current = 1;

    var stepCopy = {
      "Acheter un véhicule": ['Quel véhicule recherchez-vous ?', 'ex : Audi Q5, Tesla Model Y, Peugeot 3008…'],
      "Importer d'Europe": ['Quel véhicule voulez-vous importer ?', 'ex : BMW M340i Touring, Porsche Macan…'],
      "Flotte entreprise": ['Combien de véhicules, et de quel type ?', 'ex : 4 Renault Trafic, 2 citadines…'],
      "Pièce de collection": ['Quel véhicule et quelle pièce ?', 'ex : Citroën DS 1971, calandre d\'origine']
    };

    goTo = function (n) {
      current = n;
      steps.forEach(function (s) { s.classList.toggle('active', Number(s.dataset.step) === n); });
      bars.forEach(function (b, i) { b.classList.toggle('on', i < n); });
      var first = $('.form-step.active input:not([type=radio]), .form-step.active select', lead);
      if (first && n > 1 && window.matchMedia('(min-width: 761px)').matches) first.focus({ preventScroll: true });
    };

    var stepValid = function (n) {
      var fields = $$('.form-step[data-step="' + n + '"] [required]', lead);
      for (var i = 0; i < fields.length; i++) {
        if (!fields[i].checkValidity()) { fields[i].reportValidity(); return false; }
      }
      return true;
    };

    applyProject = function (value) {
      var copy = stepCopy[value];
      if (copy) { modeleLabel.textContent = copy[0]; modeleInput.placeholder = copy[1]; }
    };

    $$('input[name="projet"]', lead).forEach(function (r) {
      r.addEventListener('change', function () {
        applyProject(r.value);
        track('lead_step', { step: 1, projet: r.value });
        setTimeout(function () { goTo(2); }, 180);
      });
    });
    $$('[data-next]', lead).forEach(function (b) {
      b.addEventListener('click', function () {
        if (stepValid(current)) { track('lead_step', { step: current }); goTo(current + 1); }
      });
    });
    $$('[data-prev]', lead).forEach(function (b) {
      b.addEventListener('click', function () { goTo(current - 1); });
    });
    modeleInput.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') { e.preventDefault(); if (stepValid(2)) goTo(3); }
    });
  }

  // Les liens "Lancer ma recherche" pré-sélectionnent le projet
  $$('[data-preset]').forEach(function (a) {
    a.addEventListener('click', function () {
      if (lead) {
        var radio = $('input[name="projet"][value="' + a.dataset.preset + '"]', lead);
        if (radio) { radio.checked = true; applyProject(radio.value); goTo(2); }
      }
      var select = $('#cf-projet');
      if (select && !lead) select.value = a.dataset.preset;
    });
  });

  // ===== Envoi générique des formulaires =====
  function wireForm(form) {
    var card = form.parentElement;
    var success = $('.form-success', card);
    var error = $('.form-error', form);
    var submit = $('button[type="submit"]', form);
    var label = submit.innerHTML;

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      error.classList.remove('show');
      var required = $$('[required]', form);
      for (var i = 0; i < required.length; i++) {
        if (!required[i].checkValidity()) { required[i].reportValidity(); return; }
      }

      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = v; });
      data.source = form.dataset.source;
      data.page = location.pathname;
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
        var foot = $('.lead-card-foot', card);
        if (foot) foot.style.display = 'none';
        success.classList.add('show');
        track('generate_lead', { source: form.dataset.source, projet: data.projet || '', page: location.pathname });
      }).catch(function () {
        error.innerHTML = 'L\'envoi n\'a pas abouti. Appelez-nous au <a href="tel:+33756855727"><b>07 56 85 57 27</b></a> ou écrivez-nous sur <a href="https://wa.me/33756855727" target="_blank" rel="noopener"><b>WhatsApp</b></a>.';
        error.classList.add('show');
      }).finally(function () {
        submit.disabled = false;
        submit.innerHTML = label;
      });
    });
  }
  $$('form.lead-form').forEach(wireForm);

  // ===== Simulateur de financement =====
  var amount = $('#simAmount');
  var calc = null;
  var fmt = function (n) { return Math.round(n).toLocaleString('fr-FR') + ' €'; };
  if (amount) {
    var amountOut = $('#simAmountOut');
    var monthlyOut = $('#simMonthly');
    var durBtns = $$('.sim-durations button');
    var months = 48;
    calc = function () {
      var p = Number(amount.value), r = 0.039 / 12;
      var m = p * r / (1 - Math.pow(1 + r, -months));
      amountOut.textContent = fmt(p);
      monthlyOut.innerHTML = fmt(Math.ceil(m)) + ' <small>/mois</small>';
      return { prix: p, mois: months, mensualite: Math.ceil(m) };
    };
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
  }

  // ===== Modal financement =====
  var modal = $('#leasingModal');
  function closeModal() { if (modal) { modal.classList.remove('open'); document.body.style.overflow = ''; } }
  if (modal && $('#openLeasing')) {
    $('#openLeasing').addEventListener('click', function () {
      if (calc) {
        var s = calc();
        var txt = fmt(s.prix) + ' sur ' + s.mois + ' mois ≈ ' + fmt(s.mensualite) + '/mois';
        $('#leasingRecap').textContent = txt;
        $('#leasingSimField').value = txt;
      }
      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
      track('cta_click', { cta: 'open_leasing' });
      setTimeout(function () { $('#lm-nom').focus(); }, 50);
    });
    modal.addEventListener('click', function (e) { if (e.target === modal || e.target.hasAttribute('data-close')) closeModal(); });
  }
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { closeModal(); setMenu(false); }
  });

  // ===== Barre de contact mobile : visible après le haut de page, masquée sur le formulaire =====
  var bar = $('#mobileBar');
  var hero = $('.hero, .page-hero');
  var contact = $('#contact');
  var reveals = $$('.reveal');
  if ('IntersectionObserver' in window) {
    if (bar && hero && contact) {
      var heroVisible = true, contactVisible = false;
      var updateBar = function () { bar.classList.toggle('show', !heroVisible && !contactVisible); };
      new IntersectionObserver(function (en) { heroVisible = en[0].isIntersecting; updateBar(); }, { threshold: 0.15 }).observe(hero);
      new IntersectionObserver(function (en) { contactVisible = en[0].isIntersecting; updateBar(); }, { threshold: 0.2 }).observe(contact);
    }

    // ===== Apparition douce au scroll =====
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
    if (bar) bar.classList.add('show');
  }
})();
