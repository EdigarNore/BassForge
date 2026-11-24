
# BassForge — System Architecture

## 1. Overview

BassForge uses a modular architecture that separates the desktop interface, music playback, audio management, audio analysis and digital signal processing.

The architecture is designed to support both real-time music enhancement and high-quality offline audio rendering.

Each component should have a clearly defined responsibility.

## 2. Architectural Principles

- Separation of concerns.
- Modular and reusable components.
- Shared DSP algorithms across processing modes.
- Efficient audio processing.
- Responsive music playback.
- Non-destructive audio editing.
- Testable and maintainable code.
- Expandability for future features.

## 3. Main System Components

### 3.1 Desktop Interface

Technology: PySide6.

Responsibilities:
- Display the music player.
- Present music libraries and playlists.
- Provide playback controls.
- Display audio visualizations.
- Provide bass-engineering controls.
- Manage application settings.

The interface must not contain the actual DSP algorithms.

### 3.2 Application Core

Responsibilities:
- Coordinate application components.
- Manage application configuration.
- Manage user preferences.
- Coordinate project and playback operations.

### 3.3 Music Library

Responsibilities:
- Import audio files and folders.
- Scan selected music directories.
- Read audio metadata.
- Organize tracks.
- Maintain library information.

### 3.4 Playlist Manager

Responsibilities:
- Create and manage playlists.
- Add and remove tracks.
- Maintain playback queues.
- Support shuffle and repeat.
- Track playlist-specific settings.

### 3.5 Playback Engine

Responsibilities:
- Play decoded audio.
- Pause and resume playback.
- Navigate between tracks.
- Manage playback position.
- Support continuous playback.
- Coordinate real-time audio processing.

The playback engine must prioritize responsiveness and avoid blocking audio callbacks.

### 3.6 Audio Management

Responsibilities:
- Load audio files.
- Decode supported formats.
- Prepare audio data for processing.
- Manage sample rates and channel configurations.
- Coordinate audio export.

### 3.7 Audio Analysis Engine

Responsibilities:
- Analyze frequency distribution.
- Measure audio peaks.
- Identify available sub-bass.
- Evaluate low-frequency energy.
- Detect potential clipping and distortion.
- Provide information to the adaptive processing engine.

### 3.8 Digital Signal Processing Engine

The DSP engine contains the actual audio-enhancement algorithms.

Planned modules:

- Equalization.
- Bass enhancement.
- Sub-bass synthesis.
- Punch enhancement.
- Harmonic enhancement.
- Compression.
- Limiting.
- Stereo processing.

Processing algorithms should remain independent of the graphical interface.

### 3.9 Intelligent Processing Engine

Responsibilities:
- Evaluate audio-analysis results.
- Recommend processing settings.
- Adapt enhancement to individual songs.
- Respect user-defined settings.
- Maintain automatic and manual processing modes.

### 3.10 Audio Export Engine

Responsibilities:
- Render processed audio.
- Export supported formats.
- Apply output settings.
- Preserve original recordings.
- Report processing errors.

## 4. Processing Architecture

BassForge supports two processing modes.

### 4.1 Real-Time Processing

Audio playback follows this general flow:

Audio file
→ Decoder
→ Audio buffer
→ DSP processing
→ Audio output

The analysis engine should prepare track-specific settings before or during playback without interrupting the audio stream.

Real-time processing must consider:
- Low latency.
- Efficient memory usage.
- Stable audio buffers.
- Smooth track transitions.
- Prevention of audio dropouts.

Heavy analysis and file operations must not run inside the real-time audio callback.

### 4.2 Offline Processing

Offline processing follows this flow:

Audio file
→ Decoder
→ Audio analysis
→ DSP processing
→ Quality checks
→ Audio rendering
→ Export

Offline processing may use more computationally intensive algorithms because it does not have to maintain continuous real-time playback.

## 5. Shared Processing Engine

Real-time and offline processing should reuse the same core DSP algorithms wherever practical.

Processing configuration should be separated from the playback and rendering systems.

This allows improvements to individual algorithms to benefit both processing modes.

## 6. Intelligent Playlist Processing

When a playlist is played:

1. The playback engine retrieves the next track.
2. The analysis engine obtains the track's audio characteristics.
3. The intelligent processing engine determines appropriate settings.
4. User overrides and playlist preferences are applied.
5. The DSP engine processes the audio.
6. Enhanced audio is sent to the output.
7. The system prepares the next track.

The system should support pre-analysis and buffering to minimize transitions and playback interruptions.

## 7. User Settings Hierarchy

Processing settings follow this priority:

1. Individual track overrides.
2. Playlist-specific settings.
3. Global application settings.

Users can restore automatic processing for an individual track by resetting its override.

## 8. Proposed Directory Structure

```text
BassForge/
├── app/
├── player/
├── library/
├── audio/
├── processing/
├── intelligence/
├── profiles/
├── interface/
├── export/
├── tests/
└── docs/
```

Each directory will contain focused modules responsible for a specific part of the application.

## 9. Testing Strategy

Testing should cover:

- Audio loading and decoding.
- Audio analysis.
- DSP algorithms.
- Processing stability.
- Clipping and distortion behaviour.
- Playlist management.
- Playback controls.
- Track transitions.
- Real-time performance.
- Offline rendering.
- Export correctness.

## 10. Future Architecture Expansion

The modular design should eventually support:

- AI-assisted audio processing.
- Audio restoration.
- Advanced mastering.
- Device-aware enhancement.
- Batch processing.
- Authorized external music-service integrations.

These additions must not compromise the reliability of the core application.
