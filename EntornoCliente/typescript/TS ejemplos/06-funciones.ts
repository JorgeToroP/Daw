function sumar(a: number, b: number): number {
  return a + b;
}

function mostrarSaludo(nombre: string): void {
  console.log(`Hola, ${nombre}`);
}

mostrarSaludo("Marta");
console.log("4 + 6 =", sumar(4, 6));
export {};
