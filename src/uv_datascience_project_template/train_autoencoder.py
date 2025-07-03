# import os
from typing import Literal

import lightning as L  # noqa: N812
from lightning.pytorch.loggers import CSVLogger
from torch import nn, utils
from torch.nn import Sequential
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor

from .config import Settings
from .lit_auto_encoder import LitAutoEncoder


def train_litautoencoder(settings: Settings) -> tuple[Sequential, Sequential, Literal[True]]:
    """Trains a LitAutoEncoder model on the MNIST dataset and returns
    the trained encoder, decoder, and a flag indicating training completion.

    Args:
        settings (Settings): The settings object containing model, training,
            and data configurations.

    Returns:
        tuple[Sequential, Sequential, Literal[True]]: A tuple containing the trained encoder,
            decoder, and a boolean flag indicating that the model has been successfully trained.
    """  # noqa: D205

    # Define the encoder and decoder architecture
    # encoder = nn.Sequential(nn.Linear(28 * 28, 64), nn.ReLU(), nn.Linear(64, 3))
    encoder = nn.Sequential(
        nn.Linear(settings.model.input_dim, settings.model.hidden_dim),
        nn.ReLU(),
        nn.Linear(settings.model.hidden_dim, settings.model.latent_dim),
    )
    # decoder = nn.Sequential(nn.Linear(3, 64), nn.ReLU(), nn.Linear(64, 28 * 28))
    decoder = nn.Sequential(
        nn.Linear(settings.model.latent_dim, settings.model.hidden_dim),
        nn.ReLU(),
        nn.Linear(settings.model.hidden_dim, settings.model.input_dim),
    )

    # Initialize the LitAutoEncoder
    autoencoder = LitAutoEncoder(encoder, decoder, learning_rate=settings.training.learning_rate)

    # Load the MNIST dataset
    # Note: Ensure the path is set correctly in settings.data.mnist_data_path
    # dataset = MNIST(os.getcwd(), download=True, transform=ToTensor())
    dataset = MNIST(settings.data.mnist_data_path, download=True, transform=ToTensor())
    train_loader = utils.data.DataLoader(dataset)

    # Initialize the TensorBoard logger
    logger = CSVLogger("lightning_logs", name="LitAutoEncoder")

    # Train the autoencoder
    # trainer = L.Trainer(limit_train_batches=100, max_epochs=1, logger=logger)
    trainer = L.Trainer(
        limit_train_batches=settings.training.limit_train_batches,
        max_epochs=settings.training.epochs,
        logger=logger,
    )
    trainer.fit(model=autoencoder, train_dataloaders=train_loader)

    is_model_trained = True  # Mark model as trained

    return encoder, decoder, is_model_trained
