from app.main import app
from starlette.testclient import TestClient

client = TestClient(app)


def test_greeting():
    response = client.get("/v1/greeting/user")
    assert response.status_code == 200
    assert response.json() == {"username": "user"}
