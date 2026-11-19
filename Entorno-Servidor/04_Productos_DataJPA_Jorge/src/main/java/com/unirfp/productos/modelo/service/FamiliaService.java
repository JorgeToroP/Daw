package com.unirfp.productos.modelo.service;

import java.util.List;

import com.unirfp.productos.modelo.entidades.Familia;
//Interface para el controlador// familiaRestController
public interface FamiliaService {

	Familia buscarUno(int idFamilia);
	List<Familia> buscarTodas();
	List<Familia> buscarPorNombre(String subcadena);
	Familia insertOne(Familia familia);
	
	
}
