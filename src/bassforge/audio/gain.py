"""
Audio gain control module.

Provides utilities for adjusting audio signal levels
using decibel-based gain values.
"""

import numpy as np


def apply_gain(audio_data, gain_db):
    """
    Increase or decrease audio signal amplitude using decibels.

    Positive gain increases volume.
    Negative gain decreases volume.
    Zero gain leaves the signal unchanged.
    """

    gain_multiplier = 10 ** (gain_db / 20)

    adjusted_audio = audio_data * gain_multiplier

    return adjusted_audio.astype(np.float32)
