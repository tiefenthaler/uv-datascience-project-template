from fastapi.testclient import TestClient

from dev_container_uv_datascience.app_fastapi_autoencoder import app

client = TestClient(app)


def test_main() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to the LitAutoEncoder API!" in response.text
