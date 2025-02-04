import pytest
import torch
from torch import nn

from dev_container_uv_datascience.lit_auto_encoder import LitAutoEncoder


@pytest.fixture
def autoencoder() -> LitAutoEncoder:
    encoder = nn.Sequential(nn.Linear(28 * 28, 64), nn.ReLU(), nn.Linear(64, 3))
    decoder = nn.Sequential(nn.Linear(3, 64), nn.ReLU(), nn.Linear(64, 28 * 28))
    return LitAutoEncoder(encoder, decoder)


def test_training_step(autoencoder) -> None:
    batch = (torch.rand(32, 1, 28, 28), torch.rand(32, 1, 28, 28))
    batch_idx = 0
    loss = autoencoder.training_step(batch, batch_idx)
    assert loss is not None
    assert isinstance(loss, torch.Tensor)


def test_configure_optimizers(autoencoder) -> None:
    optimizer = autoencoder.configure_optimizers()
    assert optimizer is not None
    assert isinstance(optimizer, torch.optim.Adam)
