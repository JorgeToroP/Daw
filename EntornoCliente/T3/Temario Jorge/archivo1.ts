
//
let termina: boolean = false
let decimal2: number = 12.3345

let nombre: string = "Jorge"
let apellidos: string = 'Toro'

let saludo1: string = `Hola, me llamo ${nombre} ${apellidos}`
let numero = 1
let numero2 :number =3

let list: number[] = [1,2,3,4,5]
let list2: Array<number> = [6,7,8,9]
////Tupla
let t: [string, number]
t = ['hola', 32]
// Únicamente recibe string y number



//let nombre: string = “Juan” // explícito
//let nombre2 = “Juan” // implícito

//funciones

function sumar(pNumeroA: number, pNumeroB: number): number {
        let resultado: number = pNumeroA + pNumeroB;
            return resultado;
            }


//Cuando una función no devuelve nada, usamos el tipo de dato contrario a any que es void

function saludo(): void{
   console.log("Hola Mundo!!")
}



//casting

let valor: any = "Es una cadena"
let sizeValor: number = (<string>valor).length
let sizeValor2: number = (valor as string).length

