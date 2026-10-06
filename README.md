# Cohesif Auto

Site web officiel de **Cohesif Auto**, pôle Mobilité, Transport & Logistique Intégrée du Groupe Cohesif.

🌐 **Production** : [cohesifauto.fr](https://cohesifauto.fr) *(à déployer)*

---

## Présentation

Cohesif Auto centralise l'ensemble de la chaîne automobile pour ses clients particuliers et professionnels :

- **Vente** de véhicules classiques et de prestige
- **Import** depuis l'étranger (Allemagne, Italie, États-Unis, Japon)
- **Solutions particuliers** : conseil et accompagnement
- **Flottes professionnelles** : LLD, courte/moyenne durée, vente
- **Atelier collection** : pièces auto rares et vintage

---

## Stack technique

- **HTML5** sémantique
- **CSS3** moderne (variables, grid, flexbox, animations)
- **JavaScript vanilla** (pas de framework, ultra-léger)
- **SVG** vectoriels pour les visuels (performances optimales)
- **Inter** comme police principale (Google Fonts)

Aucune dépendance, aucun build step. Site 100% statique.

---

## Structure du projet

```
cohesifauto/
├── index.html                  # Page d'accueil (Flottes & véhicules)
├── assets/
│   ├── css/
│   │   ├── styles.css          # Styles principaux
│   │   └── legal.css           # Styles des pages légales
│   ├── js/
│   │   └── main.js             # Interactions (toggle, formulaire, sticky CTA)
│   └── images/
│       ├── logo-cohesif-auto.png
│       ├── hero.svg            # Visuel hero
│       ├── classique.svg       # Visuel univers Vente classique
│       ├── prestige.svg        # Visuel univers Vente prestige
│       ├── import.svg          # Visuel univers Import
│       └── vintage.svg         # Visuel atelier collection
├── legal/
│   ├── mentions-legales.html
│   ├── confidentialite.html
│   └── cgv.html
└── README.md
```

---

## Démarrer en local

Aucune dépendance à installer. Il suffit d'ouvrir `index.html` dans un navigateur, ou de servir le dossier avec un serveur local :

### Option 1 — Python
```bash
python3 -m http.server 8000
```
Puis ouvrir http://localhost:8000

### Option 2 — Node.js
```bash
npx serve .
```

### Option 3 — VSCode
Installer l'extension **Live Server** et faire clic droit sur `index.html` → "Open with Live Server".

---

## Déploiement

### Vercel (recommandé, gratuit)

1. Push ce repo sur GitHub
2. Aller sur [vercel.com](https://vercel.com) et "Import Project"
3. Connecter le repo
4. Deploy → c'est en ligne en 30 secondes

Le fichier `vercel.json` est déjà configuré pour gérer les redirections.

### Netlify

Drag & drop le dossier sur [app.netlify.com/drop](https://app.netlify.com/drop) — fonctionne instantanément.

### OVH / hébergement classique

Uploader tout le contenu du dossier à la racine du domaine via FTP. Le site fonctionnera immédiatement.

---

## Fonctionnalités

Page d'accueil pensée pour la conversion (refonte octobre 2026) :

- **Hero avec formulaire en 3 étapes** (projet → véhicule/budget → coordonnées), adapté au type de projet
- **Barre de réassurance** : contrôle du véhicule, démarches, livraison, prix annoncé à l'avance
- **Services** : achat accompagné, prestige, flottes entreprise, pièces de collection
- **Comparatif** annonces / concession / Cohesif Auto
- **Méthode en 4 étapes** et **focus import Europe**
- **Simulateur de financement** Cohesif Leasing + demande en modal
- **Bloc Groupe Cohesif** (SIRET, adresse, pôles) et **FAQ** (balisage schema.org FAQPage)
- **Contact** : téléphone, WhatsApp, email + formulaire
- **Barre de contact mobile** (Appeler / WhatsApp / Propositions)
- Tous les formulaires envoient vers Formspree (`main.js`, constante `FORM_ENDPOINT`)
- Événements de mesure (`generate_lead`, `cta_click`, `lead_step`) envoyés automatiquement à GA4 / GTM / Plausible dès qu'un de ces outils est installé

## Pages services et guides (référencement)

Les pages services, les guides, la page `guides.html`, la `404.html`, `sitemap.xml` et `llms.txt` sont **générés** :

- contenu : `tools/pages_contenu.py` (un dictionnaire par page : titre, description, H1, corps, FAQ, pages liées)
- gabarit : `tools/build_pages.py` (en-tête, pied de page, formulaire, fil d'Ariane, données structurées schema.org)

Pour ajouter ou modifier une page, éditer `tools/pages_contenu.py` puis lancer :

```bash
python3 tools/build_pages.py
```

Ne pas modifier les pages générées à la main : elles seraient écrasées au prochain lancement. `index.html` reste écrit à la main.

Règles de référencement appliquées : un seul H1 par page, titre ≤ 65 caractères, description ≤ 160 caractères, URL canonique, Open Graph, fil d'Ariane, données structurées (AutoDealer, Service, Article, FAQPage, BreadcrumbList), maillage interne entre services et guides.

## Personnalisation rapide

### Modifier les coordonnées

Les coordonnées sont à 4 endroits dans `index.html` :
- Header CTA (mobile)
- Section CTA finale (formulaire)
- Sticky CTA mobile
- Footer

Faire un **Find & Replace** :
- `cohesifauto@gmail.com` → nouvel email
- `33756855727` (liens `wa.me` et `tel:+33…`) → nouveau numéro
- `0756855727` (lien `tel:`) → nouveau numéro
- `07 56 85 57 27` (affichage) → nouveau numéro

### Modifier la palette de couleurs

Dans `styles.css`, bloc `:root` : `--blue-600` (accent / boutons), `--ink-900` et `--ink-950` (texte et sections sombres).

### Modifier les informations légales

Quand le passage en société sera effectif, modifier dans les 3 fichiers `legal/*.html` :
- Raison sociale
- Numéro SIRET
- Forme juridique
- Capital social
- Directeur de publication
- Supprimer les blocs "Évolution prévue"

---

## Roadmap

- [ ] Ajouter une vraie photo hero (remplacer le SVG abstrait)
- [ ] Page dédiée "Espace défense" (cohesif-defense.fr en projet)
- [ ] Connecter le formulaire à un backend (actuellement ouvre le client mail)
- [ ] Ajouter Google Analytics / Plausible
- [ ] Optimisation SEO avancée (schema.org, sitemap.xml, robots.txt)
- [ ] Mise à jour après le passage en société

---

## Groupe Cohesif

Cohesif Auto fait partie du **Groupe Cohesif**, qui réunit 5 pôles synergiques :

- [Cohesif BTP](https://cohesifbtp.fr) — Construire, piloter, livrer
- [Cohesif Access](https://cohesifaccess.fr) — Connect, collaborate, grow
- [Cohesif Commerce](https://cohesifcommerce.fr) — De l'idée à l'exécution
- **Cohesif Auto** — Mobilité, transport, logistique *(ce site)*
- Cohesif Energy — *(à venir)*

---

## Contact

📧 cohesifauto@gmail.com
📞 07 56 85 57 27

**Groupe Cohesif**
SIRET : 889 287 462 00036
200 rue de la Croix-Nivert, 75015 Paris

---

© 2026 Cohesif Auto · Groupe Cohesif. Tous droits réservés.
