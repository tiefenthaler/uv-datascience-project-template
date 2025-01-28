from fastapi.testclient import TestClient

from dev_container_uv_datascience.app_fastapi_autoencoder import app, train_litautoencoder

client = TestClient(app)


def test_read_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to the LitAutoEncoder API!" in response.text


def test_train_model() -> None:
    response = client.post("/train")
    assert response.status_code == 200
    assert response.json() == {"message": "Model training completed successfully."}


def test_embed() -> None:
    train_litautoencoder()  # Ensure the model is trained before embedding
    response = client.post("/embed", json={"n_fake_images": 1})
    assert response.status_code == 200
    assert "embeddings" in response.json()
