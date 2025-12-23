# -*- coding: utf-8 -*-
import os
import sys

# 1. FORCING UTF-8 ENVIRONMENT
# Це змушує Python ігнорувати системне кодування Windows і використовувати UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# 2. IDENTITY CONFIGURATION (Тут твоє ім'я)
IDENTITY = "UkrGeekLife | Андрій Івась"

# 3. HTML TEMPLATES
NAV_MENU = """
<nav role="navigation" aria-label="Головне меню" class="main-nav">
    <a href="index.html" class="nav-link">[ ГОЛОВНА ]</a>
    <a href="about.html" class="nav-link">[ ПРО МЕНЕ ]</a>
    <a href="projects.html" class="nav-link">[ ПРОЄКТИ ]</a>
    <a href="contact.html" class="nav-link">[ ТЕРМІНАЛ ]</a>
</nav>
"""

BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="matrix-bg"></div>
    <header>
        <div class="logo">{logo}</div>
        {nav}
    </header>
    <main class="container">
        {content}
    </main>
    <script src="js/matrix.js"></script>
</body>
</html>"""

PAGES = {
    "index.html": {
        "title": f"Головна | {IDENTITY}",
        "content": "<h1>System Online</h1><p>Welcome to UkrGeekLife.</p>"
    },
    "about.html": {
        "title": f"Про Мене | {IDENTITY}",
        "content": "<h1>Identity Verification</h1><p>Андрій Івась. Engineer.</p>"
    },
    "contact.html": {
        "title": f"Термінал | {IDENTITY}",
        "is_terminal": True
    }
}

def generate():
    print(f"--- GENERATING SITE: {IDENTITY} ---")
    
    for filename, data in PAGES.items():
        if data.get("is_terminal"):
            # Окрема структура для терміналу
            html = f"""<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>{data['title']}</title>
    <link rel="stylesheet" href="css/style.css">
    <style>body {{ overflow: hidden; }}</style>
</head>
<body>
    <div class="matrix-bg"></div>
    <header><div class="logo">{IDENTITY}</div>{NAV_MENU}</header>
    <div class="terminal-wrapper">
        <div id="history"><p>UkrGeekLife OS v2.0</p></div>
        <div class="input-line"><span class="prompt">guest@ukrgeek:~$</span><input type="text" id="cmd" autofocus></div>
    </div>
    <script src="js/matrix.js"></script>
    <script src="js/terminal.js"></script>
</body>
</html>"""
        else:
            html = BASE_TEMPLATE.format(
                title=data['title'],
                logo=IDENTITY,
                nav=NAV_MENU,
                content=data['content']
            )

        # 4. WRITING FILE (The Fix)
        # encoding="utf-8" вирішує проблему кракозябрів назавжди.
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ Saved: {filename}")

if __name__ == "__main__":
    generate()