const titulo = document.getElementById("titulo");
console.log(titulo);

//innerText devuelve el texto que hay dentro del elemento
console.log(titulo.innerText);

//query selector devuelve el primero que coincida con el selector
console.log(document.querySelector('.precio').innerText); //10 €

console.log(precios.length); //2

//querySelectorAll devuelve todos los elementos que coincidan con el selector
const precios = document.querySelectorAll('.precio');

console.log(document.getElementById('nada')); //null

function cambiarTitulo() {
    titulo.innerText = "Estos sonn los cambios con innerText que se hacen con la funcion cambiarTitulo CON EL ELEMENTO ONCLICK"; //cambia el texto del elemento con id titulo
}

function cambiarTexto(){
    const pasarRaton = document.getElementById('pasarRaton');//cambia el texto del elemento con id pasarRaton
    pasarRaton.innerText = "Esto es un cambio de texto con innerText que se hace con la funcion cambiarTexto CON EL ELEMENTO ONMOUSEOVER"; //cambia el texto del elemento con id pasarRaton
}

function mostrarOpcion(){
    const mostrar = document.getElementById('mostrar');//cambia el texto del elemento con id mostrar
    mostrar.innerText = "Esto es un cambio de texto con innerText que se hace con la funcion mostrarOpcion CON EL ELEMENTO ONMOUSEOUT"; //cambia el texto del elemento con id mostrar
}