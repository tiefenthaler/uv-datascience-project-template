"""Example python package.

PyTorch Lightning module used as an example as a python package for the tutorial/template
for data science projects using uv.
"""

from .lit_auto_encoder import LitAutoEncoder
from .train_autoencoder import train_litautoencoder

__all__ = ["LitAutoEncoder", "train_litautoencoder"]
