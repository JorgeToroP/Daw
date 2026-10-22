// Una tupla fija el tipo que corresponde a cada posición.
const alumno: [string, number, boolean] = ["Carlos", 20, true];
const [nombre, edad, matriculado] = alumno;

console.log(`${nombre}, ${edad} años. Matriculado: ${matriculado}`);
// const incorrecta: [string, number] = [25, "Luis"]; // Error de tipos.
export {};
