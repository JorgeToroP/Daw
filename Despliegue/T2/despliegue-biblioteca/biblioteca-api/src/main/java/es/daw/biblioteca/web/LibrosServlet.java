package es.daw.biblioteca.web;

import java.io.IOException;
import java.sql.SQLException;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import es.daw.biblioteca.datos.LibroDAO;
import es.daw.biblioteca.modelo.Libro;

/**
 * GET  /api/libros?q=texto&genero=Nombre  -> lista de libros filtrada
 * POST /api/libros (formulario)           -> da de alta un libro
 */
@WebServlet("/api/libros")
public class LibrosServlet extends HttpServlet {

    private static final long serialVersionUID = 1L;

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        long inicio = System.currentTimeMillis();
        try {
            LibroDAO dao = new LibroDAO(getServletContext());
            List<Libro> libros = dao.buscar(req.getParameter("q"), req.getParameter("genero"));

            Map<String, Object> respuesta = new LinkedHashMap<>();
            respuesta.put("total", libros.size());
            respuesta.put("tiempoMs", System.currentTimeMillis() - inicio);
            respuesta.put("libros", libros);
            Json.enviar(resp, HttpServletResponse.SC_OK, respuesta);
        } catch (SQLException e) {
            log("Error consultando libros", e);
            Json.error(resp, HttpServletResponse.SC_SERVICE_UNAVAILABLE,
                       "Error de base de datos: " + e.getMessage());
        }
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        req.setCharacterEncoding("UTF-8");

        String titulo = req.getParameter("titulo");
        String autor = req.getParameter("autor");
        String genero = req.getParameter("genero");

        if (vacio(titulo) || vacio(autor) || vacio(genero)) {
            Json.error(resp, HttpServletResponse.SC_BAD_REQUEST, "Titulo, autor y genero son obligatorios");
            return;
        }

        int anio;
        int paginas;
        double valoracion;
        try {
            anio = Integer.parseInt(req.getParameter("anio"));
            paginas = Integer.parseInt(req.getParameter("paginas"));
            valoracion = Double.parseDouble(req.getParameter("valoracion"));
        } catch (NumberFormatException | NullPointerException e) {
            Json.error(resp, HttpServletResponse.SC_BAD_REQUEST, "Anio, paginas y valoracion deben ser numericos");
            return;
        }
        if (valoracion < 0 || valoracion > 5) {
            Json.error(resp, HttpServletResponse.SC_BAD_REQUEST, "La valoracion va de 0 a 5");
            return;
        }

        try {
            int id = new LibroDAO(getServletContext())
                .insertar(titulo.trim(), autor.trim(), anio, paginas, valoracion, genero.trim());
            Map<String, Object> respuesta = new LinkedHashMap<>();
            respuesta.put("ok", true);
            respuesta.put("id", id);
            Json.enviar(resp, HttpServletResponse.SC_CREATED, respuesta);
        } catch (SQLException e) {
            log("Error insertando libro", e);
            Json.error(resp, HttpServletResponse.SC_BAD_REQUEST, e.getMessage());
        }
    }

    private static boolean vacio(String s) {
        return s == null || s.trim().isEmpty();
    }
}
