package net.unirfp.excursiones.configuracion;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import net.unirfp.excursiones.modelo.javabeans.Excursion;

@Configuration
public class ConfiguracionBeans {
	
	@Bean
	List<Excursion> getExcursiones(){
		
		List<Excursion> lista = new ArrayList<>();
		
		// Lista obtenida de chatgpt
		lista.add(new Excursion(1, "Visita cultural a Toledo", "Madrid", "Toledo",
		        LocalDate.of(2027, 3, 15), 8, "CREADO", "S",
		        40, 10, 45.50, "toledo.jpg", LocalDate.of(2026, 10, 1)));

		lista.add(new Excursion(2, "Ruta por Segovia", "Madrid", "Segovia",
		        LocalDate.of(2027, 3, 20), 7, "CREADO", "N",
		        35, 12, 39.90, "segovia.jpg", LocalDate.of(2026, 10, 5)));

		lista.add(new Excursion(3, "Excursión a Ávila", "Guadalajara", "Ávila",
		        LocalDate.of(2026, 9, 5), 6, "TERMINADO", "N",
		        30, 10, 35.00, "avila.jpg", LocalDate.of(2026, 6, 10)));

		lista.add(new Excursion(4, "Visita monumental a Salamanca", "Madrid", "Salamanca",
		        LocalDate.of(2027, 4, 12), 10, "CREADO", "S",
		        45, 15, 55.00, "salamanca.jpg", LocalDate.of(2026, 10, 10)));

		lista.add(new Excursion(5, "Ruta por Cuenca", "Alcalá de Henares", "Cuenca",
		        LocalDate.of(2026, 10, 18), 8, "CANCELADO", "N",
		        40, 12, 42.50, "cuenca.jpg", LocalDate.of(2026, 8, 15)));

		lista.add(new Excursion(6, "Monasterio de El Escorial", "Madrid", "El Escorial",
		        LocalDate.of(2027, 5, 3), 5, "CREADO", "N",
		        25, 8, 29.90, "escorial.jpg", LocalDate.of(2026, 10, 12)));

		lista.add(new Excursion(7, "Jardines de Aranjuez", "Guadalajara", "Aranjuez",
		        LocalDate.of(2026, 7, 10), 6, "TERMINADO", "S",
		        35, 10, 32.00, "aranjuez.jpg", LocalDate.of(2026, 3, 20)));

		lista.add(new Excursion(8, "Senderismo por la Sierra de Guadarrama", "Madrid", "Cercedilla",
		        LocalDate.of(2027, 5, 17), 7, "CREADO", "S",
		        20, 6, 25.00, "guadarrama.jpg", LocalDate.of(2026, 10, 15)));

		lista.add(new Excursion(9, "Visita a Alcalá de Henares", "Toledo", "Alcalá de Henares",
		        LocalDate.of(2026, 8, 7), 5, "TERMINADO", "N",
		        30, 10, 27.50, "alcala.jpg", LocalDate.of(2026, 5, 1)));

		lista.add(new Excursion(10, "Excursión gastronómica a Chinchón", "Madrid", "Chinchón",
		        LocalDate.of(2027, 6, 14), 6, "CANCELADO", "S",
		        30, 8, 60.00, "chinchon.jpg", LocalDate.of(2026, 10, 18)));
		
		
		return lista;
		
		
	}

}
