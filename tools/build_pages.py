#!/usr/bin/env python3
"""Génère les pages services, guides et la page 404 de cohesifauto.fr.

Le contenu vit dans tools/pages_contenu.py ; ce script assemble le gabarit
commun (en-tête, pied de page, formulaire, données structurées) puis
régénère sitemap.xml et llms.txt.

Usage : python3 tools/build_pages.py   (depuis la racine du dépôt)
"""
import html
import json
import os
import re
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pages_contenu import PAGES, HUB  # noqa: E402

SITE = "https://cohesifauto.fr"
PHONE_HREF = "tel:+33756855727"
PHONE = "07 56 85 57 27"
EMAIL = "cohesifauto@gmail.com"
WA = "https://wa.me/33756855727?text=Bonjour%2C%20je%20cherche%20un%20v%C3%A9hicule%20%3A%20"
TODAY = date.today().isoformat()
ASSET_V = "4"

NAV = [
    ("Chasseur auto", "chasseur-automobile.html"),
    ("Import Allemagne", "import-voiture-allemagne.html"),
    ("Prestige", "voiture-prestige.html"),
    ("Entreprises", "vehicules-entreprise-lld.html"),
    ("Financement", "financement-voiture.html"),
    ("Guides", "guides.html"),
]

BY_SLUG = {p["slug"]: p for p in PAGES}
SERVICES = [p for p in PAGES if p["kind"] == "service"]
GUIDES = [p for p in PAGES if p["kind"] == "guide"]

PROJETS = [
    ("Acheter un véhicule", "Acheter un véhicule"),
    ("Importer d'Europe", "Importer un véhicule d'Europe"),
    ("Flotte entreprise", "Véhicules pour mon entreprise"),
    ("Pièce de collection", "Pièce rare / collection"),
    ("Financement", "Financement"),
    ("Autre", "Autre demande"),
]

ICON_SPRITE = open(os.path.join(ROOT, "tools", "icons.svg"), encoding="utf-8").read()


def esc(s):
    return html.escape(s, quote=True)


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


def jsonld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False, indent=1) + "\n</script>"


# ---------------------------------------------------------------- blocs communs

def head(title, description, path, og_image="img/og-cohesif-auto.jpg", schemas=(), noindex=False):
    canonical = SITE + "/" + (path if path != "index.html" else "")
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large"
    out = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="color-scheme" content="light only">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#0b1220">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Cohesif Auto">
<meta property="og:locale" content="fr_FR">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="{SITE}/{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{SITE}/{og_image}">
<link rel="icon" type="image/png" sizes="32x32" href="img/icon-32.png">
<link rel="apple-touch-icon" href="img/icon-180.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css?v={ASSET_V}">
"""
    for s in schemas:
        out += jsonld(s) + "\n"
    return out + "</head>\n<body>\n"


def header():
    nav = "\n".join(f'      <a href="{h}">{esc(l)}</a>' for l, h in NAV)
    mnav = "\n".join(f'    <a href="{h}">{esc(l)}</a>' for l, h in NAV)
    return f"""{ICON_SPRITE}
<div class="topbar">
  <div class="container">
    <div class="topbar-left">
      <span class="topbar-dot" aria-hidden="true"></span>
      <span>Conseillers disponibles <span class="hide-sm">du lundi au samedi, 9h–19h</span></span>
    </div>
    <div class="topbar-right">
      <a href="{PHONE_HREF}">{PHONE}</a>
      <a class="hide-sm" href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
</div>

<header class="header">
  <div class="container">
    <a href="./" class="logo" aria-label="Cohesif Auto — accueil">
      <img src="img/logo-cohesif-auto.webp" alt="Cohesif Auto" width="183" height="36">
    </a>
    <nav class="nav" aria-label="Navigation principale">
{nav}
    </nav>
    <div class="header-cta">
      <a class="header-phone" href="{PHONE_HREF}" aria-label="Appeler le {PHONE}">
        <svg><use href="#i-phone"/></svg><span>{PHONE}</span>
      </a>
      <a href="#contact" class="btn btn-primary" data-track="header_cta">Mes propositions gratuites</a>
      <button class="menu-toggle" id="menuOpen" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="mobileMenu">
        <svg><use href="#i-menu"/></svg>
      </button>
    </div>
  </div>
