// any admite cualquier valor, aunque debe usarse con prudencia.
let dato: any = "TypeScript";
const longitud: number = (dato as string).length;
console.log("Longitud:", longitud);

dato = 42;
const numero: number = dato as number;
console.log("El doble es:", numero * 2);
export {};
