// UkrGeekLife Terminal Logic
const input = document.getElementById("cmd");
const history = document.getElementById("history");

input.addEventListener("keydown", function(e) {
    if (e.key === "Enter") {
        const cmd = input.value.trim().toLowerCase();
        
        // Додаємо команду в історію
        history.innerHTML += `<div><span class="prompt">guest@ukrgeek:~$</span> ${input.value}</div>`;
        
        // Відповідь системи
        let response = "";
        switch(cmd) {
            case "help":
                response = "COMMANDS: [about] [projects] [email] [slava] [clear]";
                break;
            case "email":
                response = "CONTACT: <a href='mailto:me@ukrgeek.life' style='color:#FFF'>me@ukrgeek.life</a>";
                break;
            case "slava":
                response = "<span style='color:yellow'>ГЕРОЯМ СЛАВА! 🇺🇦</span>";
                break;
            case "clear":
                history.innerHTML = "";
                break;
            default:
                response = `ERROR: Command '${cmd}' not found. Try 'help'.`;
        }
        
        if (cmd !== "clear") {
            history.innerHTML += `<div style="color:#FFF; margin-bottom:10px">${response}</div>`;
        }
        
        input.value = "";
        window.scrollTo(0, document.body.scrollHeight);
    }
});

// Авто-фокус
document.addEventListener('click', () => input.focus());