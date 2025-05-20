# Autoencoder

The LitAutoEncoder is a PyTorch Lightning module designed for unsupervised learning tasks. It consists of an encoder and a decoder network. The autoencoder's role in the project is to learn a compressed, dense representation of the input data (encoding) and then reconstruct the input data from this representation (decoding). This process helps in understanding the underlying structure of the data and is useful for tasks like anomaly detection, data denoising, and dimensionality reduction.

## Key Features

- **Encoder**: Compresses input data into a latent representation.
- **Decoder**: Reconstructs the input data from the latent representation.
- **Loss Function**: Mean Squared Error (MSE) is used to measure reconstruction quality.

## Autoencoder Class API

::: uv_datascience_project_template.lit_auto_encoder
