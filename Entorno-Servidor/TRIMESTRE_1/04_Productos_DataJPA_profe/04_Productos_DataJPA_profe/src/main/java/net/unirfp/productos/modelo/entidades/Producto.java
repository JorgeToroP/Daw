package net.unirfp.productos.modelo.entidades;

import java.math.BigDecimal;
import java.time.LocalDate;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
@AllArgsConstructor
@NoArgsConstructor
@Data
@EqualsAndHashCode(of = "codigoBarras")
@Builder

@Entity
@Table(name="PRODUCTOS")
public class Producto {
	@Id
	@Column(name = "CODIGO_BARRAS")
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer codigoBarras;
	private String descripcion;
	private String marca;
	@Column(name = "PRECIO_UNITARIO")
	private BigDecimal precioUnitario;
	private Integer  stock;
	@Column(name = "FECHA_ALTA")
	private LocalDate fechaAlta;
	// unidireccional: muchos productos de una Familia
	@ManyToOne
	@JoinColumn(name = "ID_FAMILIA")
	private Familia familia; // id_familia int not null,

}
