# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import time
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

# --- CONFIGURATION ---
IDENTITY = "UkrGeekLife | Andrii Ivas"
PORT = 8000

# Force UTF-8
sys.stdout.reconfigure(encoding='utf-8')

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(f"✅ Executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e.stderr}")

# --- ASSETS ---

CSS_CODE = """
body { background-color: #000; color: #0F0; font-family: 'Courier New', monospace; margin: 0; padding: 0; min-height: 100vh; display: flex; flex-direction: column; }
#matrix-bg { position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.15; }
header { background: rgba(0, 20, 0, 0.95); border-bottom: 2px solid #0F0; padding: 15px 0; text-align: center; position: sticky; top: 0; z-index: 100; }
.logo { font-size: 1.5rem; font-weight: bold; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 10px; text-shadow: 0 0 10px #0F0; }
nav a { color: #FFF; text-decoration: none; margin: 0 15px; font-size: 1.1rem; font-weight: bold; transition: 0.3s; }
nav a:hover { color: #0F0; text-shadow: 0 0 8px #0F0; }
.container { flex: 1; max-width: 900px; margin: 40px auto; padding: 20px; background: rgba(0, 0, 0, 0.8); border: 1px solid #333; width: 90%; }
h1, h2 { border-bottom: 1px solid #0F0; padding-bottom: 10px; text-transform: uppercase; }
p, li { font-size: 1.1rem; line-height: 1.6; }
.red-alert { color: #FF3333; font-weight: bold; }
.highlight { color: #FFF; font-weight: bold; }
.dim { color: #555; }
footer { border-top: 2px solid #0F0; background: #020202; text-align: center; padding: 30px; margin-top: auto; font-size: 0.9rem; color: #666; }
.footer-links a { color: #AAA; text-decoration: none; margin: 0 10px; font-weight: bold; }
.footer-links a:hover { color: #0F0; text-decoration: underline; }
/* Typing Cursor */
.cursor::after { content: '█'; animation: blink 1s infinite; color: #0F0; margin-left: 5px; }
@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
/* Terminal Window */
.terminal-window { background: #111; border: 1px solid #0F0; padding: 20px; height: 60vh; overflow-y: auto; font-family: 'Courier New', monospace; }
.input-line { display: flex; align-items: center; }
.prompt { color: #0F0; margin-right: 10px; font-weight: bold; }
input#cmd { background: transparent; border: none; color: #FFF; font-family: 'Courier New', monospace; font-size: 1.2rem; flex-grow: 1; outline: none; }
#typewriter-content { visibility: hidden; }
"""

JS_MATRIX = """
const canvas = document.getElementById('matrix-bg');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
const fontSize = 16;
const columns = canvas.width/fontSize;
const drops = [];
for(let x=0; x<columns; x++) drops[x]=1;
function draw() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#0F0';
    ctx.font = fontSize + 'px monospace';
    for(let i=0; i<drops.length; i++) {
        const text = chars[Math.floor(Math.random()*chars.length)];
        ctx.fillText(text, i*fontSize, drops[i]*fontSize);
        if(drops[i]*fontSize > canvas.height && Math.random() > 0.975) drops[i]=0;
        drops[i]++;
    }
}
setInterval(draw, 33);
window.addEventListener('resize', () => { canvas.width = window.innerWidth; canvas.height = window.innerHeight; });
"""

JS_TYPEWRITER = """
document.addEventListener("DOMContentLoaded", function() {
    const element = document.getElementById('typewriter-content');
    if (!element) return;
    const text = element.innerHTML;
    element.innerHTML = "";
    element.classList.add("cursor");
    element.style.visibility = "visible";
    let i = 0;
    const speed = 15;
    function type() {
        if (i < text.length) {
            if (text.charAt(i) === '<') {
                let tag = "";
                while (text.charAt(i) !== '>' && i < text.length) { tag += text.charAt(i); i++; }
                tag += '>'; i++; element.innerHTML += tag;
            } else { element.innerHTML += text.charAt(i); i++; }
            setTimeout(type, speed);
        }
    }
    type();
});
"""

# --- CONTENT (IDENTITY / COMING SOON) ---
# This is the "Coming Soon" text with Typing Effect you asked for.
IDENTITY_TEXT = """
<h1>> /SYS/IDENTITY_LOADER.EXE</h1>

<p>Initializing Core Dump...<br>
Target: <strong>Andrii Ivas (UkrGeekLife)</strong><br>
Origin: Ukraine 🇺🇦</p>

<p>Loading Manifesto...<br>
[██████████████......] 74%</p>

<p class="red-alert">ERROR: DATA ENCRYPTED. SECURITY LEVEL 5 REQUIRED.</p>

<p>Public Data Available:</p>
<ul>
    <li><strong>Diet:</strong> Vegetarian (10+ Years). Zero Meat. Zero Seafood.</li>
    <li><strong>Geopolitics:</strong> Anti-Terrorist. Patriot. We never forget.</li>
    <li><strong>Protocol:</strong> Full Automation or Nothing.</li>
</ul>

<p>System Message: <span class="highlight">"I am rewriting the kernel. Full identity reveal is COMING SOON."</span></p>

<p class="dim">System Key Hint: 0xDEADBEEF... Try 'matrix' in terminal.</p>
"""

