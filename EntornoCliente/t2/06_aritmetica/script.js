const a = 10;
const b = 3;

let Suma = a +b;
let resta = a - b;
let multi = (a * b);
let div = a/b;
let resto = a % b;

document.getElementById("resultado").innerHTML =
  "Suma: " + Suma + "<br>" +
  "Resta: " + resta + "<br>" +
  "Multiplicación: " + multi + "<br>" +
  "División: " + div + "<br>" +
  "Resto: " + resto;
