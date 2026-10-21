const frutas = ["Manzana", "Plátano", "Naranja"];

document.getElementById("resultado").innerHTML =
  "Primera fruta: " + frutas[0] + "<br>" +
  "Número de frutas: " + frutas.length + "<br>" +
  "Array completo: " + frutas.join(" ");
