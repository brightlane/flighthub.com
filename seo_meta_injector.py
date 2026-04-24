import os
from bs4 import BeautifulSoup

# =========================
# 🌐 CONFIG
# =========================
SITE_NAME = "FlightHub Deals"
DOMAIN = "https://brightlane.github.io/Flights/"
DEFAULT_IMAGE = "https://via.placeholder.com/1200x630.png?text=FlightHub"

# =========================
# 🧠 BUILD META TAGS
# =========================
def build_meta(title, description, url):
    return f"""
<meta charset="UTF-8">

<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="index, follow">

<link rel="canonical" href="{url}">

<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DEFAULT_IMAGE}">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{DEFAULT_IMAGE}">
"""

# =========================
# 🔧 INJECT META INTO FILE
# =========================
def inject_meta(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # Get existing title or fallback
    title = soup.title.string if soup.title else "FlightHub Travel Deals"

    # Get description or fallback
    desc_tag = soup.find("meta", attrs={"name": "description"})
    description = desc_tag["content"] if desc_tag else "Find cheap flights and travel deals."

    # Build full URL
    file_name = os.path.basename(file_path)
    url = DOMAIN + file_name

    meta_block = build_meta(title, description, url)

    # Ensure head exists
    if not soup.head:
        head = soup.new_tag("head")
        soup.html.insert(0, head)
    else:
        head = soup.head

    # Inject ONLY ONCE (avoid duplicates)
    if "og:title" not in str(soup):
        head.append(BeautifulSoup(meta_block, "html.parser"))

    # SAVE FILE
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(f"✔ Meta injected: {file_path}")

# =========================
# 📂 SCAN ALL HTML FILES
# =========================
def run(folder="Flights"):

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                inject_meta(path)

    print("\n🚀 DONE - ALL PAGES OPTIMIZED")

# =========================
# ▶ RUN
# =========================
if __name__ == "__main__":
    run()
