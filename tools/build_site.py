import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
BASE = "https://mnlmato.github.io"
PLAY = "https://play.google.com/store/apps/details?id=com.playink.paint.kids"


def play_link(lang):
    # Play Console groups listing visits and installs by these UTM values (G13).
    referrer = f"utm_source%3Dmnlmato.github.io%26utm_medium%3Dwebsite%26utm_campaign%3Dplayink-site-{lang}"
    return f"{PLAY}&referrer={referrer}"
VIDEO = "_KG6YSzw7Uo"
SITE_NAME = "Manuel Mato"
LASTMOD = "2026-10-27"
VERSION = "1.4.0"
MEDIUM = "https://medium.com/@manuelmato"
# The two articles about the holographic foil (G10). Each page links the one in its language.
ARTICLES = {
    "en": ("How a holographic foil effect works in Jetpack Compose",
           f"{MEDIUM}/how-a-holographic-foil-effect-works-in-jetpack-compose-9535d621c055"),
    "es": ("Cómo funciona una pegatina holográfica en un móvil Android",
           f"{MEDIUM}/c%C3%B3mo-funciona-una-pegatina-hologr%C3%A1fica-en-un-m%C3%B3vil-android-276e2c37768f"),
}

T = {
    "en": {
        "path": "/playink/",
        "title": "Playink: Scratch Art for Kids",
        "page_title": "Playink – Scratch Art App for Kids | Android",
        "desc": "Scratch art drawing for kids on Android: draw with a finger and reveal a holographic foil that shines as you tilt the phone. No ads, no in-app purchases, no account.",
        "locale": "en_US",
        "badge_alt": "Get it on Google Play",
        "eyebrow": "For Android phones and tablets",
        "h1a": "Scratch art for kids.", "h1b": "There's a hologram underneath.",
        "lede": "Draw with your finger and your phone or tablet becomes magic scratch paper. Every stroke reveals a holographic foil that shines as you tilt it.",
        "meta": "No ads · No purchases · No account",
        "wax_label": "Black demo sheet: drag your finger or mouse to scratch it and see the hologram",
        "reset": "New sheet", "hint": "Scratch here with your finger or mouse",
        "shots_eyebrow": "The app", "shots_h": "Five backgrounds, and every drawing shines differently",
        "shots": [
            ("shavings", "A cat drawn on the black layer, showing the holographic foil", "Feel the scratch: shavings fly"),
            ("hero-picker-glitter", "Background picker with holographic, glitter, gold and silver", "Holographic, glitter, gold and silver"),
            ("hero-gold", "The same drawing on a gold background", "Hidden colors that shine"),
            ("hero-silver", "The same drawing on a silver background", "Tilt your phone, watch it shine"),
            ("hero-eye", "Preview of the whole hidden foil", "Tap the eye to peek underneath"),
        ],
        "how_eyebrow": "How it works", "how_h": "Kids get it in seconds",
        "steps": [
            ("Draw", "Run your finger over the black layer."),
            ("Reveal", "Every stroke uncovers the foil underneath."),
            ("Tilt", "Move your phone and the light moves across the drawing."),
            ("Switch it up", "The magic wand picks another foil."),
        ],
        "fam_eyebrow": "For families", "fam_h": "Made for a child to use on their own",
        "fam_p": "Playink is part of the Google Play Families program. It collects no personal data and there is nothing to buy.",
        "promises": [
            ("Ads", "None"), ("In-app purchases", "None"), ("Account", "Not needed"),
            ("Personal data", "Not collected"), ("Crash reports", "Technical only, to fix bugs"),
            ("Drawings", "Saved to your gallery"),
        ],
        "fam_note": "The shiny backgrounds and video sharing need Android 13 or later. On earlier versions, every drawing reveals a color gradient.",
        "vid_eyebrow": "In motion", "vid_h": "The shine makes more sense on video",
        "vid_p": "The real app: scratching, switching foils and tilting the phone.",
        "vid_play": "Play the Playink video",
        "vid_note": "The video plays from YouTube. Nothing loads from YouTube until you press play.",
        "art_eyebrow": "Behind the hologram", "art_h": "How the holographic foil works",
        "art_p": "The foil isn't a video. It's a shader that works out the color of every pixel as you tilt the phone, imitating the colors of a soap bubble and the sparkle of glitter.",
        "art_link": "Read “{title}” on Medium",
        "faq_eyebrow": "Questions", "faq_h": "Questions parents ask",
        "faq": [
            ("Is Playink free?", "Yes. Playink is free, with no ads and no in-app purchases."),
            ("What is scratch art?", "Scratch art paper is a sheet covered with a black layer. When you scratch it, the colors underneath show through. Playink does the same on the screen, with a holographic foil underneath that moves as you tilt the phone."),
            ("Which devices does it work on?", "Android phones and tablets with Android 7.0 or later. The shiny backgrounds and video sharing need Android 13 or later; on earlier versions every drawing reveals a color gradient."),
            ("Does it need an internet connection?", "No. Drawing, saving and sharing work without a connection."),
            ("Does my child need an account?", "No. There is no sign-up and no login."),
            ("Is there an iPhone version?", "No. Playink is only available for Android, on Google Play."),
        ],
        "made": "Made by Manuel Mato, Android developer.",
        "tm": "Google Play and the Google Play logo are trademarks of Google LLC.",
    },
    "es": {
        "path": "/playink/es/",
        "title": "Playink: Dibujar y rascar",
        "page_title": "Playink – Dibujos para rascar para niños | Android",
        "desc": "Dibujos para rascar en Android: pinta con el dedo y descubre una lámina holográfica que brilla al inclinar el móvil. Sin anuncios, sin compras y sin cuenta.",
        "locale": "es_ES",
        "badge_alt": "Disponible en Google Play",
        "eyebrow": "Para móviles y tablets Android",
        "h1a": "Dibujos para rascar.", "h1b": "Debajo hay un holograma.",
        "lede": "Dibuja con el dedo y el móvil o la tablet se convierte en una lámina mágica para rascar. Cada trazo descubre una lámina holográfica que brilla al inclinarlo.",
        "meta": "Sin anuncios · Sin compras · Sin cuenta",
        "wax_label": "Lámina negra de demostración: arrastra el dedo o el ratón para rascarla y ver el holograma",
        "reset": "Otra lámina", "hint": "Rasca aquí con el dedo o el ratón",
        "shots_eyebrow": "La app", "shots_h": "Cinco fondos, y cada dibujo brilla distinto",
        "shots": [
            ("shavings", "Gato dibujado sobre la capa negra que deja ver el holograma", "Siente el rascado: saltan virutas"),
            ("hero-picker-glitter", "Selector de fondos con holográfico, purpurina, oro y plata", "Holográfico, purpurina, oro y plata"),
            ("hero-gold", "El mismo dibujo con fondo de oro", "Colores escondidos que brillan"),
            ("hero-silver", "El mismo dibujo con fondo de plata", "Inclina el móvil y el brillo se mueve"),
            ("hero-eye", "Vista previa de toda la lámina escondida", "Pulsa el ojo y mira lo que hay debajo"),
        ],
        "how_eyebrow": "Cómo funciona", "how_h": "Se aprende en segundos",
        "steps": [
            ("Dibuja", "Pasa el dedo por la capa negra."),
            ("Descubre", "Cada trazo deja ver la lámina de debajo."),
            ("Inclina", "Mueve el móvil y la luz recorre el dibujo."),
            ("Cambia el fondo", "La varita mágica elige otra lámina."),
        ],
        "fam_eyebrow": "Para familias", "fam_h": "Pensada para que un niño la use solo",
        "fam_p": "Playink está en el programa Familias de Google Play. No recoge datos personales y no hay nada que comprar.",
        "promises": [
            ("Anuncios", "Ninguno"), ("Compras dentro de la app", "Ninguna"), ("Cuenta", "No hace falta"),
            ("Datos personales", "No se recogen"), ("Informes de fallos", "Solo técnicos, para arreglar errores"),
            ("Dibujos", "Se guardan en tu galería"),
        ],
        "fam_note": "Los fondos brillantes y compartir como vídeo necesitan Android 13 o superior. En versiones anteriores cada dibujo descubre un degradado de colores.",
        "vid_eyebrow": "En movimiento", "vid_h": "El brillo se entiende mejor en vídeo",
        "vid_p": "La app de verdad: rascar, cambiar de fondo e inclinar el móvil.",
        "vid_play": "Reproducir el vídeo de Playink",
        "vid_note": "El vídeo se reproduce desde YouTube. No se carga nada de YouTube hasta que pulsas el botón.",
        "art_eyebrow": "Detrás del holograma", "art_h": "Cómo funciona la lámina holográfica",
        "art_p": "La lámina no es un vídeo. Es un shader que calcula el color de cada píxel según inclinas el móvil, imitando los colores de una pompa de jabón y el brillo de la purpurina.",
        "art_link": "Lee «{title}» en Medium",
        "faq_eyebrow": "Preguntas", "faq_h": "Lo que suelen preguntar los padres",
        "faq": [
            ("¿Playink es gratis?", "Sí. Playink es gratis, sin anuncios y sin compras dentro de la app."),
            ("¿Qué son los dibujos para rascar?", "Una lámina para rascar es una hoja cubierta por una capa negra. Al rascarla aparecen los colores de debajo. Playink hace lo mismo en la pantalla, con una lámina holográfica debajo que brilla al inclinar el móvil."),
            ("¿En qué dispositivos funciona?", "En móviles y tablets Android con Android 7.0 o superior. Los fondos brillantes y compartir como vídeo necesitan Android 13 o superior; en versiones anteriores cada dibujo descubre un degradado de colores."),
            ("¿Necesita conexión a internet?", "No. Dibujar, guardar y compartir funcionan sin conexión."),
            ("¿Mi hijo necesita una cuenta?", "No. No hay registro ni inicio de sesión."),
            ("¿Hay versión para iPhone?", "No. Playink solo está para Android, en Google Play."),
        ],
        "made": "Hecha por Manuel Mato, desarrollador Android.",
        "tm": "Google Play y el logotipo de Google Play son marcas de Google LLC.",
    },
}

