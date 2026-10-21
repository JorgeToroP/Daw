const alumno = {
  nombre: "Laura",
  edad: 20,
  curso: "Desarrollo Web"
};

document.getElementById("resultado").innerHTML =
  "Nombre: " + alumno.nombre + "<br>" +
  "Edad: " + alumno.edad + "<br>" +
  "Curso: " + alumno.curso + " " +
  typeof alumno;
  ;
