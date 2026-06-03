from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_kmp_endpoint():
    response = client.post(
        "/kmp",
        json={
            "text": "ABABDABACDABABCABAB",
            "pattern": "ABABCABAB"
        }
    )

    assert response.status_code == 200
    assert "steps" in response.json()