ASSETS = "/playink/assets"


def page(lang):
    t = T[lang]
    url = BASE + t["path"]
    ld = {
        "@context": "https://schema.org",
        "@type": "MobileApplication",
        "name": "Playink",
        "operatingSystem": "Android",
        "applicationCategory": "EntertainmentApplication",
        "description": t["desc"],
        "url": url,
        "installUrl": PLAY,
        "image": f"{BASE}{ASSETS}/img/icon-256.png",
        "inLanguage": ["en", "es"],
        "softwareVersion": VERSION,
        "screenshot": [f"{BASE}{ASSETS}/img/{f}.jpg" for f, _, _ in t["shots"]],
        "sameAs": PLAY,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
        "author": {"@type": "Person", "name": "Manuel Mato", "url": BASE + "/"},
        "subjectOf": [
            {"@type": "Article", "headline": title, "url": link, "inLanguage": l}
            for l, (title, link) in ARTICLES.items()
        ],
    }
    art_title, art_url = ARTICLES[lang]
    shots = "\n".join(
        f'      <figure class="shot"><img src="{ASSETS}/img/{f}.jpg" alt="{alt}" width="540" height="1040" loading="lazy"><figcaption>{cap}</figcaption></figure>'
        for f, alt, cap in t["shots"]
    )
    steps = "\n".join(f"      <li><h3>{h}</h3><p>{p}</p></li>" for h, p in t["steps"])
    faq = "\n".join(f"        <div class=\"faq-item\"><dt>{q}</dt><dd>{a}</dd></div>" for q, a in t["faq"])
    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]],
    }
    promises = "\n".join(f"        <li><b>{b}</b><span>{s}</span></li>" for b, s in t["promises"])
    en_cur = ' aria-current="page"' if lang == "en" else ""
    es_cur = ' aria-current="page"' if lang == "es" else ""
    other_locale = "es_ES" if lang == "en" else "en_US"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t["page_title"]}</title>
