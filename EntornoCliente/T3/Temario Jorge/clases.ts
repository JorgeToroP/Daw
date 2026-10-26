class Persona {
  private nombre: string;
  public constructor(nombre: string) {
    this.nombre = nombre;
  }
  public getNombre(): string {
    return this.nombre;
  }
}
const persona = new Persona("Juan");
console.log(persona.getNombre());    