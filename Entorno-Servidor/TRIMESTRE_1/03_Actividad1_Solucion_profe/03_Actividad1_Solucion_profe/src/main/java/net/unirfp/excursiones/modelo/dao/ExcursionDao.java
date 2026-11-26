package net.unirfp.excursiones.modelo.dao;

import java.util.List;

import net.unirfp.excursiones.modelo.javabeans.Excursion;

public interface ExcursionDao extends IntGenericoDao<Excursion, Integer>{
	
	List<Excursion> findByActivos();
	List<Excursion> findByDestacados();
	List<Excursion> findByCancelados();
	List<Excursion> findByTerminados();
	
//	ExcursionDto verDetalle(int idExcursion);

}
