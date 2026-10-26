package es.daw.biblioteca.datos;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

import javax.servlet.ServletContext;

/**
 * Centraliza la conexion con MariaDB.
 * Los datos de conexion NO estan escritos en el codigo: se leen de WEB-INF/web.xml
 * (parametros de contexto), asi se pueden cambiar sin recompilar.
 */
public final class BaseDatos {

    private static final String DRIVER = "org.mariadb.jdbc.Driver";

    private BaseDatos() {
    }

    public static Connection abrir(ServletContext ctx) throws SQLException {
        try {
            // En Tomcat conviene cargar el driver de forma explicita, porque el driver
            // esta en WEB-INF/lib (cargador de clases de la aplicacion)
            Class.forName(DRIVER);
        } catch (ClassNotFoundException e) {
            throw new SQLException("No se encuentra el driver de MariaDB en el WAR", e);
        }

        String url = ctx.getInitParameter("db.url");
        String usuario = ctx.getInitParameter("db.usuario");
        String clave = ctx.getInitParameter("db.clave");

        return DriverManager.getConnection(url, usuario, clave == null ? "" : clave);
    }
}
