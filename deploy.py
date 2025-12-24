# -*- coding: utf-8 -*-
import os, sys, subprocess, time, random

# --- 1. CONFIGURATION ---
IDENTITY = "UkrGeekLife | Andrii Ivas"
sys.stdout.reconfigure(encoding='utf-8')

# SOCIAL LINKS
LINKS = {
    "YOUTUBE": "https://www.youtube.com/@UkrGeekLife",
    "INSTA_MAIN": "https://www.instagram.com/ivas_andrii/",
    "INSTA_PHOTO": "https://www.instagram.com/andrii_photographer/",
    "FACEBOOK": "https://www.facebook.com/Andrii.Ivas/", 
    "LINKEDIN": "https://www.linkedin.com/in/ivas-andre/", 
    "X": "https://x.com/Andrii_Ivas",
    "TUMBLR": "https://www.tumblr.com/andre-ivas",
    "TWITCH": "https://www.twitch.tv/ivas_andre",
    "GITHUB": "https://github.com/ivas-andre",
    "SPOTIFY": "https://open.spotify.com/playlist/1BG0k1dDJN14PczoyvSD6T?si=JVz8SvIGQHeba0XCCsulzQ" 
}
VIDEO_ID = "-h7ygd0mp7c"

def run(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ Executed: {cmd}")
    except:
        print(f"ℹ️ Git status: Nothing to commit or ready.")

# --- 2. CONTENT GENERATION ---

print("--- READING about_me.txt ---")
try:
    with open("about_me.txt", "r", encoding="utf-8") as f: BASE_ABOUT = f.read()
except: BASE_ABOUT = "<h1>ERROR</h1><p>File missing.</p>"

# IDENTITY PAGE with HOVER REVEAL (ALIEN STYLE)
IDENTITY_EXTRAS = f"""
<div class="data-core-container">
    <div class="data-core-trigger">
        <span class="core-label">[ HOVER TO ACCESS DATA_CORE ]</span>
        <div class="hidden-links">
            <a href="video.html">/VIDEO_STREAM</a>
            <a href="photo.html">/PHOTO_GRID</a>
            <a href="blog.html">/SYS_LOGS</a>
            <a href="podcast.html">/AUDIO_FEED</a>
            <a href="{LINKS['SPOTIFY']}" target="_blank">/SPOTIFY_VIBE</a>
        </div>
    </div>
</div>
<div style="margin-top:20px; border-top:1px dashed #0F0; padding-top:10px;">
    <h3>> SOCIAL_UPLINKS</h3>
    <div class="text-links">
        <a href="{LINKS['YOUTUBE']}" target="_blank">[YOUTUBE]</a>
        <a href="{LINKS['INSTA_MAIN']}" target="_blank">[INSTA_MAIN]</a>
        <a href="{LINKS['INSTA_PHOTO']}" target="_blank">[INSTA_PHOTO]</a>
        <a href="{LINKS['LINKEDIN']}" target="_blank">[LINKEDIN]</a>
        <a href="{LINKS['GITHUB']}" target="_blank">[GITHUB]</a>
    </div>
</div>
"""
ABOUT_CONTENT = BASE_ABOUT + IDENTITY_EXTRAS

# PHOTO PAGE (3 COLUMNS DESKTOP / 1 MOBILE)
PHOTO_CONTENT = """
<h1>/MNT/DCIM/GALLERY</h1>
<p>Visual logs. Reality capture.</p>
<div class="photo-grid">
    <div class="grid-item">
        <div class="item-header">:: CAM_01 [LIVE] ::</div>
        <iframe src="https://snapwidget.com/embed/1115084" class="snapwidget-widget" allowtransparency="true" frameborder="0" scrolling="no" style="border:none; overflow:hidden; width:100%; height:100%" title="Posts from Instagram"></iframe>
    </div>
    <div class="grid-item placeholder">
        <div class="item-header">:: CAM_02 [OFFLINE] ::</div>
        <div class="noise">NO SIGNAL</div>
    </div>
    <div class="grid-item placeholder">
        <div class="item-header">:: CAM_03 [OFFLINE] ::</div>
        <div class="noise">WAITING UPLINK...</div>
    </div>
    <div class="grid-item placeholder">
        <div class="item-header">:: CAM_04 [OFFLINE] ::</div>
        <div class="noise">STATIC...</div>
    </div>
    <div class="grid-item placeholder">
        <div class="item-header">:: CAM_05 [OFFLINE] ::</div>
        <div class="noise">...</div>
    </div>
    <div class="grid-item placeholder">
        <div class="item-header">:: CAM_06 [OFFLINE] ::</div>
        <div class="noise">...</div>
    </div>
</div>
"""

INDEX_CONTENT = """<h1>SYSTEM INDEX</h1><p>Welcome to <strong>UkrGeekLife</strong>.</p><ul style="list-style:none;padding:0;"><li><strong>01. Who The Fuck Am I:</strong> Engineer. Patriot.</li><li><strong>02. Pure Hate:</strong> 500k dead. No mercy.</li><li><strong>03. Vegetarian:</strong> 10+ years.</li><li><strong>04. No Gods:</strong> Atheist protocol.</li><li><strong>05. Automation:</strong> Scripts > Humans.</li><li><strong>06. Python:</strong> My weapon.</li><li><strong>07. Void:</strong> ADHD/OCD Survivor.</li><li><strong>08. Zoo:</strong> 4 cats, 2 dogs.</li><li><strong>09. UX Nazi:</strong> Design matters.</li><li><strong>10. Open Source:</strong> Share knowledge.</li></ul>"""
PROJECTS_CONTENT = """<h1>ARSENAL</h1><ul><li><strong>Growing Box:</strong> Hydroponics automation.</li><li><strong>Lighting:</strong> Spectrum control.</li><li><strong>Global Box:</strong> Modular architecture.</li></ul><h2>SOCIAL</h2><ul><li><strong>Volunteer Cats:</strong> Helping animals.</li></ul>"""
VIDEO_CONTENT = f"""<h1>/VAR/VIDEO</h1><div class="video-wrapper"><iframe id="main-player" width="100%" height="450" src="https://www.youtube.com/embed/{VIDEO_ID}" frameborder="0" allowfullscreen></iframe></div>"""
BLOG_CONTENT = """<h1>/SYS/LOG</h1><div class="log-entry"><span class="highlight">[2025]</span> REBOOT. New philosophy.</div>"""
PODCAST_CONTENT = """<h1>/AUDIO</h1><div class="alert">Audio modules offline.</div>"""

# --- 3. CSS (RESPONSIVE FIX + HOVER EFFECT) ---
CSS_CODE = """
/* BASE */
body { background-color: #050505; color: #0F0; font-family: 'Courier New', monospace; margin: 0; padding: 0; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
#matrix-bg { position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.15; }

/* HEADER (LINUX STYLE) */
header { background: #111; border-bottom: 2px solid #333; padding: 10px 20px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; }
.window-controls { display: flex; gap: 8px; }
.dot { width: 12px; height: 12px; border-radius: 50%; }
.red { background: #ff5f56; cursor: pointer; } .yellow { background: #ffbd2e; } .green { background: #27c93f; }
.win-title { color: #666; font-weight: bold; letter-spacing: 1px; }

/* NAVIGATION (FLEXIBLE) */
nav { display: flex; gap: 15px; }
nav a { color: #AAA; text-decoration: none; font-size: 1rem; font-weight: bold; transition: 0.3s; }
nav a:hover { color: #0F0; text-shadow: 0 0 5px #0F0; }
.burger-menu { display: none; cursor: pointer; color: #0F0; font-size: 1.5rem; }

/* RESPONSIVE NAV */
@media (max-width: 768px) {
    nav { display: none; flex-direction: column; position: absolute; top: 50px; right: 0; background: #000; border: 1px solid #0F0; width: 200px; padding: 10px; }
    nav.active { display: flex; }
    .burger-menu { display: block; }
    .win-title { display: none; }
}

/* CONTAINER */
.container { flex: 1; width: 90%; max-width: 1200px; margin: 20px auto; padding: 20px; border: 1px solid #333; background: rgba(0, 0, 0, 0.9); box-sizing: border-box; }
h1 { border-bottom: 2px solid #0F0; color: #FFF; padding-bottom: 5px; }
h2 { border-bottom: 1px solid #333; color: #DDD; margin-top: 20px; }
.alert { border: 1px solid #F00; color: #F00; padding: 10px; background: rgba(50,0,0,0.2); }

/* IDENTITY HOVER EFFECT (ALIEN/DATA CORE) */
.data-core-container { margin-top: 30px; perspective: 1000px; }
.data-core-trigger { 
    background: #050505; border: 1px solid #0F0; padding: 15px; 
    text-align: center; transition: all 0.5s ease; cursor: pointer; position: relative; overflow: hidden;
}
.core-label { font-size: 1.2rem; font-weight: bold; }
.hidden-links { 
    max-height: 0; opacity: 0; transition: all 0.5s ease; 
    display: flex; flex-direction: column; gap: 10px; margin-top: 0;
}
/* HOVER STATE */
.data-core-trigger:hover { border-color: #F00; background: #100; box-shadow: 0 0 20px rgba(255,0,0,0.3); }
.data-core-trigger:hover .core-label { color: #F00; letter-spacing: 3px; }
.data-core-trigger:hover .hidden-links { max-height: 200px; opacity: 1; margin-top: 15px; }
.hidden-links a { color: #FFF; text-decoration: none; border-left: 2px solid #F00; padding-left: 10px; }
.hidden-links a:hover { background: #300; color: #F00; }

/* PHOTO GRID (RESPONSIVE) */
.photo-grid { display: grid; gap: 20px; margin-top: 20px; }
/* DESKTOP: 3 COLS */
@media (min-width: 900px) { .photo-grid { grid-template-columns: repeat(3, 1fr); } }
/* TABLET: 2 COLS */
@media (min-width: 600px) and (max-width: 899px) { .photo-grid { grid-template-columns: repeat(2, 1fr); } }
/* MOBILE: 1 COL */
@media (max-width: 599px) { .photo-grid { grid-template-columns: 1fr; } }

.grid-item { border: 1px solid #333; background: #000; height: 400px; display: flex; flex-direction: column; transition: 0.3s; }
.grid-item:hover { border-color: #0F0; box-shadow: 0 0 10px rgba(0,255,0,0.2); }
.item-header { background: #111; color: #888; padding: 5px; font-size: 0.8rem; border-bottom: 1px solid #333; font-family: monospace; }
.grid-item iframe { flex: 1; width: 100%; height: 100%; }
.placeholder .noise { flex: 1; display: flex; align-items: center; justify-content: center; color: #333; background: repeating-linear-gradient(45deg, #000, #000 5px, #111 5px, #111 10px); }

/* FOOTER (OLD SCHOOL TEXT BACK) */
footer { border-top: 2px solid #0F0; background: #020202; padding: 20px; text-align: center; color: #666; margin-top: auto; }
.zoo-list { color: #004400; font-size: 0.9rem; margin-bottom: 10px; letter-spacing: 1px; }
.zoo-list:hover { color: #0F0; }
.text-links a { color: #666; margin: 0 5px; text-decoration: none; }
.text-links a:hover { color: #FFF; text-decoration: underline; }
"""

# --- 4. JS ---
JS_MAIN = """
const canvas = document.getElementById('matrix-bg');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth; canvas.height = window.innerHeight;
const chars = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ0123456789'.split('');
const fontSize = 14; const columns = canvas.width/fontSize;
const drops = []; for(let x=0; x<columns; x++) drops[x]=1;
function draw() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)'; ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#0F0'; ctx.font = fontSize + 'px monospace';
    for(let i=0; i<drops.length; i++) {
        const text = chars[Math.floor(Math.random()*chars.length)];
        ctx.fillText(text, i*fontSize, drops[i]*fontSize);
        if(drops[i]*fontSize > canvas.height && Math.random() > 0.975) drops[i]=0;
        drops[i]++;
    }
}
setInterval(draw, 33);
window.addEventListener('resize', () => { canvas.width = window.innerWidth; canvas.height = window.innerHeight; });

function killSystem() { document.body.innerHTML='<div style="display:flex;justify-content:center;align-items:center;height:100vh;background:#000;color:red;font-size:3rem;font-family:monospace;">SYSTEM PURGED</div>'; }
function toggleMenu() { document.querySelector('nav').classList.toggle('active'); }
"""

# --- 5. TEMPLATES & BUILD ---
BASE_HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title}</title>
<link rel="stylesheet" href="css/style.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head><body><canvas id="matrix-bg"></canvas>
<header>
    <div style="display:flex; gap:10px; align-items:center;">
        <div class="window-controls"><div class="dot red" onclick="killSystem()"></div><div class="dot yellow"></div><div class="dot green"></div></div>
        <span class="win-title">root@ukrgeek:~</span>
    </div>
    <div class="burger-menu" onclick="toggleMenu()">[MENU]</div>
    <nav>
        <a href="index.html">/HOME</a><a href="about.html">/IDENTITY</a><a href="projects.html">/ARSENAL</a>
        <a href="photo.html">/PHOTO</a><a href="video.html">/VIDEO</a><a href="blog.html">/BLOG</a>
        <a href="contact.html">/TERMINAL</a>
    </nav>
