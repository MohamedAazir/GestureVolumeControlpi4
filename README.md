# GestureVolumeControlpi4

## Project Description

This project demonstrates a gesture-based volume control system using the Raspberry Pi 4, OpenCV, MediaPipe, and VLC Media Player. The main objective of the project is to provide a hands-free method of controlling the volume of audio or video playback by recognizing specific hand gestures through the camera.

## System Overview

- **Raspberry Pi 4**: Acts as the central processing unit for processing and controlling the system.
- **USB Web Camera**: Captures real-time hand gestures.
- **OpenCV**: Used for image processing and capturing video frames.
- **MediaPipe**: A machine learning framework by Google, used for detecting hand gestures using a pre-trained model.
- **VLC Media Player**: Plays audio or video files and adjusts volume based on recognized gestures.

## How It Works

1. **Gesture Detection**: The camera captures the user's hand gestures, which are processed using MediaPipe’s hand tracking model. The system identifies the position of the fingers and the overall gesture in real time.

2. **Gesture Interpretation**: Specific gestures, such as the distance between the thumb and index finger or the position of the hand, are mapped to volume control actions. For example:
   - A **pinch gesture** is used to decrease the volume.
   - A **spread fingers gesture** is used to increase the volume.

3. **Volume Adjustment**: Once the gesture is detected and processed, a corresponding action is triggered in VLC Media Player to adjust the volume up or down accordingly.

4. **VLC Integration**: The system integrates with VLC to control media playback and adjust the volume using Python scripting with VLC's interface.

## Technologies Used

- **Raspberry Pi 4**: Central computing platform.
- **OpenCV**: Library for image processing and video capture.
- **MediaPipe**: Framework for hand gesture detection.
- **VLC Media Player**: Media player for playing audio and video files.
- **Python**: Programming language used for integrating all components and implementing the gesture control logic.

## Applications

- **Hands-free control**: Useful for accessibility and people with limited mobility.
- **Smart home integration**: Can be expanded to control other devices with gestures.
- **Interactive media control**: Offers a novel and intuitive way to control media volume without the need for physical interaction.

## Resources

These are some of the resources I utilized to get the required output.

- Setting Up the Raspberry Pi4 Buster OS --> https://core-electronics.com.au/guides/flash-buster-os-pi/
- OpenCV Contrib package info --> https://www.piwheels.org/project/opencv-contrib-python/
- Installing OpenCV --> https://fernandezvictor.medium.com/installing-opencv-on-raspberry-pi-3fe36da91e86#338b
- Hand Recognition and Finger Identification with Raspberry Pi4 --> https://core-electronics.com.au/guides/hand-identification-raspberry-pi/
- Implementing Gesture Volume Control in VS Code --> https://www.youtube.com/playlist?list=PLMoSUbG1Q_r8jFS04rot-3NzidnV54Z2q
