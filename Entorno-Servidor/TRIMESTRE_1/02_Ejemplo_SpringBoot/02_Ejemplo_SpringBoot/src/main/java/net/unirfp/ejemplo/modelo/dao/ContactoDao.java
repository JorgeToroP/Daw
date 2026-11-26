package net.unirfp.ejemplo.modelo.dao;

import java.util.List;

import net.unirfp.ejemplo.modelo.javabean.Contacto;

public interface ContactoDao {
	
	Contacto findById(int idContacto);
	List<Contacto> findAll();
	Contacto insertOne(Contacto contacto);
	int updateOne(Contacto contacto);
	int deleteOne(int idContacto);
	
	List<Contacto> findByNombreContaining(String cadena);
	List<Contacto> findByFacturacionmayorQue(double facturacion);

}
