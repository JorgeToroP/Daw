// Dos formas equivalentes de declarar arrays tipados.
const notas: number[] = [7, 8, 9];
const asignaturas: Array<string> = ["DWEC", "DIW", "DAW"];

notas.push(10);
const media: number = notas.reduce((suma, nota) => suma + nota, 0) / notas.length;
console.log("Asignaturas:", asignaturas.join(", "));
console.log("Media:", media);
export {};
