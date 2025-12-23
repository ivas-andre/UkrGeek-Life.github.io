import os

html_template = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <div class="content">{content}</div>
</body>
</html>
"""

pages = {
    "login.html": {"title": "Login", "content": "<h1>Enter Matrix</h1>"}
}

for filename, data in pages.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_template.format(title=data["title"], content=data["content"]))
    print(f"Generated {filename}")