//Interfaces


interface IPersona{
   name: string
   getName(): string
}
class Persona implements IPersona{
   name: string
   getName(): string{
       return this.name
   }
}