<meta name="description" content="{t["desc"]}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{BASE}/playink/">
<link rel="alternate" hreflang="es" href="{BASE}/playink/es/">
<link rel="alternate" hreflang="x-default" href="{BASE}/playink/">
<meta name="theme-color" content="#0b0a10">
<link rel="icon" type="image/png" href="{ASSETS}/img/icon-64.png">
<link rel="apple-touch-icon" href="{ASSETS}/img/icon-180.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{t["title"]}">
<meta property="og:description" content="{t["desc"]}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}{ASSETS}/img/share-{lang}.jpg">
<meta property="og:image:width" content="1024">
<meta property="og:image:height" content="500">
<meta property="og:locale" content="{t["locale"]}">
<meta property="og:locale:alternate" content="{other_locale}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="{ASSETS}/fonts/fredoka-600.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{ASSETS}/fonts/atkinson-hyperlegible-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{ASSETS}/playink.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
</head>
<body>
<header class="site-header"><div class="wrap">
  <a class="brand" href="{t["path"]}"><img src="{ASSETS}/img/icon-64.png" alt="" width="40" height="40">Playink</a>
  <nav class="lang" aria-label="Language">
    <a href="/playink/" hreflang="en" lang="en"{en_cur}>EN</a>
    <a href="/playink/es/" hreflang="es" lang="es"{es_cur}>ES</a>
  </nav>
