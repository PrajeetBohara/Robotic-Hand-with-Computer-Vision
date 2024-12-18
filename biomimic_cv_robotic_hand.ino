#include <Servo.h>

// Create Servo objects for 5 servos
Servo servos[5];
const int servoPins[5] = {3, 5, 6, 9, 10}; // Pins connected to servos

void setup() {
  for (int i = 0; i < 5; i++) {
    servos[i].attach(servoPins[i]);  // Attach each servo to its pin
  }
  Serial.begin(9600);  // Start serial communication
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');  // Read incoming data
    int angles[5] = {0};  // Initialize array to store servo angles
    int index = 0;

    // Parse the comma-separated angles
    char *token = strtok(data.c_str(), ",");
    while (token != NULL && index < 5) {
      angles[index++] = atoi(token);  // Convert token to integer
      token = strtok(NULL, ",");
    }

    // Move servos to the received angles
    for (int i = 0; i < 5; i++) {
      if (angles[i] >= 0 && angles[i] <= 180) {
        servos[i].write(angles[i]);  // Set servo angle
      }
    }
  }
}
