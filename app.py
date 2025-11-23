from flask import Flask, redirect, url_for, render_template_string

app = Flask(__name__)

# -------------------------------------------------------------------
# TEXT CONTENT (FR & EN)
# -------------------------------------------------------------------

content = {
    "fr": {
        "lang_code": "fr",
        "lang_name": "Français",
        "switch_lang_label": "English",
        "switch_lang_url": "/en",

        "meta_title": "Maison Vanille Suisse – Vanille d’exception pour artisans",
        "meta_description": "Maison Vanille Suisse, basée à Genève, fournit une vanille d’exception aux boulangeries, pâtisseries, chocolateries et restaurants en Suisse.",

        "navbar_brand": "Maison Vanille Suisse",
        "navbar_links": {
            "about": "Notre maison",
            "products": "Nos produits",
            "clients": "Pour qui ?",
            "order": "Commander",
            "contact": "Contact"
        },

        "hero_badge": "Importateur de vanille à Genève",
        "hero_title": "Vanille d’exception pour les artisans suisses",
        "hero_subtitle": (
            "Vanille Bourbon de Madagascar et d’Ouganda, "
            "sélectionnée avec soin et importée en petites quantités pour "
            "les boulangeries, pâtisseries, chocolateries et restaurants en Suisse."
        ),
        "hero_cta_primary": "Demander la liste de prix",
        "hero_cta_secondary": "Recevoir un échantillon",
        "hero_note": "Livraison dans toute la Suisse en 24–48h.",

        "why_title": "Pourquoi Maison Vanille Suisse ?",
        "why_intro": (
            "Nous combinons la rigueur suisse avec le savoir-faire des producteurs "
            "de vanille en Afrique de l’Est et dans l’océan Indien."
        ),
        "why_points": [
            "Vanille premium Grade A & B, sélectionnée à la main",
            "Teneur en humidité et arômes adaptés à la pâtisserie et au chocolat",
            "Traçabilité des lots et relation directe avec les producteurs",
            "Import en petites quantités, fraîcheur maximale",
            "Service réactif et livraison rapide depuis Genève"
        ],

        "products_title": "Nos vanilles",
        "products": [
            {
                "name": "Bourbon Madagascar – Grade A",
                "details": [
                    "Longueur : 15–18 cm",
                    "Humidité : 30–33%",
                    "Profil aromatique : floral, crémeux, riche en vanilline"
                ],
                "price": "À partir de CHF 260 / kg (B2B, selon lot)"
            },
            {
                "name": "Vanille d’Ouganda – Grade A",
                "details": [
                    "Longueur : 14–17 cm",
                    "Humidité : 28–32%",
                    "Profil aromatique : chocolaté, chaud, idéal pour glaces et pâtisserie"
                ],
                "price": "À partir de CHF 215 / kg (B2B, selon lot)"
            },
            {
                "name": "Vanille d’Ouganda – Grade B",
                "details": [
                    "Parfaite pour infusions, macérations, sirops et préparations chaudes"
                ],
                "price": "À partir de CHF 150 / kg"
            },
            {
                "name": "Vanille pour extrait / découpes",
                "details": [
                    "Matière première à fort pouvoir aromatique pour extraction ou R&D"
                ],
                "price": "À partir de CHF 90 / kg"
            }
        ],
        "products_note": "Les prix dépendent du lot et des disponibilités. Une liste de prix actualisée peut être envoyée sur simple demande.",

        "clients_title": "Pour quels clients ?",
        "clients_intro": "Nous travaillons avec des professionnels exigeants partout en Suisse :",
        "clients_list": [
            "Pâtisseries et chocolateries",
            "Boulangeries artisanales",
            "Glaciers et fabricants de gelato",
            "Restaurants, hôtels et traiteurs",
            "Laboratoires R&D et marques de boissons artisanales"
        ],
        "clients_minimum": "Quantité minimale : 1 kg par commande. Conditions spéciales dès 5 kg.",

        "about_title": "Notre maison",
        "about_text": (
            "Maison Vanille Suisse est née à Genève avec une idée simple : "
            "offrir aux artisans suisses une vanille d’exception, traçable et "
            "sélectionnée avec soin auprès de petits producteurs. "
            "Nous privilégions des relations durables avec les familles de producteurs "
            "en Ouganda et à Madagascar, et importons en petites quantités pour "
            "garantir la fraîcheur des gousses. "
            "Chaque lot est dégusté, contrôlé et préparé avant son arrivée à Genève."
        ),
        "about_values_title": "Nos engagements",
        "about_values": [
            "Qualité avant tout",
            "Traçabilité et respect des producteurs",
            "Approvisionnement en petits lots, fraîcheur garantie",
            "Service suisse, simple et transparent"
        ],

        "order_title": "Comment commander ?",
        "order_steps": [
            "1. Demandez la liste de prix et les lots disponibles.",
            "2. Choisissez le type de vanille et le volume adaptés à votre usage (pâtisserie, chocolat, glace, infusion…).",
            "3. Nous confirmons la disponibilité, le prix et le délai de livraison.",
            "4. Livraison depuis Genève en 24–48h partout en Suisse."
        ],
        "order_options": [
            "Échantillons possibles (kit découverte, CHF 10–20).",
            "Commande minimale : 1 kg.",
            "Conditions avantageuses dès 5 kg et pour les commandes mensuelles."
        ],

        "contact_title": "Contact",
        "contact_intro": "Vous souhaitez recevoir notre liste de prix, un échantillon ou discuter d’un besoin spécifique ?",
        "contact_company": "Maison Vanille Suisse",
        "contact_city": "Genève, Suisse",
        "contact_email_label": "E-mail",
        "contact_phone_label": "Téléphone",
        "contact_form_title": "Formulaire de contact",
        "contact_form_fields": {
            "name": "Nom",
            "business": "Entreprise / Boulangerie",
            "email": "E-mail",
            "volume": "Volume souhaité (en kg)",
            "application": "Application (pâtisserie, chocolat, glace, etc.)",
            "message": "Message"
        },
        "contact_form_button": "Envoyer la demande",

        "footer_text": "© 2025 Maison Vanille Suisse — Genève, Suisse. Vanille d’exception pour artisans."
    },

    "en": {
        "lang_code": "en",
        "lang_name": "English",
        "switch_lang_label": "Français",
        "switch_lang_url": "/",

        "meta_title": "Maison Vanille Suisse – Exceptional Vanilla for Swiss Artisans",
        "meta_description": "Maison Vanille Suisse, based in Geneva, supplies exceptional vanilla beans to bakeries, pastry shops, chocolatiers, restaurants and hotels across Switzerland.",

        "navbar_brand": "Maison Vanille Suisse",
        "navbar_links": {
            "about": "Our Story",
            "products": "Our Vanilla",
            "clients": "Who We Serve",
            "order": "How to Order",
            "contact": "Contact"
        },

        "hero_badge": "Vanilla importer in Geneva",
        "hero_title": "Exceptional Vanilla for Swiss Artisans",
        "hero_subtitle": (
            "Bourbon Madagascar and Ugandan vanilla, carefully selected and "
            "imported in small batches for bakeries, pastry shops, chocolatiers "
            "and restaurants throughout Switzerland."
        ),
        "hero_cta_primary": "Request price list",
        "hero_cta_secondary": "Request a sample",
        "hero_note": "Deliveries within Switzerland in 24–48 hours.",

        "why_title": "Why Maison Vanille Suisse?",
        "why_intro": (
            "We combine Swiss precision with the craftsmanship of vanilla growers "
            "in East Africa and the Indian Ocean."
        ),
        "why_points": [
            "Premium Grade A & B vanilla, hand–selected",
            "Moisture and aroma tailored for pastry and chocolate",
            "Traceable lots and direct relationships with growers",
            "Small–batch imports for maximum freshness",
            "Responsive service and fast delivery from Geneva"
        ],

        "products_title": "Our Vanilla Collection",
        "products": [
            {
                "name": "Bourbon Madagascar – Grade A",
                "details": [
                    "Length: 15–18 cm",
                    "Moisture: 30–33%",
                    "Aroma: floral, creamy, high vanillin content"
                ],
                "price": "From CHF 260 / kg (B2B, depending on batch)"
            },
            {
                "name": "Uganda Vanilla – Grade A",
                "details": [
                    "Length: 14–17 cm",
                    "Moisture: 28–32%",
                    "Aroma: chocolaty, warm, ideal for gelato and pastry"
                ],
                "price": "From CHF 215 / kg (B2B, depending on batch)"
            },
            {
                "name": "Uganda Vanilla – Grade B",
                "details": [
                    "Perfect for infusions, macerations, syrups and hot preparations"
                ],
                "price": "From CHF 150 / kg"
            },
            {
                "name": "Extract–grade / cuts",
                "details": [
                    "High–aroma material for extraction or R&D"
                ],
                "price": "From CHF 90 / kg"
            }
        ],
        "products_note": "Prices depend on the batch and availability. A current price list can be sent on request.",

        "clients_title": "Who We Serve",
        "clients_intro": "We work with discerning professionals across Switzerland:",
        "clients_list": [
            "Pastry shops and chocolatiers",
            "Artisanal bakeries",
            "Ice cream and gelato makers",
            "Restaurants, hotels and catering",
            "R&D labs and craft beverage brands"
        ],
        "clients_minimum": "Minimum order: 1 kg per order. Preferential terms from 5 kg.",

        "about_title": "Our Story",
        "about_text": (
            "Maison Vanille Suisse was founded in Geneva with a simple idea: "
            "to offer Swiss artisans exceptional, traceable vanilla, carefully "
            "selected from small producers. We build long–term relationships with "
            "families of growers in Uganda and Madagascar, and import in small "
            "quantities to guarantee freshness. Each batch is tasted, checked and "
            "prepared before arriving in Geneva."
        ),
        "about_values_title": "Our Values",
        "about_values": [
            "Quality above all",
            "Traceability and respect for growers",
            "Small–batch sourcing, guaranteed freshness",
            "Swiss service – simple and transparent"
        ],

        "order_title": "How to Order",
        "order_steps": [
            "1. Request the price list and available batches.",
            "2. Choose the vanilla type and volume suited to your application (pastry, chocolate, ice cream, infusion, etc.).",
            "3. We confirm availability, price and delivery time.",
            "4. Delivery from Geneva within 24–48 hours anywhere in Switzerland."
        ],
        "order_options": [
            "Sample kits available (discovery kit, CHF 10–20).",
            "Minimum order: 1 kg.",
            "Preferential terms from 5 kg and for monthly contracts."
        ],

        "contact_title": "Contact",
        "contact_intro": "Want to receive our price list, a sample or discuss a specific need?",
        "contact_company": "Maison Vanille Suisse",
        "contact_city": "Geneva, Switzerland",
        "contact_email_label": "E-mail",
        "contact_phone_label": "Phone",
        "contact_form_title": "Contact Form",
        "contact_form_fields": {
            "name": "Name",
            "business": "Business / Bakery",
            "email": "E-mail",
            "volume": "Desired volume (kg)",
            "application": "Application (pastry, chocolate, ice cream, etc.)",
            "message": "Message"
        },
        "contact_form_button": "Send request",

        "footer_text": "© 2025 Maison Vanille Suisse — Geneva, Switzerland. Exceptional vanilla for artisans."
    }
}