</header>

<div class="mobile-menu" id="mobileMenu" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="mobile-menu-head">
    <img src="img/logo-cohesif-auto.webp" alt="Cohesif Auto" width="152" height="30" style="height:30px;width:auto">
    <button class="menu-toggle" id="menuClose" aria-label="Fermer le menu" style="display:inline-flex">
      <svg><use href="#i-x"/></svg>
    </button>
  </div>
  <nav aria-label="Navigation mobile">
    <a href="./">Accueil</a>
{mnav}
  </nav>
  <div class="mobile-menu-actions">
    <a href="#contact" class="btn btn-primary btn-block">Mes propositions gratuites</a>
    <a href="{PHONE_HREF}" class="btn btn-ghost btn-block"><svg><use href="#i-phone"/></svg>{PHONE}</a>
  </div>
</div>
"""


def breadcrumb_html(trail):
    items = []
    for i, (name, href) in enumerate(trail):
        if href and i < len(trail) - 1:
            items.append(f'<li><a href="{href}">{esc(name)}</a></li>')
        else:
            items.append(f'<li aria-current="page">{esc(name)}</li>')
    return '<nav class="breadcrumb" aria-label="Fil d\'Ariane"><ol>' + "".join(items) + "</ol></nav>"


def breadcrumb_schema(trail):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name,
             "item": SITE + "/" + (href if href not in ("./", "index.html") else "")}
            for i, (name, href) in enumerate(trail)
        ],
    }


def faq_html(faq):
    if not faq:
        return ""
    items = "\n".join(
        f"""      <details>
        <summary>{esc(q)}</summary>
        <div class="ans"><p>{a}</p></div>
      </details>""" for q, a in faq)
    return f"""
<section class="section section-tint" id="faq">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">Questions fréquentes</span>
      <h2>Vos questions, nos réponses</h2>
    </div>
    <div class="faq reveal">
{items}
    </div>
  </div>
</section>
"""


def faq_schema(faq):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in faq
        ],
    }


def link_card(p):
    k = "Guide" if p["kind"] == "guide" else "Service"
    return f"""      <a class="link-card" href="{p['slug']}">
        <span class="k">{k}</span>
        <b>{esc(p['card_title'])}</b>
        <span>{esc(p['card_text'])}</span>
        <span class="more">{'Lire le guide' if p['kind'] == 'guide' else 'Découvrir'} <svg><use href="#i-arrow"/></svg></span>
      </a>"""


def related_html(slugs, title="À lire aussi"):
    cards = "\n".join(link_card(BY_SLUG[s]) for s in slugs if s in BY_SLUG)
    return f"""
<section class="section" id="a-lire">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Pour aller plus loin</span>
      <h2>{esc(title)}</h2>
    </div>
    <div class="card-grid reveal">
{cards}
    </div>
  </div>
</section>
"""


def contact_html(projet, source, title="Dites-nous ce que vous cherchez. On s'occupe du reste."):
    opts = "\n".join(
        f'            <option value="{esc(v)}"{" selected" if v == projet else ""}>{esc(l)}</option>'
        for v, l in PROJETS)
    return f"""
