
const input = document.getElementById("cmd");
const history = document.getElementById("history");

if(input) {
    input.addEventListener("keydown", function(e) {
        if (e.key === "Enter") {
            const cmd = input.value.trim().toLowerCase();
            history.innerHTML += `<div><span class="prompt">guest@ukrgeek:~$</span> ${input.value}</div>`;
            
            let response = "";
            switch(cmd) {
                case "help": response = "COMMANDS: [about] [projects] [email] [slava] [clear]"; break;
                case "about": response = "Андрій Івась. Розробник. Архітектор. Патріот."; break;
                case "projects": response = "GitHub: <a href='https://github.com/ivas-andre' target='_blank' style='color:#FFF'>ivas-andre</a>"; break;
                case "email": response = "Email: contact@ukrgeek.life"; break;
                case "slava": response = "<span style='color:yellow; font-weight:bold;'>ГЕРОЯМ СЛАВА! 🇺🇦</span>"; break;
                case "clear": history.innerHTML = ""; break;
                default: response = `<span style='color:red'>Error: Command '${cmd}' not found. Try 'help'.</span>`;
            }
            
            if(cmd !== "clear") history.innerHTML += `<div style="margin-bottom: 10px; color: #EEE;">${response}</div>`;
            input.value = "";
            document.querySelector('.terminal-window').scrollTop = document.querySelector('.terminal-window').scrollHeight;
        }
    });
    document.addEventListener('click', () => input.focus());
}
