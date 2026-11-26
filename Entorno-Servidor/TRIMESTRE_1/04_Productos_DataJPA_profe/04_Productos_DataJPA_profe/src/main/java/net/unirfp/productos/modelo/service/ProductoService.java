package net.unirfp.productos.modelo.service;

import java.math.BigDecimal;
import java.util.List;

import net.unirfp.productos.modelo.entidades.Producto;

public interface ProductoService {
	
	Producto insertOne(Producto producto);
	Producto buscarUno(int codigoBarras);
	List<Producto> buscarPorFamilia(int idFamilia);
	List<Producto> buscarPorDescripcion(String  subcadena);
	List<Producto> buscarTodos();
	List<Producto> buscarPorPreciomayorIgual(BigDecimal precio);
	List<Producto> buscarPorMarca(String marca);
	
	
	
	

}
