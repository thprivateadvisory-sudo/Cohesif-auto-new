// ===== TOGGLE Particulier / Pro / Tout =====
  const toggleBtns = document.querySelectorAll('.toggle-btn');
  const universItems = document.querySelectorAll('.univers');
  const toggleInfoText = document.getElementById('toggleInfoText');

  const filterMessages = {
    all: (count) => `<strong>${count} univers</strong> affichés`,
    particulier: (count) => `<strong>${count} univers</strong> pour les particuliers`,
    pro: (count) => `<strong>${count} univers</strong> pour les professionnels`
  };

  toggleBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      toggleBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const target = btn.dataset.target;

      let visibleCount = 0;
      universItems.forEach(item => {
        const audience = item.dataset.audience || '';
        const shouldShow = (target === 'all' || audience.includes(target));

        if (shouldShow) {
          item.classList.remove('hidden');
          item.style.display = '';
          visibleCount++;
        } else {
          item.classList.add('hidden');
          // On laisse le temps à l'animation avant de réellement cacher
          setTimeout(() => {
            if (item.classList.contains('hidden')) {
              item.style.display = 'none';
            }
          }, 400);
        }
      });

      // Mettre à jour le compteur avec message contextuel
      if (toggleInfoText && filterMessages[target]) {
        toggleInfoText.innerHTML = filterMessages[target](visibleCount);
      }
    });
  });

  // ===== ANIMATIONS FADE-IN =====
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) entry.target.classList.add('visible');
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.univers, .mode, .vintage-wrap > *, .why-card, .trust-card, .process-step').forEach(el => {
    el.classList.add('fade-in');
    observer.observe(el);
  });

  // ===== COMPTEUR ANIMÉ DES STATS =====
  const animateNumber = (element, target, duration = 1800) => {
    const start = 0;
    const startTime = performance.now();
    const numberSpan = element.childNodes[0]; // le node texte avant les span (.plus / .unit)

    const update = (currentTime) => {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      // easing easeOutQuart
      const eased = 1 - Math.pow(1 - progress, 4);
      const current = Math.floor(start + (target - start) * eased);

      // On remplace seulement le contenu texte (pas les spans)
      if (numberSpan && numberSpan.nodeType === Node.TEXT_NODE) {
        numberSpan.textContent = current;
      }

      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        if (numberSpan && numberSpan.nodeType === Node.TEXT_NODE) {
          numberSpan.textContent = target;
        }
      }
    };

    requestAnimationFrame(update);
  };

  const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !entry.target.dataset.animated) {
        entry.target.dataset.animated = 'true';
        const statNums = entry.target.querySelectorAll('.stat-num');
        statNums.forEach(stat => {
          // Récupérer le nombre cible depuis le premier nœud texte
          const textNode = stat.childNodes[0];
          if (textNode && textNode.nodeType === Node.TEXT_NODE) {
            const target = parseInt(textNode.textContent.trim());
            if (!isNaN(target)) {
              textNode.textContent = '0';
              animateNumber(stat, target);
            }
          }
        });
      }
    });
  }, { threshold: 0.4 });

  document.querySelectorAll('.stats-bar').forEach(el => {
    statsObserver.observe(el);
  });

  // ===== PRÉ-REMPLISSAGE DU SUJET DEPUIS LES LIENS UNIVERS =====
  document.querySelectorAll('a[data-subject]').forEach(link => {
    link.addEventListener('click', (e) => {
      const subject = link.dataset.subject;
      const select = document.getElementById('form-subject');
      if (select && subject) {
        select.value = subject;
        // Animation visuelle pour montrer que ça a été pris en compte
        select.style.transition = 'all 0.3s ease';
        select.style.borderColor = 'var(--accent)';
        select.style.boxShadow = '0 0 0 3px rgba(30, 58, 95, 0.15)';
        setTimeout(() => {
          select.style.borderColor = '';
          select.style.boxShadow = '';
        }, 1500);
      }
    });
  });

  // ===== SOUMISSION DU FORMULAIRE =====
  const form = document.getElementById('contactForm');
  const successMsg = document.getElementById('formSuccess');
  const submitBtn = form ? form.querySelector('button[type="submit"]') : null;

  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      const data = {
        nom: form.name.value,
        societe: form.company.value || '—',
        email: form.email.value,
        telephone: form.phone.value,
        sujet: form.subject.options[form.subject.selectedIndex].text,
        message: form.message.value
      };

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Envoi en cours…';
      }

      try {
        const resp = await fetch('https://formspree.io/f/xblwjrpk', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify({
            name: data.nom,
            company: data.societe,
            email: data.email,
            phone: data.telephone,
            subject: data.sujet,
            message: data.message,
            _subject: `[Cohesif Auto] ${data.sujet} — ${data.nom}`
          })
        });

        if (resp.ok) {
          successMsg.classList.add('visible');
          successMsg.scrollIntoView({ behavior: 'smooth', block: 'center' });
          setTimeout(() => { form.reset(); }, 800);
        } else {
          throw new Error('Formspree error');
        }
      } catch {
        // Fallback: ouvre le client mail si l'envoi échoue
        const subject = encodeURIComponent(`[Cohesif Auto] ${data.sujet} — ${data.nom}`);
        const body = encodeURIComponent(
          `Nom : ${data.nom}\nSociété : ${data.societe}\nEmail : ${data.email}\nTéléphone : ${data.telephone}\nSujet : ${data.sujet}\n\nMessage :\n${data.message}`
        );
        window.location.href = `mailto:cohesifauto@gmail.com?subject=${subject}&body=${body}`;
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = 'Envoyer ma demande →';
        }
      }
    });
  }

  // ===== STICKY CTA MOBILE =====
  // Apparaît après scroll du hero, disparaît sur le formulaire de contact
  const stickyCta = document.getElementById('stickyCta');
  const heroSection = document.querySelector('.page-hero');
  const contactSection = document.getElementById('contact');

  if (stickyCta && heroSection && contactSection) {
    let lastScrollY = window.scrollY;
    let ticking = false;

    const updateStickyCta = () => {
      const heroBottom = heroSection.offsetTop + heroSection.offsetHeight;
      const contactTop = contactSection.offsetTop - 100; // marge de 100px avant le formulaire
      const scrollY = window.scrollY;
      const viewportHeight = window.innerHeight;

      // Visible si on a scrollé au-delà du hero ET pas encore arrivé au formulaire
      const shouldShow = scrollY > heroBottom - viewportHeight * 0.3
                       && scrollY + viewportHeight < contactTop + 200;

      if (shouldShow) {
        stickyCta.classList.add('visible');
        stickyCta.classList.remove('hidden');
      } else {
        stickyCta.classList.remove('visible');
        stickyCta.classList.add('hidden');
      }

      ticking = false;
    };

    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(updateStickyCta);
        ticking = true;
      }
    }, { passive: true });

    // État initial
    updateStickyCta();
  }