</header>
<main class="container">{content}</main>
<footer>
    <div class="zoo-list">[ ZOO: 4 CATS | 2 DOGS | 1 RAT | 1 TURTLE ]</div>
    <div class="text-links">
        <a href="{yt}" target="_blank">YOUTUBE</a> | <a href="{tg}" target="_blank">TELEGRAM</a> | <a href="{gh}" target="_blank">GITHUB</a> | <a href="{x}" target="_blank">X</a>
    </div>
    <div style="margin-top:10px;font-size:0.7rem;">© 2025 {id} | NO FORGIVENESS</div>
    </footer>
<script src="js/main.js"></script>
</body></html>"""

print("--- WRITING FILES ---")
os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)
with open("css/style.css", "w", encoding="utf-8") as f: f.write(CSS_CODE)
with open("js/main.js", "w", encoding="utf-8") as f: f.write(JS_MAIN)

pages = {
    "index.html": INDEX_CONTENT, "about.html": ABOUT_CONTENT, "projects.html": PROJECTS_CONTENT,
    "photo.html": PHOTO_CONTENT, "video.html": VIDEO_CONTENT, "blog.html": BLOG_CONTENT,
    "podcast.html": PODCAST_CONTENT, "contact.html": "<h1>TERMINAL</h1><p>Ready.</p>"
}

for fname, content in pages.items():
    html = BASE_HTML.format(
        title=f"{fname} | {IDENTITY}", content=content, id=IDENTITY, rnd=random.random(),
        yt=LINKS['YOUTUBE'], tg="https://t.me/UkrGeekLife", gh=LINKS['GITHUB'], x=LINKS['X']
    )
    with open(fname, "w", encoding="utf-8") as f: f.write(html)
    print(f"✅ {fname}")

print("--- DEPLOYING ---")
time.sleep(1)
run("git add .")
run(f'git commit -m "UkrGeekLife | Responsive Fix & Hover Core | {time.strftime("%H:%M:%S")}"')
run("git push origin master")
print(">>> DONE.")