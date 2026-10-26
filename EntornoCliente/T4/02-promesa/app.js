"use strict";


const button = document.querySelector("#run");
const status = document.querySelector("#status");
const log = document.querySelector("#log");
const progress = document.querySelector("#progress");
function prepare(fail) {
  return new Promise((resolve, reject) => {
    // El ejecutor corre ahora. setTimeout es quien programa la espera.
    setTimeout(() => {
      if (fail) { reject(new Error("Producto agotado")); return; }
      resolve("Pedido listo para recoger");
    }, 1600);
  });
}
button.addEventListener("click", () => {
  const fail = document.querySelector("#mode").value === "error";
  button.disabled = true; progress.removeAttribute("value");
  status.textContent = "pending: preparando…"; log.textContent = "";
  prepare(fail)
    .then(message => { status.textContent = "fulfilled"; log.textContent = message; })
    .catch(error => { status.textContent = "rejected"; log.textContent = error.message; })
    .finally(() => {
      // finally no recibe el resultado. Libera los controles en ambos casos.
      button.disabled = false; progress.value = 1;
      log.textContent += "\nfinally: botón disponible";
    });
});
