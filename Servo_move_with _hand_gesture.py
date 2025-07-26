import serial
import cv2 as cv
import mediapipe as mp
import time
import math
import numpy as np

# Initialize Arduino serial
arduino = serial.Serial('COM4', 9600)
time.sleep(2)

# Initialize camera and MediaPipe
cam = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

index_right = None
index_left = None
thumb_right = None
thumb_left = None

while True:
    success, img = cam.read()
    img = cv.flip(img, 1)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for i, handLms in enumerate(results.multi_hand_landmarks):
            handLabel = results.multi_handedness[i].classification[0].label
            h, w, c = img.shape


            if handLabel == "Right":
                for id, lm in enumerate(handLms.landmark):
                    x, y = int(lm.x * w), int(lm.y * h)

                    if id == 4:
                        thumb_right = (x, y)
                        cv.circle(img, thumb_right, 15, (25, 255, 255), cv.FILLED)

                    if id == 8:
                        index_right = (x, y)
                        cv.circle(img, index_right, 15, (25, 255, 255), cv.FILLED)

                if index_right and thumb_right:
                    cv.line(img, index_right, thumb_right, (0, 255, 0), 5)

                    mid_x = (thumb_right[0] + index_right[0]) // 2
                    mid_y = (thumb_right[1] + index_right[1]) // 2
                    mid_point = (mid_x, mid_y)
                    cv.circle(img, mid_point, 10, (0, 0, 255), cv.FILLED)

                    length = int(math.hypot(index_right[0] - thumb_right[0], index_right[1] - thumb_right[1]))

                    if length < 50:
                        cv.circle(img, mid_point, 10, (255, 0, 255), cv.FILLED)

                    angle = int(np.interp(length, [20, 250], [0, 180]))
                    arduino.write(f"{angle}\n".encode(errors='ignore'))
                    

                    # Draw vertical bar for angle on left side
                    bar_top = 100
                    bar_bottom = 400
                    bar_left = 50
                    bar_right = 80

                    bar_height = np.interp(angle, [0, 180], [bar_bottom, bar_top])

                    cv.rectangle(img, (bar_left, bar_top), (bar_right, bar_bottom), (100, 100, 100), 2)
                    
                    cv.rectangle(img, (bar_left, int(bar_height)), (bar_right, bar_bottom), (100,100,100), cv.FILLED)
                    cv.putText(img, f'{angle} deg', (30, 90), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            if handLabel == "Left":
                for id, lm in enumerate(handLms.landmark):
                    x, y = int(lm.x * w), int(lm.y * h)

                    if id == 4:
                        thumb_left = (x, y)
                        cv.circle(img, thumb_left, 15, (25, 255, 255), cv.FILLED)

                    if id == 8:
                        index_left = (x, y)
                        cv.circle(img, index_left, 15, (25, 255, 255), cv.FILLED)

                if index_left and thumb_left:
                    cv.line(img, index_left, thumb_left, (0, 255, 0), 5)

                    mid_x = (thumb_left[0] + index_left[0]) // 2
                    mid_y = (thumb_left[1] + index_left[1]) // 2
                    mid_point = (mid_x, mid_y)
                    cv.circle(img, mid_point, 10, (0, 0, 255), cv.FILLED)

                    length_left = int(math.hypot(index_left[0] - thumb_left[0], index_left[1] - thumb_left[1]))

                    if length_left < 50:
                        cv.circle(img, mid_point, 10, (255, 0, 255), cv.FILLED)

                    angle_left = int(np.interp(length_left, [20, 250], [181, 361]))
                    arduino.write(f"{angle_left}\n".encode(errors='ignore'))


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv.imshow("Image", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()
