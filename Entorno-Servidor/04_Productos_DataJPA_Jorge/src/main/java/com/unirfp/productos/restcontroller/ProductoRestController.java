package com.unirfp.productos.restcontroller;

import java.math.BigDecimal;
import java.util.List;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.unirfp.productos.modelo.entidades.Familia;
import com.unirfp.productos.modelo.entidades.Producto;
import com.unirfp.productos.modelo.service.ProductoService;

@RestController
@RequestMapping("/productos")
@CrossOrigin(origins = "*")
public class ProductoRestController {
	
	private ProductoService productoService;
	
	public ProductoRestController (ProductoService productoService) {
		this.productoService = productoService;
	}
	
	
	@GetMapping("/")
	public List<Producto> todos(){
		return productoService.buscarTodos();
	}
	
	@GetMapping("/marca/{marca}")
	public List<Producto> porMarca(@PathVariable String marca){
		return productoService.buscarPorMarca(marca);
	}
	
	@GetMapping("/precio/{precio}")
	public List<Producto> porprecio(@PathVariable BigDecimal precio){
		return productoService.buscarPorPrecioMayorIgual(precio);
	}
	
	@GetMapping("/familia/{idFamilia}")
	public List<Producto> porfamilia(@PathVariable int idFamilia){
		return productoService.buscarPorFamilia(idFamilia);
	}
	
	
	
	
}
