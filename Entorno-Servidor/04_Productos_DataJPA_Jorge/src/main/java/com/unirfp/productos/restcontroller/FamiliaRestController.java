package com.unirfp.productos.restcontroller;

import java.util.List;

import org.springframework.http.HttpStatusCode;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.unirfp.productos.modelo.entidades.Familia;
import com.unirfp.productos.modelo.repository.FamiliaRepository;
import com.unirfp.productos.modelo.service.FamiliaService;

//import io.swagger.v3.oas.annotations.parameters.RequestBody;
import org.springframework.web.bind.annotation.RequestBody;

@RestController
@RequestMapping("/familias")
@CrossOrigin(origins = "*")

public class FamiliaRestController {

	//private FamiliaRepository familiaRepository;
	private FamiliaService familiaService;
	
	public FamiliaRestController(FamiliaService familiaService) {
		this.familiaService = familiaService;
	}
	

	
	@PostMapping("/")
	public ResponseEntity<?> alta(@RequestBody Familia familia){
		familia.setIdFamilia(null);
		if (familiaService.insertOne(familia) !=null) {
			
			return new ResponseEntity<Familia>(familia, HttpStatusCode.valueOf(201));
		}else
			return new ResponseEntity<String> ("No se ha podido insertar, algo esta mal", HttpStatusCode.valueOf(400));
	}
	
	
	
	
	
	@GetMapping("/")
	public List<Familia> todas(){
		return familiaService.buscarTodas();
	}
	
	@GetMapping("/{idFamilia}")
	public Familia una(@PathVariable int idFamilia){
		return familiaService.buscarUno(idFamilia);
	}
	
	@GetMapping("/cadena/{cadena}")
	public List<Familia> cadena(@PathVariable String cadena){
		String like = "%" + cadena + "%";
		return familiaService.buscarPorNombre(like);
	}
	
	@GetMapping("/cadenaDerivado/{cadena}")
	public List<Familia> cadenaDerivado(@PathVariable String cadena){
		return familiaService.buscarPorNombre(cadena);
	}
	
	//actualizacion de jpa
	
}
