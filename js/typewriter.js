document.addEventListener("DOMContentLoaded", function() {
    const element = document.getElementById('typewriter-content');
    if (!element) return;
    
    // Save content and clear it
    const text = element.innerHTML;
    element.innerHTML = "";
    element.classList.add("cursor"); // Add blinking cursor
    element.style.visibility = "visible"; // Show element

    let i = 0;
    const speed = 10; // Speed (lower is faster)

    function type() {
        if (i < text.length) {
            // Handle HTML tags immediately (don't type < b r > char by char)
            if (text.charAt(i) === '<') {
                let tag = "";
                while (text.charAt(i) !== '>' && i < text.length) {
                    tag += text.charAt(i);
                    i++;
                }
                tag += '>';
                i++;
                element.innerHTML += tag;
            } else {
                element.innerHTML += text.charAt(i);
                i++;
            }
            setTimeout(type, speed);
        }
        // Cursor stays blinking at the end
    }
    type();
});