# -------------------------------------------------------------------
# BASE TEMPLATE (TAILWIND VIA CDN) – NO IMAGES
# -------------------------------------------------------------------

TEMPLATE = r"""
<!DOCTYPE html>
<html lang="{{ c.lang_code }}">
<head>
    <meta charset="utf-8">
    <title>{{ c.meta_title }}</title>
    <meta name="description" content="{{ c.meta_description }}">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Tailwind CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-stone-50 text-stone-900">
    <!-- NAVBAR -->
    <header class="border-b border-stone-200 bg-white/80 backdrop-blur">
        <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <div class="flex items-center gap-2">
                <div class="w-8 h-8 rounded-full bg-amber-900"></div>
                <span class="font-semibold tracking-wide text-stone-900">
                    {{ c.navbar_brand }}
                </span>
            </div>
            <nav class="hidden md:flex gap-6 text-sm">
                <a href="#about" class="hover:text-amber-800">{{ c.navbar_links.about }}</a>
                <a href="#products" class="hover:text-amber-800">{{ c.navbar_links.products }}</a>
                <a href="#clients" class="hover:text-amber-800">{{ c.navbar_links.clients }}</a>
                <a href="#order" class="hover:text-amber-800">{{ c.navbar_links.order }}</a>
                <a href="#contact" class="hover:text-amber-800">{{ c.navbar_links.contact }}</a>
            </nav>
            <div class="flex items-center gap-3">
                <a href="{{ c.switch_lang_url }}" class="text-xs border rounded-full px-3 py-1 hover:bg-stone-100">
                    {{ c.switch_lang_label }}
                </a>
            </div>
        </div>
    </header>

    <!-- HERO -->
    <main>
        <section class="bg-gradient-to-br from-amber-900 via-amber-800 to-stone-900 text-stone-50">
            <div class="max-w-6xl mx-auto px-4 py-16 md:py-24 grid md:grid-cols-2 gap-12 items-center">
                <div>
                    <div class="inline-flex items-center gap-2 rounded-full border border-amber-500/50 bg-amber-900/40 px-3 py-1 text-xs text-amber-100">
                        <span class="w-2 h-2 rounded-full bg-amber-300"></span>
                        <span>{{ c.hero_badge }}</span>
                    </div>
                    <h1 class="mt-4 text-3xl md:text-4xl font-semibold tracking-tight">
                        {{ c.hero_title }}
                    </h1>
                    <p class="mt-4 text-amber-100/90 leading-relaxed">
                        {{ c.hero_subtitle }}
                    </p>
                    <p class="mt-3 text-[11px] uppercase tracking-[0.2em] text-amber-200/80">
                        {{ c.hero_note }}
                    </p>
                    <div class="mt-6 flex flex-wrap gap-3">
                        <a href="#contact"
                           class="inline-flex items-center justify-center rounded-full bg-amber-300 px-6 py-2.5 text-sm font-medium text-amber-950 shadow-sm hover:bg-amber-200">
                            {{ c.hero_cta_primary }}
                        </a>
                        <a href="#contact"
                           class="inline-flex items-center justify-center rounded-full border border-amber-300/70 bg-transparent px-6 py-2.5 text-sm font-medium text-amber-50 hover:bg-amber-900/40">
                            {{ c.hero_cta_secondary }}
                        </a>
                    </div>
                </div>
                <div class="relative">
                    <!-- Simple decorative block instead of image -->
                    <div class="rounded-3xl border border-amber-500/40 bg-gradient-to-br from-amber-200/20 via-amber-100/10 to-stone-900/10 h-56 md:h-72 flex items-center justify-center">
                        <div class="text-center px-6">
                            <p class="text-xs uppercase tracking-[0.3em] text-amber-200/80">Maison Vanille Suisse</p>
                            <p class="mt-3 text-sm text-amber-50/90">
                                Sélection de lots de vanille Bourbon, triés à la main et importés en petits volumes pour garantir fraîcheur et constance.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- WHY -->
        <section id="about" class="py-16 md:py-20 bg-stone-50">
            <div class="max-w-6xl mx-auto px-4 grid md:grid-cols-2 gap-10">
                <div>
                    <h2 class="text-2xl md:text-3xl font-semibold text-stone-900">
                        {{ c.why_title }}
                    </h2>
                    <p class="mt-4 text-stone-700 leading-relaxed">
                        {{ c.why_intro }}
                    </p>
                </div>
                <div class="grid gap-3">
                    {% for point in c.why_points %}
                    <div class="flex items-start gap-3">
                        <div class="mt-1 w-5 h-5 rounded-full bg-amber-800 flex items-center justify-center">
                            <span class="text-[11px] text-white">✓</span>
                        </div>
                        <p class="text-sm text-stone-700">{{ point }}</p>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </section>

        <!-- PRODUCTS -->
        <section id="products" class="py-16 md:py-20 bg-stone-100">
            <div class="max-w-6xl mx-auto px-4">
                <h2 class="text-2xl md:text-3xl font-semibold text-stone-900 text-center">
                    {{ c.products_title }}
                </h2>
                <div class="mt-10 grid md:grid-cols-2 gap-6">
                    {% for p in c.products %}
                    <div class="bg-white rounded-2xl shadow-sm border border-stone-200 p-6 flex flex-col justify-between">
                        <div>
                            <h3 class="text-lg font-semibold text-stone-900">{{ p.name }}</h3>
                            <ul class="mt-3 space-y-1 text-sm text-stone-700">
                                {% for d in p.details %}
                                <li>• {{ d }}</li>
                                {% endfor %}
                            </ul>
                        </div>
                        <p class="mt-4 text-sm font-medium text-amber-900">{{ p.price }}</p>
                    </div>
                    {% endfor %}
                </div>
                <p class="mt-6 text-center text-sm text-stone-600 max-w-2xl mx-auto">
                    {{ c.products_note }}
                </p>
            </div>
        </section>

        <!-- CLIENTS + ABOUT -->
        <section id="clients" class="py-16 md:py-20 bg-stone-50">
            <div class="max-w-5xl mx-auto px-4 grid md:grid-cols-2 gap-10">
                <div>
                    <h2 class="text-2xl md:text-3xl font-semibold text-stone-900">
                        {{ c.clients_title }}
                    </h2>
                    <p class="mt-4 text-stone-700 leading-relaxed">
                        {{ c.clients_intro }}
                    </p>
                    <ul class="mt-4 space-y-1 text-sm text-stone-700">
                        {% for cl in c.clients_list %}
                        <li>• {{ cl }}</li>
                        {% endfor %}
                    </ul>
                    <p class="mt-4 text-sm font-medium text-amber-900">
                        {{ c.clients_minimum }}
                    </p>
                </div>
                <div>
                    <h3 class="text-lg font-semibold text-stone-900">
                        {{ c.about_title }}
                    </h3>
                    <p class="mt-3 text-sm text-stone-700 leading-relaxed">
                        {{ c.about_text }}
                    </p>
                    <h4 class="mt-4 text-sm font-semibold text-stone-900">
                        {{ c.about_values_title }}
                    </h4>
                    <ul class="mt-2 space-y-1 text-sm text-stone-700">
                        {% for v in c.about_values %}
                        <li>• {{ v }}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
        </section>

        <!-- ORDER -->
        <section id="order" class="py-16 md:py-20 bg-stone-100">
            <div class="max-w-5xl mx-auto px-4 grid md:grid-cols-2 gap-10">
                <div>
                    <h2 class="text-2xl md:text-3xl font-semibold text-stone-900">
                        {{ c.order_title }}
                    </h2>
                    <ol class="mt-4 space-y-2 text-sm text-stone-700">
                        {% for step in c.order_steps %}
                        <li>{{ step }}</li>
                        {% endfor %}
                    </ol>
                </div>
                <div class="bg-white rounded-2xl border border-stone-200 p-6 shadow-sm">
                    <h3 class="text-sm font-semibold text-stone-900">
                        Options & conditions
                    </h3>
                    <ul class="mt-3 space-y-1 text-sm text-stone-700">
                        {% for opt in c.order_options %}
                        <li>• {{ opt }}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
        </section>

        <!-- CONTACT -->
        <section id="contact" class="py-16 md:py-20 bg-stone-50">
            <div class="max-w-5xl mx-auto px-4 grid md:grid-cols-2 gap-10">
                <div>
                    <h2 class="text-2xl md:text-3xl font-semibold text-stone-900">
                        {{ c.contact_title }}
                    </h2>
                    <p class="mt-4 text-sm text-stone-700">
                        {{ c.contact_intro }}
                    </p>
                    <div class="mt-6 space-y-1 text-sm text-stone-800">
                        <p class="font-semibold">{{ c.contact_company }}</p>
                        <p>{{ c.contact_city }}</p>
                        <p>{{ c.contact_email_label }} :
                            <a href="mailto:contact@maisonvanillesuisse.ch" class="text-amber-900 underline">
                                contact@maisonvanillesuisse.ch
                            </a>
                        </p>
                        <p>{{ c.contact_phone_label }} :
                            <span class="text-stone-800">+41 xx xxx xx xx</span>
                        </p>
                    </div>
                    <div class="mt-4">
                        <a href="https://wa.me/" class="inline-flex items-center rounded-full border border-emerald-600 px-4 py-2 text-xs font-medium text-emerald-700 hover:bg-emerald-50">
                            WhatsApp
                        </a>
                    </div>
                </div>
                <div class="bg-stone-50 rounded-2xl border border-stone-200 p-6">
                    <h3 class="text-sm font-semibold text-stone-900">
                        {{ c.contact_form_title }}
                    </h3>
                    <form class="mt-4 grid gap-3 text-sm">
                        <div>
                            <label class="block mb-1">{{ c.contact_form_fields.name }}</label>
                            <input type="text" class="w-full rounded-lg border border-stone-300 px-3 py-2 text-sm" placeholder="">
                        </div>
                        <div>
                            <label class="block mb-1">{{ c.contact_form_fields.business }}</label>
                            <input type="text" class="w-full rounded-lg border border-stone-300 px-3 py-2 text-sm" placeholder="">
                        </div>
                        <div>
                            <label class="block mb-1">{{ c.contact_form_fields.email }}</label>
                            <input type="email" class="w-full rounded-lg border border-stone-300 px-3 py-2 text-sm" placeholder="">
                        </div>
                        <div>
                            <label class="block mb-1">{{ c.contact_form_fields.volume }}</label>
                            <input type="text" class="w-full rounded-lg border border-stone-300 px-3 py-2 text-sm" placeholder="">
                        </div>
                        <div>
                            <label class="block mb-1">{{ c.contact_form_fields.application }}</label>
                            <input type="text" class="w-full rounded-lg border border-stone-300 px-3 py-2 text-sm" placeholder="">
                        </div>
                        <div>
                            <label class="block mb-1">{{ c.contact_form_fields.message }}</label>
                            <textarea rows="3" class="w-full rounded-lg border border-stone-300 px-3 py-2 text-sm"></textarea>
                        </div>
                        <button type="button" class="mt-2 inline-flex items-center justify-center rounded-full bg-amber-800 px-5 py-2 text-xs font-medium text-white hover:bg-amber-900">
                            {{ c.contact_form_button }}
                        </button>
                        <p class="text-[11px] text-stone-500 mt-1">
                            (Formulaire de démonstration : à connecter plus tard à un e-mail ou un backend.)
                        </p>
                    </form>
                </div>
            </div>
        </section>
    </main>

    <!-- FOOTER -->
    <footer class="border-t border-stone-200 bg-white">
        <div class="max-w-6xl mx-auto px-4 py-4 text-xs text-stone-500 flex flex-col md:flex-row items-center justify-between gap-2">
            <span>{{ c.footer_text }}</span>
        </div>
    </footer>
</body>
</html>
"""

# -------------------------------------------------------------------
# ROUTES
# -------------------------------------------------------------------

@app.route("/")
def index_fr():
    c = content["fr"]
    return render_template_string(TEMPLATE, c=c)

@app.route("/en")
def index_en():
    c = content["en"]
    return render_template_string(TEMPLATE, c=c)

@app.route("/fr")
def redirect_fr():
    return redirect(url_for("index_fr"))

# -------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
