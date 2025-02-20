import pytest
from fastapi.testclient import TestClient

class TestRegression:

    @pytest.mark.parametrize("num1, num2, operation, expected_key", [
        (10, 5, "add", "result"),
        (10, 5, "subtract", "result"),
        (10, 5, "multiply", "result"),
        (10, 5, "divide", "result")
    ])
    def test_calc(self, client, num1, num2, operation, expected_key):
        """Test the /calc/{num1}/{num2}/{operation} endpoint for all operators"""
        response = client.get(f"/calc/{num1}/{num2}/{operation}")
        assert response.status_code == 200
        response_json = response.json()
        assert expected_key in response_json  # Ensure 'result' is in the response

    @pytest.mark.parametrize("val1, var1, val2, var2, operation, result, expected_key", [
        (5, "x", 5, "x", "multiply", 25, "result"),
        (2, "x", 3, "x", "add", 5, "result")
    ])
    def test_algebra(self, client, val1, var1, val2, var2, operation, result, expected_key):
        """Test the /algebra/{val1}/{var1}/{val2}/{var2}/{operation}/{result} endpoint for all operations"""
        response = client.get(f"/algebra/{val1}/{var1}/{val2}/{var2}/{operation}/{result}")
        assert response.status_code == 200
        response_json = response.json()
        assert expected_key in response_json  # Check if the response contains 'result'

    def test_root(self, client):
        """Test the root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}
