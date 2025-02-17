import pytest

class TestIntegration:
    
    @pytest.mark.parametrize("operation, val1, val2, expected", [
        ("add", 5, 3, 8),
        ("subtract", 10, 4, 6),
        ("multiply", 6, 7, 42),
        ("divide", 20, 5, 4),
        ("power", 2, 3, 8),
        ("modulus", 10, 3, 1),
        ("floor_divide", 10, 3, 3),
    ])
    def test_equation_operations(self, operation, val1, val2, expected, client):
        """Test basic math operations."""
        response = client.get(f"/equation/{operation}/{val1}/{val2}")
        assert response.status_code == 200
        assert response.json()["result"] == expected

    def test_square_root(self, client):
        """Test square root operation (single parameter)."""
        response = client.get("/equation/square_root/16")
        assert response.status_code == 200
        assert response.json()["result"] == 4.0