enum Talla {
  Pequena = 1,
  Mediana,
  Grande
}

const tallaElegida: Talla = Talla.Mediana;
console.log("Valor:", tallaElegida);       // 2
console.log("Nombre:", Talla[tallaElegida]); // Mediana
export {};
