# Pull Request — Billboard Uniagustiniana v1.1.0
**Rama:** `feature/evaluacion_mss_LG` → `develop`  
**Autor:** Luis Gutiérrez  
**Fecha:** 15 de abril de 2026  

---

## Descripción del Cambio

Evolución del sistema Billboard Uniagustiniana de la **v1.0.0** a la **v1.1.0**.  
Se aplicó un flujo de trabajo Git-Flow profesional con ramas `feature`, `develop` y `main`, finalizando con el Tag `v1.1.0`.

---

## Archivos Modificados

| Archivo | Tipo de cambio | Descripción |
|---|---|---|
| `api/main.py` | ✏️ Perfectivo | Versión de FastAPI actualizada a `1.1.0` con título y descripción |
| `docker-compose.yml` | ✏️ Perfectivo | Imagen del API actualizada de `1.0.0` a `1.1.0` |
| `README.md` | ✏️ Preventivo | Changelog SemVer 2.0.0 agregado + documentación Docker |

> **Nota:** `db/init.sql`, `api/templates/index.html` ya contenían la columna `genero` desde la v1.0.0.

---

## Descripción Técnica

En `api/main.py` se actualizó la instancia de `FastAPI()` para incluir los parámetros `version="1.1.0"`, `title` y `description`, reflejando el nuevo estado de la aplicación.  
En `docker-compose.yml` se actualizó el tag de la imagen `uniagustiniana/billboard-api` de `1.0.0` a `1.1.0` para mantener coherencia con el versionamiento SemVer.  
En `README.md` se eliminaron todas las referencias a Podman/podman-compose y se reemplazaron por los comandos equivalentes de Docker/Docker Compose, además de agregar el Changelog formal siguiendo el estándar SemVer 2.0.0.  
El motor de contenedores migró de **Podman** a **Docker Desktop v28.0.4** con **Docker Compose v2.34.0**, manteniendo el mismo `docker-compose.yml` sin modificaciones estructurales.

---

## Evidencias

### Captura 1 — Despliegue Exitoso (http://localhost:8080)
> Tabla de artistas con columna "Género" visible en el navegador.

<!-- INSERTAR CAPTURA DE PANTALLA 1 AQUÍ -->
![Despliegue exitoso - Billboard v1.1.0](./evidencias/captura1_despliegue.png)

---

### Captura 2 — Logs del API (docker compose logs)
> Terminal mostrando `docker compose logs controlador_api` sin errores.

<!-- INSERTAR CAPTURA DE PANTALLA 2 AQUÍ -->
![Logs del API corriendo sin errores](./evidencias/captura2_logs_api.png)

---

### Captura 3 — Flujo de Ramas Git-Flow (Network Graph)
> Gráfico de red de GitHub mostrando el flujo: `feature/evaluacion_mss_LG` → `develop` → `main` → Tag `v1.1.0`.

<!-- INSERTAR CAPTURA DE PANTALLA 3 AQUÍ -->
![Git Network Graph - Flujo Git-Flow](./evidencias/captura3_git_network.png)

---

## Conclusiones

1. **Git-Flow** como metodología de ramificación permite un control ordenado del ciclo de vida del software, separando claramente el trabajo en progreso (`feature`), la integración continua (`develop`) y el código productivo (`main`), lo que reduce el riesgo de introducir errores en producción.

2. **Docker Compose** demostró ser una herramienta robusta y portable para orquestar arquitecturas multi-contenedor. La migración desde Podman fue transparente ya que el `docker-compose.yml` es compatible con ambos motores sin cambios estructurales.

3. El patrón **MVC con contenedores** (MariaDB + FastAPI + Nginx) permite escalar cada capa de forma independiente y facilita el mantenimiento preventivo y perfectivo, como se evidenció al actualizar únicamente el componente Controlador (API) sin afectar el Modelo ni la Vista.

4. El **versionamiento SemVer 2.0.0** con Changelog estructurado es una práctica esencial en mantenimiento de software, ya que proporciona trazabilidad clara de qué cambió, cuándo y por qué, facilitando auditorías y rollbacks en caso de fallas.

5. La ejecución de este flujo completo (clone → branch → develop → test → merge → tag) en un entorno real demuestra la importancia de los procesos de **integración continua** y la documentación técnica como pilares del mantenimiento profesional de sistemas de software.

---

## Comandos de Verificación

```bash
# Ver todos los contenedores corriendo
docker compose ps

# Ver logs del API en tiempo real
docker compose logs controlador_api

# Verificar el flujo de ramas localmente
git log --oneline --graph --all
```

**Salida esperada del graph:**
```
*   360ce5c (HEAD -> main, tag: v1.1.0) merge: develop hacia main - release v1.1.0
|\  
| * ce2301a (develop) merge: feature/evaluacion_mss_LG hacia develop - v1.1.0
|/| 
| * c8cc901 (feature/evaluacion_mss_LG) feat: actualizar sistema a v1.1.0
|/  
* 8364a33 feat: configuracion mvc, podman y semver v1.0.0
```
