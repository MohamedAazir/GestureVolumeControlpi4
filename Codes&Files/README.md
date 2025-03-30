## Overview

The system uses computer vision to track hand landmarks and interpret gestures as volume control commands.The project consists of three main components:

1. Hand tracking module
2. Volume control script
3. Music playback utility

## File Descriptions

### `hand_tracking_module.py`

This module provides the core hand detection and tracking functionality:

- Uses MediaPipe's hand detection model to identify hand landmarks in video frames
- Provides methods to detect hands and find landmark positions
- Returns a list of coordinates for each hand landmark
- Can visualize hand landmarks and connections on the video feed
- Includes a testing function that can be run directly

<img src="Codes&Files/img/hand recognition.png" alt="Hand Recognition" width="50%" height="auto">


### `volume control advanced.py`

The main script that implements the volume control functionality:

- Captures video from the webcam
- Uses the hand tracking module to detect hand landmarks
- Calculates the distance between thumb and index finger
- Maps this distance to a volume level
- Controls system volume using PulseAudio
- Displays a visual volume bar and percentage on screen
- Shows hand landmarks and connections for visual feedback
- Includes FPS counter for performance monitoring

<img src="Codes&Files/img/volume control.png" alt="Hand Recognition" width="50%" height="auto">

### `music.py`

A utility script for testing the volume control:

- Uses VLC media player to play the audio file
- Can be run independently or imported by other scripts

## How to Use

1. Make sure you have all required dependencies installed
2. Update the `song_path` in `music.py` to point to your audio file
3. Run `volume control advanced.py`
4. Use your hand in front of the webcam:
   - Bring your thumb and index finger closer to decrease volume
   - Spread them apart to increase volume
