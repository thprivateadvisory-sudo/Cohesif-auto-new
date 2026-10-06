"""Contenu des pages services et guides de cohesifauto.fr.

Chaque page est un dictionnaire ; le gabarit est dans build_pages.py.
Règle éditoriale : aucune statistique, aucun avis ni aucun montant réglementaire
qu'on ne peut pas prouver. Les barèmes (malus, taxe régionale) changent chaque
année : on explique le mécanisme et on renvoie vers le chiffrage personnalisé.
"""


def cta(text, label="Recevoir mes propositions"):
    return f"""<div class="inline-cta"><p>{text}</p><a href="#contact" class="btn btn-primary" data-track="inline_cta">{label} <svg><use href="#i-arrow"/></svg></a></div>"""


def included(items):
    lis = "".join(
        f'<li><span class="ico"><svg><use href="#i-{i}"/></svg></span><div><b>{t}</b><span>{d}</span></div></li>'
        for i, t, d in items)
    return f'<ul class="included">{lis}</ul>'


IMG_CLIO = ("img/achat-clio.webp", "Renault Clio préparée et livrée par Cohesif Auto", 900, 600)
IMG_URUS = ("img/prestige-urus.webp", "Lamborghini Urus devant l'atelier Cohesif Auto", 900, 606)
IMG_IMPORT = ("https://images.pexels.com/photos/31390896/pexels-photo-31390896.jpeg?auto=compress&cs=tinysrgb&w=1200", "Voitures sur une autoroute allemande au coucher du soleil", 1200, 900)

PROCESS = """<ol class="num">
<li><strong>Brief de 15 minutes</strong> : modèle, budget, usage, kilométrage, options indispensables et délai.</li>
<li><strong>Propositions sous 48h</strong> : 2 à 5 véhicules sélectionnés, avec le prix total livré et immatriculé.</li>
<li><strong>Contrôle et achat</strong> : on vérifie le véhicule choisi, on négocie, on sécurise le paiement et les documents.</li>
<li><strong>Livraison</strong> : carte grise faite, véhicule livré chez vous ou au lieu de votre choix.</li>
</ol>"""

