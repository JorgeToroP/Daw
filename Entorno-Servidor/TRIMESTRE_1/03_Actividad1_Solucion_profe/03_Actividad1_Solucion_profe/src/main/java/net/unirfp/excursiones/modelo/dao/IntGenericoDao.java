package net.unirfp.excursiones.modelo.dao;

import java.util.List;

public interface IntGenericoDao<E, ID> {
	
	E findById(ID atributoId);
	List<E> findAll();
	int insertOne(E entidad);
	int updateOne(E entidad);
	int deleteOne(ID atributoId);

}
