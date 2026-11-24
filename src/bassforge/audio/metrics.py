"""
Audio metrics module.

Calculates useful measurements of an audio signal,
including peak amplitude, RMS level, and crest factor.
"""

import numpy as np


def calculate_audio_metrics(audio_data):
    """
    Calculate basic audio signal measurements.
    """

    if audio_data.size == 0:
        raise ValueError("Audio data cannot be empty.")

    peak_amplitude = float(np.max(np.abs(audio_data)))

    rms_level = float(np.sqrt(np.mean(np.square(audio_data))))

    crest_factor = (
        peak_amplitude / rms_level
        if rms_level > 0
        else 0.0
    )

    return {
        "peak_amplitude": peak_amplitude,
        "rms_level": rms_level,
        "crest_factor": crest_factor,
    }
