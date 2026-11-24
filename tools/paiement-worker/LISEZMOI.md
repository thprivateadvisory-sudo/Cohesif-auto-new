# Paiement en ligne : mise en service

Le client paie son forfait de recherche **sans quitter cohesifauto.fr** :
le formulaire de paiement Cohesif Auto s’affiche dans une fenêtre du site (carte, Apple Pay, Google Pay), sans aucune page Stripe.

Le site est hébergé sur GitHub Pages, qui ne fait qu'afficher des pages. Il faut donc un petit
programme (`worker.js`) qui prépare chaque paiement avec la clé Stripe secrète.
Il tourne gratuitement sur Cloudflare Workers. Une seule mise en place, environ 10 minutes.

## 1. Stripe : récupérer les clés

Tableau de bord Stripe > **Développeurs** > **Clés API** :

- copier la **clé publiable** (`pk_live_…`) ;
- créer une **clé restreinte** nommée « Site Cohesif Auto », avec uniquement la permission
  **PaymentIntents : écriture**, et la copier (`rk_live_…`).

Ne jamais mettre la clé secrète ou restreinte dans le site ni l'envoyer par message.

## 2. Cloudflare : créer le Worker

1. Créer un compte gratuit sur dash.cloudflare.com.
2. **Workers & Pages** > **Créer** > **Worker**, le nommer `cohesif-paiement`, puis **Déployer**.
3. **Modifier le code**, remplacer tout par le contenu de `worker.js`, puis **Déployer**.
4. **Paramètres** > **Variables et secrets** :
   - `STRIPE_SECRET_KEY`, type **Secret** : la clé restreinte `rk_live_…`
   - `STRIPE_PUBLISHABLE_KEY`, type **Texte** : la clé `pk_live_…`
5. Copier l'adresse du Worker, par exemple `https://cohesif-paiement.votre-compte.workers.dev`.

## 3. Brancher le site

Dans `paiement.js`, mettre cette adresse dans `PAIEMENT_URL` (sans `/` à la fin), puis publier.
Tant que `PAIEMENT_URL` est vide, les boutons « Lancer ma recherche » mènent au formulaire de contact.

## 4. Réglages Stripe conseillés

- **Paramètres** > **E-mails clients** : activer l'envoi du reçu pour les paiements réussis.
- **Paramètres** > **Informations publiques** : vérifier le nom affiché et le libellé sur le relevé bancaire.
  Le site ajoute déjà « COHESIF AUTO » au libellé des paiements par carte.

## Lien à envoyer à un client

Après un appel, envoyer directement le lien qui ouvre le paiement sur le site :

- France : `https://cohesifauto.fr/#payer-france`
- Europe : `https://cohesifauto.fr/#payer-europe`
- Prestige : `https://cohesifauto.fr/#payer-prestige`

## Où voir les paiements

Tableau de bord Stripe > **Paiements**. Chaque paiement indique l'offre, le téléphone, la recherche
décrite par le client et la date du consentement (démarrage immédiat et CGV), utile en cas de litige.

Produits Stripe : `prod_VgeqAd9VmkDSwB` (99 €), `prod_VgeqGlCCgOuskj` (149 €), `prod_Vgeqa3cFfJblUp` (249 €).
