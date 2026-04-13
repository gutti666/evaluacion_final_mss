import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
import sys
import os

# Esto permite que el test encuentre la carpeta 'api' que está un nivel arriba
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api.main import app

client = TestClient(app)


@patch("api.main.conectar_modelo")
def test_vista_uniagustiniana(mock_conectar):
    """Verifica el renderizado de la UI institucional"""
    mock_conexion = MagicMock()
    mock_cursor = MagicMock()

    mock_conectar.return_value = mock_conexion
    mock_conexion.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [
        {"nombre": "Artista Test", "popularidad": 80, "ultimo_exito": "Prueba", "genero": "Urbano"}
    ]

    response = client.get("/")
    assert response.status_code == 200
    assert "UNIAGUSTINIANA" in response.text.upper()


@patch("api.main.conectar_modelo")
def test_fallo_db(mock_conectar):
    """Verifica la respuesta cuando no hay base de datos"""
    mock_conectar.return_value = None
    response = client.get("/")
    assert response.status_code == 500