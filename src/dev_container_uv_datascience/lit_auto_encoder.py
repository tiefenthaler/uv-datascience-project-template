import lightning as L  # noqa: N812
from torch import Tensor, nn, optim


# define the LightningModule
class LitAutoEncoder(L.LightningModule):
    """A simple autoencoder model."""

    def __init__(self, encoder, decoder) -> None:
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder

    def training_step(self, batch, batch_idx) -> Tensor:
        """Training step that defines the train loop.

        Training_step defines the train loop, it is independent of forward.
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
