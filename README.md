# Servo_move_with_hand_gesture
This a project used your computer camara to move servo in it the more distance you have between your index and thumb the more the servo move


# Servo Control with Hand Gestures using OpenCV and Arduino

This project uses Computer Vision with MediaPipe to detect hand gestures through a webcam and control two servo motors connected to an Arduino. Based on finger positions, the servo motors rotate to specific angles in real time.

👉 Watch the video linked in the repository to see how this works!

====================
WHAT YOU’LL NEED
====================

Hardware:
- Arduino UNO or compatible board
- 2x Servo Motors (e.g., SG90)
- Jumper wires
- Battery pack or USB power for Arduino
- Breadboard (optional)

Software / Libraries:
- Python 3.8+
- OpenCV (cv2)
- MediaPipe
- pyserial
- Arduino IDE

====================
SETUP INSTRUCTIONS
====================

1. INSTALL PYTHON LIBRARIES

Open terminal or command prompt and install the required libraries:

pip install opencv-python mediapipe pyserial

2. CIRCUIT CONNECTIONS

Arduino Pin  | Connect To
-------------|---------------------
D3           | Servo 1 signal pin
D5           | Servo 2 signal pin
GND          | Servo/battery GND
5V / Vin     | Servo Power

Tip: If servos are jittering or weak, use a separate battery pack (like 4xAA) instead of USB power.

3. UPLOAD ARDUINO CODE

- Open the "Servo_move_cpp.ino" file with Arduino IDE.
- Select the correct board and COM port.
- Upload the code to your Arduino.

4. RUN THE PYTHON SCRIPT

- Open "main.py" in any code editor.
- Make sure to change the COM port in the script (e.g., 'COM4') to match your Arduino.
- Run it using:

python Servo_move_with _hand_gesture.py

- Put your hand in front of the webcam.
- The program will detect hand gestures and send angles to the Arduino to rotate the servos.

====================
HOW IT WORKS
====================

- MediaPipe detects 21 key hand landmarks via webcam.
- The code calculates the distance between the thumb tip and index finger tip.
- This distance is mapped from 0–180 degrees.
- That angle is sent via serial to Arduino.
- The Arduino rotates:
    - Servo 1 (D3) if angle is in 0–180
    - Servo 2 (D5) if angle is in 181–361

====================
WHAT I LEARNED
====================

- Real-time hand tracking with MediaPipe
- Webcam input and visualization with OpenCV
- Mapping distances to angles using NumPy
- Sending serial data from Python to Arduino
- Controlling multiple servo motors
- Python + Hardware integration

====================
CREDITS & NOTES
====================

- All core logic and implementation done by me.
- ChatGPT helped me debug and improve the logic.
- This is my own original idea and execution.
- The project shows my skill in Computer Vision and Hardware Control.
- 
====================
WATCH THE DEMO VIDEO
====================

working_video.mp4
