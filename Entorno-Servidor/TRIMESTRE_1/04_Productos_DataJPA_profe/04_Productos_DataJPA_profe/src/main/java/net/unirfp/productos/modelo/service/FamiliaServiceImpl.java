package net.unirfp.productos.modelo.service;

import java.util.List;

import org.springframework.stereotype.Service;

import net.unirfp.productos.modelo.entidades.Familia;
import net.unirfp.productos.modelo.repository.FamiliaRepository;
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
		// TODO Auto-generated method stub
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
	//	return familiaRepository.findByNombreContaining(subcadena);
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
