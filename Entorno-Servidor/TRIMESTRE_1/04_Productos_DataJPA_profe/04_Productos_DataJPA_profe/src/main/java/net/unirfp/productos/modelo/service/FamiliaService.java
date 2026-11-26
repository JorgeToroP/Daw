package net.unirfp.productos.modelo.service;

import java.util.List;

import net.unirfp.productos.modelo.entidades.Familia;
// Interface para el FamiliaRestController
public interface FamiliaService {
	
	Familia buscarUno(int idFamilia);
	List<Familia> buscarTodas();
	List<Familia> buscarPorNombre(String subcadena);
	Familia insertOne(Familia familia);
	

}
