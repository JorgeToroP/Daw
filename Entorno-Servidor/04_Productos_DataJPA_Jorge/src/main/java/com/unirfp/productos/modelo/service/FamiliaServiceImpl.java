package com.unirfp.productos.modelo.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.unirfp.productos.modelo.entidades.Familia;
import com.unirfp.productos.modelo.repository.FamiliaRepository;
import com.unirfp.productos.restcontroller.FamiliaRestController;

//import jdk.internal.org.jline.terminal.TerminalBuilder.SystemOutput;

@Service
public class FamiliaServiceImpl implements FamiliaService{
	
	
	private final ProductoServiceImpl productoServiceImpl;
	private FamiliaRepository familiaRepository;
	
	public FamiliaServiceImpl(FamiliaRepository familiaRepository, ProductoServiceImpl productoServiceImpl) {
		this.familiaRepository = familiaRepository;
		this.productoServiceImpl = productoServiceImpl;
	}
	
	@Override
	public Familia buscarUno(int idFamilia) {

		return familiaRepository.findById(idFamilia).orElse(null);
	}

	@Override
	public List<Familia> buscarTodas() {
		// TODO Auto-generated method stub
		return familiaRepository.findAll();
	}

	@Override
	public List<Familia> buscarPorNombre(String subcadena) {
		// TODO Auto-generated method stub
		return familiaRepository.findByNombreContaining(subcadena);
	}

	@Override
	public Familia insertOne(Familia familia) {
		try {
		return familiaRepository.save(familia);
		}catch(Exception e) {
			System.out.println(e.getMessage());
			return null;
		}
	}

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}
