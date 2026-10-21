const productosTienda = {

    "currency": "€",
    "products": [
        {
            "SKU": "0K3QOSOV4V",
            "title": "iFhone 13 Pro",
            "price": "938.99"
        },
        {
            "SKU": "TGD5XORY1L",
            "title": "Cargador",
            "price": "49.99"
        },
        {
            "SKU": "IOKW9BQ9F3",
            "title": "Funda de piel",
            "price": "79.99"
        },
        {
            "SKU": "IOKW9BQ000",
            "title": "Google pixel",
            "price": "979.99"
        },
        {
            "SKU": "IOKW9BQ009",
            "title": "vivo x300 ultra",
            "price": "1179.99"
        },
        {
            "SKU": "IOKW9BQ008",
            "title": "auriculares corsair",
            "price": "119.99"
        },
        {
            "SKU": "IOKW9B0009",
            "title": "vivo x500 pro",
            "price": "1079.99"
        },
        {
            "SKU": "IOKW9B0008",
            "title": "auriculares xiaomi",
            "price": "109.99"
        }
    ]
}

class Carrito {

    constructor(productos) {
        this.productos = productos;
        this.total = 0;
        this.moneda = "€"
    }
    actualizarUnidades(sku, unidades) {
        //Actualiza el número de unidades que se quieren comprar de un producto 
        let productoEncontrado = this.productos.find(uni => uni.SKU === sku);
        if (productoEncontrado) {
            productoEncontrado.quantity = unidades;
        }
    }

    obtenerInformacionProducto(sku) {
        //Devuelve los datos de un producto además de las unidades seleccionadas 
        let productoEncontrado = this.productos.find(uni => uni.SKU === sku);
        //si lo encontramos, devolvemos el objeto al completo
        if (productoEncontrado) {
            return productoEncontrado;
        }
    }

    /* Devuelve información de los productos añadidos al carrito 
      Además del total calculado de todos los productos */
    obtenerCarrito() {
        this.total = 0;
        let carrito = []

        this.productos.forEach(product => {
            if (product.quantity > 0) {
                this.total = this.total + (parseFloat(product.price) * product.quantity);
                //agrego al array un nuevo obejto solo con la informacion
                carrito.push({ sku: product.SKU })
            }
        });
        //Devuelve información de los productos añadidos al carrito 
        // Además del total calculado de todos los productos 
        return {
            total: this.total,
            currency: this.moneda,
            products: carrito
        };
    }
}

const miCarrito = new Carrito(productosTienda.products);

//-----------------------DOM-------------------------

function mostrarProducto() {
    const contenedor = document.getElementById("Lista-productos");

    let htmlAcumulado = "";

    //recorremos los datos
    productosTienda.products.forEach(product => {
        //a;adimos al acumulador un bloque html por cada producto
        htmlAcumulado = htmlAcumulado + `
            <div class="producto">
                <h3>${product.title}</h3>
                <p class="precio">Price: ${product.price} €</p>
                <button class="boton-sumar" data-sku="${product.SKU}">Agregar al carrito</button>
                <button class="boton-restar" data-sku="${product.SKU}">-</button>
                <hr>
            </div>
        `;

    });

    //intectamos ese texto html dentro del contenedor
    contenedor.innerHTML = htmlAcumulado;
}
mostrarProducto();


function actualizarPantalla() {
    let estadoCarrito = miCarrito.obtenerCarrito();

    document.getElementById("total-carrito").innerHTML = estadoCarrito.total.toFixed(2);

    const vistaCarrito = document.getElementById("resumen-carrito");
    let resumenHtml = "";

    estadoCarrito.products.forEach(item => {
        let info = miCarrito.obtenerInformacionProducto(item.sku);
        resumenHtml = resumenHtml + `
        <div class="item-resumen">
            <p><strong>Producto: </strong>${info.title}<strong> Cantidad: </strong>${info.quantity}<strong> Precio: </strong> ${(parseFloat(info.price) * info.quantity).toFixed(2)}€</p>
            <hr>
        </div>
        `;
    });

    vistaCarrito.innerHTML = resumenHtml;

}
actualizarPantalla();


function configurarBotonesSumar() {
    const botonesCesta = document.querySelectorAll('.boton-sumar');

    botonesCesta.forEach(boton => {
        //le ponemos un escuchador para el evento click"
        boton.addEventListener('click', (evento) => {
            //averiguo el id oculto recien pulsado
            let SKU = evento.target.dataset.sku;
            //pedimos la info del producto al carrito
            let prod = miCarrito.obtenerInformacionProducto(SKU);
            //calcular unidades
            let unidadesActuales = prod.quantity || 0;
            let nuevasUnidades = unidadesActuales + 1;

            //actualizamos las unidades del sku
            miCarrito.actualizarUnidades(SKU, nuevasUnidades);

            // llamamos la funcion actualizarPantalla
            actualizarPantalla();
        });
    });

}
configurarBotonesSumar();

function configurarBotonesRestar() {
    const botonesCesta = document.querySelectorAll('.boton-restar');

    botonesCesta.forEach(boton => {
        boton.addEventListener('click', (evento) => {
            let SKU = evento.target.dataset.sku;
            let prod = miCarrito.obtenerInformacionProducto(SKU);
            let unidadesActuales = prod.quantity || 0;
            if (unidadesActuales > 0) {
                let nuevasUnidades = unidadesActuales - 1;

                miCarrito.actualizarUnidades(SKU, nuevasUnidades);
                actualizarPantalla();

            }
        })
    })
}
configurarBotonesRestar();


/*

// Cada botón cambia una cantidad y vuelve a dibujar la pantalla.
function cambiar(sku, cambio) {
const producto = carrito.obtenerInformacionProducto(sku);
carrito.actualizarUnidades(sku, producto.quantity + cambio);
mostrar();

//Pedimos los productos e iniciamos el carrito.
const URL_API = "api.php";

async function iniciar() {
try {
const respuesta = await fetch(URL_API);
if (!respuesta.ok) throw new Error("HTTP " + respuesta. status);
const datos = await respuesta.json();
carrito = new Carrito(datos.products, datos.currency);
mostrar();
estado.textContent = "Productos cargados. Usa
} catch (error) {
estado.textContent = "No se pudieron cargar los productos: " + error.message;
}
}

iniciar();

y + para cambiar las unidades.";

*/