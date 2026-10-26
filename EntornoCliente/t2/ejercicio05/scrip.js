

class Coche{
    #color;
    #marca;
    #modelo;

    constructor(color, marca, modelo){
        this.#color = color;
        this.#marca = marca;
        this.#modelo = modelo;
        this.encendido = false;
        console.log("Se ha creado un coche");
    }

    arrancar(){
        this.encendido = true;
 
    }
    detener(){
        this.encendido = false;
       
    }
}

const focus = new Coche("azul", "Ford", "Focus");
console.log("color del coche: " + focus.color);//azul
console.log("marca del coche: " + focus.marca);//Ford
console.log("modelo del coche: " + focus.modelo);//Focus

focus.nPuertas = 4;
console.log("número de puertas del coche: " + focus.nPuertas);//4


focus.arrancar()
console.log("EL coche esta encendido    =  ",focus.encendido);

focus.detener();
console.log(focus.encendido);