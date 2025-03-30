import cv2
import time
import numpy as np
import hand_tracking_module as htm
import music
import math
import pulsectl

##################################
wcam, hcam = 640, 480
##################################

cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)


# Create a PulseAudio connection
with pulsectl.Pulse('volume-control') as pulse:
    # Get the default sink (speakers)
    sink = pulse.get_sink_by_name(pulse.server_info().default_sink_name)
    
    minVol = 0.0
    maxVol = 2.0
    centerVol = (minVol+maxVol)/2
    pulse.volume_set_all_chans(sink, centerVol)
    #print(f"Volume set to: {new_volume}")
    
    music.play_song()
    
    while True:
        success, img = cap.read()
        img = cv2.flip(img,1)
        img = detector.findHands(img)    
        lmList = detector.findPosition(img, draw=False)
        
        # Create volume bar on screen
        cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
        
        if len(lmList) != 0:
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]
            cx, cy = (x1 + x2)//2, (y1 + y2)//2
            
            cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
            cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
            
            length = math.hypot(x2-x1, y2-y1)
            #print(length)
            
            # Hand Range 50 - 300
            # Volume Range 0.0 - 1.0
            
            vol = np.interp(length, [50,300], [minVol, maxVol])
            print(vol)
            
            # Create filled rectangle to show current volume level
            volBar = np.interp(length, [50, 300], [400, 150])
            cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
        
            pulse.volume_set_all_chans(sink, vol)
            #print(f"Volume set to: {new_volume}")
            
            # Display volume percentage
            cv2.putText(img, f'{int((vol/2)*100)}%', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
        
            if length < 50:
                cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

        
        
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        
        cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (205,10,0), 3)
        
        cv2.imshow("img", img)
        cv2.waitKey(1)
