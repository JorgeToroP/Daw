  // Recibe dos argumentos: la función a ejecutar y el tiempo (en milisegundos) que va a esperar a ejecutarla 
 const saludar = function() {
    console.log("Hola");
  }
  setTimeout(saludar, 1000);

  // Pasado 1 segundo mostrará por consola: Hola
  setInterval(function() {
    console.log("hola");
  }, 1000);
  // Cada segundo mostrará por consola: Hola
  // Tanto setTimeout y setInterval al crearse devuelven un id
  // Ese id es necesario para poder "limpiar" el intervalo
  
  const intervalId = setInterval(function() {
    console.log("hola");
  }, 1000);


  setTimeout(function() {
    clearInterval(intervalId);
  }, 3000);




  // Segundo 1: hola
  // Segundo 2: hola
  // Segundo 3: no se ve nada por consola porque se ha limpiado el intervalo