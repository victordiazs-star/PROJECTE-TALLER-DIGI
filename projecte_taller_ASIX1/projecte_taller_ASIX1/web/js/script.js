const API_URL = "http://localhost:5000";

async function carregarClients() {
    const resposta = await fetch(`${API_URL}/clients`);
    const clients = await resposta.json();
    const select = document.getElementById("idClient");
    select.innerHTML = "";

    clients.forEach(client => {
        const opcio = document.createElement("option");
        opcio.value = client.idClient;
        opcio.textContent = `${client.idClient} - ${client.nom}`;
        select.appendChild(opcio);
    });
}

async function carregarVehicles() {
    const resposta = await fetch(`${API_URL}/vehicles`);
    const vehicles = await resposta.json();

    const select = document.getElementById("idVehicle");
    const div = document.getElementById("llistaVehicles");
    select.innerHTML = "";
    div.innerHTML = "";

    vehicles.forEach(vehicle => {
        const opcio = document.createElement("option");
        opcio.value = vehicle.idVehicle;
        opcio.textContent = `${vehicle.idVehicle} - ${vehicle.matricula} (${vehicle.model})`;
        select.appendChild(opcio);

        div.innerHTML += `
            <div class="item">
                <strong>${vehicle.matricula}</strong><br>
                Model: ${vehicle.model}<br>
                Any: ${vehicle.any_vehicle}<br>
                Client: ${vehicle.client}
            </div>
        `;
    });
}

async function carregarCites() {
    const resposta = await fetch(`${API_URL}/appointments`);
    const cites = await resposta.json();
    const div = document.getElementById("llistaCites");
    div.innerHTML = "";

    if (cites.length === 0) {
        div.innerHTML = "<p>No hi ha cites registrades.</p>";
        return;
    }

    cites.forEach(cita => {
        div.innerHTML += `
            <div class="item">
                <strong>${cita.data_cita} - ${cita.hora_cita}</strong><br>
                Client: ${cita.client}<br>
                Vehicle: ${cita.matricula} (${cita.model})<br>
                Servei: ${cita.servei_sollicitat}<br>
                Estat: ${cita.estat}
            </div>
        `;
    });
}

document.getElementById("citaForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const novaCita = {
        idClient: document.getElementById("idClient").value,
        idVehicle: document.getElementById("idVehicle").value,
        data_cita: document.getElementById("data_cita").value,
        hora_cita: document.getElementById("hora_cita").value,
        servei_sollicitat: document.getElementById("servei_sollicitat").value
    };

    const resposta = await fetch(`${API_URL}/appointments`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(novaCita)
    });

    const resultat = await resposta.json();
    document.getElementById("missatge").textContent = resultat.message;

    if (resposta.ok) {
        document.getElementById("citaForm").reset();
        carregarCites();
    }
});

document.getElementById("botoActualitzar").addEventListener("click", carregarCites);

carregarClients();
carregarVehicles();
carregarCites();
