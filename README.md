# Evaluación final unidad 3 - v1.1.0
## Uniagustiniana 2026
**Estado:** Stable
**Versionamiento:** SemVer 2.0.0

---

# Changelog

## [1.1.0] - 2026-04-15
### Added
- Nueva columna `genero` en la tabla `artistas` de la base de datos MariaDB.
- Visualización del Género Musical en la tabla de la interfaz web.
- Modelo de datos actualizado en FastAPI para soportar el nuevo campo.

### Changed
- Actualizada la versión de la aplicación a `1.1.0` en el objeto `FastAPI`.
- Reemplazado Podman/podman-compose por Docker/Docker Compose como motor de contenedores.
- Actualizada la documentación de ejecución para usar comandos `docker compose`.

## [1.0.0] - 2026-04-13
### Added
- Despliegue inicial del sistema Billboard Uniagustiniana.
- Arquitectura MVC con MariaDB, FastAPI y Nginx.
- Top 10 de artistas con ranking de popularidad.

---

Este repositorio contiene un laboratorio práctico para el despliegue de una infraestructura distribuida utilizando contenedores. Se implementa un patrón Modelo-Vista-Controlador (MVC) para gestionar un ranking de artistas musicales.

# 🏗️ Componentes del Sistema
Modelo (DB): MariaDB con carga de datos inicial via init.sql.

Controlador (API): FastAPI (Python) que gestiona la lógica y conexión a datos.

Vista (Gateway/UI): Nginx como Proxy Inverso y plantillas Jinja2 con Tailwind CSS.

# 🚀 Guía de Preparación y Ejecución
## 1. Prerequisitos
Asegúrate de tener instalado y corriendo:
- **Docker Desktop** (versión 20.x o superior)
- **Docker Compose** v2 (incluido en Docker Desktop)

```bash
# Verificar entorno
docker --version
docker compose version
```

## 2. Despliegue de la Infraestructura
Ubícate en la raíz del proyecto y ejecuta:

```bash
# Construir imágenes y levantar servicios en segundo plano
docker compose up -d --build
```

## 3. Acceso al Sistema

👉 **[http://localhost:8080](http://localhost:8080)**

```bash
# Ver estado de los servicios
docker compose ps

# Ver logs del API
docker compose logs controlador_api
```

## 🛠️ Comandos de Mantenimiento

Si realizas cambios en el código o en la base de datos, sigue este flujo para un despliegue limpio:

```bash
# 1. Detener y borrar contenedores + volúmenes
docker compose down -v

# 2. Reconstruir y levantar
docker compose up -d --build
```