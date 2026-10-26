class Carrito{
    //el constructor se ejecuta automaticamente cuando creamos un nuevo carrito
    constructor(productos){
        //creamos lista array vacia,donde guardaremos lo que el usuario comra
        this.cesta = [];
        this.productos = productos;
    }

    //Actualiza las cantidades de un producto en la cesta
    actualizarUnidades(sku, unidades) {
        //1. buscamos si el producto ya esta en la cesta
        let indice = this.cesta.findIndex(producto => producto.sku === sku);

        console.log("Actualizando el SKU : " + sku + " a " + unidades + " Unidades ");
        if(indice === -1){
            //no existe: hacemos el push que ya tenias creado
            this.cesta.push({sku: sku, unidades: unidades});
        }else{
            //existe: actualizamos la cantidad
            this.cesta[indice].cantidad = unidades;
        }
        console.log(this.cesta);
    }

    obtenerInformacionProducto(sku){
        console.log("Obteniendo datos del SKU: " + sku);
        // buscamos en el catalogo el producto que coincida con el sku
        let datosProducto = this.productos.find(producto => producto.sku === sku);
        //buscamos en la cesta las unidades que coincidan con ese sku
        let datosCesta = this.cesta.find(item => item.sku===sku);
        console.log("......Obtener informacion del producto ")
        console.log("nombre = " + datosProducto.title);
        console.log("precio = " + datosProducto.price);
        console.log("cantidad en el carrito = " + datosCesta.cantidad);

    }
    obtenerCarrito(cesta){
        console.log("Obtener datos del Carrito ");

        let carrito = this.cesta.find(cesta => cesta.Carrito === carrito);
        console.log("...........carrito info " + carrito.datosCesta);

    }
}

// 1. Creamos nuestra "base de datos" temporal de productos simulando el JSON de la API
const catalogoProductos = [
  { sku: "0K3QOSOV4V", title: "iPhone 13 Pro", price: "938.99" },
  { sku: "TGD5XORY1L", title: "Cargador", price: "49.99" },
  { sku: "IOKW9BQ9F3", title: "Funda de piel", price: "79.99" }
];

// 2. Instanciamos el carrito pasándole el catálogo al constructor
const miCarrito = new Carrito(catalogoProductos);

// 3. Hacemos una llamada de prueba a tu método
miCarrito.actualizarUnidades("0K3QOSOV4V", 2);
miCarrito.actualizarUnidades("0K3QOSOV4V", 5);
miCarrito.actualizarUnidades("0K3QOSOV4V", 3);
miCarrito.obtenerInformacionProducto("0K3QOSOV4V");
miCarrito.obtenerCarrito;
