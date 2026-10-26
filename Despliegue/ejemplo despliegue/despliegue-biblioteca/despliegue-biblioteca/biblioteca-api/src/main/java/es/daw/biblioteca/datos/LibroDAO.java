package es.daw.biblioteca.datos;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.ServletContext;

import es.daw.biblioteca.modelo.Libro;

/**
 * DAO (Data Access Object): unico sitio donde se escribe SQL.
 * Los servlets no saben nada de SQL, solo piden datos al DAO.
 * Se usan siempre PreparedStatement con parametros (?) para evitar inyeccion SQL.
 */
public class LibroDAO {

    private final ServletContext ctx;

    public LibroDAO(ServletContext ctx) {
        this.ctx = ctx;
    }

    /** Consulta 1: busqueda de libros por texto y/o genero (SELECT con JOIN y filtros). */
    public List<Libro> buscar(String texto, String genero) throws SQLException {
        StringBuilder sql = new StringBuilder(
            "SELECT l.id, l.titulo, l.autor, l.anio, l.paginas, l.valoracion, " +
            "       g.nombre AS genero, g.color " +
            "FROM libros l JOIN generos g ON l.genero_id = g.id " +
            "WHERE 1 = 1 ");
        List<String> parametros = new ArrayList<>();

        if (texto != null && !texto.trim().isEmpty()) {
            sql.append("AND (l.titulo LIKE ? OR l.autor LIKE ?) ");
            String patron = "%" + texto.trim() + "%";
            parametros.add(patron);
            parametros.add(patron);
        }
        if (genero != null && !genero.trim().isEmpty()) {
            sql.append("AND g.nombre = ? ");
            parametros.add(genero.trim());
        }
        sql.append("ORDER BY l.valoracion DESC, l.titulo");

        List<Libro> libros = new ArrayList<>();
        try (Connection con = BaseDatos.abrir(ctx);
             PreparedStatement ps = con.prepareStatement(sql.toString())) {
            for (int i = 0; i < parametros.size(); i++) {
                ps.setString(i + 1, parametros.get(i));
            }
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    libros.add(new Libro(
                        rs.getInt("id"),
                        rs.getString("titulo"),
                        rs.getString("autor"),
                        rs.getInt("anio"),
                        rs.getInt("paginas"),
                        rs.getDouble("valoracion"),
                        rs.getString("genero"),
                        rs.getString("color")));
                }
            }
        }
        return libros;
    }

    /** Consulta 2: lista de generos con su color. */
    public List<Map<String, Object>> generos() throws SQLException {
        String sql = "SELECT id, nombre, color FROM generos ORDER BY nombre";
        List<Map<String, Object>> lista = new ArrayList<>();
        try (Connection con = BaseDatos.abrir(ctx);
             PreparedStatement ps = con.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                Map<String, Object> fila = new LinkedHashMap<>();
                fila.put("id", rs.getInt("id"));
                fila.put("nombre", rs.getString("nombre"));
                fila.put("color", rs.getString("color"));
                lista.add(fila);
            }
        }
        return lista;
    }

    /** Consulta 3: estadisticas por genero (GROUP BY con COUNT, AVG y SUM). */
    public List<Map<String, Object>> estadisticas() throws SQLException {
        String sql =
            "SELECT g.nombre, g.color, COUNT(l.id) AS total, " +
            "       ROUND(AVG(l.valoracion), 2) AS media, " +
            "       COALESCE(SUM(l.paginas), 0) AS paginas " +
            "FROM generos g LEFT JOIN libros l ON l.genero_id = g.id " +
            "GROUP BY g.id, g.nombre, g.color " +
            "ORDER BY total DESC, g.nombre";
        List<Map<String, Object>> lista = new ArrayList<>();
        try (Connection con = BaseDatos.abrir(ctx);
             PreparedStatement ps = con.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                Map<String, Object> fila = new LinkedHashMap<>();
                fila.put("genero", rs.getString("nombre"));
                fila.put("color", rs.getString("color"));
                fila.put("total", rs.getInt("total"));
                fila.put("media", rs.getDouble("media"));
                fila.put("paginas", rs.getLong("paginas"));
                lista.add(fila);
            }
        }
        return lista;
    }

    /** Consulta 4: alta de un libro nuevo (INSERT). Devuelve el id generado. */
    public int insertar(String titulo, String autor, int anio, int paginas,
                        double valoracion, String genero) throws SQLException {
        String sql =
            "INSERT INTO libros (titulo, autor, anio, paginas, valoracion, genero_id) " +
            "SELECT ?, ?, ?, ?, ?, id FROM generos WHERE nombre = ?";
        try (Connection con = BaseDatos.abrir(ctx);
             PreparedStatement ps = con.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {
            ps.setString(1, titulo);
            ps.setString(2, autor);
            ps.setInt(3, anio);
            ps.setInt(4, paginas);
            ps.setDouble(5, valoracion);
            ps.setString(6, genero);
            int filas = ps.executeUpdate();
            if (filas == 0) {
                throw new SQLException("El genero '" + genero + "' no existe");
            }
            try (ResultSet claves = ps.getGeneratedKeys()) {
                return claves.next() ? claves.getInt(1) : -1;
            }
        }
    }

    /** Comprobacion rapida de que la base de datos responde. Devuelve la version de MariaDB. */
    public String versionServidor() throws SQLException {
        try (Connection con = BaseDatos.abrir(ctx);
             PreparedStatement ps = con.prepareStatement("SELECT VERSION()");
             ResultSet rs = ps.executeQuery()) {
            return rs.next() ? rs.getString(1) : "desconocida";
        }
    }
}
