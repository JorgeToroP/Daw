package net.unirfp.productos.modelo.dto;

import net.unirfp.productos.modelo.entidades.Producto;

public record ProductoDto(int codigoBarras, String descripcion, 
		String marca, String nombreFamilia) {
	
	public static ProductoDto convertA(Producto pro) {
		ProductoDto pdto = new ProductoDto(pro.getCodigoBarras(), pro.getDescripcion(), 
					pro.getMarca(), pro.getFamilia().getNombre());
		return pdto;
	}

}
