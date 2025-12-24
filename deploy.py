# -*- coding: utf-8 -*-
import os, sys, subprocess, time

# --- [0] HELPER MODULE: LOGGING & EXECUTION ---
LOG_FILE = "deploy.log"

def log_action(message):
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {message}\n")

def run(cmd):
    log_action(f"CMD_START: {cmd}")
    try:
        # ЗАХОПЛЕННЯ ВИВОДУ ДЛЯ АУДИТУ
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            log_action(f"STDOUT: {result.stdout.strip()}")
        print(f"✅ {cmd}")
    except subprocess.CalledProcessError as e:
        log_action(f"GIT_ERROR: {e.stderr.strip()}")
        print(f"❌ FAILED: {cmd}")

# --- [1] MODULAR CONTENT GENERATORS ---
ID_PROJECT, ID_NAME = "Ukrainian Gig Life", "Andrii Ivas"
IDENTITY = f"{ID_PROJECT} | {ID_NAME}"

def get_head():
    return f"""<head><meta charset="UTF-8"><title>{IDENTITY}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="css/style.css"></head>"""

def get_header():
    return f"""<header>
    <div class="identity-wrapper">
        <div class="hal-eye-unit" onclick="halSpeak()"></div>
        <div class="site-title" onclick="toggleMenu()">[{ID_PROJECT}]</div>
        <a href="index.html" class="owner-name">{ID_NAME}</a>
    </div>
    <div class="header-modules">
        <button class="shatter-donate" onclick="triggerShatter()">DONATE;</button>
        <div class="aliens-radar"><div class="sweep"></div><div class="ping"></div></div>
        <div class="social-tier-1">
            <a href="#" class="flat-icon"><i class="fab fa-youtube"></i></a>
            <a href="#" class="flat-icon"><i class="fab fa-instagram"></i></a>
            <a href="#" class="flat-icon"><i class="fab fa-facebook"></i></a>
            <a href="#" class="flat-icon"><i class="fab fa-linkedin"></i></a>
        </div>
    </div>
</header>"""

def get_footer():
    # FOOTER PRESERVED - AS REQUESTED
    return f"""<footer>
    <div class="zoo-line">[ SYSTEM RESOURCES: 4 CATS | 2 DOGS | 1 RAT | 1 TURTLE ]</div>
    <div class="footer-links">
        <a href="#"><i class="fab fa-twitter"></i></a><a href="#"><i class="fab fa-tumblr"></i></a>
        <a href="#"><i class="fab fa-twitch"></i></a><a href="#"><i class="fab fa-github"></i></a>
    </div>
    <div style="margin-top:10px;opacity:0.5;font-size:0.7rem;">© 2025 {IDENTITY} | NO FORGIVENESS</div>
    <script src="js/main.js"></script></footer>"""

# --- [EXECUTION SEQUENCE] ---
log_action("--- NEW DEPLOYMENT SESSION ---")
os.makedirs("css", exist_ok=True); os.makedirs("js", exist_ok=True)

# Складання сторінки з жорстким тригером анімації
index_html = f"<!DOCTYPE html><html>{get_head()}<body>{get_header()}<main id='typewriter'><h1>CORE_ONLINE</h1></main>{get_footer()}</body></html>"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)
log_action("Files generated. Starting Git synchronization.")

# ПОВНИЙ АУДИТ КОМАНД
run("git add .")
run(f'git commit -m "Modular system upgrade with full Git audit log"')
run("git push origin master")

print(">>> Protocol executed. Check deploy.log for Git stdout.")