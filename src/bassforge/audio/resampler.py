"""
Audio resampling module.

Responsible for converting audio from one sample rate
to another.
"""

from math import gcd

from scipy.signal import resample_poly


def resample_audio(audio_data, original_sample_rate, target_sample_rate):
    """
    Convert audio samples to a different sample rate.

    Supports mono and multichannel audio.
    """

    if original_sample_rate <= 0 or target_sample_rate <= 0:
        raise ValueError("Sample rates must be positive.")

    if original_sample_rate == target_sample_rate:
        return audio_data.copy()

    common_divisor = gcd(original_sample_rate, target_sample_rate)

    up = target_sample_rate // common_divisor
    down = original_sample_rate // common_divisor

    resampled_audio = resample_poly(
        audio_data,
        up,
        down,
        axis=0
    )

    return resampled_audio.astype("float32")
