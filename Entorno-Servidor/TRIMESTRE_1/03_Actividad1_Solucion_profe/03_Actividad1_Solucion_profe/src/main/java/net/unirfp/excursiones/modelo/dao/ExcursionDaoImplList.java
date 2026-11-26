package net.unirfp.excursiones.modelo.dao;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import net.unirfp.excursiones.modelo.javabeans.Excursion;
@Repository
// @Service
public class ExcursionDaoImplList implements ExcursionDao{
	
//	@Autowired
	private List<Excursion> lista;
	
	public ExcursionDaoImplList(List<Excursion> lista) {
		this.lista = lista;
	}

	@Override
	public Excursion findById(Integer atributoId) {
		// TODO Auto-generated method stub
		return lista.stream()
				.filter(ex -> ex.getIdExcursion() == atributoId)
				.findFirst()
				.orElse(null)
				;
	}

	@Override
	public List<Excursion> findAll() {
		// TODO Auto-generated method stub
		return lista;
	}

	@Override
	public int insertOne(Excursion entidad) {
		if (lista.contains(entidad))
			return 0;
		else
		{
			lista.add(entidad);
			return 1;
		}
	}

	@Override
	public int updateOne(Excursion entidad) {
		int posicion = lista.indexOf(entidad);
		
		if (posicion == -1)
			return 0;
		else {
			lista.set(posicion, entidad);
			return 1;
		}
	}

	@Override
	public int deleteOne(Integer atributoId) {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public List<Excursion> findByActivos() {
		// TODO Auto-generated method stub
		return lista.stream()
				.filter(ex -> ex.getEstado().equals("CREADO"))
				.toList();
				
				
	}

	@Override
	public List<Excursion> findByDestacados() {
		return lista.stream()
				.filter(ex -> ex.getDestacado().equals("S"))
				.toList();
	}

	@Override
	public List<Excursion> findByCancelados() {
		return lista.stream()
				.filter(ex -> ex.getEstado().equals("CANCELADO"))
				.toList();
	}

	@Override
	public List<Excursion> findByTerminados() {
		return lista.stream()
				.filter(ex -> ex.getEstado().equals("TERMINADO"))
				.toList();
	}

}