</div></header>

<main>
  <div class="hero"><div class="wrap">
    <div class="hero-copy">
      <p class="eyebrow">{t["eyebrow"]}</p>
      <h1>{t["h1a"]} <span class="foil-text">{t["h1b"]}</span></h1>
      <p class="lede">{t["lede"]}</p>
      <div class="cta-row">
        <a class="play-badge" href="{play_link(lang)}"><img class="badge-{lang}" src="{ASSETS}/img/badge-{lang}.png" alt="{t["badge_alt"]}" width="646" height="250"></a>
        <p class="meta">{t["meta"]}</p>
      </div>
    </div>
    <div class="sheet-frame">
      <div class="sheet" id="sheet">
        <canvas id="holo" aria-hidden="true"></canvas>
        <canvas id="wax" role="img" aria-label="{t["wax_label"]}"></canvas>
        <button type="button" class="sheet-reset" id="reset">{t["reset"]}</button>
        <p class="sheet-hint" id="hint">{t["hint"]}</p>
      </div>
    </div>
  </div></div>

  <section><div class="wrap">
    <div class="section-head">
      <p class="eyebrow">{t["shots_eyebrow"]}</p>
      <h2>{t["shots_h"]}</h2>
    </div>
    <div class="shots">
{shots}
    </div>
  </div></section>

  <section><div class="wrap">
    <div class="section-head">
      <p class="eyebrow">{t["how_eyebrow"]}</p>
      <h2>{t["how_h"]}</h2>
    </div>
    <ol class="steps">
{steps}
    </ol>
  </div></section>

  <section><div class="wrap family">
    <div class="section-head">
      <p class="eyebrow">{t["fam_eyebrow"]}</p>
      <h2>{t["fam_h"]}</h2>
      <p>{t["fam_p"]}</p>
    </div>
    <div>
      <ul class="promises">
{promises}
      </ul>
      <p class="family-note">{t["fam_note"]}</p>
    </div>
  </div></section>

  <section><div class="wrap">
    <div class="section-head">
      <p class="eyebrow">{t["faq_eyebrow"]}</p>
      <h2>{t["faq_h"]}</h2>
    </div>
    <dl class="faq">
{faq}
    </dl>
  </div></section>

  <section><div class="wrap video">
    <div class="video-frame">
      <button type="button" class="video-play" data-video="{VIDEO}" data-title="Playink - Holographic scratch art for kids" aria-label="{t["vid_play"]}">
        <img src="{ASSETS}/img/video-poster.jpg" alt="" width="1280" height="720" loading="lazy">
      </button>
    </div>
    <div class="video-copy">
      <p class="eyebrow">{t["vid_eyebrow"]}</p>
      <h2>{t["vid_h"]}</h2>
      <p>{t["vid_p"]}</p>
      <p class="small">{t["vid_note"]}</p>
    </div>
  </div></section>

  <section><div class="wrap">
    <div class="section-head">
      <p class="eyebrow">{t["art_eyebrow"]}</p>
      <h2>{t["art_h"]}</h2>
      <p>{t["art_p"]}</p>
      <p><a href="{art_url}">{t["art_link"].format(title=art_title)}</a></p>
    </div>
  </div></section>
</main>

<footer class="site-footer"><div class="wrap">
  <div class="legal"><p>{t["made"]}</p><p class="tm">{t["tm"]}</p></div>
  <nav aria-label="Links"><a href="https://www.linkedin.com/in/manuelmatomarino">LinkedIn</a><a href="{MEDIUM}">Medium</a></nav>
</div></footer>