PAGES = [
    # ================================================================ SERVICES
    {
        "slug": "chasseur-automobile.html",
        "kind": "service",
        "menu": "Chasseur automobile",
        "crumb": "Chasseur automobile",
        "card_title": "Chasseur automobile",
        "card_text": "On cherche, on vérifie, on négocie et on livre la voiture qu'il vous faut.",
        "service_type": "Chasseur automobile / mandataire auto",
        "title": "Chasseur automobile : on trouve votre voiture | Cohesif Auto",
        "description": "Chasseur et mandataire auto : recherche en France et en Europe, contrôle, négociation, carte grise et livraison. Propositions gratuites sous 48h.",
        "eyebrow": "Chasseur automobile",
        "h1": "Un chasseur automobile qui trouve, vérifie et négocie pour vous",
        "lead": "Vous nous décrivez la voiture idéale et votre budget. On parcourt le marché français et européen, on écarte les mauvaises affaires et on vous présente uniquement des véhicules contrôlés, au prix total annoncé.",
        "image": IMG_CLIO,
        "projet": "Acheter un véhicule",
        "body": f"""
<h2>Qu'est-ce qu'un chasseur automobile ?</h2>
<p>Un chasseur automobile (ou chasseur de voitures) est un professionnel qui recherche un véhicule <strong>pour le compte de l'acheteur</strong>. Contrairement à un vendeur en concession, il ne cherche pas à écouler un stock : il travaille pour vous, avec un seul objectif, trouver le bon véhicule au bon prix.</p>
<p>Chez Cohesif Auto, ce rôle va jusqu'au bout : recherche, contrôle, négociation, paiement sécurisé, démarches d'immatriculation et livraison. Vous ne faites que choisir.</p>

<h2>Ce que nous faisons à votre place</h2>
{included([
    ("search", "Recherche ciblée", "Annonces de professionnels et de particuliers, en France et en Europe"),
    ("shield", "Contrôle du véhicule", "État, historique d'entretien, kilométrage, avant tout engagement"),
    ("euro", "Négociation", "On négocie le prix et les conditions pour vous"),
    ("doc", "Démarches", "Contrat, paiement sécurisé, carte grise"),
    ("truck", "Livraison", "Chez vous ou au lieu de votre choix, partout en France"),
    ("user", "Un seul interlocuteur", "Joignable par téléphone et WhatsApp du début à la fin"),
])}

<h2>Pourquoi passer par un chasseur plutôt qu'acheter seul ?</h2>
<p>Acheter une voiture d'occasion seul, c'est des soirées sur les annonces, des déplacements pour rien et le risque de tomber sur un compteur trafiqué ou un véhicule mal entretenu. Un chasseur vous fait gagner :</p>
<ul>
<li><strong>Du choix</strong> : en élargissant la recherche à l'Europe, on accède à beaucoup plus de véhicules, notamment en Allemagne pour les modèles premium bien équipés.</li>
<li><strong>De la sécurité</strong> : chaque véhicule est contrôlé avant achat et l'historique est vérifié.</li>
<li><strong>Du temps</strong> : un appel de 15 minutes remplace des semaines de recherche.</li>
<li><strong>De la transparence</strong> : vous recevez un devis écrit avec le prix total, honoraires, transport et immatriculation compris, avant de vous engager.</li>
</ul>
{cta("<strong>Un modèle en tête ?</strong> Recevez 2 à 5 véhicules sélectionnés et chiffrés sous 48h.")}

<h2>Comment ça se passe</h2>
{PROCESS}

<h2>Neuf, occasion récente ou véhicule de collection</h2>
<p>Nous recherchons tous types de véhicules : citadines, familiales, SUV, utilitaires, hybrides et électriques, véhicules de <a href="voiture-prestige.html">prestige</a> et youngtimers. Pour les professionnels, nous pouvons constituer une <a href="vehicules-entreprise-lld.html">flotte complète</a> en LLD ou à l'achat.</p>
<p>Si le véhicule idéal se trouve à l'étranger, nous gérons l'<a href="import-voiture-allemagne.html">import depuis l'Allemagne</a> ou depuis un <a href="import-voiture-europe.html">autre pays européen</a>, démarches comprises.</p>
""",
        "faq": [
            ("Combien coûte un chasseur automobile ?", "Le brief et les propositions sont gratuits. Nos honoraires dépendent du véhicule et du service ; ils figurent dans le devis écrit que vous recevez avant de vous engager, avec le prix total du véhicule livré."),
            ("Quelle différence entre un chasseur automobile et un mandataire auto ?", "Le mandataire achète des véhicules (souvent neufs) auprès de concessionnaires européens pour les revendre ; le chasseur recherche un véhicule précis pour le compte de son client. Cohesif Auto combine les deux : recherche sur mesure et achat accompagné, en France comme à l'étranger."),
            ("En combien de temps trouvez-vous un véhicule ?", "Vous recevez des propositions sous 48h ouvrées. La livraison intervient généralement en 1 à 3 semaines pour un véhicule trouvé en France et en 4 à 8 semaines pour un import."),
            ("Puis-je refuser les propositions ?", "Oui. Les propositions sont gratuites et sans engagement : vous ne vous engagez qu'au moment où vous choisissez un véhicule, sur la base d'un devis écrit."),
            ("Reprenez-vous mon ancien véhicule ?", "Oui, la reprise est possible. Indiquez-le dans votre demande : nous l'estimons et la déduisons du prix final."),
        ],
        "related": ["import-voiture-allemagne.html", "guide-acheter-voiture-occasion-sans-arnaque.html", "financement-voiture.html"],
    },
    {
        "slug": "import-voiture-allemagne.html",
        "kind": "service",
        "menu": "Import voiture Allemagne",
        "crumb": "Import voiture Allemagne",
        "card_title": "Import de voiture d'Allemagne",
        "card_text": "Recherche, contrôle sur place, transport et carte grise française : clé en main.",
        "service_type": "Import de véhicules depuis l'Allemagne",
        "title": "Import voiture Allemagne clé en main | Cohesif Auto",
        "description": "Importez une voiture d'Allemagne sans démarches : recherche, contrôle sur place, transport, COC, quitus fiscal et carte grise française. Devis sous 48h.",
        "eyebrow": "Import Allemagne",
        "h1": "Import de voiture d'Allemagne, livrée et immatriculée en France",
        "lead": "Le plus grand marché automobile d'Europe, sans la barrière de la langue ni la paperasse. On trouve le véhicule, on le fait contrôler sur place, on le rapatrie et on vous le livre avec sa carte grise française.",
        "image": IMG_IMPORT,
        "projet": "Importer d'Europe",
        "cta": "Chiffrer mon import",
        "body": f"""
<h2>Pourquoi acheter sa voiture en Allemagne ?</h2>
<p>L'Allemagne est le premier marché automobile d'Europe. Pour un acheteur français, cela se traduit par trois avantages concrets :</p>
<ul>
<li><strong>Beaucoup plus de choix</strong>, en particulier sur les marques allemandes (Audi, BMW, Mercedes-Benz, Porsche, Volkswagen) et les versions bien équipées.</li>
<li><strong>Des véhicules souvent mieux suivis</strong>, avec carnet d'entretien (Scheckheft) et contrôles techniques réguliers (HU/TÜV).</li>
<li><strong>Des prix souvent plus intéressants</strong> sur le haut de gamme et les sportives, même une fois le transport et l'immatriculation payés. On fait le calcul complet pour vous avant d'acheter.</li>
</ul>

<h2>Notre service d'import clé en main</h2>
{included([
    ("search", "Recherche en allemand", "mobile.de, AutoScout24 et réseau de vendeurs professionnels"),
    ("shield", "Contrôle sur place", "Inspection, photos et vérification des documents avant achat"),
    ("euro", "Négociation et paiement", "Contrat de vente et paiement sécurisés"),
    ("truck", "Rapatriement", "Transport par camion ou convoyage, assuré"),
    ("doc", "Formalités françaises", "Certificat de conformité, quitus fiscal, contrôle technique si besoin"),
    ("check", "Carte grise française", "Demande d'immatriculation et pose des plaques"),
])}
{cta("<strong>Vous avez repéré une annonce ?</strong> Envoyez-la-nous : on vérifie le véhicule et on chiffre l'import complet.", "Chiffrer mon import")}

<h2>Les étapes d'un import réussi</h2>
<ol class="num">
<li><strong>Recherche et sélection</strong> des annonces correspondant à votre cahier des charges.</li>
<li><strong>Vérification</strong> du véhicule, de son historique et de ses documents allemands (Zulassungsbescheinigung Teil I et Teil II, carnet d'entretien).</li>
<li><strong>Achat</strong> : négociation, contrat et paiement sécurisé.</li>
<li><strong>Transport</strong> jusqu'en France.</li>
<li><strong>Immatriculation</strong> : certificat de conformité européen, quitus fiscal, contrôle technique français si le véhicule a plus de 4 ans, puis demande de carte grise.</li>
<li><strong>Livraison</strong> chez vous.</li>
</ol>
<p>Le détail de chaque étape est expliqué dans notre <a href="guide-importer-voiture-allemagne.html">guide complet de l'import d'une voiture d'Allemagne</a>.</p>

<h2>Combien coûte un import d'Allemagne ?</h2>
<p>Le prix final se compose du prix du véhicule, du transport, du coût de la carte grise (dont la taxe régionale et l'éventuel malus) et de nos honoraires. Pour un véhicule considéré comme neuf fiscalement (moins de 6 mois ou moins de 6 000 km), la TVA est due en France.</p>
<p>Nous vous remettons un <strong>chiffrage complet avant l'achat</strong>, pour comparer avec le même modèle en France en toute transparence. Pour comprendre les taxes, lisez notre <a href="guide-malus-tva-voiture-importee.html">guide sur la TVA et le malus d'une voiture importée</a>.</p>
""",
        "faq": [
            ("Combien de temps faut-il pour importer une voiture d'Allemagne ?", "Comptez en général 4 à 8 semaines entre l'achat et la livraison avec la carte grise française, selon le délai de transport et d'immatriculation."),
            ("Est-ce vraiment moins cher d'acheter en Allemagne ?", "Souvent sur les modèles premium, les sportives et les versions bien équipées, mais pas systématiquement. C'est pour ça que nous chiffrons le coût total (transport, carte grise, malus) avant l'achat, pour vous permettre de comparer."),
            ("Faut-il payer la TVA en France ?", "Seulement si le véhicule est considéré comme neuf fiscalement : moins de 6 mois depuis sa première mise en circulation ou moins de 6 000 km. Dans ce cas, il est acheté hors taxes en Allemagne et la TVA française est payée lors de la demande de quitus fiscal."),
            ("Le malus s'applique-t-il à une voiture importée d'occasion ?", "Oui, le malus écologique s'applique à la première immatriculation en France, avec une réduction selon l'ancienneté du véhicule. Nous l'intégrons dans le chiffrage avant l'achat."),
            ("La garantie constructeur est-elle valable en France ?", "La garantie constructeur des grandes marques est généralement européenne : un véhicule encore couvert peut être entretenu dans le réseau de la marque en France. Nous vérifions la couverture exacte pour chaque véhicule."),
        ],
        "related": ["guide-importer-voiture-allemagne.html", "guide-carte-grise-vehicule-importe.html", "import-voiture-europe.html"],
    },
    {
        "slug": "import-voiture-europe.html",
        "kind": "service",
        "menu": "Import voiture Europe",
        "crumb": "Import voiture Europe",
        "card_title": "Import de voiture d'Europe",
        "card_text": "Belgique, Italie, Espagne, Pays-Bas, Luxembourg : le bon véhicule, où qu'il soit.",
        "service_type": "Import de véhicules depuis l'Union européenne",
        "title": "Import voiture Europe : Belgique, Italie, Espagne | Cohesif Auto",
        "description": "Import de voiture depuis la Belgique, l'Italie, l'Espagne, les Pays-Bas ou le Luxembourg : recherche, contrôle, transport et carte grise française.",
        "eyebrow": "Import Europe",
        "h1": "Import de voiture depuis toute l'Europe, démarches comprises",
        "lead": "Le véhicule que vous cherchez n'existe pas en France, ou pas à ce prix ? On le cherche dans toute l'Union européenne et on vous le livre immatriculé.",
        "image": IMG_IMPORT,
        "projet": "Importer d'Europe",
        "cta": "Chiffrer mon import",
        "body": f"""
<h2>Où chercher ? Les marchés que nous couvrons</h2>
<table>
<thead><tr><th>Pays</th><th>Points forts</th></tr></thead>
<tbody>
<tr><td><strong>Allemagne</strong></td><td>Le plus grand marché d'Europe, marques premium, véhicules bien équipés. <a href="import-voiture-allemagne.html">Voir notre page dédiée</a>.</td></tr>
<tr><td><strong>Belgique</strong></td><td>Proximité, documents en français, beaucoup de véhicules de société récents.</td></tr>
<tr><td><strong>Pays-Bas</strong></td><td>Large offre de véhicules électriques et hybrides récents.</td></tr>
<tr><td><strong>Italie</strong></td><td>Sportives et marques italiennes, youngtimers et véhicules de collection.</td></tr>
<tr><td><strong>Espagne</strong></td><td>Véhicules récents et configurations parfois introuvables en France.</td></tr>
<tr><td><strong>Luxembourg</strong></td><td>Véhicules haut de gamme récents, souvent bien entretenus.</td></tr>
</tbody>
</table>
<p>Nous recherchons aussi au-delà sur demande, notamment pour les véhicules de collection.</p>

<h2>Le même service, quel que soit le pays</h2>
{included([
    ("search", "Recherche multilingue", "Annonces professionnelles et particulières"),
    ("shield", "Contrôle avant achat", "État, historique, documents"),
    ("truck", "Transport assuré", "Jusqu'à votre domicile"),
    ("doc", "Immatriculation française", "COC, quitus fiscal, carte grise"),
])}
{cta("<strong>Dites-nous ce que vous cherchez</strong> : on compare les marchés et on vous propose les meilleures options.")}

<h2>Les formalités d'un import intra-européen</h2>
<p>À l'intérieur de l'Union européenne, il n'y a pas de droits de douane à payer sur un véhicule. Les démarches restent cependant précises :</p>
<ul>
<li>un <strong>certificat de conformité européen</strong> (COC) délivré par le constructeur ;</li>
<li>un <strong>quitus fiscal</strong> obtenu auprès du service des impôts, qui atteste que la TVA est réglée ;</li>
<li>un <strong>contrôle technique</strong> de moins de 6 mois si le véhicule a plus de 4 ans ;</li>
<li>la <strong>demande de certificat d'immatriculation</strong> française.</li>
</ul>
<p>Nous nous en occupons de bout en bout. Pour tout comprendre, consultez notre <a href="guide-carte-grise-vehicule-importe.html">guide de la carte grise d'un véhicule importé</a>.</p>
""",
        "faq": [
            ("Y a-t-il des droits de douane sur une voiture achetée dans l'Union européenne ?", "Non. Entre pays de l'Union européenne, il n'y a pas de droits de douane. Seules la TVA (pour un véhicule neuf fiscalement) et les taxes d'immatriculation françaises s'appliquent."),
            ("Pouvez-vous importer depuis un pays hors Union européenne ?", "Sur demande, notamment pour des véhicules de collection. Les formalités sont alors différentes (dédouanement, homologation) : nous étudions chaque cas avant de vous faire une proposition."),
            ("Quel est le délai pour un import européen ?", "En général 4 à 8 semaines entre l'achat et la livraison avec carte grise française, selon le pays et le véhicule."),
        ],
        "related": ["import-voiture-allemagne.html", "guide-carte-grise-vehicule-importe.html", "guide-malus-tva-voiture-importee.html"],
    },
    {
        "slug": "voiture-prestige.html",
        "kind": "service",
        "menu": "Voitures de prestige",
        "crumb": "Voitures de prestige",
        "card_title": "Voitures de prestige et sportives",
        "card_text": "La configuration exacte que vous voulez, contrôlée et livrée en toute discrétion.",
        "service_type": "Recherche de véhicules de prestige",
        "title": "Voiture de prestige et sportive sur mesure | Cohesif Auto",
        "description": "Porsche, AMG, BMW M, Audi RS, Lamborghini : recherche sur mesure en France et en Europe, contrôle complet, livraison fermée. Propositions sous 48h.",
        "eyebrow": "Prestige & sportives",
        "h1": "Voitures de prestige et sportives, trouvées sur mesure",
        "lead": "Couleur, options, historique : sur un véhicule d'exception, chaque détail compte. On cherche la configuration exacte que vous voulez, en France et en Europe, et on la contrôle avant tout engagement.",
        "image": IMG_URUS,
        "projet": "Acheter un véhicule",
        "cta": "Trouver mon véhicule",
        "body": f"""
<h2>Un service pensé pour les véhicules d'exception</h2>
<p>Sur une sportive ou un SUV haut de gamme, l'écart entre une bonne et une mauvaise affaire se joue sur l'historique, l'entretien et la configuration. Le marché français étant étroit sur ces modèles, nous recherchons aussi en Allemagne, en Belgique, en Italie et au Luxembourg.</p>
{included([
    ("search", "Configuration précise", "Couleur, intérieur, options, pack, année"),
    ("shield", "Contrôle complet", "Historique, entretien constructeur, état"),
    ("doc", "Documents vérifiés", "Factures, carnet, conformité"),
    ("truck", "Livraison fermée", "Transport en camion fermé sur demande"),
])}

<h2>Les marques que nous recherchons le plus</h2>
<p>Porsche (911, Cayenne, Macan, Taycan), Mercedes-AMG et Classe G, BMW M, Audi RS, Lamborghini, Ferrari, Maserati, Bentley, Aston Martin, Land Rover et Range Rover, ainsi que les youngtimers recherchées. Si la configuration existe en Europe, nous la trouvons.</p>
{cta("<strong>Décrivez la configuration de vos rêves.</strong> On vous présente les meilleures options disponibles sous 48h.", "Trouver mon véhicule")}

<h2>Discrétion et sécurité</h2>
<p>Paiement sécurisé, vérification de la propriété et de l'absence de gage, documents contrôlés : nous sécurisons chaque étape. Le véhicule peut être livré en camion fermé, à votre domicile ou à l'adresse de votre choix.</p>

<h2>Financer un véhicule de prestige</h2>
<p>LOA, LLD ou crédit : notre partenaire du groupe, Cohesif Leasing, peut monter le dossier pendant que nous cherchons votre véhicule. <a href="financement-voiture.html">Découvrir les solutions de financement</a>.</p>
""",
        "faq": [
            ("Pouvez-vous trouver une configuration très précise ?", "Oui, c'est le cœur de notre service. Plus votre cahier des charges est précis (couleur, options, kilométrage, année), plus la recherche est ciblée. Si la configuration est rare, nous élargissons à toute l'Europe."),
            ("Le véhicule est-il contrôlé avant l'achat ?", "Oui : état général, historique d'entretien, cohérence du kilométrage et documents. Vous recevez les photos et les conclusions avant de vous engager."),
            ("Livrez-vous en camion fermé ?", "Oui, sur demande, partout en France."),
        ],
        "related": ["import-voiture-allemagne.html", "financement-voiture.html", "chasseur-automobile.html"],
    },
    {
        "slug": "vehicules-entreprise-lld.html",
        "kind": "service",
        "menu": "Véhicules d'entreprise & LLD",
        "crumb": "Véhicules d'entreprise",
        "card_title": "Véhicules d'entreprise, utilitaires et LLD",
        "card_text": "De 1 à 50 véhicules en LLD, LOA ou achat, livrés clés en main.",
        "service_type": "Location longue durée et flottes d'entreprise",
        "title": "LLD utilitaire et véhicules d'entreprise | Cohesif Auto",
        "description": "Utilitaires et flottes de 1 à 50 véhicules en LLD, LOA, location courte durée ou achat, livrés clés en main. Devis entreprise sous 48h.",
        "eyebrow": "Entreprises & artisans",
        "h1": "Véhicules d'entreprise et utilitaires en LLD, LOA ou à l'achat",
        "lead": "Artisans, PME, entreprises du BTP ou de transport : on sélectionne, on finance et on livre vos véhicules clés en main. Un contrat, un interlocuteur, aucune trésorerie immobilisée si vous le souhaitez.",
        "image": IMG_CLIO,
        "projet": "Flotte entreprise",
        "cta": "Demander un devis entreprise",
        "aside_title": "Devis entreprise sous 48h",
        "aside_text": "Nombre de véhicules, usage, durée : on vous propose la formule la plus adaptée.",
        "body": f"""
<h2>Trois formules selon votre besoin</h2>
<div class="feature-grid">
<div class="feature"><div class="svc-icon"><svg><use href="#i-fleet"/></svg></div><h3>LLD · 24 à 60 mois</h3><p>Un loyer fixe, entretien et assistance inclus selon la formule. Pas d'apport immobilisé, vous rendez le véhicule à la fin du contrat.</p></div>
<div class="feature"><div class="svc-icon"><svg><use href="#i-clock"/></svg></div><h3>Location courte et moyenne durée</h3><p>Quelques jours à quelques mois : chantier, renfort saisonnier, remplacement d'un véhicule immobilisé.</p></div>
<div class="feature"><div class="svc-icon"><svg><use href="#i-euro"/></svg></div><h3>Achat ou LOA</h3><p>Neuf ou occasion récente, comptant ou financé, avec reprise possible de vos anciens véhicules.</p></div>
</div>

<h2>Utilitaires et véhicules pour les métiers</h2>
<p>Fourgons et fourgonnettes (Renault Trafic et Master, Peugeot Expert et Boxer, Citroën Jumpy et Jumper, Ford Transit, Mercedes Vito et Sprinter), pick-up, bennes et plateaux, véhicules de fonction et de direction, citadines de service. Les aménagements (étagères, galerie, cloison, attelage) peuvent être prévus avant la livraison.</p>
{included([
    ("fleet", "1 à 50 véhicules", "De l'artisan à la flotte complète"),
    ("gear", "Aménagements", "Étagères, galerie, attelage, marquage"),
    ("doc", "Un seul contrat", "Et un interlocuteur dédié"),
    ("truck", "Livraison clés en main", "Sur votre site ou au dépôt"),
])}
{cta("<strong>Besoin de véhicules pour vos équipes ?</strong> Recevez un devis entreprise détaillé sous 48h.", "Demander un devis")}

<h2>LLD ou achat : que choisir pour une entreprise ?</h2>
<p>La LLD préserve votre trésorerie et rend le budget prévisible : les loyers sont comptabilisés en charges. L'achat est souvent plus avantageux sur des véhicules gardés longtemps et très utilisés. Sur un utilitaire, la TVA est en principe récupérable ; sur un véhicule de tourisme, elle ne l'est généralement pas. Votre expert-comptable reste le meilleur juge pour votre situation.</p>
<p>Nous détaillons les différences dans notre <a href="guide-lld-loa-credit-auto.html">guide LLD, LOA ou crédit auto</a>.</p>

<h2>La force du Groupe Cohesif</h2>
<p>Cohesif Auto travaille avec les autres sociétés du groupe : <a href="https://cohesifleasing.fr" target="_blank" rel="noopener">Cohesif Leasing</a> pour le financement, <a href="https://cohesifenergy.fr" target="_blank" rel="noopener">Cohesif Energy</a> pour l'installation de bornes de recharge si vous passez à l'électrique, et <a href="https://cohesifbtp.fr" target="_blank" rel="noopener">Cohesif BTP</a> pour le matériel de chantier.</p>
""",
        "faq": [
            ("À partir de combien de véhicules travaillez-vous ?", "Dès un véhicule. Nous équipons aussi bien un artisan qui remplace son utilitaire qu'une entreprise qui constitue une flotte de plusieurs dizaines de véhicules."),
            ("Que comprend un loyer de LLD ?", "Le loyer couvre la mise à disposition du véhicule pour une durée et un kilométrage définis. Selon la formule choisie, il peut inclure l'entretien, l'assistance, les pneumatiques et le véhicule de remplacement. Le détail figure dans le devis."),
            ("Pouvez-vous livrer des utilitaires aménagés ?", "Oui. Les aménagements (étagères, galerie, cloison, attelage, marquage) peuvent être prévus avant la livraison."),
            ("La TVA est-elle récupérable ?", "En principe, la TVA est récupérable sur les véhicules utilitaires et ne l'est généralement pas sur les véhicules de tourisme. Faites valider votre situation par votre expert-comptable."),
        ],
        "related": ["guide-lld-loa-credit-auto.html", "financement-voiture.html", "chasseur-automobile.html"],
    },
    {
        "slug": "financement-voiture.html",
        "kind": "service",
        "menu": "Financement auto",
        "crumb": "Financement auto",
        "card_title": "Financement auto : LOA, LLD, crédit",
        "card_text": "Simulez votre mensualité et faites monter votre dossier pendant qu'on cherche votre véhicule.",
        "service_type": "Financement automobile",
        "title": "Financement voiture : LOA, LLD ou crédit | Cohesif Auto",
        "description": "Financez votre voiture en LOA, LLD ou crédit avec Cohesif Leasing. Simulez votre mensualité en ligne, pour particuliers et professionnels.",
        "eyebrow": "Financement",
        "h1": "Financer votre voiture : LOA, LLD ou crédit auto",
        "lead": "Une seule démarche : pendant que nous cherchons votre véhicule, notre partenaire du groupe Cohesif Leasing monte votre dossier de financement.",
        "projet": "Financement",
        "cta": "Demander un financement",
        "body": """
<h2>Simulez votre mensualité</h2>
<div class="sim" id="simulateur" style="box-shadow:none">
  <div class="sim-range">
    <div class="sim-range-top">
      <label for="simAmount">Prix du véhicule</label>
      <output id="simAmountOut" for="simAmount">25 000 €</output>
    </div>
    <input type="range" id="simAmount" min="5000" max="150000" step="1000" value="25000">
  </div>
  <div class="sim-range-top"><label>Durée</label></div>
  <div class="sim-durations" role="group" aria-label="Durée du financement">
    <button type="button" data-months="12">12 m</button>
    <button type="button" data-months="24">24 m</button>
    <button type="button" data-months="36">36 m</button>
    <button type="button" data-months="48" class="on">48 m</button>
    <button type="button" data-months="60">60 m</button>
  </div>
  <div class="sim-result">
    <span>Mensualité estimée</span>
    <strong id="simMonthly">—</strong>
  </div>
  <a href="#contact" class="btn btn-primary btn-block" data-preset="Financement" data-track="sim_cta">Faire une demande de financement</a>
  <p class="sim-note">Simulation indicative sur la base d'un taux de 3,9 %, hors assurance. Sous réserve d'acceptation du dossier.</p>
</div>

<h2>Trois façons de financer votre véhicule</h2>
<table>
<thead><tr><th></th><th>Crédit auto</th><th>LOA</th><th>LLD</th></tr></thead>
<tbody>
<tr><td><strong>Propriétaire ?</strong></td><td>Oui, dès l'achat</td><td>Oui, si vous levez l'option d'achat</td><td>Non</td></tr>
<tr><td><strong>Fin de contrat</strong></td><td>Le véhicule est à vous</td><td>Achat, restitution ou nouveau contrat</td><td>Restitution ou nouveau contrat</td></tr>
<tr><td><strong>Kilométrage</strong></td><td>Libre</td><td>Prévu au contrat</td><td>Prévu au contrat</td></tr>
<tr><td><strong>Entretien inclus</strong></td><td>Non</td><td>En option</td><td>Souvent inclus</td></tr>
<tr><td><strong>Idéal pour</strong></td><td>Garder le véhicule longtemps</td><td>Changer souvent, avec le choix d'acheter</td><td>Un budget fixe sans surprise</td></tr>
</tbody>
</table>
<p>Pour aller plus loin, lisez notre <a href="guide-lld-loa-credit-auto.html">comparatif détaillé LLD, LOA et crédit auto</a>.</p>

<h2>Comment ça se passe</h2>
<ol class="num">
<li>Vous simulez votre mensualité et envoyez votre demande.</li>
<li>Un conseiller Cohesif Leasing vous rappelle pour étudier votre situation.</li>
<li>Pendant ce temps, nous recherchons votre véhicule.</li>
<li>Vous signez le financement et le véhicule en même temps : une seule démarche.</li>
</ol>
<div class="callout"><p>Un crédit vous engage et doit être remboursé. Vérifiez vos capacités de remboursement avant de vous engager.</p></div>
""",
        "faq": [
            ("Puis-je financer une voiture importée ?", "Oui. Le financement porte sur le prix total du véhicule livré, qu'il soit trouvé en France ou importé d'Europe."),
            ("Les professionnels peuvent-ils en bénéficier ?", "Oui. Cohesif Leasing accompagne aussi bien les particuliers que les professionnels, en LOA, LLD ou crédit."),
            ("La simulation m'engage-t-elle ?", "Non. La simulation est indicative et la demande est sans engagement tant que vous n'avez pas signé d'offre de financement."),
        ],
        "related": ["guide-lld-loa-credit-auto.html", "vehicules-entreprise-lld.html", "chasseur-automobile.html"],
    },
    {
        "slug": "pieces-auto-collection.html",
        "kind": "service",
        "menu": "Pièces de collection",
        "crumb": "Pièces de collection",
        "card_title": "Pièces auto de collection",
        "card_text": "Pièces NOS, d'origine ou reconditionnées pour anciennes et youngtimers.",
        "service_type": "Recherche de pièces automobiles de collection",
        "title": "Pièces auto anciennes et de collection | Cohesif Auto",
        "description": "Recherche de pièces auto anciennes, NOS, d'origine ou reconditionnées pour voitures de collection et youngtimers, en Europe et aux États-Unis.",
        "eyebrow": "Atelier collection",
        "h1": "Pièces auto anciennes et de collection, même introuvables",
        "lead": "Vous restaurez une ancienne ou une youngtimer et une pièce vous bloque ? Nous la recherchons auprès de spécialistes et de collectionneurs en Europe et aux États-Unis.",
        "projet": "Pièce de collection",
        "cta": "Trouver ma pièce",
        "aside_title": "Une pièce vous bloque ?",
        "aside_text": "Envoyez-nous le modèle, l'année et la référence ou une photo de la pièce.",
        "body": f"""
<h2>Les pièces que nous recherchons</h2>
{included([
    ("gear", "Mécanique", "Carburateurs, pièces moteur, boîte, freinage"),
    ("car", "Carrosserie", "Calandres, chromes, pare-chocs, optiques"),
    ("user", "Sellerie et intérieur", "Garnitures, compteurs, commandes"),
    ("doc", "Documentation", "Manuels, revues techniques"),
])}
<p>Nous recherchons des pièces <strong>NOS</strong> (New Old Stock, pièces neuves d'époque jamais montées), d'origine d'occasion ou reconditionnées. Quand une pièce n'existe plus, nous pouvons vous orienter vers des solutions de refabrication.</p>

<h2>Comment formuler votre demande</h2>
<ul>
<li>la marque, le modèle et l'année exacte du véhicule ;</li>
<li>la référence de la pièce si vous l'avez, ou des photos ;</li>
<li>l'état souhaité (NOS, occasion, reconditionnée) et votre budget.</li>
</ul>
{cta("<strong>Envoyez-nous votre recherche</strong> : on active notre réseau de spécialistes et on revient vers vous.", "Trouver ma pièce")}

<h2>Vous cherchez le véhicule lui-même ?</h2>
<p>Nous recherchons aussi des youngtimers et des véhicules de collection, en France et en Europe, avec contrôle avant achat. <a href="import-voiture-europe.html">Voir l'import européen</a>.</p>
""",
        "faq": [
            ("Qu'est-ce qu'une pièce NOS ?", "NOS signifie New Old Stock : une pièce neuve, fabriquée à l'époque, jamais montée sur un véhicule. C'est la solution la plus recherchée pour une restauration fidèle."),
            ("Combien de temps prend une recherche de pièce ?", "Cela dépend de la rareté de la pièce : de quelques jours pour une pièce courante à plusieurs semaines pour une pièce très rare. Nous vous tenons informé à chaque étape."),
        ],
        "related": ["import-voiture-europe.html", "voiture-prestige.html", "chasseur-automobile.html"],
    },
    {
        "slug": "mandataire-auto-paris.html",
        "kind": "service",
        "menu": "Mandataire auto Paris",
        "crumb": "Mandataire auto Paris",
        "card_title": "Mandataire auto à Paris et en Île-de-France",
        "card_text": "Un interlocuteur basé à Paris 15e, livraison dans toute l'Île-de-France.",
        "service_type": "Mandataire automobile",
        "area": [{"@type": "City", "name": "Paris"}, {"@type": "AdministrativeArea", "name": "Île-de-France"}],
        "title": "Mandataire auto à Paris et en Île-de-France | Cohesif Auto",
        "description": "Mandataire et chasseur auto à Paris 15e : recherche en France et en Europe, contrôle, carte grise et livraison dans toute l'Île-de-France.",
        "eyebrow": "Paris & Île-de-France",
        "h1": "Mandataire et chasseur automobile à Paris",
        "lead": "Basés rue de la Croix-Nivert, dans le 15e arrondissement, nous accompagnons les particuliers et les entreprises de Paris et d'Île-de-France, de la recherche à la livraison.",
        "image": IMG_URUS,
        "projet": "Acheter un véhicule",
        "body": f"""
<h2>Un interlocuteur à Paris, un choix européen</h2>
<p>Acheter une voiture à Paris, c'est souvent un choix limité et des prix tirés vers le haut. Cohesif Auto vous donne accès au marché français et européen, tout en restant joignable à Paris par téléphone, WhatsApp ou sur rendez-vous.</p>
{included([
    ("pin", "Basé à Paris 15e", "200 rue de la Croix-Nivert"),
    ("truck", "Livraison en Île-de-France", "À domicile ou sur votre lieu de travail"),
    ("shield", "Véhicules contrôlés", "Avant tout engagement"),
    ("doc", "Carte grise comprise", "Y compris pour un import"),
])}

<h2>Zones de livraison</h2>
<p>Nous livrons à Paris (75) et dans toute l'Île-de-France : Hauts-de-Seine (92), Seine-Saint-Denis (93), Val-de-Marne (94), Yvelines (78), Essonne (91), Val-d'Oise (95) et Seine-et-Marne (77), ainsi que partout en France.</p>
{cta("<strong>Vous êtes à Paris ou en Île-de-France ?</strong> Recevez vos propositions sous 48h et faites-vous livrer chez vous.")}

<h2>Nos services à Paris</h2>
<ul>
<li><a href="chasseur-automobile.html">Chasseur automobile</a> : recherche sur mesure, neuf ou occasion.</li>
<li><a href="import-voiture-allemagne.html">Import de voiture d'Allemagne</a> et d'<a href="import-voiture-europe.html">autres pays européens</a>.</li>
<li><a href="voiture-prestige.html">Voitures de prestige</a> et sportives.</li>
<li><a href="vehicules-entreprise-lld.html">Véhicules d'entreprise et utilitaires</a> pour les sociétés franciliennes.</li>
<li><a href="financement-voiture.html">Financement</a> en LOA, LLD ou crédit.</li>
</ul>

<h2>Électrique et hybride en Île-de-France</h2>
<p>Vous passez à l'électrique ? Nous trouvons le véhicule et la société du groupe <a href="https://cohesifenergy.fr" target="_blank" rel="noopener">Cohesif Energy</a> peut installer votre borne de recharge, à domicile, en copropriété ou en entreprise.</p>
""",
        "faq": [
            ("Peut-on vous rencontrer à Paris ?", "Oui, sur rendez-vous. Nous sommes situés au 200 rue de la Croix-Nivert, 75015 Paris. La plupart des échanges se font aussi très bien par téléphone et WhatsApp."),
            ("Livrez-vous en banlieue parisienne ?", "Oui, dans tous les départements d'Île-de-France et partout en France."),
            ("Combien de temps pour recevoir ma voiture à Paris ?", "Généralement 1 à 3 semaines pour un véhicule trouvé en France et 4 à 8 semaines pour un import, après validation de votre choix."),
        ],
        "related": ["chasseur-automobile.html", "import-voiture-allemagne.html", "vehicules-entreprise-lld.html"],
    },

    # ================================================================ GUIDES
    {
        "slug": "guide-importer-voiture-allemagne.html",
        "kind": "guide",
        "menu": "Importer une voiture d'Allemagne",
        "crumb": "Importer une voiture d'Allemagne",
        "card_title": "Importer une voiture d'Allemagne : le guide complet",
        "card_text": "Recherche, vérifications, documents, transport et carte grise, étape par étape.",
        "published": "2026-10-06",
        "title": "Importer une voiture d'Allemagne : le guide complet 2026",
        "description": "Où chercher, quoi vérifier, documents allemands, transport, quitus fiscal, COC et carte grise : toutes les étapes pour importer une voiture d'Allemagne.",
        "eyebrow": "Guide import",
        "h1": "Importer une voiture d'Allemagne : le guide complet",
        "lead": "Où chercher, quoi vérifier, quels documents réclamer et comment immatriculer le véhicule en France : toutes les étapes d'un import réussi.",
        "projet": "Importer d'Europe",
        "aside_title": "On importe pour vous",
        "aside_text": "Recherche, contrôle, transport et carte grise : un seul interlocuteur, zéro démarche.",
        "body": f"""
<h2>Pourquoi importer une voiture d'Allemagne ?</h2>
<p>L'Allemagne est le premier marché automobile d'Europe. Pour un acheteur français, cela signifie plus de choix, en particulier sur les marques allemandes et les versions bien équipées, et des prix souvent intéressants sur le haut de gamme. Mais l'économie n'est réelle que si l'on calcule le <strong>coût total</strong> : véhicule, transport, carte grise et éventuel malus.</p>

<h2>Étape 1 : chercher au bon endroit</h2>
<p>Les deux plateformes de référence sont <strong>mobile.de</strong> et <strong>AutoScout24</strong>. Quelques conseils :</p>
<ul>
<li>privilégiez les <strong>vendeurs professionnels</strong> (Händler), plus faciles à joindre et qui fournissent une facture ;</li>
<li>repérez la mention <strong>« Scheckheftgepflegt »</strong> : le véhicule a un carnet d'entretien suivi ;</li>
<li>méfiez-vous des prix nettement sous le marché, surtout si le vendeur demande un acompte avant toute visite.</li>
</ul>

<h2>Étape 2 : vérifier le véhicule et ses documents</h2>
<p>Avant de payer quoi que ce soit, vérifiez :</p>
<ul>
<li>la <strong>Zulassungsbescheinigung Teil I</strong> (équivalent de la carte grise) et la <strong>Teil II</strong> (titre de propriété), indispensables pour immatriculer en France ;</li>
<li>le <strong>carnet d'entretien</strong> et les factures, pour contrôler la cohérence du kilométrage ;</li>
<li>la date du dernier contrôle technique allemand (<strong>HU</strong>, souvent appelé TÜV) ;</li>
<li>l'état réel du véhicule, idéalement par une inspection sur place.</li>
</ul>
<div class="callout warn"><p>Ne versez jamais d'acompte à un vendeur que vous n'avez pas pu vérifier. Les fausses annonces de véhicules « bloqués à l'étranger » sont une arnaque classique.</p></div>

<h2>Étape 3 : acheter et payer en sécurité</h2>
<p>Exigez un <strong>contrat de vente</strong> (Kaufvertrag) ou une facture mentionnant le numéro de châssis (VIN), le prix, la date et le kilométrage. Pour un véhicule neuf au sens fiscal (moins de 6 mois ou moins de 6 000 km), l'achat se fait hors taxes en Allemagne et la TVA est payée en France.</p>

<h2>Étape 4 : rapatrier le véhicule</h2>
<p>Deux solutions : le <strong>transport par camion</strong>, le plus simple et le plus sûr, ou le <strong>convoyage par la route</strong> avec des plaques d'export allemandes (Ausfuhrkennzeichen) et l'assurance correspondante. Le transport par camion évite d'ajouter des kilomètres et les aléas du trajet.</p>

<h2>Étape 5 : réunir les documents français</h2>
<ul>
<li>le <strong>certificat de conformité européen</strong> (COC), délivré par le constructeur ;</li>
<li>le <strong>quitus fiscal</strong>, demandé au service des impôts, qui atteste que la TVA est réglée ;</li>
<li>un <strong>contrôle technique français</strong> de moins de 6 mois si le véhicule a plus de 4 ans ;</li>
<li>la facture ou le contrat de vente et les documents d'immatriculation allemands.</li>
</ul>
{cta("<strong>Trop de démarches ?</strong> On s'occupe de tout, de la recherche à la carte grise.", "Confier mon import")}

<h2>Étape 6 : immatriculer en France</h2>
<p>La demande de certificat d'immatriculation se fait en ligne sur le site de l'ANTS ou auprès d'un professionnel habilité. Le coût de la carte grise comprend notamment la taxe régionale (calculée selon la puissance fiscale et votre région) et, le cas échéant, le malus écologique. Tout est détaillé dans notre <a href="guide-carte-grise-vehicule-importe.html">guide de la carte grise d'un véhicule importé</a>.</p>

<h2>Combien de temps et combien ça coûte ?</h2>
<p>Comptez en général 4 à 8 semaines entre l'achat et l'obtention de la carte grise française. Côté budget, ajoutez au prix du véhicule le transport, le contrôle technique éventuel, la carte grise et le malus éventuel. Pour comprendre les taxes, lisez notre <a href="guide-malus-tva-voiture-importee.html">guide sur la TVA et le malus</a>.</p>

<h2>Faire soi-même ou se faire accompagner ?</h2>
<p>Importer seul est tout à fait possible si vous parlez allemand, avez du temps et savez juger l'état d'un véhicule. Si ce n'est pas le cas, un professionnel sécurise l'achat et vous fait gagner des semaines. Découvrez notre <a href="import-voiture-allemagne.html">service d'import d'Allemagne clé en main</a>.</p>
""",
        "faq": [
            ("Quels documents faut-il pour immatriculer une voiture allemande en France ?", "Le certificat de conformité européen (COC), le quitus fiscal, un contrôle technique de moins de 6 mois si le véhicule a plus de 4 ans, la facture ou le contrat de vente et les documents d'immatriculation allemands (Zulassungsbescheinigung Teil I et Teil II)."),
            ("Faut-il payer des droits de douane ?", "Non, il n'y a pas de droits de douane entre pays de l'Union européenne. La TVA n'est due en France que pour un véhicule neuf au sens fiscal (moins de 6 mois ou moins de 6 000 km)."),
            ("Combien de temps dure un import d'Allemagne ?", "En général 4 à 8 semaines entre l'achat et la carte grise française, selon le transport et les délais administratifs."),
        ],
        "related": ["import-voiture-allemagne.html", "guide-carte-grise-vehicule-importe.html", "guide-malus-tva-voiture-importee.html"],
    },
    {
        "slug": "guide-carte-grise-vehicule-importe.html",
        "kind": "guide",
        "menu": "Carte grise d'un véhicule importé",
        "crumb": "Carte grise véhicule importé",
        "card_title": "Carte grise d'un véhicule importé : démarches et coût",
        "card_text": "COC, quitus fiscal, contrôle technique, ANTS : les documents et le calcul du prix.",
        "published": "2026-10-06",
        "title": "Carte grise d'un véhicule importé : démarches et prix",
        "description": "Carte grise d'une voiture importée de l'UE : COC, quitus fiscal, contrôle technique, démarche ANTS et calcul du prix, expliqués simplement.",
        "eyebrow": "Guide démarches",
        "h1": "Carte grise d'un véhicule importé : documents, démarches et prix",
        "lead": "Vous avez acheté une voiture dans un autre pays de l'Union européenne ? Voici la liste des documents, les étapes de la demande et la façon dont le prix de la carte grise est calculé.",
        "projet": "Importer d'Europe",
        "aside_title": "On gère votre carte grise",
        "aside_text": "Dans le cadre d'un import avec Cohesif Auto, toutes les démarches sont comprises.",
        "body": f"""
<h2>Les documents à réunir</h2>
<p>Pour immatriculer en France un véhicule acheté dans l'Union européenne, il faut en principe :</p>
<ol class="num">
<li>le <strong>certificat d'immatriculation étranger</strong> (ou les documents équivalents) ;</li>
<li>la <strong>facture ou le certificat de vente</strong> ;</li>
<li>le <strong>certificat de conformité européen</strong> (COC) ou, à défaut, une attestation d'identification du constructeur ;</li>
<li>le <strong>quitus fiscal</strong> délivré par le service des impôts ;</li>
<li>un <strong>contrôle technique</strong> de moins de 6 mois si le véhicule a plus de 4 ans ;</li>
<li>un justificatif d'identité et un justificatif de domicile.</li>
</ol>

<h2>Le certificat de conformité (COC)</h2>
<p>Le COC atteste que le véhicule est conforme à un type homologué au niveau européen. Il est délivré par le constructeur ou son importateur, parfois gratuitement, parfois contre paiement. Sans COC, il faut obtenir une attestation d'identification ou passer par une réception à titre isolé, une démarche plus longue.</p>

<h2>Le quitus fiscal</h2>
<p>Le quitus fiscal prouve que la situation du véhicule au regard de la TVA est régularisée. Il se demande auprès du service des impôts compétent. Pour un véhicule d'occasion, il est délivré sans paiement ; pour un véhicule neuf au sens fiscal (moins de 6 mois ou moins de 6 000 km), la TVA française doit être payée pour l'obtenir.</p>
{cta("<strong>Vous ne voulez pas vous occuper des démarches ?</strong> Avec notre service d'import, la carte grise est comprise.", "Confier mon import")}

<h2>La demande d'immatriculation</h2>
<p>La demande se fait en ligne sur le site officiel de l'ANTS (Agence nationale des titres sécurisés) ou auprès d'un professionnel habilité. En attendant la carte grise définitive, une immatriculation provisoire « WW » peut être délivrée pour circuler.</p>

<h2>Comment est calculé le prix de la carte grise ?</h2>
<table>
<thead><tr><th>Composante</th><th>Ce qu'il faut savoir</th></tr></thead>
<tbody>
<tr><td><strong>Taxe régionale</strong></td><td>Puissance fiscale (chevaux fiscaux) multipliée par le tarif de votre région. Certaines régions appliquent des réductions pour les véhicules peu polluants.</td></tr>
<tr><td><strong>Malus écologique</strong></td><td>Dû à la première immatriculation en France selon les émissions de CO2, réduit selon l'ancienneté pour un véhicule d'occasion importé.</td></tr>
<tr><td><strong>Taxe sur la masse</strong></td><td>Peut s'appliquer aux véhicules lourds selon le barème en vigueur.</td></tr>
<tr><td><strong>Taxe fixe et acheminement</strong></td><td>Montants forfaitaires de gestion et d'envoi du titre.</td></tr>
</tbody>
</table>
<p>Les barèmes changent régulièrement, en général au 1er janvier. Le simulateur officiel de l'ANTS permet d'estimer le montant ; nous l'intégrons systématiquement dans nos chiffrages. Voir aussi notre <a href="guide-malus-tva-voiture-importee.html">guide sur la TVA et le malus</a>.</p>

<h2>Les erreurs qui retardent le dossier</h2>
<ul>
<li>un COC qui ne correspond pas exactement à la version du véhicule ;</li>
<li>un contrôle technique de plus de 6 mois au moment de la demande ;</li>
<li>une facture sans numéro de châssis (VIN) ou sans date de vente ;</li>
<li>des documents étrangers incomplets ou illisibles.</li>
</ul>
""",
        "faq": [
            ("Combien coûte la carte grise d'une voiture importée ?", "Cela dépend de la puissance fiscale, de votre région, des émissions de CO2 (malus) et de l'âge du véhicule. Le simulateur officiel de l'ANTS donne une estimation ; nous l'intégrons dans chacun de nos chiffrages."),
            ("Peut-on rouler en attendant la carte grise française ?", "Oui, avec une immatriculation provisoire WW, valable pour une durée limitée, le temps d'obtenir la carte grise définitive."),
            ("Le contrôle technique est-il obligatoire ?", "Oui si le véhicule a plus de 4 ans : il doit avoir moins de 6 mois au moment de la demande d'immatriculation."),
        ],
        "related": ["guide-importer-voiture-allemagne.html", "guide-malus-tva-voiture-importee.html", "import-voiture-europe.html"],
    },
    {
        "slug": "guide-malus-tva-voiture-importee.html",
        "kind": "guide",
        "menu": "TVA et malus d'une voiture importée",
        "crumb": "TVA et malus voiture importée",
        "card_title": "TVA et malus d'une voiture importée",
        "card_text": "Neuf ou occasion au sens fiscal, quitus, malus réduit : ce que vous paierez vraiment.",
        "published": "2026-10-06",
        "title": "TVA et malus d'une voiture importée : les règles 2026",
        "description": "Voiture importée de l'UE : quand payer la TVA en France, comment fonctionne le malus sur une occasion importée et comment éviter les surprises.",
        "eyebrow": "Guide fiscalité",
        "h1": "TVA et malus d'une voiture importée : ce que vous paierez vraiment",
        "lead": "Deux questions reviennent dans chaque projet d'import : faut-il payer la TVA en France, et combien coûtera le malus ? Voici les règles, expliquées simplement.",
        "projet": "Importer d'Europe",
        "aside_title": "Un chiffrage complet avant d'acheter",
        "aside_text": "TVA, malus, carte grise, transport : on calcule le prix final avant tout engagement.",
        "body": f"""
<h2>Neuf ou occasion : la distinction qui change tout</h2>
<p>Pour la TVA, un véhicule est considéré comme <strong>neuf</strong> s'il a été mis en circulation depuis <strong>moins de 6 mois</strong> ou s'il a parcouru <strong>moins de 6 000 km</strong>. Il suffit qu'une des deux conditions soit remplie.</p>
<table>
<thead><tr><th></th><th>Véhicule neuf (fiscalement)</th><th>Véhicule d'occasion</th></tr></thead>
<tbody>
<tr><td><strong>Achat dans le pays d'origine</strong></td><td>Hors taxes</td><td>Prix du vendeur, taxes du pays d'origine comprises le cas échéant</td></tr>
<tr><td><strong>TVA en France</strong></td><td>Oui, au taux français</td><td>Non</td></tr>
<tr><td><strong>Quitus fiscal</strong></td><td>Délivré après paiement de la TVA</td><td>Délivré sans paiement</td></tr>
</tbody>
</table>
<div class="callout warn"><p>Un véhicule « presque neuf » à 4 000 km et 3 mois est un véhicule neuf au sens fiscal : la TVA française sera due. Vérifiez ce point avant de comparer les prix.</p></div>

<h2>Le malus écologique sur une voiture importée</h2>
<p>Le malus écologique s'applique lors de la <strong>première immatriculation en France</strong>, y compris pour une voiture d'occasion déjà immatriculée à l'étranger. Pour un véhicule d'occasion importé, le montant est <strong>réduit en fonction de son ancienneté</strong>.</p>
<p>Le barème dépend des émissions de CO2 du véhicule et évolue chaque année, en général au 1er janvier. Une taxe sur la masse peut aussi s'appliquer aux véhicules lourds. Pour une sportive ou un gros SUV, ces montants peuvent changer complètement l'intérêt d'un import : c'est le premier point à vérifier.</p>
{cta("<strong>Vous hésitez sur un import ?</strong> On calcule TVA, malus et carte grise avant que vous ne vous engagiez.", "Chiffrer mon import")}

<h2>Comment éviter les mauvaises surprises</h2>
<ol class="num">
<li><strong>Vérifiez l'âge et le kilométrage</strong> pour savoir si la TVA est due en France.</li>
<li><strong>Récupérez les émissions de CO2</strong> exactes (sur le COC ou les documents du véhicule).</li>
<li><strong>Estimez le malus et la carte grise</strong> avec le simulateur officiel de l'ANTS.</li>
<li><strong>Comparez le prix total</strong> avec le même modèle en France, transport compris.</li>
</ol>

<h2>Et les droits de douane ?</h2>
<p>Entre pays de l'Union européenne, il n'y a pas de droits de douane. Pour un véhicule importé d'un pays hors Union européenne, des droits de douane et la TVA à l'importation s'appliquent, avec des formalités d'homologation spécifiques.</p>
<p>Pour la suite des démarches, consultez notre <a href="guide-carte-grise-vehicule-importe.html">guide de la carte grise d'un véhicule importé</a>.</p>
""",
        "faq": [
            ("Quand faut-il payer la TVA sur une voiture importée ?", "Quand le véhicule est neuf au sens fiscal : moins de 6 mois depuis sa première mise en circulation ou moins de 6 000 km. La TVA est alors payée en France, ce qui permet d'obtenir le quitus fiscal."),
            ("Le malus s'applique-t-il à une voiture d'occasion importée ?", "Oui, lors de sa première immatriculation en France, avec une réduction selon l'ancienneté du véhicule. Le barème dépend des émissions de CO2 et change chaque année."),
            ("Où trouver les émissions de CO2 de mon véhicule ?", "Sur le certificat de conformité européen (COC) et, en général, sur les documents d'immatriculation du pays d'origine."),
        ],
        "related": ["guide-carte-grise-vehicule-importe.html", "guide-importer-voiture-allemagne.html", "import-voiture-allemagne.html"],
    },
    {
        "slug": "guide-lld-loa-credit-auto.html",
        "kind": "guide",
        "menu": "LLD, LOA ou crédit auto",
        "crumb": "LLD, LOA ou crédit auto",
        "card_title": "LLD, LOA ou crédit auto : que choisir ?",
        "card_text": "Comparatif clair pour les particuliers et les professionnels.",
        "published": "2026-10-06",
        "title": "LLD, LOA ou crédit auto : que choisir ? Comparatif 2026",
        "description": "LLD, LOA ou crédit auto : fonctionnement, avantages, inconvénients et profils adaptés, pour les particuliers comme pour les entreprises.",
        "eyebrow": "Guide financement",
        "h1": "LLD, LOA ou crédit auto : quelle solution choisir ?",
        "lead": "Propriétaire ou locataire, budget fixe ou flexibilité, particulier ou entreprise : le bon mode de financement dépend de votre usage. Voici comment choisir.",
        "projet": "Financement",
        "aside_title": "Simulez votre mensualité",
        "aside_text": "Notre partenaire Cohesif Leasing étudie votre dossier pendant qu'on cherche votre véhicule.",
        "body": f"""
<h2>Le crédit auto : devenir propriétaire tout de suite</h2>
<p>Avec un crédit auto, vous achetez le véhicule et le remboursez en mensualités. Il vous appartient dès l'achat : vous pouvez rouler autant que vous voulez, le personnaliser et le revendre quand vous le souhaitez.</p>
<ul>
<li><strong>Pour</strong> : aucune limite de kilométrage, pas de frais de restitution, le véhicule est à vous.</li>
<li><strong>Contre</strong> : mensualités souvent plus élevées, entretien et revente à votre charge.</li>
</ul>

<h2>La LOA : louer avec le choix d'acheter</h2>
<p>La location avec option d'achat (LOA) est une location sur une durée et un kilométrage définis. À la fin du contrat, vous pouvez <strong>acheter le véhicule</strong> en levant l'option, le rendre ou repartir sur un nouveau véhicule.</p>
<ul>
<li><strong>Pour</strong> : mensualités souvent plus basses qu'un crédit, liberté de choix en fin de contrat.</li>
<li><strong>Contre</strong> : kilométrage limité, frais de remise en état si le véhicule est restitué abîmé.</li>
</ul>

<h2>La LLD : un budget fixe, sans se soucier de la revente</h2>
<p>La location longue durée (LLD) est une location sans option d'achat. Le loyer peut inclure l'entretien, l'assistance et les pneumatiques selon la formule. Vous rendez le véhicule à la fin et en prenez un nouveau.</p>
<ul>
<li><strong>Pour</strong> : budget prévisible, pas de revente à gérer, véhicule régulièrement renouvelé.</li>
<li><strong>Contre</strong> : vous n'êtes jamais propriétaire, kilométrage et état surveillés à la restitution.</li>
</ul>
{cta("<strong>Vous ne savez pas quelle formule choisir ?</strong> Un conseiller vous aide à comparer selon votre usage.", "Être conseillé")}

<h2>Tableau comparatif</h2>
<table>
<thead><tr><th></th><th>Crédit auto</th><th>LOA</th><th>LLD</th></tr></thead>
<tbody>
<tr><td><strong>Propriété</strong></td><td>Dès l'achat</td><td>Si option levée</td><td>Jamais</td></tr>
<tr><td><strong>Apport</strong></td><td>Facultatif</td><td>Souvent un premier loyer majoré</td><td>Souvent un premier loyer majoré</td></tr>
<tr><td><strong>Kilométrage</strong></td><td>Libre</td><td>Contractuel</td><td>Contractuel</td></tr>
<tr><td><strong>Entretien</strong></td><td>À votre charge</td><td>En option</td><td>Souvent inclus</td></tr>
<tr><td><strong>Fin de contrat</strong></td><td>Rien à faire</td><td>Achat, restitution ou renouvellement</td><td>Restitution ou renouvellement</td></tr>
</tbody>
</table>

<h2>Le cas des professionnels</h2>
<p>Pour une entreprise, la LLD et la LOA permettent de ne pas immobiliser de trésorerie et de passer les loyers en charges, dans les limites prévues par la réglementation pour les véhicules de tourisme. La TVA est en principe récupérable sur les véhicules utilitaires, mais généralement pas sur les véhicules de tourisme. Les véhicules de tourisme affectés à l'activité de l'entreprise sont aussi soumis à des taxes annuelles. Faites toujours valider le choix par votre expert-comptable.</p>
<p>Découvrez notre offre <a href="vehicules-entreprise-lld.html">véhicules d'entreprise et LLD</a>.</p>

<h2>Notre conseil pour choisir</h2>
<ul>
<li>Vous roulez beaucoup et gardez vos voitures longtemps : <strong>crédit</strong>.</li>
<li>Vous voulez changer régulièrement tout en gardant la possibilité d'acheter : <strong>LOA</strong>.</li>
<li>Vous voulez un budget fixe sans vous occuper de rien : <strong>LLD</strong>.</li>
</ul>
<p>Estimez votre mensualité avec notre <a href="financement-voiture.html">simulateur de financement</a>.</p>
""",
        "faq": [
            ("Quelle est la différence entre LOA et LLD ?", "La LOA comporte une option d'achat : en fin de contrat, vous pouvez acheter le véhicule. La LLD n'en comporte pas : vous rendez le véhicule. La LLD inclut plus souvent l'entretien dans le loyer."),
            ("Que se passe-t-il si je dépasse le kilométrage en LOA ou LLD ?", "Les kilomètres supplémentaires sont facturés au tarif prévu au contrat. Il est souvent possible d'ajuster le kilométrage en cours de contrat : mieux vaut l'anticiper."),
            ("Peut-on financer une voiture d'occasion en LOA ?", "Oui, de nombreuses offres de LOA portent sur des véhicules d'occasion récents, selon l'âge et la valeur du véhicule."),
        ],
        "related": ["financement-voiture.html", "vehicules-entreprise-lld.html", "chasseur-automobile.html"],
    },
    {
        "slug": "guide-acheter-voiture-occasion-sans-arnaque.html",
        "kind": "guide",
        "menu": "Acheter une occasion sans arnaque",
        "crumb": "Acheter une occasion sans arnaque",
        "card_title": "Acheter une voiture d'occasion sans se faire arnaquer",
        "card_text": "Les vérifications indispensables avant de payer, avec la checklist complète.",
        "published": "2026-10-06",
        "title": "Acheter une voiture d'occasion sans arnaque : checklist",
        "description": "Compteur trafiqué, véhicule gagé, fausse annonce, paiement risqué : les vérifications indispensables avant d'acheter une voiture d'occasion.",
        "eyebrow": "Guide achat",
        "h1": "Acheter une voiture d'occasion sans se faire arnaquer",
        "lead": "Compteur trafiqué, véhicule gagé, faux vendeur : la plupart des mauvaises affaires s'évitent avec quelques vérifications simples. Voici la checklist complète.",
        "projet": "Acheter un véhicule",
        "aside_title": "On vérifie pour vous",
        "aside_text": "Chaque véhicule que nous proposons est contrôlé avant achat.",
        "body": f"""
<h2>Les arnaques les plus courantes</h2>
<ul>
<li><strong>La fausse annonce</strong> : prix très attractif, vendeur « à l'étranger » qui demande un acompte ou un paiement avant toute visite.</li>
<li><strong>Le compteur trafiqué</strong> : un kilométrage réduit pour vendre plus cher.</li>
<li><strong>Le véhicule gagé ou volé</strong> : impossible à immatriculer, voire saisi.</li>
<li><strong>Le véhicule accidenté maquillé</strong> : réparé à la hâte, avec des défauts de sécurité.</li>
<li><strong>Le paiement frauduleux</strong> : faux chèque de banque, faux virement.</li>
</ul>

<h2>Vérifier l'historique avec HistoVec</h2>
<p><strong>HistoVec</strong> est le service officiel et gratuit du ministère de l'Intérieur. Le vendeur génère un rapport et vous le transmet : il indique les changements de propriétaires, les sinistres déclarés, l'historique des kilométrages relevés au contrôle technique et la situation administrative (gage, opposition). Un vendeur qui refuse de le fournir doit vous alerter.</p>

<h2>Contrôler le kilométrage</h2>
<ul>
<li>comparez le compteur avec les kilométrages des contrôles techniques et des factures d'entretien ;</li>
<li>observez l'usure du volant, du levier de vitesses, des pédales et du siège conducteur ;</li>
<li>méfiez-vous d'un carnet d'entretien sans factures ou rempli d'un seul coup.</li>
</ul>
{cta("<strong>Pas le temps ou pas l'œil ?</strong> On sélectionne et on contrôle les véhicules pour vous.")}

<h2>Les documents obligatoires</h2>
<ol class="num">
<li>la <strong>carte grise</strong> barrée, datée et signée par le vendeur, avec la mention « vendu le … » ;</li>
<li>le <strong>certificat de cession</strong> rempli et signé par les deux parties ;</li>
<li>un <strong>contrôle technique de moins de 6 mois</strong> si le véhicule a plus de 4 ans ;</li>
<li>le <strong>certificat de situation administrative</strong> (non-gage), de moins de 15 jours.</li>
</ol>

<h2>Payer en sécurité</h2>
<ul>
<li>ne versez <strong>jamais d'acompte</strong> à distance avant d'avoir vu le véhicule et le vendeur ;</li>
<li>préférez un <strong>virement instantané</strong> effectué au moment de la remise des clés et des documents ;</li>
<li>pour un chèque de banque, <strong>appelez vous-même la banque émettrice</strong> avec un numéro trouvé indépendamment.</li>
</ul>

<h2>Particulier ou professionnel : vos garanties</h2>
<p>Acheté à un professionnel, un véhicule d'occasion bénéficie de la <strong>garantie légale de conformité</strong>, en plus de la garantie des vices cachés. Entre particuliers, seule la garantie des vices cachés s'applique, et elle est plus difficile à faire valoir.</p>

<h2>La checklist avant de signer</h2>
<ul>
<li>Rapport HistoVec cohérent et sans gage</li>
<li>Kilométrage cohérent avec l'historique</li>
<li>Carnet d'entretien et factures</li>
<li>Contrôle technique récent, sans contre-visite non réalisée</li>
<li>Essai routier : démarrage à froid, freinage, boîte de vitesses, bruits</li>
<li>Numéro de châssis identique sur le véhicule et la carte grise</li>
<li>Paiement sécurisé au moment de la remise des documents</li>
</ul>
<p>Vous préférez déléguer ? Notre <a href="chasseur-automobile.html">service de chasseur automobile</a> s'occupe de toutes ces vérifications.</p>
""",
        "faq": [
            ("Comment savoir si une voiture d'occasion est gagée ?", "Demandez au vendeur le certificat de situation administrative, ou un rapport HistoVec, qui indique s'il existe un gage ou une opposition sur le véhicule."),
            ("Comment vérifier le kilométrage d'une voiture d'occasion ?", "Comparez le compteur avec les kilométrages relevés lors des contrôles techniques (visibles sur HistoVec) et avec les factures d'entretien, et observez l'usure de l'intérieur."),
            ("Quel moyen de paiement utiliser pour acheter une voiture à un particulier ?", "Un virement instantané effectué au moment de la remise des clés et des documents est le plus sûr. Pour un chèque de banque, vérifiez-le auprès de la banque émettrice avec un numéro trouvé par vos propres moyens."),
        ],
        "related": ["chasseur-automobile.html", "guide-importer-voiture-allemagne.html", "guide-lld-loa-credit-auto.html"],
    },
]

HUB = {
    "title": "Guides auto : import, carte grise, financement | Cohesif Auto",
    "description": "Guides pratiques pour acheter, importer et financer une voiture : import d'Allemagne, carte grise, TVA et malus, LLD ou LOA, occasion sans arnaque.",
    "h1": "Guides pratiques pour acheter, importer et financer votre voiture",
    "lead": "Des réponses claires aux questions que tout le monde se pose avant d'acheter une voiture, en France ou à l'étranger.",
}
