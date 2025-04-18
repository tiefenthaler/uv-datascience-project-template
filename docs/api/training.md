# Training

The training process for the autoencoder involves optimizing the autoencoder to minimize reconstruction error on the input data.

## Steps

1. **Data Preparation**: Load and preprocess the dataset.
2. **Model Initialization**: Instantiate the LitAutoEncoder model.
3. **Training Loop**: Use PyTorch Lightning's Trainer to handle the training process.

## Example

```python
from uv_datascience_project_template.train_autoencoder import train

# Train the autoencoder
train(data_loader, epochs=10, learning_rate=0.001)
```

## Training API

::: uv_datascience_project_template.train_autoencoder