<script src="{ASSETS}/playink.js" defer></script>
</body>
</html>
"""


WEBSITE = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": SITE_NAME,
    "alternateName": ["mnlmato", "mnlmato.github.io"],
    "url": BASE + "/",
}

PERSON = {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Manuel Mato",
    "jobTitle": "Android developer",
    "url": BASE + "/",
    "sameAs": ["https://www.linkedin.com/in/manuelmatomarino", "https://github.com/mnlmato", MEDIUM],
}

HOME = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Manuel Mato – Android developer</title>
<meta name="description" content="Manuel Mato, Android developer. Apps on Google Play, including Playink, a scratch art app for kids with a holographic foil.">
<link rel="canonical" href="{BASE}/">
<meta property="og:type" content="profile">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="Manuel Mato – Android developer">
<meta property="og:description" content="Apps I build and publish on Google Play, including Playink.">
<meta property="og:url" content="{BASE}/">
<meta property="og:image" content="{BASE}{ASSETS}/img/share-en.jpg">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps(WEBSITE, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(PERSON, ensure_ascii=False)}</script>
<meta name="theme-color" content="#0b0a10">
<link rel="icon" type="image/png" href="{ASSETS}/img/icon-64.png">
<link rel="preload" href="{ASSETS}/fonts/fredoka-600.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{ASSETS}/playink.css">
</head>
<body>
<main class="wrap home">
  <p class="eyebrow">Android developer</p>
  <h1>Manuel Mato</h1>
  <p class="lede">Apps I build and publish on Google Play.</p>
  <a class="project" href="/playink/">
    <img src="{ASSETS}/img/icon-256.png" alt="" width="72" height="72">
    <div><h2>Playink</h2><p>Scratch art for kids, with a holographic foil that shines as you tilt the phone.</p></div>
  </a>
  <p><a href="https://www.linkedin.com/in/manuelmatomarino">LinkedIn</a> · <a href="{MEDIUM}">Medium</a></p>
</main>
</body>
</html>
"""

SITEMAP = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>{BASE}/</loc>
    <lastmod>{LASTMOD}</lastmod>
  </url>
  <url>
    <loc>{BASE}/playink/</loc>
    <lastmod>{LASTMOD}</lastmod>
    <xhtml:link rel="alternate" hreflang="en" href="{BASE}/playink/"/>
    <xhtml:link rel="alternate" hreflang="es" href="{BASE}/playink/es/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}/playink/"/>
  </url>
  <url>
    <loc>{BASE}/playink/es/</loc>
    <lastmod>{LASTMOD}</lastmod>
    <xhtml:link rel="alternate" hreflang="en" href="{BASE}/playink/"/>
    <xhtml:link rel="alternate" hreflang="es" href="{BASE}/playink/es/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}/playink/"/>
  </url>
</urlset>
"""

NOT_FOUND = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Page not found</title>
<meta name="robots" content="noindex">
<meta name="theme-color" content="#0b0a10">
<link rel="icon" type="image/png" href="{ASSETS}/img/icon-64.png">
<link rel="stylesheet" href="{ASSETS}/playink.css">
</head>
<body>
<main class="wrap home">
  <p class="eyebrow">404</p>
  <h1>This page doesn't exist</h1>
  <p class="lede">Esta página no existe.</p>
  <a class="project" href="/playink/">
    <img src="{ASSETS}/img/icon-256.png" alt="" width="72" height="72">
    <div><h2>Playink</h2><p>Scratch art for kids · <span lang="es">Dibujos para rascar</span></p></div>
  </a>
</main>
</body>
</html>
"""

ROBOTS = f"""User-agent: *
Allow: /

Sitemap: {BASE}/sitemap.xml
"""

README = """# mnlmato.github.io

Personal site, served by GitHub Pages at https://mnlmato.github.io.

- `/` short home page.
- `/playink/` Playink in English (default), `/playink/es/` in Spanish.
- `playink/assets/` shared CSS, JS, self-hosted fonts (OFL) and images.
- `google23549ff51cca8ebe.html` verifies the site in Google Search Console. Do not delete it.
- `404.html` is the page GitHub Pages shows for missing URLs.
- `f56dbd5227f22322df7ee110829f2d0e.txt` is the IndexNow key, used to tell Bing and other search engines when pages change. Do not delete it.

Plain static files, no analytics, no cookies. The YouTube video only loads after pressing play.

The HTML pages, `sitemap.xml`, `robots.txt`, `404.html` and this README are generated by `tools/build_site.py`, so the English and Spanish pages stay in sync. Edit the texts there, not in the HTML, and run:

```bash
python3 tools/build_site.py .
```

CSS and JS live in `playink/assets/` and are edited by hand.

To preview locally:

```bash
python3 -m http.server 8000
```
"""

(ROOT / "playink" / "index.html").write_text(page("en"))
(ROOT / "playink" / "es" / "index.html").write_text(page("es"))
(ROOT / "index.html").write_text(HOME)
(ROOT / "sitemap.xml").write_text(SITEMAP)
(ROOT / "404.html").write_text(NOT_FOUND)
(ROOT / "robots.txt").write_text(ROBOTS)
(ROOT / "README.md").write_text(README)
print("ok")
