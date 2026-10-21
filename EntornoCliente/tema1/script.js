// buscamos el boton en el documento html
const boton = document.getElementById("boton");
//buscamos el parrafo
const mensaje = document.getElementById("mensaje");



// cuando hacemo click en el boton, se ejecuta la funcion
boton.addEventListener("click", function(){
    mensaje.textContent = "sorpresa";
})

if (mensaje.textContent === "sorpresa") {
    mensaje.textContent = "nuevoCambio";
}   