<section class="section contact" id="contact">
  <div class="container contact-grid">
    <div class="reveal">
      <span class="eyebrow">Parlons de votre projet</span>
      <h2>{esc(title)}</h2>
      <p class="contact-lead">Propositions chiffrées sous 48h ouvrées, gratuitement et sans engagement. Souvent un premier appel dans la journée.</p>
      <div class="channels">
        <a class="channel" href="{PHONE_HREF}" data-track="contact_call">
          <span class="ci"><svg><use href="#i-phone"/></svg></span>
          <div><small>Téléphone</small><b>{PHONE}</b></div>
        </a>
        <a class="channel" href="{WA}" target="_blank" rel="noopener" data-track="contact_whatsapp">
          <span class="ci wa"><svg><use href="#i-wa"/></svg></span>
          <div><small>WhatsApp</small><b>Écrire un message</b></div>
        </a>
        <a class="channel" href="mailto:{EMAIL}">
          <span class="ci"><svg><use href="#i-mail"/></svg></span>
          <div><small>Email</small><b>{EMAIL}</b></div>
        </a>
      </div>
    </div>

    <div class="lead-card reveal">
      <div class="lead-card-head">
        <h2>Votre demande en 1 minute</h2>
        <p>Plus vous êtes précis, plus nos propositions seront justes.</p>
      </div>
      <form class="lead-form" id="contactForm" novalidate data-source="{esc(source)}">
        <div class="field">
          <label for="cf-projet">Votre projet</label>
          <select id="cf-projet" name="projet" required>
{opts}
          </select>
        </div>
        <div class="field-row">
          <div class="field">
            <label for="cf-nom">Prénom et nom</label>
            <input id="cf-nom" name="nom" type="text" required autocomplete="name" placeholder="Jean Dupont">
          </div>
          <div class="field">
            <label for="cf-societe">Société <small>(facultatif)</small></label>
            <input id="cf-societe" name="societe" type="text" autocomplete="organization" placeholder="Nom de l'entreprise">
          </div>
        </div>
        <div class="field-row">
          <div class="field">
            <label for="cf-tel">Téléphone</label>
            <input id="cf-tel" name="telephone" type="tel" required autocomplete="tel" inputmode="tel" placeholder="06 12 34 56 78">
          </div>
          <div class="field">
            <label for="cf-email">Email</label>
            <input id="cf-email" name="email" type="email" required autocomplete="email" placeholder="vous@exemple.fr">
          </div>
        </div>
        <div class="field">
          <label for="cf-msg">Votre recherche <small>(modèle, budget, délai…)</small></label>
          <textarea id="cf-msg" name="message" placeholder="ex : BMW X3 hybride, moins de 60 000 km, budget 40 000 €, livraison avant juin."></textarea>
        </div>
        <button type="submit" class="btn btn-primary btn-block">Recevoir mes propositions</button>
        <p class="form-legal">Gratuit et sans engagement. <a href="confidentialite.html">Politique de confidentialité</a></p>
        <p class="form-error" role="alert"></p>
      </form>
      <div class="form-success" role="status">
        <div class="ok"><svg><use href="#i-check"/></svg></div>
        <h3>Demande bien reçue !</h3>
        <p>Un conseiller revient vers vous sous 48h ouvrées.</p>
        <a class="btn btn-wa" href="https://wa.me/33756855727" target="_blank" rel="noopener"><svg><use href="#i-wa"/></svg>Continuer sur WhatsApp</a>
      </div>
    </div>
  </div>
</section>
"""


def footer():
    svc = "\n".join(f'          <li><a href="{p["slug"]}">{esc(p["menu"])}</a></li>' for p in SERVICES)
    gd = "\n".join(f'          <li><a href="{p["slug"]}">{esc(p["menu"])}</a></li>' for p in GUIDES)
    return f"""
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="img/logo-cohesif-auto-white.webp" alt="Cohesif Auto" loading="lazy" width="173" height="34">
        <p>Mandataire et chasseur automobile : achat accompagné, import de véhicules d'Europe, flottes d'entreprise et pièces de collection. Le pôle mobilité du Groupe Cohesif.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
{svc}
        </ul>
      </div>
      <div>
        <h4>Guides</h4>
        <ul>
{gd}
          <li><a href="guides.html">Tous les guides</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="{PHONE_HREF}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>200 rue de la Croix-Nivert<br>75015 Paris</li>
        </ul>
        <h4 style="margin-top:26px">Groupe Cohesif</h4>
        <ul>
          <li><a href="https://cohesifleasing.fr" target="_blank" rel="noopener">Cohesif Leasing</a></li>
          <li><a href="https://cohesifenergy.fr" target="_blank" rel="noopener">Cohesif Energy</a></li>
          <li><a href="https://cohesifbtp.fr" target="_blank" rel="noopener">Cohesif BTP</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Cohesif Auto · Groupe Cohesif</span>
      <nav aria-label="Liens légaux">
        <a href="mentions-legales.html">Mentions légales</a>
        <a href="confidentialite.html">Confidentialité</a>
        <a href="cgv.html">CGV</a>
      </nav>
    </div>
  </div>
