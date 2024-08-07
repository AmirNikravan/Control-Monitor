#include "myheader.h"
// #include <arduinoThread
void setup() {
  // Initialize serial communication at a baud rate of 9600
  set_ping_mode();
  Serial.begin(115200);
  digitalWrite(stop_lamp_pin,HIGH);
  digitalWrite(starter_pin,LOW);
  analogWrite(pwm_pin,0);
  digitalWrite(stop_pin,LOW);
  pinMode(pwm_pin,OUTPUT);
   
  // Print a message indicating the start of the program
  // Serial.println("Arduino is ready to receive data...");
}

void loop() {
  // Check if there is incoming data
  if (Serial.available() > 0) {
    // Read the incoming data as a string
    receivedData = Serial.readStringUntil('\n');
    // Print the received data to the Serial Monitor
    // Serial.print("Received: ");
    // Serial.println(receivedData);
    if (receivedData == "s1")
      set_speed(30,14);
    
    else if (receivedData == "s2")
      set_speed(30,12);
    else if (receivedData == "s3")
      set_speed(0,0);
    else if (receivedData == "s4")
      set_speed(0,0);
    else if (receivedData == "s5")
      set_speed(0,0);
    else if (receivedData == "s6")
      set_speed(0,0);
    else if (receivedData == "s7")
      set_speed(0,0);
    else if (receivedData == "s8")
      set_speed(0,0);
    else if (receivedData == "s9")
      set_speed(0,0);
    else if (receivedData == "s10")
      set_speed(0,0);
    else if (receivedData == "in")
      increase_speed();
    else if (receivedData == "de")
      decrease_speed();
    else if (receivedData == "st")
      {start();
      // speed();
      }
    else if (receivedData == "sp")
      stop();
    else if (receivedData == "re")
      reset();
    else if (receivedData == "nf")
      nf();
      else if (receivedData == "mg")
      emg_stop();
  }
  if (receivedData != "-1")
     speed();
}
