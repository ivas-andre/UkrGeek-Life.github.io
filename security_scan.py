import os
import re

def scan_for_secrets():
    # Пошук потенційних API токенів або вразливостей
    patterns = [r'api[_-]?key', r'secret', r'password', r'token']
    vulnerabilities = 0
    
    print("--- Starting Security Scan v0.1 ---")
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith((".html", ".js", ".css", ".py")):
                with open(os.path.join(root, file), 'r', errors='ignore') as f:
                    content = f.read().lower()
                    for pattern in patterns:
                        if re.search(pattern, content):
                            print(f"[!] Warning: Possible sensitive data in {file}: '{pattern}'")
                            vulnerabilities += 1
    
    if vulnerabilities == 0:
        print("[+] Scan Clean. No obvious security leaks found.")
    else:
        print(f"[!] Found {vulnerabilities} potential issues.")

if __name__ == "__main__":
    scan_for_secrets()