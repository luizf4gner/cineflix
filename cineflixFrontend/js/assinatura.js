document.getElementById("toggle-theme").addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
    const toggle = document.getElementById("toggle-theme");
    toggle.textContent = document.body.classList.contains("dark-mode")
        ? "☀️ Modo Claro"
        : "🌙 Modo Escuro";
});

async function cadastrarAssinatura() {
    const username = document.getElementById("username").value;
    const inicio = document.getElementById("data_inicial").value;
    const fim = document.getElementById("data_final").value;
    const msg = document.getElementById("mensagem");

    if (!username || !inicio || !fim) {
        msg.textContent = "Preencha todos os campos!";
        msg.style.color = "red";
        return;
    }

    const dados = {
        username: username,
        data_inicial: inicio,
        data_final: fim
    };

    try {
        const response = await fetch("http://127.0.0.1:5000/assinaturas/create", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dados)
        });

        const resultado = await response.json();

        if (response.ok) {
            msg.textContent = resultado.message;
            msg.style.color = "green";
            listarAssinaturas();
        } else {
            msg.textContent = resultado.error || "Erro ao cadastrar.";
            msg.style.color = "red";
        }
    } catch (erro) {
        msg.textContent = "Erro na conexão com o servidor.";
        msg.style.color = "red";
    }

    document.getElementById("username").value = "";
    document.getElementById("data_inicial").value = "";
    document.getElementById("data_final").value = "";
}

async function listarAssinaturas() {
    const lista = document.getElementById("lista-assinaturas");
    lista.innerHTML = "Carregando...";

    try {
        const response = await fetch("http://127.0.0.1:5000/assinaturas");
        const assinaturas = await response.json();

        if (response.ok) {
            lista.innerHTML = "";
            if (assinaturas.length === 0) {
                lista.innerHTML = "<p>Nenhuma assinatura encontrada.</p>";
                return;
            }

            assinaturas.forEach(a => {
                const item = document.createElement("div");
                item.style.marginBottom = "10px";
                item.innerHTML = `
                    <strong>${a.username}</strong> |
                    <em>${a.data_inicial}</em> → <em>${a.data_final}</em>
                    <button onclick="deletarAssinatura(${a.id})" style="margin-left: 10px;">🗑️</button>
                `;
                lista.appendChild(item);
            });
        } else {
            lista.innerHTML = "<p>Erro ao carregar assinaturas.</p>";
        }
    } catch (erro) {
        lista.innerHTML = "<p>Erro na conexão.</p>";
    }
}

async function deletarAssinatura(id) {
    if (!confirm("Deseja deletar esta assinatura?")) return;

    try {
        const response = await fetch(`http://127.0.0.1:5000/assinaturas/delete${id}`, {
            method: "DELETE"
        });

        const resultado = await response.json();
        alert(resultado.message || resultado.error);
        listarAssinaturas();
    } catch (erro) {
        alert("Erro ao deletar assinatura.");
    }
}

listarAssinaturas();