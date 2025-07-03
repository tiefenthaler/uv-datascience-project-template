import os
from typing import Literal

import lightning as L  # noqa: N812
from lightning.pytorch.callbacks import ModelCheckpoint
from lightning.pytorch.loggers import CSVLogger
from torch import nn, utils
from torch.nn import Sequential
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor

from .config import Settings
from .lit_auto_encoder import LitAutoEncoder


def train_litautoencoder(settings: Settings) -> tuple[Sequential, Sequential, Literal[True], str]:
    """Trains a LitAutoEncoder model on the MNIST dataset and returns
    the trained encoder, decoder, a flag indicating training completion, and the checkpoint path.

    Args:
        settings (Settings): The settings object containing model, training,
            and data configurations.

    Returns:
        tuple[Sequential, Sequential, Literal[True], str]: A tuple containing the trained encoder,
            decoder, a boolean flag indicating that the model has been successfully trained,
            and the path to the saved model checkpoint.
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

    # Define ModelCheckpoint callback
    checkpoint_dir = os.path.join(
        settings.data.mnist_data_path, "lightning_logs", "LitAutoEncoder", "checkpoints"
    )
    os.makedirs(checkpoint_dir, exist_ok=True)
    checkpoint_callback = ModelCheckpoint(
        dirpath=checkpoint_dir, filename="autoencoder-{epoch:02d}", save_last=True
    )

    # Train the autoencoder
    # trainer = L.Trainer(limit_train_batches=100, max_epochs=1, logger=logger)
    trainer = L.Trainer(
        limit_train_batches=settings.training.limit_train_batches,
        max_epochs=settings.training.epochs,
        logger=logger,
        callbacks=[checkpoint_callback],
    )
    trainer.fit(model=autoencoder, train_dataloaders=train_loader)

    # Save a checkpoint explicitly at the end of training
    final_checkpoint_path = os.path.join(
        str(settings.data.mnist_data_path),
        "lightning_logs",
        "LitAutoEncoder",
        "checkpoints",
        "final_autoencoder.ckpt",
    )
    os.makedirs(os.path.dirname(final_checkpoint_path), exist_ok=True)
    trainer.save_checkpoint(final_checkpoint_path)

    is_model_trained = True  # Mark model as trained

    # Return the path to the best model checkpoint
    return autoencoder.encoder, autoencoder.decoder, is_model_trained, final_checkpoint_path
