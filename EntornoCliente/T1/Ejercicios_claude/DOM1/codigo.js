//getElementById devuelve el elemento que tenga el id que le pasemos
const s = document.getElementById('saludo');
console.log(s);

//innerText devuelve el texto que hay dentro del elemento
console.log(s.innerText);

//query selector devuelve el rpiumero que coincida con el selector
console.log(document.querySelector('.nota').innerText); //7

//querySelectorAll devuelve todos los elementos que coincidan con el selector
const notas = document.querySelectorAll('.nota');
console.log(notas.length); //NodeList(3) [li.nota, li.nota, li.nota]

//buscar algo que no existe devuelve null
console.log(document.getElementById('#nada')); //null

//funcion que se ejecuta cuando se hace click en el boton
function cambiar() {
    s.innerText = "esto lo metimos en la constante s y la llamamos con la funcion cambiar"; //cambia el texto del elemento con id saludo
}

