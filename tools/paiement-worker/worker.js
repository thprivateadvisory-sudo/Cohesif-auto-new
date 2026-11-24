// Cohesif Auto : paiement du forfait de recherche, directement sur le site.
// Cloudflare Worker (gratuit). Le formulaire est celui du site (logo, couleurs) ;
// ce programme crée le paiement avec la clé Stripe, qui ne quitte jamais Cloudflare.
//
// Variables à définir dans Cloudflare (Settings > Variables and Secrets) :
//   STRIPE_SECRET_KEY       (secret)  clé restreinte Stripe rk_live_ (permission PaymentIntents : écriture)
//   STRIPE_PUBLISHABLE_KEY  (texte)   clé publiable Stripe pk_live_

const OFFRES = {
  france:   { montant: 9900,  nom: 'Recherche en France' },
  europe:   { montant: 14900, nom: 'Recherche et import Europe' },
  prestige: { montant: 24900, nom: 'Recherche prestige et collection' },
};
const ORIGINES = ['https://cohesifauto.fr', 'https://www.cohesifauto.fr'];

function cors(origin) {
  return {
    'Access-Control-Allow-Origin': ORIGINES.includes(origin) ? origin : ORIGINES[0],
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Vary': 'Origin',
  };
}
function json(data, status, origin) {
  return new Response(JSON.stringify(data), {
    status: status || 200,
    headers: Object.assign({ 'Content-Type': 'application/json' }, cors(origin)),
  });
}
function texte(v, max) { return String(v || '').replace(/\s+/g, ' ').trim().slice(0, max); }

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const origin = request.headers.get('Origin') || '';
    if (request.method === 'OPTIONS') return new Response(null, { headers: cors(origin) });

    if (request.method === 'GET' && url.pathname === '/config') {
      return json({ publishableKey: env.STRIPE_PUBLISHABLE_KEY }, 200, origin);
    }

    if (request.method === 'POST' && url.pathname === '/paiement') {
      if (origin && !ORIGINES.includes(origin)) return json({ error: 'Origine refusée' }, 403, origin);
      let input = {};
      try { input = await request.json(); } catch (e) {}
      const offre = OFFRES[input.offre];
      if (!offre) return json({ error: 'Offre inconnue' }, 400, origin);
      if (input.consentement !== true) return json({ error: 'Consentement requis' }, 400, origin);
      const nom = texte(input.nom, 120);
      const email = texte(input.email, 200);
      const tel = texte(input.telephone, 40);
      if (!nom || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) || tel.replace(/\D/g, '').length < 9) {
        return json({ error: 'Coordonnées incomplètes' }, 400, origin);
      }

      const params = new URLSearchParams({
        amount: String(offre.montant),
        currency: 'eur',
        'payment_method_types[]': 'card',
        description: 'Cohesif Auto – ' + offre.nom,
        receipt_email: email,
        statement_descriptor_suffix: 'COHESIF AUTO',
        'metadata[offre]': input.offre,
        'metadata[nom]': nom,
        'metadata[email]': email,
        'metadata[telephone]': tel,
        'metadata[recherche]': texte(input.recherche, 480),
        'metadata[consentement_execution_immediate]': 'oui',
        'metadata[consentement_cgv]': 'oui',
        'metadata[consentement_horodatage]': new Date().toISOString(),
      });
      const res = await fetch('https://api.stripe.com/v1/payment_intents', {
        method: 'POST',
        headers: { Authorization: 'Bearer ' + env.STRIPE_SECRET_KEY, 'Content-Type': 'application/x-www-form-urlencoded' },
        body: params.toString(),
      });
      const data = await res.json();
      if (!res.ok) return json({ error: 'Paiement indisponible' }, 502, origin);
      return json({ clientSecret: data.client_secret }, 200, origin);
    }

    return json({ error: 'Introuvable' }, 404, origin);
  },
};
