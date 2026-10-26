// Tipos básicos y tipado explícito.
const nombre: string = "Ana";
const edad: number = 22;
const estudiaTypeScript: boolean = true;
const presentacion: string = `${nombre} tiene ${edad} años.`;

console.log(presentacion);
console.log("¿Estudia TypeScript?", estudiaTypeScript);
// edad = "veintidós"; // Error: un string no se puede asignar a number.
export {};
