package net.unirfp.productos.modelo.service;

import java.math.BigDecimal;
import java.util.List;

import org.springframework.stereotype.Service;

import net.unirfp.productos.modelo.entidades.Producto;
import net.unirfp.productos.modelo.repository.ProductoRepository;
@Service
public class ProductoServiceImpl implements ProductoService{
	
	private ProductoRepository productoRepository;
	
	public ProductoServiceImpl(ProductoRepository productoRepository) {
		this.productoRepository = productoRepository;
	}

	@Override
	public Producto insertOne(Producto producto) {
		// TODO Auto-generated method stub
		return null;
	}

	
	@Override
	public Producto buscarUno(int codigoBarras) {
		// TODO Auto-generated method stub
		return productoRepository.findById(codigoBarras).orElse(null);
	}

	@Override
	public List<Producto> buscarPorFamilia(int idFamilia) {
		// TODO Auto-generated method stub
		return productoRepository.findPorFamilia(idFamilia);
	}

	@Override
	public List<Producto> buscarPorDescripcion(String subcadena) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public List<Producto> buscarTodos() {
		// TODO Auto-generated method stub
		return productoRepository.findAll();
	}

	@Override
	public List<Producto> buscarPorPreciomayorIgual(BigDecimal precio) {
		// TODO Auto-generated method stub
		return productoRepository.findByPrecioUnitarioGreaterThanEqual(precio);
	}

	@Override
	public List<Producto> buscarPorMarca(String marca) {
		// TODO Auto-generated method stub
		return productoRepository.findByMarca(marca);
	}

}
