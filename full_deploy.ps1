$OutputEncoding = [Console]::InputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Write-Host "--- Launching UkrGeekLife Repair & Deploy ---" -ForegroundColor Cyan

# 1. CLEANUP
Stop-Process -Name "python" -Force -ErrorAction SilentlyContinue

# 2. BUILD
python generate_page.py

# 3. AUDIT
python security_scan.py

# 4. IDENTITY INJECTION (The code that broke before)
$pages = @{
    "index.html"   = "Головна | UkrGeekLife | Андрій Івась"
    "about.html"   = "Про Мене | UkrGeekLife | Андрій Івась"
    "contact.html" = "Контакти | Термінал | UkrGeekLife | Андрій Івась"
    "blog.html"    = "Блог | Думки | UkrGeekLife | Андрій Івась"
}

foreach ($file in $pages.Keys) {
    if (Test-Path $file) {
        $raw = Get-Content $file -Raw
        $title = "<title></title>"
        
        # Replace Title
        $raw = $raw -replace '<title>.*</title>', $title
        
        # Replace Alt Tags (Hardcore A11y)
        $raw = $raw -replace '<img([^>]*)alt="[^"]*"', '<img$1alt="UkrGeekLife: Андрій Івась — IT-архітектор та патріот України"'
        
        # Save with UTF8
        $raw | Set-Content $file -Encoding UTF8
    }
}

# 5. DEPLOY
git add .
git commit -m "UkrGeekLife | Андрій Івась | Auto-Fix Encoding 2025-12-23 23:52"
git push origin master

# 6. FINISH
Write-Host "--- SUCCESS ---" -ForegroundColor Green
Start-Process "http://localhost:8000/index.html"
