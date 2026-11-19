package com.unirfp.productos.modelo.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import com.unirfp.productos.modelo.entidades.Producto;
import java.math.BigDecimal;


public interface ProductoRepository extends JpaRepository<Producto, Integer>{
//	@Query("from Producto p where p.marca = ?1 " )
	public List<Producto> findByMarca(String marca);
	
	public List<Producto> findByPrecioUnitarioGreaterThanEqual(BigDecimal precio);
	
	//select * from productos where id_familia = 1;
	@Query("select p from Producto p where p.familia.idFamilia = ?1 ")
	public List<Producto> findPorFamilia(int idFamilia);
	
	public List<Producto> findByFamilia_IdFamilia(int idFamilia);
	
	
}
