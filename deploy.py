# -*- coding: utf-8 -*-
import os, sys, subprocess, time, random

# --- CONFIGURATION ---
IDENTITY = "UkrGeekLife | Andrii Ivas"
sys.stdout.reconfigure(encoding='utf-8')

# SOCIAL LINKS (NO TELEGRAM)
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
    "SPOTIFY": "https://open.spotify.com/user/ivas_andre" 
}
VIDEO_ID = "-h7ygd0mp7c"

def run(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ Executed: {cmd}")
    except:
        print(f"ℹ️ Git: Ready.")

print("--- READING DATA ---")
try:
    with open("about_me.txt", "r", encoding="utf-8") as f: BASE_ABOUT = f.read()
except: BASE_ABOUT = "<h1>ERROR</h1><p>File missing.</p>"

# --- CONTENT BLOCKS ---

# IDENTITY PAGE (HAL 9000 LINKS)
HAL_LINKS = f"""
<div style="margin-top:40px;border-top:2px solid #333;padding-top:20px;">
    <h2 style="color:#FFF;letter-spacing:2px;">> DIRECT_UPLINK_CHANNELS</h2>
    <div class="hal-grid">
        <a href="{LINKS['YOUTUBE']}" target="_blank" class="hal-btn"><div class="hal-eye"></div><span>YOUTUBE_CORE</span></a>
        <a href="{LINKS['INSTA_MAIN']}" target="_blank" class="hal-btn"><div class="hal-eye"></div><span>LIFE_LOGS</span></a>
        <a href="{LINKS['INSTA_PHOTO']}" target="_blank" class="hal-btn"><div class="hal-eye"></div><span>VISUAL_DATA</span></a>
        <a href="{LINKS['LINKEDIN']}" target="_blank" class="hal-btn"><div class="hal-eye"></div><span>CAREER_NET</span></a>
        <a href="{LINKS['GITHUB']}" target="_blank" class="hal-btn"><div class="hal-eye"></div><span>CODE_REPO</span></a>
        <a href="{LINKS['FACEBOOK']}" target="_blank" class="hal-btn"><div class="hal-eye"></div><span>FACEBOOK</span></a>
        <a href="{LINKS['X']}" target="_blank" class="hal-btn"><div class="hal-eye"></div><span>X_SIGNAL</span></a>
        <a href="{LINKS['TWITCH']}" target="_blank" class="hal-btn"><div class="hal-eye"></div><span>LIVE_FEED</span></a>
    </div>
</div>
"""
ABOUT_CONTENT = BASE_ABOUT + HAL_LINKS

# PHOTO PAGE (GRID + SNAPWIDGET)
PHOTO_CONTENT = """
<h1>/MNT/DCIM/GALLERY_GRID</h1>
<p>Visual Database. Multiple streams connected.</p>
<div class="photo-grid-container">
    <div class="widget-box">
        <div class="widget-header">CAM_01: MAIN_FEED</div>
        <iframe src="https://snapwidget.com/embed/1115084" class="snapwidget-widget" allowtransparency="true" frameborder="0" scrolling="no" style="border:none; overflow:hidden; width:100%; height:100%" title="Posts from Instagram"></iframe>
    </div>
    <div class="widget-box placeholder"><div class="widget-header">CAM_02: SIGNAL_LOST</div><div class="static-noise">NO SIGNAL</div></div>
    <div class="widget-box placeholder"><div class="widget-header">CAM_03: OFFLINE</div><div class="static-noise">Waiting for uplink...</div></div>
    <div class="widget-box placeholder"><div class="widget-header">CAM_04: OFFLINE</div><div class="static-noise">Waiting for uplink...</div></div>
</div>
"""

# TERMINAL CONTENT (RESTORED FUNCTIONALITY)
CONTACT_CONTENT = """
<h1>Terminal Access</h1>
<div class='terminal-window'>
    <div id='history'>
        <p>UkrGeekLife OS v17.0 (Restored)...</p>
        <p>Type 'help' for commands.</p>
    </div>
    <div class='input-line'>
        <span class='prompt'>root@ukrgeek:~#</span>
        <input type='text' id='cmd' autofocus autocomplete='off' enterkeyhint='go'>
    </div>
</div>
"""

INDEX_CONTENT = """<h1>SYSTEM INDEX</h1><p>Welcome to <strong>UkrGeekLife</strong>.</p><ul style="list-style:none;padding:0;"><li><strong>01. Who The Fuck Am I:</strong> Engineer. Patriot.</li><li><strong>02. Pure Hate:</strong> 500k dead. No mercy.</li><li><strong>03. Vegetarian:</strong> 10+ years.</li><li><strong>04. No Gods:</strong> Atheist protocol.</li><li><strong>05. Automation:</strong> Scripts > Humans.</li><li><strong>06. Python:</strong> My weapon.</li><li><strong>07. Void:</strong> ADHD/OCD Survivor.</li><li><strong>08. Zoo:</strong> 4 cats, 2 dogs.</li><li><strong>09. UX Nazi:</strong> Design matters.</li><li><strong>10. Open Source:</strong> Share knowledge.</li></ul>"""
PROJECTS_CONTENT = """<h1>ARSENAL</h1><ul><li><strong>Growing Box:</strong> Hydroponics automation.</li><li><strong>Lighting:</strong> Spectrum control.</li><li><strong>Global Box:</strong> Modular architecture.</li></ul><h2>SOCIAL</h2><ul><li><strong>Volunteer Cats:</strong> Helping animals.</li></ul>"""
VIDEO_CONTENT = f"""<h1>/VAR/VIDEO</h1><div class="video-wrapper"><iframe id="main-player" width="100%" height="450" src="https://www.youtube.com/embed/{VIDEO_ID}" frameborder="0" allowfullscreen></iframe></div>"""
BLOG_CONTENT = """<h1>/SYS/LOG</h1><div class="log-entry"><span class="highlight">[2025]</span> REBOOT. New philosophy.</div>"""
PODCAST_CONTENT = """<h1>/AUDIO</h1><div class="alert">Audio modules offline.</div>"""

# --- CSS CODE ---
CSS_CODE = """
body { background-color: #050505; color: #0F0; font-family: 'Courier New', monospace; margin: 0; padding: 0; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
#matrix-bg { position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.15; }
header { background: #1a1a1a; border-bottom: 1px solid #333; padding: 10px 15px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; }
.header-social { display: flex; gap: 15px; }
.social-icon { color: #888; font-size: 1.2rem; text-decoration: none; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; border: 1px solid #333; background: rgba(0,0,0,0.5); border-radius: 4px; }
.social-icon:hover { color: #0F0; border-color: #0F0; box-shadow: 0 0 8px #0F0; }

nav { display: flex; gap: 10px; }
nav a { color: #FFF; text-decoration: none; font-size: 0.9rem; padding: 5px; }
nav a:hover { color: #0F0; background: #111; }
@media(max-width: 900px) { nav { display: none; } }

.container { flex: 1; max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #333; background: rgba(0, 0, 0, 0.9); }
h1, h2 { border-bottom: 1px solid #0F0; color: #FFF; }
.alert { border: 1px solid #F00; color: #F88; padding: 10px; }
.video-wrapper { border: 2px solid #0F0; padding: 5px; background: #000; }

/* HAL 9000 GRID */
.hal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 15px; margin-top: 20px; }
.hal-btn { display: flex; flex-direction: column; align-items: center; padding: 15px; border: 1px solid #444; background: #111; color: #888; text-decoration: none; transition: 0.3s; }
.hal-eye { width: 20px; height: 20px; background: #300; border-radius: 50%; margin-bottom: 10px; border: 2px solid #500; box-shadow: 0 0 5px #500; transition: 0.3s; }
.hal-btn:hover { border-color: #F00; color: #FFF; background: #000; }
.hal-btn:hover .hal-eye { background: #F00; border-color: #FFF; box-shadow: 0 0 15px #F00; transform: scale(1.2); }

/* PHOTO GRID */
.photo-grid-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 20px; }
.widget-box { border: 1px solid #0F0; height: 400px; display: flex; flex-direction: column; background: #000; }
.widget-header { background: #002200; color: #0F0; padding: 5px; font-size: 0.8rem; border-bottom: 1px solid #0F0; }
.widget-box iframe { flex: 1; }
.placeholder .widget-header { background: #222; color: #888; border-color: #555; }
.static-noise { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; color: #444; background: repeating-linear-gradient(0deg, #111, #111 2px, #222 3px); }

/* FOOTER (ICONS RESTORED) */
footer { border-top: 1px dashed #0F0; padding: 20px; text-align: center; font-size: 0.8rem; color: #555; margin-top: auto; }
.footer-links { margin-top: 10px; }
.footer-links a { color: #555; margin: 0 10px; font-size: 1.2rem; transition: 0.3s; }
.footer-links a:hover { color: #FFF; text-shadow: 0 0 5px #FFF; }
.burger-menu { cursor: pointer; display: none; color: #0F0; font-weight: bold; } 
@media(max-width: 900px) { .burger-menu { display: block; } }

/* TERMINAL FIXES */
.terminal-window { background: #111; border: 1px solid #0F0; padding: 15px; height: 50vh; overflow-y: auto; font-family: 'Courier New', monospace; font-size: 1rem; text-align: left; }
.input-line { display: flex; align-items: center; }
.prompt { color: #0F0; margin-right: 10px; font-weight: bold; white-space: nowrap; }
input#cmd { background: transparent; border: none; color: #FFF; font-family: 'Courier New', monospace; font-size: 1rem; flex-grow: 1; outline: none; width: 100%; }
#typewriter-content { visibility: hidden; }
.cursor::after { content: '█'; animation: blink 1s infinite; color: #0F0; margin-left: 5px; }
@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
"""

# --- JS CODE (RESTORED TYPEWRITER & TERMINAL) ---
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

function killSystem() { document.body.innerHTML='<div style="display:flex;justify-content:center;align-items:center;height:100vh;background:#000;color:red;font-size:2rem;">SYSTEM HALTED</div>'; }
function toggleMenu() { 
    let nav = document.querySelector('nav');
    if(nav.style.display==='flex') nav.style.display='none'; 
    else { nav.style.display='flex'; nav.style.flexDirection='column'; nav.style.position='fixed'; nav.style.top='50px'; nav.style.right='0'; nav.style.background='#000'; nav.style.border='1px solid #0F0'; }
}

// LIVE TYPEWRITER RESTORED
document.addEventListener("DOMContentLoaded", function() {
    const element = document.getElementById('typewriter-content');
    if (element) {
        const text = element.innerHTML;
        element.innerHTML = "";
        element.classList.add("cursor");
        element.style.visibility = "visible";
        let i = 0;
        function type() {
            if (i < text.length) {
                if (text.charAt(i) === '<') {
                    let tag = "";
                    while (text.charAt(i) !== '>' && i < text.length) { tag += text.charAt(i); i++; }
                    tag += '>'; i++; element.innerHTML += tag;
                } else { element.innerHTML += text.charAt(i); i++; }
                setTimeout(type, 3);
            }
        }
        type();
    }
    
    // TERMINAL LOGIC RESTORED
    const input = document.getElementById("cmd");
    const history = document.getElementById("history");
    if(input) {
        input.focus();
        document.querySelector('.terminal-window').addEventListener('click', () => input.focus());
        input.addEventListener("keydown", function(e) {
            if (e.key === "Enter") {
                const rawCmd = input.value.trim();
                const cmd = rawCmd.toLowerCase();
                history.innerHTML += `<div><span class="prompt">root@ukrgeek:~#</span> ${rawCmd}</div>`;
                let res = "";
                switch(cmd) {
                    case "help": res = "COMMANDS: [about] [projects] [video] [photo] [blog] [email] [slava] [kill]"; break;
                    case "about": window.location='about.html'; break;
                    case "projects": window.location='projects.html'; break;
                    case "photo": window.location='photo.html'; break;
                    case "video": window.location='video.html'; break;
                    case "blog": window.location='blog.html'; break;
                    case "slava": res = "<span style='color:yellow'>GEROYAM SLAVA! 🇺🇦</span>"; break;
                    case "kill": killSystem(); break;
                    case "clear": history.innerHTML = ""; break;
                    case "": res = ""; break;
                    default: res = `<span style='color:red'>bash: ${rawCmd}: command not found</span>`;
                }
                if(cmd !== "clear" && res !== "") history.innerHTML += `<div style='color:#DDD'>${res}</div>`;
                input.value = "";
                document.querySelector('.terminal-window').scrollTop = document.querySelector('.terminal-window').scrollHeight;
            }
        });
    }
});
"""

# --- TEMPLATES ---
BASE_HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title}</title>
<link rel="stylesheet" href="css/style.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head><body><canvas id="matrix-bg"></canvas>
<header>
    <div style="display:flex; gap:10px;"><div class="dot red" style="width:12px;height:12px;background:#f55;border-radius:50%;cursor:pointer;" onclick="killSystem()"></div><span style="color:#888;font-weight:bold;">root@ukrgeek:~</span></div>
    <div class="header-social">
        <a href="{yt}" class="social-icon"><i class="fab fa-youtube"></i></a>
        <a href="{im}" class="social-icon"><i class="fab fa-instagram"></i></a>
        <a href="{fb}" class="social-icon"><i class="fab fa-facebook"></i></a>
        <a href="{li}" class="social-icon"><i class="fab fa-linkedin"></i></a>
    </div>
    <nav>
        <a href="index.html">/HOME</a><a href="about.html">/IDENTITY</a><a href="projects.html">/ARSENAL</a>
        <a href="photo.html">/PHOTO</a><a href="video.html">/VIDEO</a><a href="blog.html">/BLOG</a>
        <a href="contact.html">/TERMINAL</a>
    </nav>
    <div class="burger-menu" onclick="toggleMenu()">[MENU]</div>
</header>
<main class="container"><div id="typewriter-content">{content}</div></main>
<footer>
    <div style="margin-bottom:10px;">[ SYSTEM RESOURCES: 4 CATS | 2 DOGS | 1 RAT | 1 TURTLE ]</div>
    <div class="footer-links">
        <a href="{x}"><i class="fab fa-twitter"></i></a><a href="{tu}"><i class="fab fa-tumblr"></i></a>
        <a href="{tw}"><i class="fab fa-twitch"></i></a><a href="{gh}"><i class="fab fa-github"></i></a>
        <a href="{sp}"><i class="fab fa-spotify"></i></a>
    </div>
    <div style="margin-top:10px;opacity:0.5;font-size:0.7rem;">© 2025 {id} | NO FORGIVENESS</div>
    </footer>
<script src="js/main.js"></script>
</body></html>"""

# --- EXECUTION ---
print("--- WRITING FILES ---")
os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)
with open("css/style.css", "w", encoding="utf-8") as f: f.write(CSS_CODE)
with open("js/main.js", "w", encoding="utf-8") as f: f.write(JS_MAIN)

