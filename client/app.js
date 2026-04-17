async function creaOrdine() {
    try {
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

        console.log("Ordine creato:", data);

        document.getElementById("result").textContent =
            "Ordine effettuato con successo ✅";

    } catch (err) {
        console.error("Errore creazione ordine:", err);

        document.getElementById("result").textContent =
            "Errore durante l'ordine ❌";
    }
}