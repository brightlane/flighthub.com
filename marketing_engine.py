import os
import random
from datetime import datetime

# =========================
# 🔗 AFFILIATE LINK
# =========================
AFFILIATE = "https://track.rqqft.com/aff_c?offer_id=25630&aff_id=21885"

# =========================
# 📁 OUTPUT FOLDER
# =========================
SITE_FOLDER = "site_output"
POST_FOLDER = f"{SITE_FOLDER}/posts"

os.makedirs(POST_FOLDER, exist_ok=True)

# =========================
# 🧠 KEYWORDS (SEO ENGINE)
# =========================
KEYWORDS = [
    "cheap flights to paris",
    "flight deals 2026",
    "last minute flights",
    "budget travel tips",
    "cheap international flights"
]

# =========================
# 🧾 SOCIAL POSTS ENGINE
# =========================
def social_posts():
    return {
        "facebook": f"✈️ Cheap flights made easy!\nCompare & save instantly:\n{AFFILIATE}",
        "instagram": f"✈️ Travel cheaper in 2026 🌍\nCompare flights instantly\n{AFFILIATE}",
        "twitter": f"Flights are cheaper when you compare ✈️\n{AFFILIATE}",
        "tiktok": f"Stop overpaying for flights!\nCompare now ✈️\n{AFFILIATE}"
    }

# =========================
# 📄 SEO PAGE GENERATOR
# =========================
def create_page(keyword):
    slug = keyword.replace(" ", "-") + ".html"
    path = f"{POST_FOLDER}/{slug}"

    html = f"""
    <html>
    <head>
        <title>{keyword.title()} | Flight Deals</title>
        <meta name="description" content="Find {keyword} and save money on travel deals.">
    </head>

    <body>
        <h1>{keyword.title()}</h1>

        <p>
            Discover the best {keyword} offers and save money by comparing airlines instantly.
        </p>

        <a href="{AFFILIATE}" style="padding:10px;background:red;color:white;">
            Book Now
        </a>
    </body>
    </html>
    """

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    return slug

# =========================
# 🗺 SITEMAP GENERATOR
# =========================
def create_sitemap(pages):
    today = datetime.today().strftime("%Y-%m-%d")

    xml = "<?xml version='1.0' encoding='UTF-8'?>\n"
    xml += "<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>\n"

    for p in pages:
        xml += f"""
  <url>
    <loc>https://yourdomain.com/posts/{p}</loc>
    <lastmod>{today}</lastmod>
  </url>
"""

    xml += "</urlset>"

    with open(f"{SITE_FOLDER}/sitemap.xml", "w") as f:
        f.write(xml)

# =========================
# 🚀 RUN SYSTEM
# =========================
def
