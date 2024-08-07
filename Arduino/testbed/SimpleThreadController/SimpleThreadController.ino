#include "myheader.h"
#include <Thread.h>
#include <ThreadController.h>

// ThreadController that will controll all threads
ThreadController controll = ThreadController();

//My Thread (as a pointer)
Thread* myThread = new Thread();
//His Thread (not pointer)
Thread hisThread = Thread();

// callback for myThread
void niceCallback(){
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

}

// callback for hisThread
void boringCallback(){
	     speed();

}

void setup(){
	// Serial.begin(9600);
  set_ping_mode();
  Serial.begin(115200);
  digitalWrite(stop_lamp_pin,HIGH);
  digitalWrite(starter_pin,LOW);
  analogWrite(pwm_pin,0);
  digitalWrite(stop_pin,LOW);
  pinMode(pwm_pin,OUTPUT);
	// Configure myThread
	myThread->onRun(niceCallback);
	myThread->setInterval(5000);

	// Configure myThread
	hisThread.onRun(boringCallback);
	hisThread.setInterval(0);

	// Adds both threads to the controller
	controll.add(myThread);
	controll.add(&hisThread); // & to pass the pointer to it
}

void loop(){
	// run ThreadController
	// this will check every thread inside ThreadController,
	// if it should run. If yes, he will run it;
	controll.run();

	// Rest of code
	float h = 3.1415;
	h/=2;
}