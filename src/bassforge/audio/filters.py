"""
Digital audio filtering module.

Provides filters for isolating specific frequency ranges.
"""

from scipy.signal import butter, sosfiltfilt


def apply_lowpass_filter(audio_data, sample_rate, cutoff_frequency, order=4):
    """
    Allow frequencies below the specified cutoff to pass through.
    """

    if not 0 < cutoff_frequency < sample_rate / 2:
        raise ValueError(
            "Cutoff frequency must be between 0 and the Nyquist frequency."
        )

    filter_coefficients = butter(
        order,
        cutoff_frequency,
        btype="lowpass",
        fs=sample_rate,
        output="sos"
    )

    filtered_audio = sosfiltfilt(
        filter_coefficients,
        audio_data,
        axis=0
    )

    return filtered_audio.astype("float32")
