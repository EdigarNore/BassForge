"""
Audio loading module.

Responsible for loading audio samples into memory
for analysis and processing.
"""

import soundfile as sf


def load_audio(file_path):
    """
    Load an audio file and return its samples and sample rate.
    """

    audio_data, sample_rate = sf.read(
        file_path,
        dtype="float32",
        always_2d=True
    )

    return audio_data, sample_rate
