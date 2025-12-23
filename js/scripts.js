// navigation slide-in
$(window).load(function() {
  $('.nav_slide_button').click(function() {
    $('.pull').slideToggle();
  });
});
// first-flexslider
$(window).load(function() {
  $('#firstSlider').flexslider({
    animation: "slide",
    directionNav: false,
    controlNav: true,
    touch: false,
    start: function() {
      $.waypoints('refresh');
    }
  });
});
// second-flexslider
$(window).load(function() {
  $('#secondSlider').flexslider({
    animation: "slide",
    directionNav: false,
    controlNav: false,
    touch: false,
  });
});
$('.prev, .next').on('click', function() {
  var href = $(this).attr('href');
  $('#secondSlider').flexslider(href)
  return false;
})
// waypoints
$(document).ready(function() {

  $('.wp1').waypoint(function() {
    $('.wp1').addClass('animated fadeInUp');
  }, {
    offset: '75%'
  });

  $('.wp2').waypoint(function() {
    $('.wp2').addClass('animated fadeInUp');
  }, {
    offset: '75%'
  });

  $('.wp3').waypoint(function() {
    $('.wp3').addClass('animated fadeInUpD');
  }, {
    offset: '75%'
  });

});
// smooth scroll
$(function() {
  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//, '') === this.pathname.replace(/^\//, '') && location.hostname === this.hostname) {

      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 2000);
        return false;
      }
    }
  });
});
// fancyBox
$(document).ready(function() {
  $(".various").fancybox({
    maxWidth: 800,
    maxHeight: 450,
    fitToView: false,
    width: '70%',
    height: '70%',
    autoSize: false,
    closeClick: false,
    openEffect: 'none',
    closeEffect: 'none'
  });
});

// UkrGeekLife Modern JS v0.1.2
const systemConfig = {
    version: "0.1.2",
    env: "Production",
    lastSecurityScan: new Date().toLocaleDateString()
};

document.addEventListener('DOMContentLoaded', () => {
    console.log(`%c System Online: UkrGeekLife v${systemConfig.version}`, "color: #22c55e; font-weight: bold;");

    // Адаптивне меню: автоматичне закриття після кліку
    const navLinks = document.querySelectorAll('.navbar-collapse a');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            const navbar = document.querySelector('.navbar-collapse');
            if (navbar.classList.contains('in')) {
                jQuery('.navbar-collapse').collapse('hide');
            }
        });
    });

    // Cyber Security Touch: Логування спроб доступу до консолі
    window.addEventListener('resize', () => {
        if (window.outerWidth - window.innerWidth > 100) {
            console.warn("Security Alert: DevTools activity detected.");
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const terminalInput = document.getElementById('terminal-input');
    
    if (terminalInput) {
        terminalInput.addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                const command = this.value.toLowerCase().trim();
                this.value = '';

                // Easter Eggs Logic
                if (command === 'slava ukraini') {
                    alert('HEROYAM SLAVA! 🇺🇦');
                    document.body.style.background = 'linear-gradient(to bottom, #0057b7 50%, #ffd700 50%)';
                } else if (command === 'vegetarian') {
                    console.log("Status: 10+ years of discipline [cite: 2025-12-23]");
                    alert('Respect! No meat for 10+ years. System purified.');
                } else if (command === 'russia') {
                    document.body.innerHTML = '<h1 style="color:red; text-align:center; margin-top:20%; font-family:serif;">ERROR: ACCESS DENIED. TERRORIST STATE NOT RECOGNIZED. [cite: 2025-12-23]</h1>';
                    setTimeout(() => location.reload(), 3000);
                } else if (command === 'help') {
                    alert('Available commands: slava ukraini, vegetarian, scan, russia');
                } else if (command === 'scan') {
                    alert('Running Python Security Scan v0.2... Issues found: 0 [cite: 2025-12-23]');
                }
            }
        });
    }
});

// Security Logic: Anti-Aggressor Protocol [cite: 2025-12-23]
const blockRussianLanguage = (input) => {
    // Регулярний вираз для пошуку російських літер (ы, э, ъ, ё)
    const ruPattern = /[ыэъё]/i;
    
    if (ruPattern.test(input)) {
        console.error("CRITICAL: Unauthorized language detected. Initiating Lockdown.");
        
        // Імітація збору даних для психологічного ефекту
        const fakeIp = "192.168." + Math.floor(Math.random() * 255) + ".1";
        const fakeMac = "00-B0-D0-63-C2-26";

        document.body.innerHTML = `
            <div style="background:#000; color:#ff0000; height:100vh; padding:50px; font-family:monospace; text-align:center;">
                <h1>🛑 ACCESS DENIED PERMANENTLY</h1>
                <p>IP: \${fakeIp} | MAC: \${fakeMac} | STATUS: LOGGED</p>
                <hr style="border-color:red;">
                <h2 style="color:#ffd700;">GLORY TO UKRAINE! 🇺🇦</h2>
                <p style="color:#fff; font-size:20px;">You are violent on my site forever. Terrorist language is not accepted here.</p>
                <p style="margin-top:50px;">[cite: 2025-12-23] Ми змінюємо світ. Я це пам'ятаю.</p>
            </div>
        `;
        
        // Блокування доступу через LocalStorage
        localStorage.setItem('site_blocked', 'true');
    }
};

// Перевірка при завантаженні
if (localStorage.getItem('site_blocked') === 'true') {
    document.body.innerHTML = "<h1 style='color:red; text-align:center; margin-top:20%;'>YOU ARE BANNED.</h1>";
}