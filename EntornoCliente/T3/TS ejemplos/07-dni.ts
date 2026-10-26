const LETRAS_DNI: string = "TRWAGMYFPDXBNJZSQVHLCKE";

function calcularLetraDni(numero: number): string {
  if (!Number.isInteger(numero) || numero < 0 || numero > 99_999_999) {
    throw new Error("El DNI debe contener hasta 8 números.");
  }
  return LETRAS_DNI[numero % 23];
}

const numeroDni: number = 12_345_678;
console.log(`DNI completo: ${numeroDni.toString().padStart(8, "0")}${calcularLetraDni(numeroDni)}`);
export {};
