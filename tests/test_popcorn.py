import sys
import os

# Agregar la ruta del proyecto a sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.popcorn import app  # Importa la aplicación FastAPI

# Crear un cliente de pruebas
client = TestClient(app)

# Test para la ruta principal "/"
def test_hola():
    response = client.get("/")
    print("Respuesta recibida:", response.json())  # Para depuración
    assert response.status_code == 200
    assert response.json() == ["Bienvenido a PopcornIA"]

# Test para la ruta de recomendación con películas
def test_recomendacion_peliculas():
    payload = {"peliculas": ["Interstellar", "Inception"]}
    response = client.post("/recomendacion", json=payload)
    assert response.status_code == 200
    assert "respuesta" in response.json()

# Test para la ruta de recomendación con contexto
def test_recomendacion_contexto():
    payload = {"contexto": "una película para ver en pareja"}
    response = client.post("/recomendacion", json=payload)
    assert response.status_code == 200
    assert "respuesta" in response.json()

# Test para la ruta de recomendación con películas y contexto
def test_recomendacion_mixta():
    payload = {"peliculas": ["Gladiator"], "contexto": "una película motivadora"}
    response = client.post("/recomendacion", json=payload)
    assert response.status_code == 200
    assert "respuesta" in response.json()

def test_recomendacion_vacio():
    """Prueba el endpoint de recomendación sin datos"""
    payload = {"peliculas": None, "contexto": None}
    response = client.post("/recomendacion", json=payload)
    assert response.status_code == 200
    assert "respuesta" in response.json() or "error" in response.json()
