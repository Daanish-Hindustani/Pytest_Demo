import pytest
from fastapi.testclient import TestClient

class TestUnit:

    @pytest.mark.parametrize("num1, num2, operation, expected_result", [
        (10, 5, "add", 15),
        (10, 5, "subtract", 5),
        (10, 5, "multiply", 50),
        (10, 5, "divide", 2)
    ])
    def test_calc(self, client, num1, num2, operation, expected_result):
        """Test the /calc/{num1}/{num2}/{operation} endpoint for all operators"""
        response = client.get(f"/calc/{num1}/{num2}/{operation}")
        assert response.status_code == 200
        response_json = response.json()
        print(response_json)
        assert expected_result == response_json['result']  # Ensure 'result' is correct value

    @pytest.mark.parametrize("val1, var1, val2, var2, operation, result, expected_result", [
        (5, "x", 5, "x", "add", 25, "5/2"),
        (4, "x", 3, "x", "subtract", 2, "2"),
        (1, "x", 3, "x", "divide", 6, "-3*sqrt(2)"),
        (12, "x", 2, "x", "multiply", 60, "-sqrt(10)/2"),
        (2, "x", 2, "y", "add", 2, "1 - y"),
        (2, "y", 2, "x", "add", 2, "1 - x"),
        (6, "x", 2, "y", "subtract", 3, "y/3 + 1/2"),
        (2, "x", 3, "y", "multiply", 7, "7/(6*y)"),
        (4, "x", 2, "y", "divide", 1, "1/(2*y)")
    ])
    def test_algebra(self, client, val1, var1, val2, var2, operation, result, expected_result):
        """Test the /algebra/{val1}/{var1}/{val2}/{var2}/{operation}/{result} endpoint for all operations"""
        response = client.get(f"/algebra/{val1}/{var1}/{val2}/{var2}/{operation}/{result}")
        assert response.status_code == 200
        response_json = response.json()
        assert expected_result == response_json['result']  # Ensure 'result' is correct value

    def test_root(self, client):
        """Test the root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}