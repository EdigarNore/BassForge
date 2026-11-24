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
def apply_highpass_filter(audio_data, sample_rate, cutoff_frequency, order=4):
    """
    Allow frequencies above the specified cutoff to pass through.
    """

    if not 0 < cutoff_frequency < sample_rate / 2:
        raise ValueError(
            "Cutoff frequency must be between 0 and the Nyquist frequency."
        )

    filter_coefficients = butter(
        order,
        cutoff_frequency,
        btype="highpass",
        fs=sample_rate,
        output="sos"
    )

    filtered_audio = sosfiltfilt(
        filter_coefficients,
        audio_data,
        axis=0
    )

    return filtered_audio.astype("float32")
def apply_bandpass_filter(
    audio_data,
    sample_rate,
    low_cutoff,
    high_cutoff,
    order=4
):
    """
    Allow frequencies within a selected range to pass through.
    """

    nyquist_frequency = sample_rate / 2

    if not 0 < low_cutoff < high_cutoff < nyquist_frequency:
        raise ValueError(
            "Cutoff frequencies must satisfy: "
            "0 < low_cutoff < high_cutoff < Nyquist frequency."
        )

    filter_coefficients = butter(
        order,
        [low_cutoff, high_cutoff],
        btype="bandpass",
        fs=sample_rate,
        output="sos"
    )

    filtered_audio = sosfiltfilt(
        filter_coefficients,
        audio_data,
        axis=0
    )

    return filtered_audio.astype("float32")
