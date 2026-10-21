class Usuario{
    #email;

    constructor(nombre,email){
        this.nombre = nombre;
        this.#email = email;
    }

    saludar(){
        console.log("Hoola soy " + this.nombre);

    }
    leerEmail(){
        console.log("el email de " + this.nombre + " es " + this.#email);
    }

}

const user1 = new Usuario("Jorge","jorge@gmail.com");
user1.saludar();

user1.leerEmail();

class Administrador extends Usuario{
    constructor(nombre,email){
        super(nombre,email);
    }

    borrarUsuario(){
        console.log("Borrando datos...");
    }
}

const admin1 = new Administrador("Admin", "admin@gmail.com");

admin1.saludar();
admin1.leerEmail();
admin1.borrarUsuario();