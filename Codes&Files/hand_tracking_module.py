import cv2
import time
import mediapipe as mp
import numpy as np

##################################
# Set the dimensions for the webcam feed
wcam, hcam = 640, 480
##################################

# Uncomment the following lines to set the webcam resolution
# cap.set(3, wcam)  # Set width of the webcam feed
# cap.set(4, hcam)  # Set height of the webcam feed

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        """
        Initializes the handDetector class with the given parameters.

        Parameters:
        - mode: Whether to detect hands in static images or video streams.
        - maxHands: Maximum number of hands to detect.
        - detectionCon: Minimum confidence value for hand detection.
        - trackCon: Minimum confidence value for hand tracking.
        """
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        # Initialize Mediapipe Hands and Drawing utilities
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        """
        Detects hands in the given image and optionally draws landmarks.

        Parameters:
        - img: Input image in which hands are to be detected.
        - draw: Whether to draw hand landmarks on the image.

        Returns:
        - img: Image with hand landmarks drawn (if draw=True).
        """
        # Convert the image to RGB as Mediapipe processes RGB images
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)  # Process the image to detect hands
    
        # If hands are detected, draw landmarks on the image
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        """
        Finds the position of hand landmarks in the given image.

        Parameters:
        - img: Input image in which hand landmarks are to be detected.
        - handNo: Index of the hand to analyze (default is 0).
        - draw: Whether to draw circles on the landmarks.

        Returns:
        - lmList: List of landmark positions [id, x, y].
        """
        lmList = []  # List to store landmark positions
        if self.results.multi_hand_landmarks:
            # Get the landmarks of the specified hand
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # Convert normalized landmark coordinates to pixel values
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])  # Append landmark ID and coordinates
                
                if draw:
                    # Draw a circle at each landmark position
                    cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
        return lmList


def main():
    """
    Main function to test the handDetector class.
    Captures video from the webcam and detects hands in real-time.
    """
    pTime = 0  # Previous time for FPS calculation
    cTime = 0  # Current time for FPS calculation
    cap = cv2.VideoCapture(0)  # Start video capture from webcam
    detector = handDetector()  # Create an instance of the handDetector class
    
    while True:
        success, img = cap.read()  # Read a frame from the webcam
        img = detector.findHands(img)  # Detect hands in the frame
        lmList = detector.findPosition(img)  # Get landmark positions
        if len(lmList) != 0:
            print(lmList[4])  # Print the position of the 4th landmark (e.g., thumb tip)
        
        # Calculate and display the Frames Per Second (FPS)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        
        cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (205, 10, 0), 3)
    
        # Display the processed frame
        cv2.imshow("img", img)
        cv2.waitKey(1)  # Wait for 1 ms before displaying the next frame
    
if __name__ == "__main__":
    main()  # Run the main function