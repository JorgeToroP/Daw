package com.unirfp.productos.modelo.entidades;

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
@Table(name= "PRODUCTOS")
public class Producto {
	@Id
	@Column(name = "CODIGO_BARRAS")
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	
	private Integer codigoBarras; //codigo_barras;// int not null primary key auto_increment,
    private String descripcion; //varchar(200) not null,
    private String marca; // varchar(100),
    @Column(name = "PRECIO_UNITARIO")
    private BigDecimal precioUnitario; //dec(9,2),
    private Integer stock; // int,
    @Column(name = "FECHA_ALTA")
    private LocalDate fechaAlta; //fecha_alta; // date
    //unidireccional : muchos productos de una Familia
    @ManyToOne
    @JoinColumn(name = "ID_FAMILIA")
    private Familia familia; // int not null,
	
}
