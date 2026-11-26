package net.unirfp.productos.modelo.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import net.unirfp.productos.modelo.entidades.Familia;

public interface FamiliaRepository extends JpaRepository<Familia, Integer> {
	
	@Query("from Familia f where f.nombre like ?1")
	public List<Familia> buscarTodas(String cadena);
	
	public List<Familia> findByNombreContaining(String cadena);
	
	

}
