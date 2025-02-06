import os
from typing import Any

import uvicorn
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, conint
from torch import rand

from .lit_auto_encoder import LitAutoEncoder
from .train_autoencoder import train_litautoencoder

app = FastAPI()

# Global variables for encoder/decoder
encoder = None
decoder = None
is_model_trained = False  # Track model training status


# Input validation model
class NumberFakeImages(BaseModel):
    n_fake_images: conint(ge=1, le=10)  # type: ignore # Between 1 and 10 fake images allowed


# ROOT endpoint
@app.get("/")
def read_root() -> Response:
    """Root endpoint that provides information about the API."""

    message = """
    ⚡⚡⚡ Welcome to the LitAutoEncoder API! ⚡⚡⚡
    - To train the model, send a POST request to '/train' without providing any additional input.
    - To get encodings for random fake images, POST to '/embed' with JSON input: 
      {'n_fake_images': [1-10]} in the request body.
    """
    return Response(content=message, media_type="text/plain")


# POST endpoint to train the autoencoder
@app.post("/train")
def train_model() -> dict[str, str]:
    """Train the autoencoder model.

    Returns:
        dict[str, str]: A message indicating the training status.
    """
    global encoder, decoder, is_model_trained

    if is_model_trained:
        return {"message": "Model is already trained."}

    encoder, decoder, is_model_trained = train_litautoencoder()
    return {"message": "Model training completed successfully."}


# POST endpoint to embed fake images using the trained autoencoder
@app.post("/embed")
def embed(input_data: NumberFakeImages) -> dict[str, Any]:
    """Embed fake images using the trained autoencoder.

    Args:
        input_data (NumberFakeImages): Input data containing the number of fake images to embed.

    Returns:
        dict[str, Any]: A dictionary containing the embeddings of the fake images.
    """
    global encoder, decoder

    if encoder is None or decoder is None:
        raise HTTPException(
            status_code=500, detail="Model not initialized. Train the model first."
        )

    n_fake_images = input_data.n_fake_images
    checkpoint_path = "./lightning_logs/LitAutoEncoder/version_0/checkpoints/epoch=0-step=100.ckpt"

    if not os.path.exists(checkpoint_path):
        raise HTTPException(
            status_code=500, detail="Checkpoint file not found. Train the model first."
        )

    # Load the trained autoencoder from the checkpoint
    autoencoder = LitAutoEncoder.load_from_checkpoint(
        checkpoint_path, encoder=encoder, decoder=decoder
    )
    encoder_model = autoencoder.encoder
    encoder_model.eval()

    # Generate fake image embeddings based on user input
    fake_image_batch = rand(n_fake_images, 28 * 28, device=autoencoder.device)
    embeddings = encoder_model(fake_image_batch)
    # print("⚡" * 20, "\nPredictions (image embeddings):\n", embeddings, "\n", "⚡" * 20)

    return {"embeddings": embeddings.tolist()}


# Application entry point
if __name__ == "__main__":
    # Run the FastAPI application
    uvicorn.run(app, host="0.0.0.0", port=8000)
