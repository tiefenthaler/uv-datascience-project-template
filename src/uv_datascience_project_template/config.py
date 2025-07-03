"""Configuration management for the application.

This module defines Pydantic models for managing application settings,
including model parameters, training configurations, data paths, and API settings.
Settings can be loaded from environment variables or a .env file.
"""

import os
from pathlib import Path
from typing import Any

import toml
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelSettings(BaseSettings):
    """Model-specific settings."""

    input_dim: int = 784
    hidden_dim: int = 64
    latent_dim: int = 3


class TrainingSettings(BaseSettings):
    """Training-specific settings."""

    epochs: int = 1
    limit_train_batches: int = 100
    learning_rate: float = 0.001


class DataSettings(BaseSettings):
    """Data-specific settings."""

    mnist_data_path: Path = Path("./MNIST")


class APISettings(BaseSettings):
    """API-specific settings."""

    host: str = "0.0.0.0"
    port: int = 8000


class Settings(BaseSettings):
    """Main application settings.

    Settings are loaded from environment variables or a .env file.
    """

    model: ModelSettings = Field(default_factory=ModelSettings)
    training: TrainingSettings = Field(default_factory=TrainingSettings)
    data: DataSettings = Field(default_factory=DataSettings)
    api: APISettings = Field(default_factory=APISettings)

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


def get_settings() -> Settings:
    """Returns a Settings object initialized with current configurations.

    Settings are loaded from 'settings.toml' and can be overridden by environment variables.
    """
    settings_file_path = Path(os.getcwd()) / "settings.toml"
    if settings_file_path.exists():
        with open(settings_file_path, "r") as f:
            toml_settings = toml.load(f)
    else:
        toml_settings = {}

    # Flatten the TOML structure for Pydantic's from_field method
    flat_settings: dict[str, Any] = {}
    for section, values in toml_settings.items():
        for key, value in values.items():
            flat_settings[f"{section.upper()}_{key.upper()}"] = value

    return Settings(**flat_settings)
