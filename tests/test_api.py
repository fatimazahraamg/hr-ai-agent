from fastapi.testclient import TestClient
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app

client = TestClient(app)

def test_api_repond():
    """Vérifie que l'API démarre et répond"""
    response = client.get("/docs")
    assert response.status_code == 200