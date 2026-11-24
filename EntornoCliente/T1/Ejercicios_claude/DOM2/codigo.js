const titulo = document.getElementById("titulo");
console.log(titulo);

//innerText devuelve el texto que hay dentro del elemento
console.log(titulo.innerText);

//query selector devuelve el primero que coincida con el selector
console.log(document.querySelector('.precio').innerText); //10 €

//querySelectorAll devuelve todos los elementos que coincidan con el selector
const precios = document.querySelectorAll('.precio');

console.log(document.getElementById('nada')); //null

function cambiarTitulo() {
    titulo.innerText = "Estos sonn los cambios con innerText que se hacen con la funcion cambiarTitulo"; //cambia el texto del elemento con id titulo
}

