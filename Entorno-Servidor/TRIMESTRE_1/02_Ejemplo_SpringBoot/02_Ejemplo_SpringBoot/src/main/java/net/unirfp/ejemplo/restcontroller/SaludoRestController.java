package net.unirfp.ejemplo.restcontroller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SaludoRestController {
	
	
	@GetMapping("/saludar")
	public String saludo() {
		
		return "Hola me llamo Tomas y soy tu profe";
	}
	
	@GetMapping("/param")
	public String parametrosDePeticion(@RequestParam String nombre, 
										@RequestParam int edad) {
		
		
		return "Hola te llamas : " + nombre + " edad : " + edad;
	}
	
//	@GetMapping("/variable/{nombre}/{edad}")
	@GetMapping("/variable/nombre/{nombre}/edad/{edad}")
	
	public String variablesDelPath(@PathVariable String nombre, 
									@PathVariable int edad) {
		
		
		return "Hola te llamas desde pathVariable : " + nombre + " edad : " + edad;
	}
	

}
