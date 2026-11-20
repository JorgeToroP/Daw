/* =========================================================
   Logica del cliente (se ejecuta en el navegador).
   Apache solo entrega este fichero; las consultas se hacen
   con fetch() contra la API que vive en Tomcat.
   ========================================================= */

// Dos rutas posibles hacia el servidor de aplicaciones
const RUTAS = {
  // Recomendada: misma maquina y mismo puerto que la web. Apache reenvia a Tomcat (proxy inverso)
  proxy: "/biblioteca-api",
  // Directa: el navegador habla con Tomcat en otro puerto (necesita CORS, ver CorsFilter.java)
  directo: "http://" + (location.hostname || "localhost") + ":8080/biblioteca/api"
};

let modo = "proxy";
let generoActivo = "";
let temporizador = null;

const $ = (sel) => document.querySelector(sel);

/* ---------- Animacion del diagrama ---------- */

function animarPeticion(ok, llegoABD) {
  const nodos = modo === "proxy"
    ? ["nodo-navegador", "nodo-apache", "nodo-tomcat", "nodo-bd"]
    : ["nodo-navegador", "nodo-tomcat", "nodo-bd"];
  const enlaces = modo === "proxy" ? ["enlace-1", "enlace-2", "enlace-3"] : ["enlace-2", "enlace-3"];

  nodos.forEach((id, i) => {
    if (id === "nodo-bd" && !llegoABD) return;
    setTimeout(() => {
      const n = document.getElementById(id);
      n.classList.add("activo");
      setTimeout(() => n.classList.remove("activo"), 500);
    }, i * 180);
  });
  enlaces.forEach((id, i) => {
    if (id === "enlace-3" && !llegoABD) return;
    setTimeout(() => {
      const e = document.getElementById(id);
      e.classList.remove("viaja");
      void e.offsetWidth;          // reinicia la animacion CSS
      e.classList.add("viaja");
    }, i * 180);
  });
  document.getElementById("nodo-tomcat").classList.toggle("caido", !ok);
}

function pintarModo() {
  document.querySelectorAll(".modo-btn").forEach((b) => b.classList.toggle("activo", b.dataset.modo === modo));
  const sinApache = modo === "directo";
  $("#nodo-apache").classList.toggle("saltado", sinApache);
  $("#enlace-1").classList.toggle("saltado", sinApache);
}

/* ---------- Cliente HTTP con registro ---------- */

async function api(ruta, opciones = {}) {
  const url = RUTAS[modo] + ruta;
  const inicio = performance.now();
  let estado = 0;
  let resp;
  try {
    resp = await fetch(url, opciones);
  } catch (e) {
    // Error de red: el servidor no responde o CORS bloquea la respuesta
    registrar(opciones.method || "GET", url, "ERR", performance.now() - inicio);
    animarPeticion(false, false);
    throw new Error("No se pudo contactar con " + url + ". ¿Está arrancado el servidor?");
  }
  estado = resp.status;
  registrar(opciones.method || "GET", url, estado, performance.now() - inicio);

  // Si Tomcat esta parado, Apache devuelve una pagina HTML de error (502/503), no JSON
  const texto = await resp.text();
  let datos = null;
  try { datos = JSON.parse(texto); } catch (e) { /* no era JSON */ }

  if (datos === null) {
    animarPeticion(false, false);
    throw new Error(`HTTP ${estado}: la respuesta no viene de Tomcat. ¿Está arrancado y desplegado biblioteca.war?`);
  }
  animarPeticion(true, estado !== 503);
  if (!resp.ok) throw new Error(datos.mensaje || "HTTP " + estado);
  return datos;
}

function registrar(metodo, url, estado, ms) {
  const li = document.createElement("li");
  const ok = typeof estado === "number" && estado < 400;
  li.innerHTML =
    `<span class="metodo">${metodo}</span>` +
    `<span class="url">${escapar(url)}</span>` +
    `<span class="${ok ? "cod-ok" : "cod-err"}">${estado}</span>` +
    `<span class="ms">${Math.round(ms)} ms</span>`;
  $("#registro").prepend(li);
}

/* ---------- Carga de datos ---------- */

async function cargarGeneros() {
  const generos = await api("/generos");
  const filtros = $("#filtros");
  const select = $("#select-genero");
  filtros.innerHTML = "";
  select.innerHTML = "";

  filtros.appendChild(crearChip("Todos", "", "var(--acento)"));
  generos.forEach((g) => {
    filtros.appendChild(crearChip(g.nombre, g.nombre, g.color));
    select.add(new Option(g.nombre, g.nombre));
  });
}

function crearChip(texto, valor, color) {
  const b = document.createElement("button");
  b.className = "chip" + (valor === generoActivo ? " activo" : "");
  b.textContent = texto;
  b.style.setProperty("--color", color);
  b.addEventListener("click", () => {
    generoActivo = valor;
    document.querySelectorAll(".chip").forEach((c) => c.classList.toggle("activo", c === b));
    cargarLibros();
  });
  return b;
}

