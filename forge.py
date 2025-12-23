import json
import os
from bs4 import BeautifulSoup

def build():
    # Андрію, тут ми використовуємо utf-8-sig, щоб ігнорувати BOM
    if not os.path.exists('site_data.json'):
        print("Error: site_data.json not found")
        return

    with open('site_data.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    
    with open('index.html', 'r', encoding='utf-8') as f:
        template = f.read()

    for page in data['pages']:
        soup = BeautifulSoup(template, 'html.parser')
        if soup.title: soup.title.string = page['title']
        
        main_area = soup.find('main') or soup.find(id='app_content')
        if main_area:
            main_area.clear()
            main_area.append(BeautifulSoup(page['content'], 'html.parser'))
        
        # Автоматичний пошук Google у хедері
        if soup.header and not soup.find(id='google-search'):
            search_box = '<div id="google-search" class="m-2"><script async src="https://cse.google.com/cse.js?cx=YOUR_ID"></script><div class="gcse-search"></div></div>'
            soup.header.append(BeautifulSoup(search_box, 'html.parser'))

        with open(f"{page['name']}.html", 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
        print(f"✅ Success: {page['name']}.html")

if __name__ == "__main__":
    build()
