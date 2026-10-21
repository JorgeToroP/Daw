document.addEventListener("DOMContentLoaded", function(event) {
//codigo Javascript que manipula el DOM


const titulo = document.getElementById("titulo");
console.log(titulo);


const parrafos = document.querySelectorAll(".parrafo");
console.log(parrafos);


titulo.innerText = "!Hola DOM!";

const parrafo1 = document.getElementById("parrafo1");
parrafo1.classList.add("destacado");

const boton = document.createElement("button");
boton.innerText = "pulsame";
document.body.appendChild(boton);

boton.addEventListener("click", function(){
    alert("Has pulsado el botón");

})





})