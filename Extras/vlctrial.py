import cv2
import time
import numpy as np
import hand_tracking_module as htm
import math
import vlc
import os

##################################
wcam, hcam = 640, 480
##################################

# Path to your music file
MUSIC_PATH = "/home/aazir/Desktop/CVproject/asrna.mp3"  # Change this to your actual file path

# Initialize VLC media player
instance = vlc.Instance('--no-xlib')
player = instance.media_player_new()
media = instance.media_new(MUSIC_PATH)
player.set_media(media)

# Start playing the music
player.play()

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)
pTime = 0
detector = htm.handDetector(detectionCon=0.7)

# Volume settings
minVol = 0
maxVol = 100  # VLC volume is 0-100 percentage

# Wait for player to load
time.sleep(0.5)

# Set initial volume
player.audio_set_volume(50)  # Start at 50% volume

while True:
    success, img = cap.read()
    if not success:
        print("Failed to get frame from camera")
        break
        
    img = cv2.flip(img, 1)
    img = detector.findHands(img)    
    lmList = detector.findPosition(img, draw=False)
    
    # Create volume bar on screen
    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    
    if len(lmList) != 0:
        # Get thumb and index finger positions
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2)//2, (y1 + y2)//2
        
        # Draw circles and line for thumb and index finger
        cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
        cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
        
        # Calculate length between fingers
        length = math.hypot(x2-x1, y2-y1)
        
        # Convert hand range to volume range
        # Hand Range 50 - 300
        # Volume Range 0 - 100
        vol = np.interp(length, [50, 300], [minVol, maxVol])
        
        # Create filled rectangle to show current volume level
        volBar = np.interp(length, [50, 300], [400, 150])
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
        
        # Set VLC volume
        player.audio_set_volume(int(vol))
        
        # Display volume percentage
        cv2.putText(img, f'{int(vol)}%', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
        
        # Change center circle color when volume is minimum
        if length < 50:
            cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
    
    # Calculate and display FPS
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    
    # Show status of VLC player
    status = "Playing" if player.is_playing() else "Paused"
    cv2.putText(img, f'Status: {status}', (320, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    
    cv2.imshow("Volume Control", img)
    key = cv2.waitKey(1)
    
    # Press 'q' to quit, 'p' to pause/play
    if key == ord('q'):
        break
    elif key == ord('p'):
        if player.is_playing():
            player.pause()
        else:
            player.play()

# Cleanup
cap.release()
cv2.destroyAllWindows()
player.stop()