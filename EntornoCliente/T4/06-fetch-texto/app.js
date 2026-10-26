"use strict";


const button = document.querySelector("#run");
const status = document.querySelector("#status");
const meta = document.querySelector("#meta");
const result = document.querySelector("#result");
button.addEventListener("click", () => {
  button.disabled = true; status.textContent = "Cargando…"; meta.textContent = ""; result.textContent = "";
  fetch(document.querySelector("#resource").value, { cache: "no-store" })
    .then(response => {
      meta.textContent = `Response recibida\nstatus: ${response.status}\nok: ${response.ok}`;
      // Un 404 no rechaza automáticamente la promesa de fetch.
      if (!response.ok) throw new Error(`Error HTTP ${response.status}`);
      return response.text(); // Devolvemos la promesa para encadenar la lectura.
    })
    .then(text => { result.textContent = text; status.textContent = "Texto recibido"; })
    .catch(error => { status.textContent = error.message; })
    .finally(() => { button.disabled = false; });
});
