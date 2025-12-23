import os

# --- КОНФІГУРАЦІЯ (Тут ти керуєш усім) ---
IDENTITY = "UkrGeekLife | Андрій Івась"
NAV_MENU = """
<nav role="navigation" aria-label="Головне меню" class="main-nav">
    <a href="index.html" class="nav-link">[ ГОЛОВНА ]</a>
    <a href="about.html" class="nav-link">[ ПРО МЕНЕ ]</a>
    <a href="projects.html" class="nav-link">[ ПРОЄКТИ ]</a>
    <a href="contact.html" class="nav-link">[ ТЕРМІНАЛ ]</a>
</nav>
"""

# HTML Шаблон для звичайних сторінок (Адаптивний + Матриця)
BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>{title}</title>
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

# Контент для сторінок (Тут міняєш текст)
PAGES = {
    "index.html": {
        "title": f"Головна | {IDENTITY}",
        "content": "<h1>Вітаю в системі.</h1><p>Це цифровий простір Андрія Івася.</p>"
    },
    "about.html": {
        "title": f"Про Мене | {IDENTITY}",
        "content": "<h1>Хто я?</h1><p>Інженер. Патріот. Розробник.</p>"
    },
    "projects.html": {
        "title": f"Проєкти | {IDENTITY}",
        "content": "<h1>Мої розробки</h1><p>Системи автоматизації та веб-рішення.</p>"
    },
    "contact.html": {
        "title": f"Термінал | {IDENTITY}",
        "is_terminal": True # Маркер для спец-обробки
    }
}

def update_system():
    print(f"--- ЗАПУСК ПУБЛІКАЦІЇ: {IDENTITY} ---")
    
    for filename, data in PAGES.items():
        # Спеціальна логіка для Терміналу (Contact Page)
        if data.get("is_terminal"):
            html_content = f"""<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['title']}</title>
    <link rel="stylesheet" href="css/style.css">
    <style>body {{ overflow: hidden; }}</style> </head>
<body>
    <div class="matrix-bg"></div>
    <header>
        <div class="logo">{IDENTITY}</div>
        {NAV_MENU}
    </header>
    
    <div class="terminal-wrapper">
        <div id="history">
            <p>UkrGeekLife OS v2.0 initialized...</p>
            <p>Type 'help' for commands.</p>
        </div>
        <div class="input-line">
            <span class="prompt">guest@ukrgeek:~$</span>
            <input type="text" id="cmd" autofocus>
        </div>
    </div>

    <script src="js/matrix.js"></script>
    <script src="js/terminal.js"></script> </body>
</html>"""
        else:
            # Генерація звичайних сторінок
            html_content = BASE_TEMPLATE.format(
                title=data['title'],
                logo=IDENTITY,
                nav=NAV_MENU,
                content=data['content']
            )

        # ЗАПИС (UTF-8 ГАРАНТОВАНО)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"✅ Оновлено: {filename}")

if __name__ == "__main__":
    update_system()