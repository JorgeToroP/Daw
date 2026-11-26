package net.unirfp.ejemplo.restcontroller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import net.unirfp.ejemplo.modelo.dao.ContactoDao;
import net.unirfp.ejemplo.modelo.javabean.Contacto;
@RestController
@RequestMapping("/contactos")
public class ContactoRestController {
	
	private ContactoDao contactoDao;
	
	public ContactoRestController(ContactoDao contactoDao) {
		this.contactoDao = contactoDao;
	}
	
	@PostMapping("/")
	public Contacto alta(@RequestBody Contacto contacto) {
		return contactoDao.insertOne(contacto);
	}
	
	@GetMapping("/{idContacto}")
	public Contacto uno(@PathVariable Integer idContacto){
		
		return contactoDao.findById(idContacto);
		
	}
	
	@GetMapping("/")
	public List<Contacto> todos(){
		
		return contactoDao.findAll();
		
	}
	
	

}
