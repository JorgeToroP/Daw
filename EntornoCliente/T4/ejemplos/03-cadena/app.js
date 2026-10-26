"use strict";


const button = document.querySelector("#run");
const log = document.querySelector("#log");
const status = document.querySelector("#status");
function write(text) { const li = document.createElement("li"); li.textContent = text; log.append(li); }
function discount(price) {
  return new Promise(resolve => setTimeout(() => resolve(price * 0.9), 700));
}
button.addEventListener("click", () => {
  button.disabled = true; log.replaceChildren(); status.textContent = "Calculando…";
  // Los errores que lancemos en then también llegan al catch posterior.
  Promise.resolve(Number(document.querySelector("#price").value))
    .then(price => {
      if (!Number.isFinite(price) || price <= 0) throw new Error("El precio debe ser mayor que 0");
      write(`Precio inicial: ${price.toFixed(2)} €`);
      return discount(price); // Hay que devolver esta promesa para esperar su resultado.
    })
    .then(net => { write(`Tras descuento: ${net.toFixed(2)} €`); return net * 1.21; })
    .then(total => { status.textContent = `Total: ${total.toFixed(2)} €`; write("Cadena completada"); })
    .catch(error => { status.textContent = error.message; write("El error salta los then de éxito restantes"); })
    .finally(() => { button.disabled = false; write("finally: controles liberados"); });
});
