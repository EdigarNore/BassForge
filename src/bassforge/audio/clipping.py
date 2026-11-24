"""
Audio clipping detection module.

Identifies audio samples that exceed the
standard digital amplitude range.
"""

import numpy as np


def detect_clipping(audio_data, threshold=1.0):
    """
    Detect samples whose absolute amplitude reaches
    or exceeds the specified threshold.
    """

    clipping_mask = np.abs(audio_data) >= threshold

    clipping_count = int(np.count_nonzero(clipping_mask))

    return {
        "has_clipping": clipping_count > 0,
        "clipping_count": clipping_count,
        "clipping_percentage": (
            clipping_count / audio_data.size * 100
            if audio_data.size > 0
            else 0.0
        ),
    }
