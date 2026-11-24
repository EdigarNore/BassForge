"""
Audio normalization module.

Provides utilities for adjusting audio levels
to a consistent amplitude range.
"""

import numpy as np


def normalize_audio(audio_data, target_peak=0.95):
    """
    Normalize audio samples to a target peak amplitude.

    The original audio data is not modified.
    """

    peak = np.max(np.abs(audio_data))

    if peak == 0:
        return audio_data.copy()

    normalized_audio = audio_data * (target_peak / peak)

    return normalized_audio.astype(np.float32)
