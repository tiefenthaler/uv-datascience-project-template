from fastapi.testclient import TestClient

from dev_container_uv_datascience.app_fastapi_autoencoder import app

client = TestClient(app)


def test_main() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to the LitAutoEncoder API!" in response.text


def test_train_endpoint() -> None:
    response = client.post("/train")
    assert response.status_code == 200
    assert any(
        phrase in response.json()["message"]
        for phrase in ["training completed", "is already trained"]
    )


def test_embed_endpoint() -> None:
    # First, ensure the model is trained
    client.post("/train")

    # Test with valid input
    response = client.post("/embed", json={"n_fake_images": 5})
    assert response.status_code == 200
    assert "embeddings" in response.json()
    assert len(response.json()["embeddings"]) == 5
    assert all(isinstance(embedding, list) for embedding in response.json()["embeddings"])

    # Test with invalid input (too many images)
    response = client.post("/embed", json={"n_fake_images": 11})
    assert response.status_code == 422

    # Test with invalid input (too few images)
    response = client.post("/embed", json={"n_fake_images": 0})
    assert response.status_code == 422

    # Test with invalid input type
    response = client.post("/embed", json={"n_fake_images": "not a number"})
    assert response.status_code == 422
