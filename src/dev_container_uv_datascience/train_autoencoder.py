import os
from typing import Literal

import lightning as L  # noqa: N812
from lightning.pytorch.loggers import CSVLogger
from torch import nn, utils
from torch.nn import Sequential
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor

from .lit_auto_encoder import LitAutoEncoder


def train_litautoencoder() -> tuple[Sequential, Sequential, Literal[True]]:
    """Training function to initialize models and perform training."""

    # Define the encoder and decoder architecture
    encoder = nn.Sequential(nn.Linear(28 * 28, 64), nn.ReLU(), nn.Linear(64, 3))
    decoder = nn.Sequential(nn.Linear(3, 64), nn.ReLU(), nn.Linear(64, 28 * 28))

    # Initialize the LitAutoEncoder
    autoencoder = LitAutoEncoder(encoder, decoder)

    # Load the MNIST dataset
    dataset = MNIST(os.getcwd(), download=True, transform=ToTensor())
    train_loader = utils.data.DataLoader(dataset)

    # Initialize the TensorBoard logger
    logger = CSVLogger("lightning_logs", name="LitAutoEncoder")

    # Train the autoencoder
    trainer = L.Trainer(limit_train_batches=100, max_epochs=1, logger=logger)
    trainer.fit(model=autoencoder, train_dataloaders=train_loader)

    is_model_trained = True  # Mark model as trained

    return encoder, decoder, is_model_trained
