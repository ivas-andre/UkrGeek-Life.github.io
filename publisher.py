# -*- coding: utf-8 -*-
import os
import sys

# --- 1. CONFIGURATION & SETUP ---
sys.stdout.reconfigure(encoding='utf-8')
IDENTITY = "UkrGeekLife | Андрій Івась"

# Створення папок
os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)

# --- 2. ASSETS (CSS & JS) ---

CSS_CODE = """
body {
    background-color: #000;
    color: #0F0;
    font-family: 'Courier New', monospace;
    margin: 0;
    padding: 0;
    overflow-x: hidden;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}
/* Matrix Canvas */
#matrix-bg {
    position: fixed;
    top: 0;
    left: 0;
    z-index: -1;
    opacity: 0.15;
}
/* Header */
header {
    background: rgba(0, 20, 0, 0.95);
    border-bottom: 2px solid #0F0;
    padding: 15px 0;
    text-align: center;
    position: sticky;
    top: 0;
    z-index: 100;
}
.logo {
    font-size: 1.5rem;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 3px;
    margin-bottom: 10px;
    text-shadow: 0 0 10px #0F0;
}
nav a {
    color: #FFF;
    text-decoration: none;
    margin: 0 15px;
    font-size: 1.1rem;
    font-weight: bold;
    transition: 0.3s;
}
nav a:hover {
    color: #0F0;
    text-shadow: 0 0 8px #0F0;
}
/* Content */
.container {
    flex: 1; /* Pushes footer down */
    max-width: 900px;
    margin: 40px auto;
    padding: 20px;
    background: rgba(0, 0, 0, 0.8);
    border: 1px solid #333;
    width: 90%;
}
h1, h2 { border-bottom: 1px solid #0F0; padding-bottom: 10px; }
p, li { font-size: 1.1rem; line-height: 1.6; }

/* Footer Styles */
footer {
    border-top: 2px solid #0F0;
    background: #050505;
    text-align: center;
    padding: 20px;
    margin-top: auto;
    font-size: 0.9rem;
}
.footer-links a { color: #888; text-decoration: none; margin: 0 10px; }
.footer-links a:hover { color: #0F0; }
.easter-egg { color: #000; cursor: help; margin-top: 10px; user-select: none; }
.easter-egg:hover { color: #111; }

/* Terminal */
.terminal-window {
    background: #111;
    border: 1px solid #0F0;
    padding: 20px;
    height: 60vh;
    overflow-y: auto;
}
.input-line { display: flex; align-items: center; }
.prompt { color: #0F0; margin-right: 10px; font-weight: bold; }
input#cmd {
    background: transparent;
    border: none;
    color: #FFF;
    font-family: monospace;
    font-size: 1.2rem;
    flex-grow: 1;
    outline: none;
}
"""

JS_MATRIX = """
const canvas = document.getElementById('matrix-bg');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
const chars = 'ҐЄ