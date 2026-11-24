// Cohesif Auto : création des paiements Stripe intégrés au site.
// Cloudflare Worker (gratuit). Le site ne quitte jamais cohesifauto.fr :
// ce programme prépare la session de paiement, Stripe l'affiche dans le site.
//
// Variables à définir dans Cloudflare (Settings > Variables and Secrets) :
//   STRIPE_SECRET_KEY       (secret)  clé secrète Stripe, commence par sk_live_
//   STRIPE_PUBLISHABLE_KEY  (texte)   clé publiable Stripe, commence par pk_live_

const OFFRES = {
  france:   { price: 'price_1UfHWyRmrarRZT7e29c6IfOf', nom: 'Recherche en France' },
  europe:   { price: 'price_1UfHX5RmrarRZT7e1eqAYSLK', nom: 'Recherche et import Europe' },
  prestige: { price: 'price_1UfHX8RmrarRZT7eNXuVNdu0', nom: 'Recherche prestige et collection' },
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

async function stripe(env, method, path, params) {
  const body = params ? new URLSearchParams(params).toString() : undefined;
  const res = await fetch('https://api.stripe.com/v1/' + path, {
    method,
    headers: {
      Authorization: 'Bearer ' + env.STRIPE_SECRET_KEY,
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body,
  });
  return { ok: res.ok, data: await res.json() };
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const origin = request.headers.get('Origin') || '';

    if (request.method === 'OPTIONS') return new Response(null, { headers: cors(origin) });

    // Création d'une session de paiement
    if (request.method === 'POST' && url.pathname === '/session') {
      if (origin && !ORIGINES.includes(origin)) return json({ error: 'Origine refusée' }, 403, origin);
      let input = {};
      try { input = await request.json(); } catch (e) { /* corps vide */ }
      const offre = OFFRES[input.offre];
      if (!offre) return json({ error: 'Offre inconnue' }, 400, origin);
      if (input.consentement !== true) return json({ error: 'Consentement requis' }, 400, origin);

      const maintenant = new Date().toISOString();
      const params = {
        mode: 'payment',
        'line_items[0][price]': offre.price,
        'line_items[0][quantity]': '1',
        locale: 'fr',
        redirect_on_completion: 'if_required',
        return_url: 'https://cohesifauto.fr/?paiement={CHECKOUT_SESSION_ID}#tarifs',
        customer_creation: 'always',
        'phone_number_collection[enabled]': 'true',
        'custom_fields[0][key]': 'recherche',
        'custom_fields[0][label][type]': 'custom',
        'custom_fields[0][label][custom]': 'Votre recherche (modèle, budget, délai)',
        'custom_fields[0][type]': 'text',
        'custom_fields[0][optional]': 'true',
        'custom_text[submit][message]': 'Paiement sécurisé par Stripe. Ce forfait est déduit de nos honoraires si vous achetez un véhicule par notre intermédiaire.',
        'payment_intent_data[description]': 'Cohesif Auto – ' + offre.nom,
        'payment_intent_data[statement_descriptor_suffix]': 'COHESIF AUTO',
        'payment_intent_data[metadata][offre]': input.offre,
        'metadata[offre]': input.offre,
        'metadata[consentement_execution_immediate]': 'oui',
        'metadata[consentement_cgv]': 'oui',
        'metadata[consentement_horodatage]': maintenant,
      };

      // Selon la version d'API du compte, le mode intégré s'appelle "embedded_page" ou "embedded".
      let r = await stripe(env, 'POST', 'checkout/sessions', Object.assign({ ui_mode: 'embedded_page' }, params));
      if (!r.ok && r.data && r.data.error && /ui_mode|redirect_on_completion/.test(r.data.error.message || '')) {
        r = await stripe(env, 'POST', 'checkout/sessions', Object.assign({ ui_mode: 'embedded' }, params));
      }
      if (!r.ok) return json({ error: 'Paiement indisponible' }, 502, origin);
      return json({ clientSecret: r.data.client_secret, publishableKey: env.STRIPE_PUBLISHABLE_KEY }, 200, origin);
    }

    // Vérification après un paiement avec redirection (PayPal, Klarna…)
    if (request.method === 'GET' && url.pathname === '/statut') {
      const id = url.searchParams.get('session_id') || '';
      if (!/^cs_(live|test)_[A-Za-z0-9]+$/.test(id)) return json({ error: 'Session invalide' }, 400, origin);
      const r = await stripe(env, 'GET', 'checkout/sessions/' + id);
      if (!r.ok) return json({ error: 'Introuvable' }, 404, origin);
      return json({ statut: r.data.payment_status, offre: (r.data.metadata || {}).offre || '' }, 200, origin);
    }

    return json({ error: 'Introuvable' }, 404, origin);
  },
};
