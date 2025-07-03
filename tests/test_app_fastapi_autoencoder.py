from fastapi.testclient import TestClient

from uv_datascience_project_template.app_fastapi_autoencoder import app
from uv_datascience_project_template.config import get_settings
from uv_datascience_project_template.train_autoencoder import train_litautoencoder

client = TestClient(app)

settings = get_settings()


def test_root_endpoint() -> None:
    """Test the root endpoint returns welcome message and status 200."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to the LitAutoEncoder API!" in response.text


def test_train_endpoint() -> None:
    """Test the /train endpoint returns a success message and status 200."""
    response = client.post("/train")
    assert response.status_code == 200
    assert any(
        phrase in response.json()["message"]
        for phrase in ["training completed", "is already trained"]
    )


def test_train_endpoint_idempotent() -> None:
    """Test that repeated calls to /train endpoint do not fail and return valid messages."""
    for _ in range(2):
        response = client.post("/train")
        assert response.status_code == 200
        assert any(
            phrase in response.json()["message"]
            for phrase in ["training completed", "is already trained"]
        )


def test_embed_endpoint() -> None:
    """Test the /embed endpoint for valid and invalid input cases."""
    # First, ensure the model is trained
    train_litautoencoder(settings)

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

    # Test with missing field
    response = client.post("/embed", json={})
    assert response.status_code == 422

    # Test with negative value
    response = client.post("/embed", json={"n_fake_images": -3})
    assert response.status_code == 422
