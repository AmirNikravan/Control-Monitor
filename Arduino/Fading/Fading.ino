#include "myheader.h"
#include <TaskScheduler.h>

// Scheduler
Scheduler runner;

// Flag to track if start function has been called
bool isStarted = false;  

// Variable to store incoming data
// String receivedData = "";  

// Create task for speed function
void speedTaskCallback();
Task speedTask(0, TASK_FOREVER, &speedTaskCallback);

void setup() {
  // Initialize serial communication at a baud rate of 115200
  Serial.begin(115200);
  pinMode(stop_lamp_pin, OUTPUT);
  pinMode(starter_pin, OUTPUT);
  pinMode(pwm_pin, OUTPUT);
  pinMode(stop_pin, OUTPUT);

  digitalWrite(stop_lamp_pin, HIGH);
  digitalWrite(starter_pin, LOW);
  analogWrite(pwm_pin, 0);
  digitalWrite(stop_pin, LOW);

  // Print a message indicating the start of the program
  Serial.println("Arduino is ready to receive data...");

  // Add tasks to the scheduler
  runner.init();
  runner.addTask(speedTask);
}

void loop() {
  // Check if there is incoming data
  if (Serial.available() > 0) {
    // Read the incoming data as a string
    receivedData = Serial.readStringUntil('\n');
    // Process the received data
    handleInput(receivedData);
  }

  // Execute the scheduler
  runner.execute();
}

void handleInput(String input) {
  if (input == "s1") {
    set_speed(30, 14);
  } else if (input == "s2") {
    set_speed(30, 12);
  } else if (input == "s3") {
    set_speed(0, 0);
  } else if (input == "s4") {
    set_speed(0, 0);
  } else if (input == "s5") {
    set_speed(0, 0);
  } else if (input == "s6") {
    set_speed(0, 0);
  } else if (input == "s7") {
    set_speed(0, 0);
  } else if (input == "s8") {
    set_speed(0, 0);
  } else if (input == "s9") {
    set_speed(0, 0);
  } else if (input == "s10") {
    set_speed(0, 0);
  } else if (input == "in") {
    increase_speed();
  } else if (input == "de") {
    decrease_speed();
  } else if (input == "st") {
    start();
    isStarted = true;  // Set the flag to true
    speedTask.enable(); // Enable the speed task
  } else if (input == "sp") {
    stop();
    isStarted = false;  // Reset the flag to false
    speedTask.disable(); // Disable the speed task
  } else if (input == "re") {
    reset();
    isStarted = false;  // Reset the flag to false
    speedTask.disable(); // Disable the speed task
  } else if (input == "nf") {
    nf();
  } else if (input == "mg") {
    emg_stop();
    isStarted = false;  // Reset the flag to false in case of emergency stop
    speedTask.disable(); // Disable the speed task
  }
}

void speedTaskCallback() {
  if (isStarted) {
    speed();
  }
}