  class Persona {
    #nombre
    #apellidos

    constructor(nombre, apellidos) {
      this.#nombre = nombre;
      this.#apellidos = apellidos;
    }
    get nombreCompleto() {
      return this.#nombre + ' ' + this.#apellidos;
    }
    set nombreCompleto(input) {
      const arrayInput = input.split(' '); // Devuelve un array con cada elemento que esté separado 
       this.#nombre = arrayInput[0];       //    por el carácter ' ' (espacio)
      this.#apellidos = arrayInput[1];
    }
  }


  const persona = new Persona('Jorge', 'Toro');
  console.log(persona.nombreCompleto); // Jorge Toro
  persona.nombreCompleto = "Laura Daniela ";
  console.log(persona.nombreCompleto); // Laura Daniela 

