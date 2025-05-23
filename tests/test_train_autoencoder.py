from uv_datascience_project_template.train_autoencoder import train_litautoencoder


def test_train_litautoencoder() -> None:
    """Test that train_litautoencoder returns valid encoder, decoder, and True flag.

    Ensures the function returns non-None encoder and decoder, and the flag is True.
    """
    encoder, decoder, is_model_trained = train_litautoencoder()
    assert encoder is not None
    assert decoder is not None
    assert is_model_trained is True


def test_train_litautoencoder_idempotent() -> None:
    """Test that repeated calls to train_litautoencoder do not raise errors.

    Ensures the function is idempotent and returns valid results on multiple calls.
    """
    for _ in range(2):
        encoder, decoder, is_model_trained = train_litautoencoder()
        assert encoder is not None
        assert decoder is not None
        assert is_model_trained is True
