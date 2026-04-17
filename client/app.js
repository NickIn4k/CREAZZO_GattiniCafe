const API_URL = "http://127.0.0.1:8000/api";

let accessToken = localStorage.getItem("token");

// LOGIN
async function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const res = await fetch(`${API_URL}/auth/login/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
    });

    const data = await res.json();

    if (data.access) {
        accessToken = data.access;
        localStorage.setItem("token", accessToken);
        alert("Login riuscito!");
    } else {
        alert("Errore login");
    }
}

// CARICA PRODOTTI
async function loadProdotti() {
    const res = await fetch(`${API_URL}/prodotti/`);
    const prodotti = await res.json();

    const list = document.getElementById("prodotti-list");
    list.innerHTML = "";

    prodotti.forEach(p => {
        const li = document.createElement("li");
        li.textContent = `${p.id} - ${p.nome} (€${p.prezzo})`;
        list.appendChild(li);
    });
}

// CREA ORDINE
async function creaOrdine() {
    const prodotto_id = parseInt(document.getElementById("prodotto_id").value);
    const quantita = parseInt(document.getElementById("quantita").value);

    const res = await fetch(`${API_URL}/ordini/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${accessToken}`
        },
        body: JSON.stringify({
            note: "Ordine da client JS",
            prodotti: [
                { prodotto_id, quantita }
            ]
        })
    });

    const data = await res.json();

    document.getElementById("result").textContent = JSON.stringify(data);
}