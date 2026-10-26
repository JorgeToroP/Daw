# Biblioteca distribuida: Apache + Tomcat + MariaDB (XAMPP)

Ejemplo de despliegue en tres capas:

- **Apache (puerto 80)**: sirve la web estática (`web/`) y reenvía `/biblioteca-api/` a Tomcat (proxy inverso).
- **Tomcat (puerto 8080)**: ejecuta `biblioteca.war`, una API JSON hecha con servlets.
- **MariaDB (puerto 3306)**: base de datos `biblioteca`.

Pensado para el Tomcat 8.5.96 que incluye XAMPP para Windows (usa `javax.servlet`, no `jakarta.servlet`).

## Contenido

| Carpeta | Qué es | Dónde va |
|---|---|---|
| `biblioteca-api/` | Proyecto Maven para Eclipse que genera `biblioteca.war` | Workspace de Eclipse |
| `web/` | `index.html`, `css/estilos.css`, `js/app.js` | `C:\xampp\htdocs\biblioteca\` |
| `apache/httpd-biblioteca.conf` | Configuración del proxy | `C:\xampp\apache\conf\extra\` |
| `sql/biblioteca.sql` | BD, usuario `biblio`/`biblio123` y datos | phpMyAdmin |
| `extra/biblioteca.war` | WAR ya compilado, de reserva | Solo si falla Eclipse |

## Pasos

1. **Base de datos**: en XAMPP arrancar Apache y MySQL. En http://localhost/phpmyadmin, pestaña SQL, pegar y ejecutar `sql/biblioteca.sql`.
2. **WAR**: en Eclipse, `File > Import > Maven > Existing Maven Projects` y elegir `biblioteca-api`. Clic derecho en `Generar WAR.launch > Run As > Generar WAR` (o `Run As > Maven build...` con goals `clean package`). El WAR queda en `biblioteca-api/target/biblioteca.war`.
3. **Tomcat**: arrancar Tomcat en XAMPP y copiar `biblioteca.war` a `C:\xampp\tomcat\webapps\`. Probar http://localhost:8080/biblioteca/api/estado
   (o usar `Generar y desplegar WAR.launch`, que lo copia solo).
4. **Apache**: copiar el contenido de `web/` a `C:\xampp\htdocs\biblioteca\`, copiar `httpd-biblioteca.conf` a `C:\xampp\apache\conf\extra\`, añadir al final de `httpd.conf`:

   ```
   Include conf/extra/httpd-biblioteca.conf
   ```

   Reiniciar Apache y abrir http://localhost/biblioteca/

## API

| Petición | Respuesta |
|---|---|
| `GET /api/libros?q=texto&genero=Nombre` | Libros filtrados |
| `POST /api/libros` (titulo, autor, anio, paginas, valoracion, genero) | Alta (INSERT) |
| `GET /api/generos` | Géneros |
| `GET /api/estadisticas` | Total, media y páginas por género |
| `GET /api/estado` | Versión de Tomcat, Java, MariaDB y si pasó por Apache |

## Requisitos

- Eclipse con soporte Maven (m2e), configurado con un JDK 8 o superior.
- Tomcat necesita Java instalado (JAVA_HOME). El código se compila para Java 8.
