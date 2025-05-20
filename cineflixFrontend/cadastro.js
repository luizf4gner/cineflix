// Força da senha
const strengthBar = document.getElementById("strength-bar").firstElementChild;

function checkStrength() {
    const val = document.getElementById("senha").value;
    let strength = 0;
    if (val.length >= 6) strength++;
    if (/[A-Z]/.test(val)) strength++;
    if (/[0-9]/.test(val)) strength++;
    if (/[^A-Za-z0-9]/.test(val)) strength++;

    strengthBar.style.width = (strength * 25) + "%";
    strengthBar.style.background = ["#ccc", "#f66", "#f90", "#fc0", "#0c0"][strength];
}

// Modo escuro
const toggle = document.getElementById("toggle-theme");
toggle.onclick = () => {
    document.body.classList.toggle("dark-mode");
    toggle.textContent = document.body.classList.contains("dark-mode") ? "☀️ Modo Claro" : "🌙 Modo Escuro";
};

// Mostrar/ocultar senha
function toggleSenha() {
    const pwdInput = document.getElementById("senha");
    pwdInput.type = pwdInput.type === "password" ? "text" : "password";
}

// Enviar dados
async function cadastrar() {
    const dados = {
        username: document.getElementById("username").value,
        senha: document.getElementById("senha").value,
        email: document.getElementById("email").value,
        tipo: document.getElementById("tipo").value
    };

    const mensagem = document.getElementById("mensagem");
    mensagem.textContent = "Enviando...";

    try {
        const response = await fetch("http://127.0.0.1:5000/usuarios/create", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dados)
        });

        const resultado = await response.json();
        if (response.ok) {
            mensagem.textContent = resultado.message;
            mensagem.style.color = "green";
        } else {
            mensagem.textContent = resultado.error || "Erro ao cadastrar.";
            mensagem.style.color = "red";
        }
    } catch (erro) {
        mensagem.textContent = "Erro na conexão com o servidor.";
        mensagem.style.color = "red";
    }
}