</footer>

<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Nous écrire sur WhatsApp" data-track="float_whatsapp">
  <svg><use href="#i-wa"/></svg>
</a>

<nav class="mobile-bar" id="mobileBar" aria-label="Contact rapide">
  <a class="mb-call" href="{PHONE_HREF}" data-track="bar_call"><svg><use href="#i-phone"/></svg>Appeler</a>
  <a class="mb-wa" href="{WA}" target="_blank" rel="noopener" data-track="bar_whatsapp"><svg><use href="#i-wa"/></svg>WhatsApp</a>
  <a class="mb-quote" href="#contact" data-track="bar_quote">Mes propositions</a>
</nav>
"""


def tail():
    return f'<script src="main.js?v={ASSET_V}" defer></script>\n</body>\n</html>\n'


# ---------------------------------------------------------------- pages

ORG = {"@type": "AutoDealer", "name": "Cohesif Auto", "url": SITE + "/", "telephone": "+33756855727",
       "address": {"@type": "PostalAddress", "streetAddress": "200 rue de la Croix-Nivert",
                   "addressLocality": "Paris", "postalCode": "75015", "addressCountry": "FR"}}


def add_ids_and_toc(body):
    """Ajoute un id à chaque h2 du contenu et retourne (body, sommaire)."""
    toc = []

    def repl(m):
        attrs, text = m.group(1), m.group(2)
        slug = re.sub(r"[^a-z0-9]+", "-", strip_tags(text).lower()
                      .translate(str.maketrans("àâäéèêëîïôöùûüç’'", "aaaeeeeiioouuuc--"))).strip("-")[:60]
        toc.append((slug, strip_tags(text)))
        return f'<h2 id="{slug}"{attrs}>{text}</h2>'

    body = re.sub(r"<h2([^>]*)>(.*?)</h2>", repl, body)
    return body, toc


def read_minutes(body):
    return max(3, round(len(strip_tags(body).split()) / 220))


def build_page(p):
    is_guide = p["kind"] == "guide"
    parent = ("Guides", "guides.html") if is_guide else ("Services", "./#services")
    trail = [("Accueil", "./"), parent, (p["crumb"], p["slug"])]
    body, toc = add_ids_and_toc(p["body"])
    minutes = read_minutes(body)

    og = "img/og-cohesif-auto.jpg"
    if p.get("image"):
        jpg = p["image"][0].rsplit(".", 1)[0] + ".jpg"
        if os.path.exists(os.path.join(ROOT, jpg)):
            og = jpg

    schemas = [breadcrumb_schema(trail)]
    if is_guide:
        schemas.append({
            "@context": "https://schema.org", "@type": "Article", "headline": p["h1"],
            "description": p["description"], "inLanguage": "fr-FR",
            "datePublished": p.get("published", "2026-10-06"), "dateModified": p.get("modified", p.get("published", "2026-10-06")),
            "mainEntityOfPage": SITE + "/" + p["slug"],
            "image": SITE + "/" + og,
            "author": {"@type": "Organization", "name": "Cohesif Auto", "url": SITE + "/"},
            "publisher": {"@type": "Organization", "name": "Cohesif Auto",
                          "logo": {"@type": "ImageObject", "url": SITE + "/logo-cohesif-auto.png"}},
        })
    else:
        schemas.append({
            "@context": "https://schema.org", "@type": "Service", "name": p["h1"],
            "serviceType": p.get("service_type", p["crumb"]), "description": p["description"],
            "url": SITE + "/" + p["slug"], "provider": ORG,
            "areaServed": p.get("area", {"@type": "Country", "name": "France"}),
        })
    if p.get("faq"):
        schemas.append(faq_schema(p["faq"]))

    out = head(p["title"], p["description"], p["slug"], og_image=og, schemas=schemas)
    out += header()
    media = ""
    if p.get("image"):
        src, alt, w, h = p["image"]
        media = f"""
    <div class="page-hero-media">
      <img src="{src}" alt="{esc(alt)}" width="{w}" height="{h}" fetchpriority="high">
    </div>"""
    meta = ""
    if is_guide:
        meta = f'<div class="page-meta"><span>Guide Cohesif Auto</span><span>Lecture : {minutes} min</span><span>Mis à jour le {date.fromisoformat(p.get("modified", p.get("published", "2026-10-06"))).strftime("%d/%m/%Y")}</span></div>'
    ctas = "" if is_guide else f"""
      <div class="hero-ctas">
        <a href="#contact" class="btn btn-primary" data-track="page_hero_cta">{esc(p.get('cta', 'Recevoir mes propositions'))} <svg><use href="#i-arrow"/></svg></a>
        <a href="{PHONE_HREF}" class="btn btn-ghost-light"><svg><use href="#i-phone"/></svg>{PHONE}</a>
      </div>
      <ul class="hero-checks">
        <li><svg><use href="#i-check"/></svg>Propositions sous 48h</li>
        <li><svg><use href="#i-check"/></svg>Gratuit et sans engagement</li>
        <li><svg><use href="#i-check"/></svg>Livraison partout en France</li>
      </ul>"""
    out += f"""
