package net.unirfp.ejemplo.modelo.dao;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Repository;
import org.springframework.stereotype.Service;

import net.unirfp.ejemplo.modelo.javabean.Contacto;
@Repository
public class ContactDaoImpl implements ContactoDao{
	
	private List<Contacto> lista;
	
	public ContactDaoImpl() {
		lista = new ArrayList<>();
		cargarDatos();
	}
	
	private void cargarDatos() {
		lista.add(new Contacto(1001, "Eva", 1_200_000.00, 125, LocalDate.of(2021, 3, 15)));
		lista.add(new Contacto(1002, "Evaristo", 2_200_000.00, 1_125, LocalDate.of(2022, 12, 15)));
		lista.add(new Contacto(1003, "Tomas", 4_200_000.00, 6125, LocalDate.of(1999, 1, 22)));
		lista.add(new Contacto(1004, "Antonio", 200_000.00, 8, LocalDate.of(1987, 7, 7)));
		
		
		
	}

	@Override
	public Contacto findById(int idContacto) {
	/*	for (Contacto contacto: lista) {
			if (contacto.getIdContacto().equals(idContacto))
				return contacto;
		}
		return null;
		*/
		return lista.stream()
				.filter(c -> c.getIdContacto().equals(idContacto))
				.findFirst()
				.orElse(null);
	}

	@Override
	public List<Contacto> findAll() {
		// TODO Auto-generated method stub
		return lista;
	}

	@Override
	public Contacto insertOne(Contacto contacto) {
		if (lista.contains(contacto))
			return null;
		lista.add(contacto);
		return contacto;
	}

	@Override
	public int updateOne(Contacto contacto) {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public int deleteOne(int idContacto) {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public List<Contacto> findByNombreContaining(String cadena) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public List<Contacto> findByFacturacionmayorQue(double facturacion) {
		// TODO Auto-generated method stub
		return null;
	}

}
