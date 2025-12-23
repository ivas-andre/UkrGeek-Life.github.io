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