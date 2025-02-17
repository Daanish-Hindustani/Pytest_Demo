import pytest
from src import equation
class TestSmoke:
    
    def test_root_endpoint(self, client):
        response = client.get("/")
        assert response.status_code == 200
        assert "message" in response.json()
        assert response.json()["message"] == "Welcome to the Equation API!"
    def test_equation_two_values(self, client):
        response = client.get("/equation/add/1/2")
        assert response.status_code == 200
        assert "result" in response.json()
        assert response.json()["result"] == 3
    
