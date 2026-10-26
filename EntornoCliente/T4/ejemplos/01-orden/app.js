"use strict";


const run = document.querySelector("#run");
const log = document.querySelector("#log");
const status = document.querySelector("#status");
let clicks = 0;
document.querySelector("#touch").addEventListener("click", () => {
  document.querySelector("#count").textContent = `Clics: ${++clicks}`;
});
function write(text) {
  const li = document.createElement("li"); li.textContent = text; log.append(li);
}
run.addEventListener("click", () => {
  run.disabled = true; log.replaceChildren();
  status.textContent = "Esperando al temporizador… Puedes contar clics.";
  write("1. Inicio: código síncrono");
  // El navegador programa el callback. No detiene el código siguiente.
  setTimeout(() => {
    write("4. Temporizador: tarea posterior");
    status.textContent = "Terminado"; run.disabled = false;
  }, 2000);
  // Los callbacks de promesas se ejecutan como microtareas.
  Promise.resolve().then(() => write("3. Promesa: microtarea"));
  write("2. Fin del código síncrono");
});
