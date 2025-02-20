def test_smoke_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_smoke_calc(client):
    response = client.get("/calc/10/5/add")
    assert response.status_code == 200
    assert "result" in response.json()

def test_smoke_algebra(client):
    response = client.get("/algebra/5/x/5/x/multiply/25")
    assert response.status_code == 200
    assert "result" in response.json()