<main>
<section class="page-hero{'' if media else ' no-media'}">
  <div class="container">
    <div>
      {breadcrumb_html(trail)}
      <span class="eyebrow">{esc(p['eyebrow'])}</span>
      <h1>{p['h1']}</h1>
      <p class="hero-lead">{p['lead']}</p>{ctas}
      {meta}
    </div>{media}
  </div>
</section>
"""
    toc_html = ""
    if len(toc) >= 3:
        lis = "".join(f'<li><a href="#{s}">{esc(t)}</a></li>' for s, t in toc)
        toc_html = f'<nav class="aside-card toc" aria-label="Sommaire"><h3>Sommaire</h3><ol>{lis}</ol></nav>'
    out += f"""
<section class="section">
  <div class="container content-layout">
    <article class="prose">
{body}
    </article>
    <aside class="aside-sticky">
      {toc_html}
      <div class="aside-card dark">
        <h3>{esc(p.get('aside_title', 'On s’en occupe pour vous'))}</h3>
        <p>{esc(p.get('aside_text', 'Dites-nous ce que vous cherchez : propositions chiffrées sous 48h, gratuitement.'))}</p>
        <a href="#contact" class="btn btn-primary" data-track="aside_cta">Recevoir mes propositions</a>
        <a href="{PHONE_HREF}" class="btn btn-ghost-light"><svg><use href="#i-phone"/></svg>{PHONE}</a>
      </div>
    </aside>
  </div>
</section>
"""
    out += faq_html(p.get("faq"))
    out += related_html(p.get("related", []))
    out += contact_html(p.get("projet", "Acheter un véhicule"), "Page " + p["slug"])
    out += "</main>\n" + footer() + tail()
    return out


def build_hub():
    trail = [("Accueil", "./"), ("Guides", "guides.html")]
    schemas = [breadcrumb_schema(trail), {
        "@context": "https://schema.org", "@type": "CollectionPage", "name": HUB["h1"],
        "description": HUB["description"], "url": SITE + "/guides.html",
        "hasPart": [{"@type": "Article", "headline": g["h1"], "url": SITE + "/" + g["slug"]} for g in GUIDES],
    }]
    out = head(HUB["title"], HUB["description"], "guides.html", schemas=schemas)
    out += header()
    guides = "\n".join(link_card(g) for g in GUIDES)
    services = "\n".join(link_card(s) for s in SERVICES)
    out += f"""
<main>
<section class="page-hero no-media">
  <div class="container">
    <div>
      {breadcrumb_html(trail)}
      <span class="eyebrow">Guides pratiques</span>
      <h1>{HUB['h1']}</h1>
      <p class="hero-lead">{HUB['lead']}</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="card-grid">
{guides}
    </div>
  </div>
</section>

<section class="section section-tint">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Nos services</span>
      <h2>Vous préférez déléguer ?</h2>
      <p>On s'occupe de la recherche, des vérifications et des démarches à votre place.</p>
    </div>
    <div class="card-grid reveal">
{services}
    </div>
  </div>
