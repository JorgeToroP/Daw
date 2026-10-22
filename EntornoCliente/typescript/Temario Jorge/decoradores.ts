//decoradores de clase

function Bienvenida(target: Function): void{
   target.prototype.saludo = function(): void{
       console.log("Hola Mundo")
   }
}
@Bienvenida
class Saludar{
   constructor(){}
}
let s = new Saludar()
s.saludo()


////


function Bienvenida(saludo: string){
   return function(target: Function){
       target.prototype.saludo = function(): void{
           console.log(saludo)
       }
   }
}
@Bienvenida("Saludando")
class Saludar{
   constructor(){}
}
let s = new Saludar()
s.saludo()



/////



function LogCambios (target: Object, key: string){
  var valueProp: string = this[key]
   if(delete this[key]){
       Object.defineProperty(target, key, {
           get: function(){
               return valueProp
           },
           set: function(newValue){
               valueProp = newValue
               console.log(`${key} es ahora ${valueProp}`)
           }
       })
   }
}


class Animal{
   @LogCambios
   name: string
}
var a = new Animal()
a.name = 'Pipo'