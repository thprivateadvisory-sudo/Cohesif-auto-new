/**
 * Cohesif Auto - Assistant "Alex"
 * Structure inspirée de Cohesif Energy & Sport
 */
(function () {
  'use strict';

  const BRAND_NAVY  = '#1e3a5f';
  const BRAND_WARM  = '#8b5a2b';
  const BRAND_SOFT  = '#f4f0ea';

  // ─── FAQ ─────────────────────────────────────────────────────────────────
  const faqData = [
    {
      id: 'vente',
      question: 'Vente de véhicules',
      answer: 'Cohesif Auto propose une sélection de véhicules classiques et de prestige, neufs ou d\'occasion sourcée avec soin. Chaque véhicule est vérifié avant proposition. Nous nous adaptons à votre budget et à vos exigences. 🚗',
      suggestions: ['Véhicules prestige', 'Import automobile', 'Devis gratuit']
    },
    {
      id: 'prestige',
      question: 'Véhicules prestige',
      answer: 'Notre sélection prestige couvre les grandes marques européennes, américaines et japonaises. Sourcing direct, transparence sur l\'historique, préparation avant livraison. Pour ceux qui ne veulent pas de compromis. 🏎️',
      suggestions: ['Vente de véhicules', 'Import automobile', 'Pièces de collection']
    },
    {
      id: 'import',
      question: 'Import automobile',
      answer: 'Nous importons des véhicules depuis l\'Allemagne, l\'Italie, les États-Unis, le Japon et bien d\'autres pays. Délai moyen : 4 à 8 semaines. Nous gérons les formalités douanières, l\'homologation et le contrôle technique. 🌍',
      suggestions: ['Vente de véhicules', 'Flottes professionnelles', 'Devis gratuit']
    },
    {
      id: 'flottes',
      question: 'Flottes professionnelles',
      answer: 'Nous équipons les entreprises en flottes automobiles : LLD, location courte et moyenne durée, achat direct. Un interlocuteur unique, des délais maîtrisés, des conditions négociées. Idéal pour les TPE/PME et grands comptes. 🚐',
      suggestions: ['LLD', 'Particuliers', 'Devis gratuit']
    },
    {
      id: 'lld',
      question: 'LLD',
      answer: 'La Location Longue Durée via Cohesif Auto vous permet de renouveler régulièrement votre flotte sans immobiliser de capital. Loyers déductibles, entretien inclus selon formule, gestion simplifiée. On monte le dossier pour vous. 📋',
      suggestions: ['Flottes professionnelles', 'Devis gratuit', 'Contact']
    },
    {
      id: 'particuliers',
      question: 'Particuliers',
      answer: 'Vous cherchez votre prochain véhicule sans les galères ? Nous vous accompagnons de A à Z : définition du besoin, recherche, négociation, import si nécessaire, démarches administratives. Un service clé en main pour particuliers exigeants. 👤',
      suggestions: ['Vente de véhicules', 'Import automobile', 'Devis gratuit']
    },
    {
      id: 'collection',
      question: 'Pièces de collection',
      answer: 'Notre atelier collection spécialisé recherche et fournit des pièces auto rares et vintage. Réseaux de fournisseurs spécialisés, sourcing international, expertise technique. Pour les passionnés et les restaurateurs. 🔩',
      suggestions: ['Véhicules prestige', 'Vente de véhicules', 'Contact']
    },
    {
      id: 'delais',
      question: 'Délais de livraison',
      answer: 'Les délais varient selon la prestation : stock disponible (1-3 semaines), import (4-8 semaines selon origine), recherche pièce collection (à définir selon la rareté), constitution flotte (4-8 semaines). Tout retard fait l\'objet d\'une information immédiate. ⏱️',
      suggestions: ['Import automobile', 'Flottes professionnelles', 'Contact']
    },
    {
      id: 'devis',
      question: 'Devis gratuit',
      answer: 'Tous nos devis sont gratuits, personnalisés et sans engagement. Valables 30 jours. On vous répond sous 48h. Remplissez notre formulaire de contact ou appelez-nous directement au <a href="tel:0760903774" style="color:#1e3a5f;font-weight:600">07 60 90 37 74</a>. 📞',
      suggestions: ['Contact', 'Flottes professionnelles', 'Import automobile']
    },
    {
      id: 'garanties',
      question: 'Garanties',
      answer: 'Tous les véhicules vendus bénéficient de la garantie légale de conformité et de la garantie contre les vices cachés. Des garanties commerciales spécifiques peuvent être proposées selon le véhicule (constructeur, garantie étendue). 🛡️',
      suggestions: ['Vente de véhicules', 'Devis gratuit', 'Contact']
    },
    {
      id: 'paiement',
      question: 'Paiement',
      answer: 'Modalités flexibles : acompte de 30% à la commande, solde à la livraison ou selon échéancier convenu. Virement bancaire, chèque, carte bancaire acceptés. Des paiements échelonnés sont possibles selon le projet — discutons-en ! 💳',
      suggestions: ['Devis gratuit', 'LLD', 'Contact']
    },
    {
      id: 'contact',
      question: 'Contact',
      answer: 'Contactez-nous par email : <a href="mailto:cohesifauto@gmail.com" style="color:#1e3a5f;font-weight:600">cohesifauto@gmail.com</a>, par téléphone au <a href="tel:0760903774" style="color:#1e3a5f;font-weight:600">07 60 90 37 74</a> ou via notre <a href="#contact" style="color:#1e3a5f;font-weight:600;text-decoration:underline">formulaire de contact</a>. Réponse sous 48h ! 📩',
      suggestions: ['Devis gratuit', 'Flottes professionnelles', 'Import automobile']
    },
    {
      id: 'groupe',
      question: 'Groupe Cohesif',
      answer: 'Cohesif Auto est le pôle Mobilité, Transport & Logistique du Groupe Cohesif — un groupe français multi-métiers avec 8 pôles : Cohesif Auto, Cohesif Energy (solaire, bornes), Cohesif BTP (rénovation), Cohesif Sport, Cohesif Commerce, Cohesif Agro, Cohesif Négoce et Cohesif Access. 🏗️',
      suggestions: ['Contact', 'Devis gratuit', 'Vente de véhicules']
    },
  ];

  const INITIAL_SUGGESTIONS = [
    '🚗 Vente de véhicules',
    '🌍 Import automobile',
    '🚐 Flottes professionnelles',
    '🔩 Pièces de collection',
    '📋 Devis gratuit',
  ];

  // ─── Avatar SVG (Alex, conseiller Cohesif Auto) ───────────────────────────
  const AVATAR_SVG = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44 44" fill="none">
    <circle cx="22" cy="22" r="22" fill="#1e3a5f"/>
    <path d="M8 44c0-8.8 6.3-16 14-16s14 7.2 14 16" fill="#163050"/>
    <path d="M14 30 L22 28 L30 30 L30 44 L14 44Z" fill="#2a4d7a"/>
    <path d="M19 29 L22 32 L25 29 L22 28Z" fill="#fff"/>
    <rect x="21" y="29" width="2" height="5" rx="1" fill="#e8f0fc" opacity="0.8"/>
    <circle cx="22" cy="16" r="9" fill="#f5c5a0"/>
    <path d="M13 12c1-5 4.5-7.5 9-7.5s8 2.5 9 7.5" fill="#1a1a1a"/>
    <path d="M13 12 Q22 10 31 12" stroke="#1a1a1a" stroke-width="1.5" fill="none"/>
    <circle cx="18.5" cy="16" r="1.3" fill="#2d1b00"/>
    <circle cx="25.5" cy="16" r="1.3" fill="#2d1b00"/>
    <circle cx="19" cy="15.5" r="0.4" fill="#fff"/>
    <circle cx="26" cy="15.5" r="0.4" fill="#fff"/>
    <path d="M18.5 19.5 Q22 22 25.5 19.5" stroke="#c47a4a" stroke-width="1.2" stroke-linecap="round" fill="none"/>
    <path d="M16 11 Q22 8 28 11" stroke="#8b5a2b" stroke-width="2" fill="none" stroke-linecap="round"/>
  </svg>`;

  // ─── CSS ──────────────────────────────────────────────────────────────────
  const CSS = `
    /* ──────────── ASSISTANT IA COHESIF AUTO */
    .cohesif-ai-assistant {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 9999;
    }

    .cohesif-ai-bubble {
      position: absolute;
      bottom: 88px;
      right: 0;
      background: #fff;
      border: 1px solid #e5e7eb;
      border-radius: 18px 18px 4px 18px;
      padding: 16px 20px;
      box-shadow: 0 12px 32px rgba(0,0,0,0.12);
      width: 260px;
      opacity: 0;
      transform: translateY(10px) scale(0.95);
      transition: opacity 0.4s, transform 0.4s;
      pointer-events: none;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    .cohesif-ai-bubble.show {
      opacity: 1;
      transform: translateY(0) scale(1);
      pointer-events: auto;
    }
    .cohesif-ai-bubble-close {
      position: absolute;
      top: 8px; right: 8px;
      width: 22px; height: 22px;
      border-radius: 50%;
      background: #f3f4f6;
      display: flex; align-items: center; justify-content: center;
      cursor: pointer;
      font-size: 12px;
      color: #6b7280;
      border: none;
      transition: background 0.15s;
      line-height: 1;
    }
    .cohesif-ai-bubble-close:hover { background: #e5e7eb; }
    .cohesif-ai-bubble-name {
      font-size: 12px; font-weight: 700;
      color: #1e3a5f;
      letter-spacing: 1px; text-transform: uppercase;
      margin-bottom: 4px;
    }
    .cohesif-ai-bubble-text {
      font-size: 14px;
      color: #111;
      line-height: 1.45;
    }

    .cohesif-ai-avatar {
      width: 72px; height: 72px;
      border-radius: 50%;
      background: linear-gradient(135deg, #e8f0fc 0%, #c8d9f0 100%);
      border: 3px solid #fff;
      cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      box-shadow: 0 8px 28px rgba(30,58,95,0.3),
                  0 0 0 1px rgba(30,58,95,0.2);
      transition: transform 0.25s, box-shadow 0.25s;
      position: relative;
      overflow: hidden;
      padding: 0;
    }
    .cohesif-ai-avatar:hover {
      transform: scale(1.08) rotate(-3deg);
      box-shadow: 0 14px 36px rgba(30,58,95,0.45),
                  0 0 0 1px rgba(30,58,95,0.35);
    }
    .cohesif-ai-avatar svg { width: 90%; height: auto; }
    .cohesif-ai-avatar-status {
      position: absolute;
      bottom: 4px; right: 4px;
      width: 16px; height: 16px;
      background: #16a34a;
      border: 3px solid #fff;
      border-radius: 50%;
      animation: cohesif-ai-pulse 2s infinite;
      z-index: 2;
    }
    @keyframes cohesif-ai-pulse {
      0%   { box-shadow: 0 0 0 0 rgba(22,163,74,0.5); }
      70%  { box-shadow: 0 0 0 10px rgba(22,163,74,0); }
      100% { box-shadow: 0 0 0 0 rgba(22,163,74,0); }
    }

    .cohesif-ai-chat {
      position: absolute;
      bottom: 88px;
      right: 0;
      width: 360px;
      max-width: calc(100vw - 32px);
      height: 540px;
      max-height: calc(100vh - 120px);
      background: #fff;
      border: 1px solid #e5e7eb;
      border-radius: 20px;
      box-shadow: 0 24px 60px rgba(0,0,0,0.18);
      display: none;
      flex-direction: column;
      overflow: hidden;
      transform-origin: bottom right;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    .cohesif-ai-chat.open {
      display: flex;
      animation: cohesif-ai-chat-open 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes cohesif-ai-chat-open {
      from { opacity: 0; transform: translateY(10px) scale(0.95); }
      to   { opacity: 1; transform: translateY(0) scale(1); }
    }

    .cohesif-ai-chat-header {
      background: #1e3a5f;
      color: #fff;
      padding: 18px 20px;
      display: flex; align-items: center; gap: 12px;
      flex-shrink: 0;
    }
    .cohesif-ai-chat-mini-avatar {
      width: 44px; height: 44px;
      border-radius: 50%;
      background: linear-gradient(135deg, #e8f0fc 0%, #c8d9f0 100%);
      flex-shrink: 0;
      overflow: hidden;
      display: flex; align-items: center; justify-content: center;
      border: 2px solid rgba(255,255,255,0.2);
    }
    .cohesif-ai-chat-mini-avatar svg { width: 90%; height: auto; }
    .cohesif-ai-chat-info { flex: 1; line-height: 1.2; }
    .cohesif-ai-chat-name { font-size: 15px; font-weight: 700; color: #fff; }
    .cohesif-ai-chat-status {
      font-size: 11px;
      color: rgba(255,255,255,0.65);
      display: flex; align-items: center; gap: 6px;
      margin-top: 2px;
    }
    .cohesif-ai-chat-status::before {
      content: '';
      width: 6px; height: 6px;
      background: #4ade80;
      border-radius: 50%;
    }
    .cohesif-ai-chat-close {
      width: 32px; height: 32px;
      border-radius: 50%;
      background: rgba(255,255,255,0.1);
      display: flex; align-items: center; justify-content: center;
      cursor: pointer;
      color: #fff;
      font-size: 18px;
      border: none;
      transition: background 0.15s;
      line-height: 1;
    }
    .cohesif-ai-chat-close:hover { background: rgba(255,255,255,0.2); }

    .cohesif-ai-chat-body {
      flex: 1;
      overflow-y: auto;
      padding: 20px;
      display: flex; flex-direction: column;
      gap: 14px;
      background: #f9fafb;
    }
    .cohesif-ai-chat-body::-webkit-scrollbar { width: 6px; }
    .cohesif-ai-chat-body::-webkit-scrollbar-thumb { background: #d1d5db; border-radius: 3px; }

    .cohesif-ai-msg {
      max-width: 85%;
      padding: 11px 15px;
      border-radius: 16px;
      font-size: 14px;
      line-height: 1.5;
      animation: cohesif-ai-msg-in 0.3s ease both;
    }
    @keyframes cohesif-ai-msg-in {
      from { opacity: 0; transform: translateY(8px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    .cohesif-ai-msg-bot {
      background: #fff;
      border: 1px solid #e5e7eb;
      color: #111;
      align-self: flex-start;
      border-bottom-left-radius: 4px;
    }
    .cohesif-ai-msg-user {
      background: #1e3a5f;
      color: #fff;
      align-self: flex-end;
      border-bottom-right-radius: 4px;
    }
    .cohesif-ai-msg-bot a {
      color: #1e3a5f;
      text-decoration: underline;
      font-weight: 600;
    }

    .cohesif-ai-typing {
      display: inline-flex;
      gap: 4px;
      padding: 4px 0;
    }
    .cohesif-ai-typing span {
      width: 7px; height: 7px;
      background: #9ca3af;
      border-radius: 50%;
      animation: cohesif-ai-typing-anim 1.2s infinite;
    }
    .cohesif-ai-typing span:nth-child(2) { animation-delay: 0.2s; }
    .cohesif-ai-typing span:nth-child(3) { animation-delay: 0.4s; }
    @keyframes cohesif-ai-typing-anim {
      0%, 60%, 100% { opacity: 0.3; transform: translateY(0); }
      30% { opacity: 1; transform: translateY(-3px); }
    }

    .cohesif-ai-suggestions {
      display: flex; flex-wrap: wrap; gap: 6px;
      padding: 0 4px;
    }
    .cohesif-ai-suggestion {
      background: #fff;
      border: 1px solid #d1d5db;
      padding: 8px 14px;
      border-radius: 999px;
      font-size: 13px;
      color: #111;
      cursor: pointer;
      transition: border-color 0.15s, background 0.15s, transform 0.15s;
      font-family: inherit;
    }
    .cohesif-ai-suggestion:hover {
      border-color: #1e3a5f;
      background: #f4f0ea;
      transform: translateY(-1px);
    }

    .cohesif-ai-chat-footer {
      padding: 14px 16px;
      border-top: 1px solid #e5e7eb;
      background: #fff;
      flex-shrink: 0;
    }
    .cohesif-ai-chat-footer-text {
      font-size: 11px;
      color: #9ca3af;
      text-align: center;
      letter-spacing: 0.3px;
    }
    .cohesif-ai-chat-footer-cta {
      display: block;
      background: #1e3a5f;
      color: #fff;
      text-align: center;
      padding: 12px;
      border-radius: 999px;
      font-weight: 600; font-size: 14px;
      margin-top: 8px;
      transition: background 0.15s;
      text-decoration: none;
    }
    .cohesif-ai-chat-footer-cta:hover { background: #8b5a2b; color: #fff; }

    .cohesif-mobile-sticky-cta { display: none; }

    @media (max-width: 768px) {
      .cohesif-ai-assistant { bottom: 90px; right: 16px; }
      .cohesif-ai-avatar { width: 56px; height: 56px; }
      .cohesif-ai-bubble { bottom: 72px; width: 240px; }
      .cohesif-ai-chat { bottom: 72px; width: calc(100vw - 32px); height: 70vh; }

      .cohesif-mobile-sticky-cta {
        display: flex;
        position: fixed;
        bottom: 16px; left: 16px; right: 16px;
        z-index: 9998;
        background: #1e3a5f;
        border-radius: 999px;
        padding: 4px 4px 4px 20px;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
        box-shadow: 0 12px 40px rgba(0,0,0,0.25),
                    0 0 0 1px rgba(255,255,255,0.05);
        transform: translateY(120%);
        transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        text-decoration: none;
      }
      .cohesif-mobile-sticky-cta.visible { transform: translateY(0); }
      .cohesif-mobile-sticky-cta-text {
        color: #fff;
        font-size: 14px; font-weight: 600;
        line-height: 1.2;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      }
      .cohesif-mobile-sticky-cta-text small {
        display: block;
        color: rgba(255,255,255,0.6);
        font-size: 11px; font-weight: 500;
        margin-top: 2px; letter-spacing: 0.5px;
      }
      .cohesif-mobile-sticky-cta-btn {
        background: #8b5a2b;
        color: #fff;
        font-size: 13px; font-weight: 700;
        padding: 12px 18px;
        border-radius: 999px;
        white-space: nowrap; flex-shrink: 0;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      }
    }
  `;

  // ─── Init ─────────────────────────────────────────────────────────────────
  function init() {
    if (document.getElementById('cohesif-ai-widget')) return;

    const style = document.createElement('style');
    style.textContent = CSS;
    document.head.appendChild(style);

    const widget = document.createElement('div');
    widget.id = 'cohesif-ai-widget';
    widget.innerHTML = `
      <div class="cohesif-ai-assistant">

        <div class="cohesif-ai-bubble">
          <button class="cohesif-ai-bubble-close" title="Fermer">&#x2715;</button>
          <div class="cohesif-ai-bubble-name">COHESIF AUTO</div>
          <div class="cohesif-ai-bubble-text">Vente, import, flottes&hellip; une question ? Je suis l&agrave; !</div>
        </div>

        <button class="cohesif-ai-avatar" title="Parler à Alex">
          ${AVATAR_SVG}
          <div class="cohesif-ai-avatar-status"></div>
        </button>

        <div class="cohesif-ai-chat">
          <div class="cohesif-ai-chat-header">
            <div class="cohesif-ai-chat-mini-avatar">${AVATAR_SVG}</div>
            <div class="cohesif-ai-chat-info">
              <div class="cohesif-ai-chat-name">Alex &mdash; Conseiller Cohesif Auto</div>
              <div class="cohesif-ai-chat-status">En ligne &middot; R&eacute;pond instantan&eacute;ment</div>
            </div>
            <button class="cohesif-ai-chat-close" title="Fermer">&#x2715;</button>
          </div>

          <div class="cohesif-ai-chat-body"></div>

          <div class="cohesif-ai-chat-footer">
            <div class="cohesif-ai-chat-footer-text">Propuls&eacute; par IA &middot; Cohesif Auto</div>
            <a href="#contact" class="cohesif-ai-chat-footer-cta">Demander un devis gratuit</a>
          </div>
        </div>

      </div>

      <a href="#contact" class="cohesif-mobile-sticky-cta">
        <div class="cohesif-mobile-sticky-cta-text">
          Votre prochain v&#233;hicule
          <small>Devis gratuit en 48h</small>
        </div>
        <div class="cohesif-mobile-sticky-cta-btn">D&#233;marrer</div>
      </a>
    `;
    document.body.appendChild(widget);

    const bubble      = widget.querySelector('.cohesif-ai-bubble');
    const bubbleClose = widget.querySelector('.cohesif-ai-bubble-close');
    const avatar      = widget.querySelector('.cohesif-ai-avatar');
    const chatWindow  = widget.querySelector('.cohesif-ai-chat');
    const chatClose   = widget.querySelector('.cohesif-ai-chat-close');
    const chatBody    = widget.querySelector('.cohesif-ai-chat-body');
    const mobileCta   = widget.querySelector('.cohesif-mobile-sticky-cta');

    let chatOpen = false;

    setTimeout(function () {
      if (!chatOpen) bubble.classList.add('show');
    }, 3000);

    bubbleClose.addEventListener('click', function (e) {
      e.stopPropagation();
      bubble.classList.remove('show');
    });

    avatar.addEventListener('click', function () {
      chatOpen = !chatOpen;
      if (chatOpen) {
        chatWindow.classList.add('open');
        bubble.classList.remove('show');
        initChat();
      } else {
        chatWindow.classList.remove('open');
      }
    });

    chatClose.addEventListener('click', function () {
      chatOpen = false;
      chatWindow.classList.remove('open');
    });

    function initChat() {
      if (chatBody.children.length === 0) {
        addBotMsg('Bonjour ! 👋 Je suis Alex, votre conseiller Cohesif Auto. Vente, import, flottes professionnelles, pièces de collection — posez-moi vos questions. Par où on commence ?');
        setTimeout(function () { showSuggestions(INITIAL_SUGGESTIONS); }, 400);
      }
    }

    function addBotMsg(html) {
      var el = document.createElement('div');
      el.className = 'cohesif-ai-msg cohesif-ai-msg-bot';
      el.innerHTML = html;
      chatBody.appendChild(el);
      chatBody.scrollTop = chatBody.scrollHeight;
    }

    function addUserMsg(text) {
      var el = document.createElement('div');
      el.className = 'cohesif-ai-msg cohesif-ai-msg-user';
      el.textContent = text;
      chatBody.appendChild(el);
      chatBody.scrollTop = chatBody.scrollHeight;
    }

    function showTyping() {
      var el = document.createElement('div');
      el.id = 'cohesif-typing-indicator';
      el.className = 'cohesif-ai-msg cohesif-ai-msg-bot';
      el.innerHTML = '<div class="cohesif-ai-typing"><span></span><span></span><span></span></div>';
      chatBody.appendChild(el);
      chatBody.scrollTop = chatBody.scrollHeight;
    }

    function hideTyping() {
      var el = document.getElementById('cohesif-typing-indicator');
      if (el) el.remove();
    }

    function showSuggestions(list) {
      var container = document.createElement('div');
      container.className = 'cohesif-ai-suggestions';
      list.forEach(function (text) {
        var btn = document.createElement('button');
        btn.className = 'cohesif-ai-suggestion';
        btn.textContent = text;
        btn.addEventListener('click', function () { handleInput(text); });
        container.appendChild(btn);
      });
      chatBody.appendChild(container);
      chatBody.scrollTop = chatBody.scrollHeight;
    }

    function handleInput(text) {
      addUserMsg(text);
      showTyping();

      var clean = text.replace(/[\u{1F300}-\u{1FFFF}]|\p{Emoji}/gu, '').trim().toLowerCase();
      var faq = null;
      for (var i = 0; i < faqData.length; i++) {
        var q = faqData[i].question.toLowerCase();
        if (clean.includes(q) || q.includes(clean)) { faq = faqData[i]; break; }
      }

      setTimeout(function () {
        hideTyping();
        if (faq) {
          addBotMsg(faq.answer);
          setTimeout(function () { showSuggestions(faq.suggestions); }, 300);
        } else {
          addBotMsg('Je ne suis pas sûr de comprendre. Voici les sujets sur lesquels je peux vous aider :');
          setTimeout(function () { showSuggestions(INITIAL_SUGGESTIONS); }, 300);
        }
      }, 700 + Math.random() * 300);
    }

    function toggleMobileCta() {
      if (!mobileCta) return;
      if (window.scrollY > 300) {
        mobileCta.classList.add('visible');
      } else {
        mobileCta.classList.remove('visible');
      }
    }
    window.addEventListener('scroll', toggleMobileCta, { passive: true });
    toggleMobileCta();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
