"use strict";


const button = document.querySelector("#run");
const status = document.querySelector("#status");
const list = document.querySelector("#products");
function render(products) {
  list.replaceChildren();
  for (const product of products) {
    const card = document.createElement("article"); card.className = "product";
    const title = document.createElement("h2"); title.textContent = product.nombre;
    const price = document.createElement("p"); price.textContent = `${product.precio.toFixed(2)} €`;
    card.append(title, price); list.append(card);
  }
}
button.addEventListener("click", () => {
  button.disabled = true; status.textContent = "Cargando…"; list.replaceChildren();
  fetch(document.querySelector("#resource").value, { cache: "no-store" })
    .then(response => {
      if (!response.ok) throw new Error(`Error HTTP ${response.status}`);
      return response.json(); // Ya convierte el JSON en datos JS. No hacer JSON.parse después.
    })
    .then(products => {
      if (!Array.isArray(products) || !products.every(p => p && typeof p.nombre === "string" && typeof p.precio === "number" && Number.isFinite(p.precio))) {
        throw new Error("El catálogo no tiene el formato esperado");
      }
      render(products);
      status.textContent = products.length ? `${products.length} productos cargados` : "No hay productos";
    })
    .catch(error => { status.textContent = `No se pudo cargar: ${error.message}`; })
    .finally(() => { button.disabled = false; });
});
