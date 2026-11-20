package es.daw.biblioteca.modelo;

/**
 * Clase de modelo (POJO). Cada objeto representa una fila de la tabla "libros".
 * Gson la convierte automaticamente a JSON usando el nombre de los atributos.
 */
public class Libro {

    private int id;
    private String titulo;
    private String autor;
    private int anio;
    private int paginas;
    private double valoracion;
    private String genero;
    private String color;

    public Libro() {
    }

    public Libro(int id, String titulo, String autor, int anio, int paginas,
                 double valoracion, String genero, String color) {
        this.id = id;
        this.titulo = titulo;
        this.autor = autor;
        this.anio = anio;
        this.paginas = paginas;
        this.valoracion = valoracion;
        this.genero = genero;
        this.color = color;
    }

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getTitulo() { return titulo; }
    public void setTitulo(String titulo) { this.titulo = titulo; }

    public String getAutor() { return autor; }
    public void setAutor(String autor) { this.autor = autor; }

    public int getAnio() { return anio; }
    public void setAnio(int anio) { this.anio = anio; }

    public int getPaginas() { return paginas; }
    public void setPaginas(int paginas) { this.paginas = paginas; }

    public double getValoracion() { return valoracion; }
    public void setValoracion(double valoracion) { this.valoracion = valoracion; }

    public String getGenero() { return genero; }
    public void setGenero(String genero) { this.genero = genero; }

    public String getColor() { return color; }
    public void setColor(String color) { this.color = color; }
}
