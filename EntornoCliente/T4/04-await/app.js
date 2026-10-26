"use strict";


const button = document.querySelector("#run");
const status = document.querySelector("#status");
const log = document.querySelector("#log");
let clicks = 0;
document.querySelector("#touch").addEventListener("click", () => {
  document.querySelector("#count").textContent = `Clics: ${++clicks}`;
});
function loadProfile(fail) {
  return new Promise((resolve, reject) => setTimeout(() => {
    if (fail) { reject(new Error("Perfil no disponible")); return; }
    resolve({ nombre: "Ana", curso: "2.º DAW" });
  }, 1500));
}
async function showProfile() {
  const fail = document.querySelector("#mode").value === "error";
  button.disabled = true; status.textContent = "Cargando…"; log.textContent = "1. Antes de await";
  try {
    const profile = await loadProfile(fail);
    log.textContent += `\n3. Tras await: ${profile.nombre}, ${profile.curso}`;
    status.textContent = "Perfil cargado";
  } catch (error) {
    status.textContent = error.message;
  } finally {
    button.disabled = false;
    log.textContent += "\n4. finally: fin de la operación";
  }
}
button.addEventListener("click", () => {
  const returned = showProfile(); // Una función async siempre devuelve una promesa.
  log.textContent += `\n2. El manejador continúa. ¿Promesa? ${returned instanceof Promise}`;
});
