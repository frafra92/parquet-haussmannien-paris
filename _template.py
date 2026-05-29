# Shared template parts for satellite site
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">'

NAV = '''<nav>
  <div class="nav-inner">
    <a href="index.html" class="nav-brand">Parquet Haussmannien · Paris</a>
    <div class="nav-links">
      <a href="histoire.html">Histoire</a>
      <a href="point-de-hongrie.html">Point de Hongrie</a>
      <a href="essences.html">Essences</a>
      <a href="restauration.html">Restauration</a>
      <a href="glossaire.html">Glossaire</a>
      <a href="artisan.html">L'artisan</a>
    </div>
  </div>
</nav>'''

FOOTER = '''<footer>
  <div class="footer-inner">
    <div>
      <div class="footer-brand">Parquet Haussmannien Paris</div>
      <p class="footer-text">Encyclopédie du patrimoine parquet parisien.<br>Contenu éditorial indépendant.</p>
    </div>
    <div class="footer-links">
      <a href="index.html">Accueil</a>
      <a href="histoire.html">Histoire</a>
      <a href="essences.html">Essences de bois</a>
      <a href="glossaire.html">Glossaire</a>
      <a href="artisan.html">L'artisan</a>
      <a href="https://poncageparquetvitrificationfrancois.com/" target="_blank" rel="noopener">→ Site de François Gaillard</a>
    </div>
  </div>
</footer>'''

def page(title, desc, canonical, content, schema=None):
    schema_tag = f'<script type="application/ld+json">{schema}</script>' if schema else ''
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:locale" content="fr_FR">
{FONTS}
<link rel="stylesheet" href="style.css">
{schema_tag}
</head>
<body>
{NAV}
<main>
{content}
</main>
{FOOTER}
</body>
</html>'''