</section>
"""
    out += contact_html("Acheter un véhicule", "Page guides.html")
    out += "</main>\n" + footer() + tail()
    return out


def build_404():
    out = head("Page introuvable | Cohesif Auto", "Cette page n'existe pas ou a été déplacée.", "404.html", noindex=True)
    out = out.replace('href="styles.css', 'href="/styles.css')
    out += header()
    cards = "\n".join(link_card(BY_SLUG[s]) for s in ("chasseur-automobile.html", "import-voiture-allemagne.html", "vehicules-entreprise-lld.html"))
    out += f"""
<main>
<section class="err-page page-hero" style="background:var(--white);color:var(--ink-900)">
  <div class="container" style="display:block">
    <div class="code">404</div>
    <h1 style="color:var(--ink-900)">Cette page a pris une autre route.</h1>
    <p style="font-size:18px;max-width:560px;margin:0 auto">La page que vous cherchez n'existe pas ou a été déplacée. Voici par où repartir.</p>
    <div class="hero-ctas">
      <a href="/" class="btn btn-primary">Retour à l'accueil</a>
      <a href="{PHONE_HREF}" class="btn btn-ghost"><svg><use href="#i-phone"/></svg>{PHONE}</a>
    </div>
  </div>
</section>
<section class="section section-tint">
  <div class="container">
    <div class="card-grid">
{cards}
    </div>
  </div>
</section>
<section id="contact"></section>
</main>
""" + footer() + tail()
    # La 404 est servie à n'importe quelle profondeur d'URL : chemins absolus.
    out = re.sub(r'(href|src)="(?!https?:|tel:|mailto:|#|/)([^"]+)"', r'\1="/\2"', out)
    out = out.replace('href="/./"', 'href="/"')
    return out


def build_sitemap():
    urls = [("", "1.0", "weekly")]
    urls += [(p["slug"], "0.9", "monthly") for p in SERVICES]
    urls += [("guides.html", "0.7", "weekly")]
    urls += [(p["slug"], "0.8", "monthly") for p in GUIDES]
    urls += [(u, "0.2", "yearly") for u in ("mentions-legales.html", "confidentialite.html", "cgv.html")]
    body = "\n".join(
        f"  <url>\n    <loc>{SITE}/{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>{c}</changefreq>\n    <priority>{pr}</priority>\n  </url>"
        for u, pr, c in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n'


def build_llms():
    lines = [
        "# Cohesif Auto",
        "",
        "> Cohesif Auto (cohesifauto.fr) est un mandataire et chasseur automobile du Groupe Cohesif, basé à Paris (75015). "
        "Il recherche, contrôle, achète et livre des véhicules neufs et d'occasion trouvés en France ou importés d'Europe (Allemagne, Belgique, Italie, Espagne, Pays-Bas), "
        "gère la carte grise, équipe les entreprises (LLD, LOA, achat, utilitaires) et recherche des pièces de collection. Propositions chiffrées gratuites sous 48 h, livraison partout en France.",
        "",
        f"Contact : +33 7 56 85 57 27 (téléphone et WhatsApp) · {EMAIL} · 200 rue de la Croix-Nivert, 75015 Paris. Financement via Cohesif Leasing.",
        "",
        "## Services",
    ]
    lines += [f"- [{p['card_title']}]({SITE}/{p['slug']}) : {p['card_text']}" for p in SERVICES]
    lines += ["", "## Guides"]
    lines += [f"- [{p['card_title']}]({SITE}/{p['slug']}) : {p['card_text']}" for p in GUIDES]
    return "\n".join(lines) + "\n"


def french_spacing(page):
    """Espace insécable avant ? ! : ; dans le texte visible (typographie française)."""
    head_part, sep, body_part = page.partition("<body>")

    def fix(m):
        return ">" + re.sub(r" ([?!:;»])", "\u00a0\\1", re.sub(r"« ", "«\u00a0", m.group(1))) + "<"

    return head_part + sep + re.sub(r">([^<]+)<", fix, body_part)


def write(name, content):
    if name.endswith(".html"):
        content = french_spacing(content)
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("écrit", name)


if __name__ == "__main__":
    for p in PAGES:
        write(p["slug"], build_page(p))
    write("guides.html", build_hub())
    write("404.html", build_404())
    write("sitemap.xml", build_sitemap())
    write("llms.txt", build_llms())
