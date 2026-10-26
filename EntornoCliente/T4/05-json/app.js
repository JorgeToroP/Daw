"use strict";


const source = document.querySelector("#source");
const status = document.querySelector("#status");
const result = document.querySelector("#result");
const student = { nombre: "Ana", edad: 20, matriculada: true, modulos: ["DWEC", "DWES"] };
document.querySelector("#valid").addEventListener("click", () => {
  source.value = JSON.stringify(student, null, 2); status.textContent = "Texto válido preparado";
});
document.querySelector("#invalid").addEventListener("click", () => {
  source.value = "{'nombre':'Ana',}"; status.textContent = "¿Qué dos reglas incumple este texto?";
});
document.querySelector("#parse").addEventListener("click", () => {
  try {
    const data = JSON.parse(source.value); // Es síncrono. Puede lanzar SyntaxError.
    const type = data === null ? "null" : Array.isArray(data) ? "array" : typeof data;
    status.textContent = `Entrada: string. Resultado: ${type}`;
    result.textContent = JSON.stringify(data, null, 2);
    if (data !== null && typeof data === "object" && !Array.isArray(data)) {
      result.textContent += `\n\nAcceso a propiedad nombre: ${data.nombre ?? "(ausente)"}`;
    }
  } catch (error) { status.textContent = "JSON no válido"; result.textContent = error.message; }
});
document.querySelector("#stringify").addEventListener("click", () => {
  const text = JSON.stringify(student, null, 2);
  source.value = text; status.textContent = `Objeto JS convertido en ${typeof text}`;
  result.textContent = text;
});
