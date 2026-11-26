package net.unirfp.ejemplo.modelo.javabean;

import java.io.Serializable;
import java.time.LocalDate;
import java.util.Objects;

public class Contacto implements Serializable{
	
	
	private static final long serialVersionUID = 1L;
	
	
	private Integer idContacto;
	private String nombre;
	private Double facturacionAnual;
	private Integer cantidadEmpleados;
	private LocalDate fechaCreacion;
	
	public Contacto() {
		super();
	}

	public Contacto(Integer idContacto, String nombre, Double facturacionAnual, Integer cantidadEmpleados,
			LocalDate fechaCreacion) {
		super();
		this.idContacto = idContacto;
		this.nombre = nombre;
		this.facturacionAnual = facturacionAnual;
		this.cantidadEmpleados = cantidadEmpleados;
		this.fechaCreacion = fechaCreacion;
	}

	public Integer getIdContacto() {
		return idContacto;
	}

	public void setIdContacto(Integer idContacto) {
		this.idContacto = idContacto;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public Double getFacturacionAnual() {
		return facturacionAnual;
	}

	public void setFacturacionAnual(Double facturacionAnual) {
		this.facturacionAnual = facturacionAnual;
	}

	public Integer getCantidadEmpleados() {
		return cantidadEmpleados;
	}

	public void setCantidadEmpleados(Integer cantidadEmpleados) {
		this.cantidadEmpleados = cantidadEmpleados;
	}

	public LocalDate getFechaCreacion() {
		return fechaCreacion;
	}

	public void setFechaCreacion(LocalDate fechaCreacion) {
		this.fechaCreacion = fechaCreacion;
	}

	@Override
	public int hashCode() {
		return Objects.hash(idContacto);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!(obj instanceof Contacto))
			return false;
		Contacto other = (Contacto) obj;
		return Objects.equals(idContacto, other.idContacto);
	}

	@Override
	public String toString() {
		return "Contacto [idContacto=" + idContacto + ", nombre=" + nombre + ", facturacionAnual=" + facturacionAnual
				+ ", cantidadEmpleados=" + cantidadEmpleados + ", fechaCreacion=" + fechaCreacion + "]";
	}
	
	
	public double ratioFacturacion() {
		return facturacionAnual / cantidadEmpleados;
	}

}