# --- PAGES ---

NAV_MENU = """
<nav role="navigation">
    <a href="index.html">[ HOME ]</a>
    <a href="about.html">[ IDENTITY ]</a>
    <a href="projects.html">[ ARSENAL ]</a>
    <a href="contact.html">[ TERMINAL ]</a>
</nav>
"""

FOOTER = f"""
<footer>
    <div>System Online :: &copy; 2025 {IDENTITY}</div>
    <div class="footer-links">
        <a href="index.html">/ROOT</a>
        <a href="about.html">/BIN/WHOAMI</a>
        <a href="contact.html">/DEV/STDIN</a>
    </div>
    <div style="margin-top:5px; font-size:0.7rem; color:#444;">Zoo Status: 4 Cats, 2 Dogs, 1 Rat, 1 Turtle. Stable.</div>
</footer>
"""

# Inline JS for Terminal (Guarantees it works)
TERMINAL_SCRIPT_INLINE = """
<script>
    document.addEventListener("DOMContentLoaded", function() {
        const input = document.getElementById("cmd");
        const history = document.getElementById("history");
        if(input) {
            input.focus();
            document.addEventListener('click', () => input.focus());
            input.addEventListener("keydown", function(e) {
                if (e.key === "Enter") {
                    const rawCmd = input.value.trim();
                    const cmd = rawCmd.toLowerCase();
                    history.innerHTML += `<div><span class="prompt">guest@ukrgeek:~$</span> ${rawCmd}</div>`;
                    let res = "";
                    switch(cmd) {
                        case "help": res = "COMMANDS: [about] [projects] [email] [slava] [matrix] [clear]"; break;
                        case "about": res = "Identity Encrypted... See /BIN/WHOAMI page."; break;
                        case "slava": res = "<span style='color:yellow'>GEROYAM SLAVA! 🇺🇦</span>"; break;
                        case "matrix": res = "Wake up, Andrii..."; break;
                        case "clear": history.innerHTML = ""; break;
                        default: res = "<span style='color:red'>Command not found.</span>";
                    }
                    if(cmd !== "clear") history.innerHTML += `<div style='color:#DDD'>${res}</div>`;
                    input.value = "";
                    document.querySelector('.terminal-window').scrollTop = document.querySelector('.terminal-window').scrollHeight;
                }
            });
        }
    });
</script>
"""

PAGES = {
    "index.html": { "title": f"Home | {IDENTITY}", "content": "<h1>System Online</h1><p>Welcome to the digital space.</p>", "js": "" },
    "about.html": { 
        "title": f"Identity | {IDENTITY}", 
        "content": IDENTITY_TEXT, 
        "js": "<script src='js/typewriter.js'></script>" # TYPING EFFECT HERE
    },
    "projects.html": { "title": f"Arsenal | {IDENTITY}", "content": "<h1>Arsenal</h1><ul><li>Automation</li><li>Security</li></ul>", "js": "" },
    "contact.html": { 
        "title": f"Terminal | {IDENTITY}", 
        "content": "<h1>Terminal Access</h1><div class='terminal-window'><div id='history'><p>UkrGeekLife OS v6.0...</p><p>Type 'help'...</p></div><div class='input-line'><span class='prompt'>guest@ukrgeek:~$</span><input type='text' id='cmd' autofocus></div></div>", 
        "js": TERMINAL_SCRIPT_INLINE 
    }
}

# --- EXECUTION ---
def build():
    print("--- BUILDING SYSTEM ---")
    os.makedirs("css", exist_ok=True)
    os.makedirs("js", exist_ok=True)
    with open("css/style.css", "w", encoding="utf-8") as f: f.write(CSS_CODE)
    with open("js/matrix.js", "w", encoding="utf-8") as f: f.write(JS_MATRIX)
    with open("js/typewriter.js", "w", encoding="utf-8") as f: f.write(JS_TYPEWRITER)
    
    BASE_HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title}</title><link rel="stylesheet" href="css/style.css"></head><body><canvas id="matrix-bg"></canvas><header><div class="logo">{logo}</div>{nav}</header><main class="container"><div id="typewriter-content">{content}</div></main>{footer}<script src="js/matrix.js"></script>{extra_js}</body></html>"""
    
    for fname, data in PAGES.items():
        html = BASE_HTML.format(title=data['title'], logo=IDENTITY, nav=NAV_MENU, content=data['content'], footer=FOOTER, extra_js=data['js'])
        with open(fname, "w", encoding="utf-8") as f: f.write(html)
        print(f"✅ {fname}")

def deploy():
    print("--- DEPLOYING ---")
    run_command("git add .")
    run_command('git commit -m "UkrGeekLife | Identity Loader"')
    run_command("git push origin master")

if __name__ == "__main__":
    build()
    deploy()
    print(">>> DONE. Check the Identity page.")
    # Simple Python Server Start (Optional, usually you check via Browser)
    run_command("python -m http.server 8000")