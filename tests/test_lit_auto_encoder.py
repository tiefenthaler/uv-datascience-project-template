import pytest
import torch
from torch import nn

from uv_datascience_project_template.lit_auto_encoder import LitAutoEncoder


@pytest.fixture
def autoencoder() -> LitAutoEncoder:
    """Fixture to provide a LitAutoEncoder instance for testing."""
    encoder = nn.Sequential(nn.Linear(28 * 28, 64), nn.ReLU(), nn.Linear(64, 3))
    decoder = nn.Sequential(nn.Linear(3, 64), nn.ReLU(), nn.Linear(64, 28 * 28))
    return LitAutoEncoder(encoder, decoder)


def test_training_step(autoencoder) -> None:
    """Test that training_step returns a valid loss tensor for a normal batch.

    Args:
        autoencoder (LitAutoEncoder): The autoencoder fixture.
    """
    batch = (torch.rand(32, 1, 28, 28), torch.rand(32, 1, 28, 28))
    batch_idx = 0
    loss = autoencoder.training_step(batch, batch_idx)
    assert loss is not None
    assert isinstance(loss, torch.Tensor)


def test_training_step_empty_batch(autoencoder) -> None:
    """Test that training_step raises an error for an empty batch."""
    batch = (torch.empty(0, 1, 28, 28), torch.empty(0, 1, 28, 28))
    batch_idx = 0
    with pytest.raises(RuntimeError):
        autoencoder.training_step(batch, batch_idx)


def test_training_step_invalid_shape(autoencoder) -> None:
    """Test that training_step raises an error for invalid input shape."""
    batch = (torch.rand(32, 10), torch.rand(32, 10))
    batch_idx = 0
    with pytest.raises(RuntimeError):
        autoencoder.training_step(batch, batch_idx)


def test_configure_optimizers(autoencoder) -> None:
    """Test that configure_optimizers returns an Adam optimizer instance.

    Args:
        autoencoder (LitAutoEncoder): The autoencoder fixture.
    """
    optimizer = autoencoder.configure_optimizers()
    assert optimizer is not None
    assert isinstance(optimizer, torch.optim.Adam)
