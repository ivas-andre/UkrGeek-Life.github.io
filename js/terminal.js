
document.addEventListener("DOMContentLoaded", function() {
    const input = document.getElementById("cmd");
    const history = document.getElementById("history");
    
    if(input) {
        // Auto-focus on load
        input.focus();
        
        // Always refocus when clicking anywhere
        document.addEventListener('click', () => input.focus());

        input.addEventListener("keydown", function(e) {
            if (e.key === "Enter") {
                const cmd = input.value.trim().toLowerCase();
                
                // Echo command
                history.innerHTML += `<div><span class="prompt">guest@ukrgeek:~$</span> ${input.value}</div>`;
                
                let res = "";
                switch(cmd) {
                    case "help": 
                        res = "COMMANDS: [about] [projects] [email] [slava] [clear]"; 
                        break;
                    case "about": 
                        res = "Andrii Ivas. Vegetarian. Patriot. Automation Architect."; 
                        break;
                    case "projects": 
                        res = "GitHub: ivas-andre. Automation. Security."; 
                        break;
                    case "email":
                        res = "Email: contact@ukrgeek.life";
                        break;
                    case "slava": 
                        res = "<span style='color:yellow'>GEROYAM SLAVA! 🇺🇦</span>"; 
                        break;
                    case "clear": 
                        history.innerHTML = ""; 
                        break;
                    default: 
                        res = "<span style='color:red'>Error: Command not found. Try 'help'.</span>";
                }
                
                if(cmd !== "clear") {
                    history.innerHTML += `<div style='margin-bottom:10px; color:#DDD'>${res}</div>`;
                }
                
                input.value = "";
                // Auto-scroll to bottom
                document.querySelector('.terminal-window').scrollTop = document.querySelector('.terminal-window').scrollHeight;
            }
        });
    }
});
