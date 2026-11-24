"""
Tests for the audio metrics module.
"""

import numpy as np
import pytest

from bassforge.audio.metrics import calculate_audio_metrics


def test_calculate_audio_metrics():
    audio_data = np.array([0.5, -0.5, 1.0, -1.0])

    metrics = calculate_audio_metrics(audio_data)

    assert metrics["peak_amplitude"] == 1.0
    assert metrics["rms_level"] == pytest.approx(0.7905694)
    assert metrics["crest_factor"] == pytest.approx(1.264911)


def test_zero_audio_metrics():
    audio_data = np.zeros(100)

    metrics = calculate_audio_metrics(audio_data)

    assert metrics["peak_amplitude"] == 0.0
    assert metrics["rms_level"] == 0.0
    assert metrics["crest_factor"] == 0.0


def test_empty_audio_raises_error():
    audio_data = np.array([])

    with pytest.raises(ValueError):
        calculate_audio_metrics(audio_data)
