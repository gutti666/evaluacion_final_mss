from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import mariadb
import os
import time

app = FastAPI()
# Asegúrate de que la ruta coincida con tu estructura de carpetas
templates = Jinja2Templates(directory="templates")

def conectar_modelo():
    """
    Intenta conectar al contenedor de base de datos usando las
    variables de entorno definidas en el docker-compose.
    """
    # Recuperamos las variables con valores por defecto de la Uniagustiniana
    db_host = os.getenv("DB_HOST", "modelo_db")
    db_pass = os.getenv("MYSQL_ROOT_PASSWORD", "uniagustiniana_pass")
    db_name = "academia_agustiniana_db" # <--- Cambiado para coincidir con el YAML

    for i in range(5):
        try:
            return mariadb.connect(
                host=db_host,
                user="root",
                password=db_pass,
                database=db_name
            )
        except mariadb.Error as e:
            print(f"Intento {i+1}: Error conectando a MariaDB: {e}")
            time.sleep(2)
    return None

@app.get("/", response_class=HTMLResponse)
async def leer_vista(request: Request):
    conexion = conectar_modelo()
    if not conexion:
        # Si falla, devolvemos el error 500
        return HTMLResponse(
            content="<h1>Error de Conexión al Modelo - Uniagustiniana</h1>",
            status_code=500
        )

    try:
        cursor = conexion.cursor(dictionary=True)
        # Consulta para el ranking de popularidad
        cursor.execute("SELECT * FROM artistas ORDER BY popularidad DESC LIMIT 10")
        datos = cursor.fetchall()
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={"artistas": datos}
        )
    except mariadb.Error as e:
        return HTMLResponse(content=f"<h1>Error en la consulta: {e}</h1>", status_code=500)
    finally:
        if conexion:
            conexion.close()