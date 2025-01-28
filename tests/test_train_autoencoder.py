from dev_container_uv_datascience.train_autoencoder import train_litautoencoder


def test_train_litautoencoder() -> None:
    encoder, decoder, is_model_trained = train_litautoencoder()
    assert encoder is not None
    assert decoder is not None
    assert is_model_trained is True
