package es.daw.biblioteca.web;

import java.io.IOException;
import java.net.InetAddress;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.LinkedHashMap;
import java.util.Map;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import es.daw.biblioteca.datos.LibroDAO;

/**
 * GET /api/estado -> informacion de la infraestructura.
 * Sirve para comprobar el despliegue: que version de Tomcat responde,
 * con que Java, desde que contexto y si la base de datos esta accesible.
 */
@WebServlet("/api/estado")
public class EstadoServlet extends HttpServlet {

    private static final long serialVersionUID = 1L;

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        Map<String, Object> estado = new LinkedHashMap<>();

        Map<String, Object> app = new LinkedHashMap<>();
        app.put("servidor", getServletContext().getServerInfo());
        app.put("java", System.getProperty("java.version"));
        app.put("contexto", req.getContextPath());
        app.put("host", InetAddress.getLocalHost().getHostName());
        app.put("puerto", req.getLocalPort());
        app.put("hora", new SimpleDateFormat("dd/MM/yyyy HH:mm:ss").format(new Date()));
        estado.put("aplicacion", app);

        Map<String, Object> bd = new LinkedHashMap<>();
        long inicio = System.currentTimeMillis();
        try {
            bd.put("conectada", true);
            bd.put("version", new LibroDAO(getServletContext()).versionServidor());
        } catch (Exception e) {
            bd.put("conectada", false);
            bd.put("error", e.getMessage());
        }
        bd.put("url", getServletContext().getInitParameter("db.url"));
        bd.put("tiempoMs", System.currentTimeMillis() - inicio);
        estado.put("baseDatos", bd);

        // Cabecera que pone Apache cuando hace de proxy: demuestra que la peticion paso por el
        String viaApache = req.getHeader("X-Forwarded-Host");
        estado.put("pasaPorProxy", viaApache != null);
        estado.put("proxyHost", viaApache);

        Json.enviar(resp, HttpServletResponse.SC_OK, estado);
    }
}
