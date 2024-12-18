Computer Vision Robotic Hand Project
This project involves two sets of code: biomimic and linearmimic. The biomimic code, available in both Python and Arduino IDE formats, maps each finger's angle to the corresponding servo to simulate realistic hand movements. The linearmimic code determines if a finger is open or closed and sends the signal to the Arduino, causing the servo to hold a position at either 0 degrees (closed) or 180 degrees (open).

Hardware Requirements
MG90S positional servo
Arduino Uno
Setup and Execution Steps
1.Assemble the Circuit:

Refer to the provided circuit diagram to connect your MG90S servo to the Arduino Uno.
2.Upload Arduino Code:

Open the .ino file in the Arduino IDE.
Select the correct COM port for your Arduino connection.
Upload the code to the Arduino Uno.
3.Prepare Python Environment:

Open the Python file corresponding to your project.
Update the COM port variable to match the port your Arduino is connected to.
4.Run the Python Script:

Ensure that the Arduino IDE is not using the COM port by temporarily changing it to an unused port in the IDE.
Execute the Python script to start controlling the robotic hand via computer vision.
