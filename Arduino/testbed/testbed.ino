#include "myheader.h"
void setup() {
  // Initialize serial communication at a baud rate of 9600
  Serial.begin(9600);
  pinMode(pwm_pin,OUTPUT);
  // Print a message indicating the start of the program
  Serial.println("Arduino is ready to receive data...");
}

void loop() {
  // Check if there is incoming data
  if (Serial.available() > 0) {
    // Read the incoming data as a string
    String receivedData = Serial.readStringUntil('\n');
    // Print the received data to the Serial Monitor
    Serial.print("Received: ");
    Serial.println(receivedData);
    if (receivedData == "s1")
      set_speed(5);
    
    else if (receivedData == "s2")
      set_speed(5);
    else if (receivedData == "s3")
      set_speed(5);
    else if (receivedData == "s4")
      set_speed(5);
    else if (receivedData == "s5")
      set_speed(5);
    else if (receivedData == "s6")
      set_speed(5);
    else if (receivedData == "s7")
      set_speed(5);
    else if (receivedData == "s8")
      set_speed(5);
    else if (receivedData == "s9")
      set_speed(5);
    else if (receivedData == "s10")
      set_speed(5);
    else if (receivedData == "in")
      set_speed(5);
    else if (receivedData == "de")
      set_speed(5);
    else if (receivedData == "st")
      set_speed(5);
    else if (receivedData == "sp")
      set_speed(5);
  }
}
