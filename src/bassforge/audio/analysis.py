"""
Audio analysis module.

Responsible for inspecting audio files and extracting
basic technical information.
"""

import soundfile as sf


def analyze_audio_file(file_path):
    """
    Extract basic technical information from an audio file.
    """

    audio_info = sf.info(file_path)

    return {
        "duration": audio_info.duration,
        "sample_rate": audio_info.samplerate,
        "channels": audio_info.channels,
        "frames": audio_info.frames,
        "format": audio_info.format,
        "subtype": audio_info.subtype,
    }
