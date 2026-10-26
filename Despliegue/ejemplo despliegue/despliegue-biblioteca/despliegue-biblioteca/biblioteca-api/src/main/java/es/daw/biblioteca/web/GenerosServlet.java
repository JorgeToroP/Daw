package es.daw.biblioteca.web;

import java.io.IOException;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import es.daw.biblioteca.datos.LibroDAO;

/** GET /api/generos -> lista de generos (para los filtros del frontend). */
@WebServlet("/api/generos")
public class GenerosServlet extends HttpServlet {

    private static final long serialVersionUID = 1L;

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        try {
            Json.enviar(resp, HttpServletResponse.SC_OK, new LibroDAO(getServletContext()).generos());
        } catch (SQLException e) {
            log("Error consultando generos", e);
            Json.error(resp, HttpServletResponse.SC_SERVICE_UNAVAILABLE,
                       "Error de base de datos: " + e.getMessage());
        }
    }
}