pages = {
    "index.html": INDEX_CONTENT, "about.html": ABOUT_CONTENT, "projects.html": PROJECTS_CONTENT,
    "photo.html": PHOTO_CONTENT, "video.html": VIDEO_CONTENT, "blog.html": BLOG_CONTENT,
    "podcast.html": PODCAST_CONTENT, "contact.html": CONTACT_CONTENT
}

for fname, content in pages.items():
    html = BASE_HTML.format(
        title=f"{fname} | {IDENTITY}", content=content, id=IDENTITY, rnd=random.random(),
        yt=LINKS['YOUTUBE'], im=LINKS['INSTA_MAIN'], fb=LINKS['FACEBOOK'], li=LINKS['LINKEDIN'],
        x=LINKS['X'], tu=LINKS['TUMBLR'], tw=LINKS['TWITCH'], gh=LINKS['GITHUB'], sp=LINKS['SPOTIFY']
    )
    with open(fname, "w", encoding="utf-8") as f: f.write(html)
    print(f"✅ {fname}")

print("--- DEPLOYING ---")
time.sleep(1)
run("git add .")
run(f'git commit -m "UkrGeekLife | Fixed Terminal & Icons | {time.strftime("%H:%M:%S")}"')
run("git push origin master")
print(">>> DONE. EVERYTHING RESTORED.")