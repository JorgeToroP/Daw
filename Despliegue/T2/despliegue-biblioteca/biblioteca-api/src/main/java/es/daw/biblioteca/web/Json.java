package es.daw.biblioteca.web;

import java.io.IOException;
import java.util.LinkedHashMap;
import java.util.Map;

import javax.servlet.http.HttpServletResponse;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

/** Utilidad para responder siempre en JSON con UTF-8. */
public final class Json {

    private static final Gson GSON = new GsonBuilder()
        .setPrettyPrinting()
        .disableHtmlEscaping()   // muestra comillas y simbolos tal cual (el frontend ya escapa al pintar)
        .create();

    private Json() {
    }

    public static void enviar(HttpServletResponse resp, int estado, Object datos) throws IOException {
        resp.setStatus(estado);
        resp.setContentType("application/json");
        resp.setCharacterEncoding("UTF-8");
        resp.getWriter().write(GSON.toJson(datos));
    }

    public static void error(HttpServletResponse resp, int estado, String mensaje) throws IOException {
        Map<String, Object> cuerpo = new LinkedHashMap<>();
        cuerpo.put("error", true);
        cuerpo.put("mensaje", mensaje);
        enviar(resp, estado, cuerpo);
    }
}