async function cargarLibros() {
  const params = new URLSearchParams();
  const texto = $("#buscar").value.trim();
  if (texto) params.set("q", texto);
  if (generoActivo) params.set("genero", generoActivo);
  const qs = params.toString() ? "?" + params : "";

  const contenedor = $("#libros");
  try {
    const datos = await api("/libros" + qs);
    $("#resumen").textContent =
      `${datos.total} libro(s) encontrados · consulta SQL resuelta en ${datos.tiempoMs} ms dentro de Tomcat`;

    if (datos.libros.length === 0) {
      contenedor.innerHTML = `<div class="vacio">Ningún libro coincide con la búsqueda</div>`;
      return;
    }
    contenedor.innerHTML = datos.libros.map((l, i) => `
      <article class="libro" style="--color:${l.color}; animation-delay:${i * 30}ms">
        <div class="genero">${escapar(l.genero)}</div>
        <h3>${escapar(l.titulo)}</h3>
        <div class="autor">${escapar(l.autor)}</div>
        <div class="meta">
          <span>${l.anio} · ${l.paginas} págs.</span>
          <span class="estrellas" title="${l.valoracion}">${estrellas(l.valoracion)}</span>
        </div>
      </article>`).join("");
  } catch (e) {
    $("#resumen").textContent = "";
    contenedor.innerHTML = `<div class="aviso">${escapar(e.message)}</div>`;
  }
}

async function cargarEstadisticas() {
  try {
    const filas = await api("/estadisticas");
    const max = Math.max(1, ...filas.map((f) => f.total));
    $("#estadisticas").innerHTML = filas.map((f) => `
      <div class="barra">
        <div class="barra-cab">
          <span>${escapar(f.genero)}</span>
          <span>${f.total} libros · ★ ${f.media.toFixed(2)}</span>
        </div>
        <div class="barra-fondo">
          <div class="barra-relleno" style="--color:${f.color}; width:${(f.total / max) * 100}%"></div>
        </div>
      </div>`).join("");
  } catch (e) {
    $("#estadisticas").innerHTML = `<div class="aviso">${escapar(e.message)}</div>`;
  }
}

async function comprobarEstado() {
  try {
    const e = await api("/estado");
    $("#info-tomcat").textContent = `${e.aplicacion.servidor} · Java ${e.aplicacion.java}`;
    $("#info-bd").textContent = e.baseDatos.conectada
      ? `MariaDB ${e.baseDatos.version}`
      : "Sin conexión";
    $("#nodo-bd").classList.toggle("caido", !e.baseDatos.conectada);

    aviso(
      e.baseDatos.conectada ? "Despliegue correcto" : "Tomcat responde, pero MariaDB no",
      `Servidor: ${e.aplicacion.servidor}\n` +
      `Contexto: ${e.aplicacion.contexto}  (puerto ${e.aplicacion.puerto})\n` +
      `Pasa por Apache: ${e.pasaPorProxy ? "sí (" + e.proxyHost + ")" : "no"}\n` +
      `BD: ${e.baseDatos.conectada ? e.baseDatos.version : e.baseDatos.error}`,
      !e.baseDatos.conectada
    );
  } catch (err) {
    $("#info-tomcat").textContent = "No responde";
    aviso("Error de despliegue", err.message, true);
  }
}

/* ---------- Alta de libros ---------- */

$("#form-alta").addEventListener("submit", async (ev) => {
  ev.preventDefault();
  const form = ev.target;
  // URLSearchParams envia el formulario como application/x-www-form-urlencoded,
  // el formato que entiende request.getParameter() en el servlet
  const cuerpo = new URLSearchParams(new FormData(form));
  try {
    const r = await api("/libros", { method: "POST", body: cuerpo });
    aviso("Libro guardado", `INSERT correcto, id = ${r.id}`);
    form.reset();
    cargarLibros();
    cargarEstadisticas();
  } catch (e) {
    aviso("No se pudo guardar", e.message, true);
  }
});

/* ---------- Utilidades ---------- */

function estrellas(v) {
  const llenas = Math.round(v);
  return "★".repeat(llenas) + "☆".repeat(5 - llenas);
}

function escapar(txt) {
  return String(txt ?? "").replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

function aviso(titulo, detalle, esError = false) {
  document.querySelectorAll(".toast").forEach((t) => t.remove());
  const div = document.createElement("div");
  div.className = "toast" + (esError ? " error" : "");
  div.innerHTML = `<strong>${escapar(titulo)}</strong>${detalle ? `<pre>${escapar(detalle)}</pre>` : ""}`;
  document.body.appendChild(div);
  setTimeout(() => div.remove(), 6000);
}

/* ---------- Eventos e inicio ---------- */

$("#buscar").addEventListener("input", () => {
  clearTimeout(temporizador);
  temporizador = setTimeout(cargarLibros, 300);   // espera a que el usuario deje de escribir
});

$("#btn-estado").addEventListener("click", comprobarEstado);

document.querySelectorAll(".modo-btn").forEach((b) =>
  b.addEventListener("click", () => {
    modo = b.dataset.modo;
    pintarModo();
    iniciar();
  }));

async function iniciar() {
  try {
    await cargarGeneros();
  } catch (e) {
    $("#libros").innerHTML = `<div class="aviso">${escapar(e.message)}</div>`;
    $("#resumen").textContent = "";
    return;
  }
  cargarLibros();
  cargarEstadisticas();
  comprobarEstado();
}

pintarModo();
iniciar();
