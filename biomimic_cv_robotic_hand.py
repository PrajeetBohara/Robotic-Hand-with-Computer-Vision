import cv2
import mediapipe as mp
import serial
import time

arduino = serial.Serial('COM4', 9600)
time.sleep(2)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Flip frame for easier interaction
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with Mediapipe
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Define landmarks for fingertips and DIP joints
            fingertips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky tips
            dips = [3, 6, 10, 14, 18]        # DIP joints just below the tips

            angles = []  # List to store calculated servo angles

            for tip, dip in zip(fingertips, dips):
                # Get y-coordinates of tip and dip
                tip_y = hand_landmarks.landmark[tip].y
                dip_y = hand_landmarks.landmark[dip].y

                # Calculate the difference and normalize to 0-1
                # Adjust the scaling factor (0.2) as needed for your hand size and gesture
                diff = dip_y - tip_y
                normalized_diff = max(0, min(1, diff / 0.2))  # Scale the difference

                # Map to servo angle range (0 to 180 degrees)
                angle = int(normalized_diff * 180)
                angles.append(angle)

            # Send angles for all servos to Arduino
            command = ",".join(map(str, angles)) + "\n"
            arduino.write(command.encode())
            print(f"Finger Angles: {angles}")

            # Draw hand landmarks on the video frame
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    else:
        print("No hand detected")

    # Display the video feed with annotations
    cv2.imshow("Hand Tracking", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
arduino.close()
