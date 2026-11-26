package net.unirfp.excursiones.restcontroller;

import java.util.List;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

//import io.swagger.v3.oas.annotations.parameters.RequestBody;
import net.unirfp.excursiones.modelo.dao.ExcursionDao;
import net.unirfp.excursiones.modelo.javabeans.Excursion;

@RestController
@RequestMapping("/excursiones")
//@CrossOrigin(origins = "*")
public class ExcursionRestController {
	
	private ExcursionDao excursionDao;
	
	public ExcursionRestController(ExcursionDao excursionDao) {
		this.excursionDao = excursionDao;
	}
	/*
	 * ojo que requestbody está en swagger y hay que importarlo de spring
	 */
	@PostMapping("/")
	public String altaExcursion(@RequestBody  Excursion excursion) {
		System.out.println(excursion);
		if (excursionDao.insertOne(excursion) == 1)
			return "Alta confirmada";
		else
			return "Alta no confirmada, normalmente ya existe este ID";
	}
	
	@GetMapping("/{idExcursion}")
	public Excursion buscarUna(@PathVariable int idExcursion) {
		return excursionDao.findById(idExcursion);
	}
	
	@GetMapping("/")
	List<Excursion> todos(){
		
		return excursionDao.findAll();
		
		
	}
	
	@GetMapping("/terminados")
	List<Excursion> terminados(){
		
		return excursionDao.findByTerminados();
		
		
	}
	
	@GetMapping("/destacados")
	List<Excursion> destacados(){
		
		return excursionDao.findByDestacados();
		
		
	}
	
	@PutMapping("/")
	public String update(@RequestBody Excursion excursion) {
		
		if (excursionDao.updateOne(excursion) == 1)
			return "Excursion modificada con exito";
		else
			return "LA Excursion no se ha modificado, seguramente porque el id no existe";
		
		
		
		
	}

}
