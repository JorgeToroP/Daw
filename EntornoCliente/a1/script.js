
const API = "https://jsonblob.com/api/jsonBlob/01a13a6b-8047-7f34-a7e2-172107c33ad4";

const contenedor = document.getElementById("productos");

document.getElementById("cargar").addEventListener("click", cargarProductos);

async function cargarProductos() {
  contenedor.textContent = "Cargando productos...";

  try {
    // 1. Consultamos la API
    const respuesta = await fetch(API);

    if (!respuesta.ok) {
      throw new Error("Error HTTP: " + respuesta.status);
    }

    // 2. Convertimos la respuesta a JSON
    const datos = await respuesta.json();

    // 3. Limpiamos el contenedor
    contenedor.innerHTML = "";

    // 4. Mostramos los productos
    datos.products.forEach(producto => {
      const tarjeta = document.createElement("div");
      tarjeta.className = "producto";

      const nombre = document.createElement("h3");
      nombre.textContent = producto.title;

      const precio = document.createElement("p");
      precio.className = "precio";
      precio.textContent = producto.price + " " + datos.currency;

      tarjeta.append(nombre, precio);
      contenedor.appendChild(tarjeta);
    });

  } catch (error) {
    contenedor.textContent = "No se pudieron cargar los productos.";
    console.error(error);
  }
}
