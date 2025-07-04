import pytest
from fastapi.testclient import TestClient

from uv_datascience_project_template.app_fastapi_autoencoder import app
from uv_datascience_project_template.config import get_settings
from uv_datascience_project_template.train_autoencoder import train_litautoencoder

settings = get_settings()


@pytest.fixture(name="client")
def client_fixture(tmp_path):
    # Create a temporary directory for MNIST data
    temp_mnist_data_path = tmp_path / "MNIST"
    temp_mnist_data_path.mkdir()

    # Override the settings for the test
    original_mnist_data_path = settings.data.mnist_data_path
    settings.data.mnist_data_path = temp_mnist_data_path

    with TestClient(app) as client:
        app.dependency_overrides = {}
        app.state.encoder = None
        app.state.decoder = None
        app.state.is_model_trained = False
        app.state.checkpoint_path = None
        yield client

    # Restore original settings after the test
    settings.data.mnist_data_path = original_mnist_data_path


def test_root_endpoint(client: TestClient) -> None:
    """Test the root endpoint returns welcome message and status 200."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to the LitAutoEncoder API!" in response.text


def test_train_endpoint(client: TestClient) -> None:
    """Test the /train endpoint returns a success message and status 200."""
    response = client.post("/train")
    assert response.status_code == 200
    assert any(
        phrase in response.json()["message"]
        for phrase in ["training completed", "is already trained"]
    )


def test_train_endpoint_idempotent(client: TestClient) -> None:
    """Test that repeated calls to /train endpoint do not fail and return valid messages."""
    for _ in range(2):
        response = client.post("/train")
        assert response.status_code == 200
        assert any(
            phrase in response.json()["message"]
            for phrase in ["training completed", "is already trained"]
        )


def test_embed_endpoint(client: TestClient) -> None:
    """Test the /embed endpoint for valid and invalid input cases."""
    # First, ensure the model is trained
    app.state.encoder, app.state.decoder, _, app.state.checkpoint_path = train_litautoencoder(
        settings
    )

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
