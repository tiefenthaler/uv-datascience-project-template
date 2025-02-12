from typing import Tuple

import lightning as L  # noqa: N812
from torch import Tensor, nn, optim


# define the LightningModule
class LitAutoEncoder(L.LightningModule):
    """A simple autoencoder model.

    Args:
        encoder: The encoder component, responsible for encoding input data.
        decoder: The decoder component, responsible for decoding encoded data.
    """

    def __init__(self, encoder: nn.Sequential, decoder: nn.Sequential) -> None:
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder

    def training_step(self, batch: Tuple[Tensor, Tensor], batch_idx: int) -> Tensor:
        """Performs a single training step for the model.

        Args:
            batch (Tuple[Tensor, Tensor]): A tuple containing the input data (x) and
                the corresponding labels (y).
            batch_idx (int): The index of the current batch.

        Returns:
            Tensor: The computed loss for the current training step.
        """

        x, y = batch
        x = x.view(x.size(0), -1)
        z = self.encoder(x)
        x_hat = self.decoder(z)
        loss = nn.functional.mse_loss(x_hat, x)
        # Logging to TensorBoard (if installed) by default
        # self.log("train_loss", loss)
        return loss

    def configure_optimizers(self) -> optim.Adam:
        """Configure the Adam optimizer."""
        optimizer = optim.Adam(self.parameters(), lr=1e-3)
        return optimizer
