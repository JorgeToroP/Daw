const titulo = document.getElementById("titulo");
const mensaje = document.getElementById("mensaje");
const boton = document.getElementById("boton");


boton.addEventListener("click", function() {
   
    titulo.textContent = "Cambiamos el titulo";
    mensaje.textContent = "¡lo que sucede si clickeas el boton!";

});

