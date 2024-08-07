
#include <Thread.h>
#include <ThreadController.h>
#include"myheader.h"
// ThreadController that will controll all threads
ThreadController controll = ThreadController();

//My Thread (as a pointer)
// Thread* myThread = new Thread();
//His Thread (not pointer)
Thread hisThread = Thread();

// callback for myThread
void niceCallback(){
	Serial.print("COOL! I'm running on: ");
	Serial.println(millis());
}

// callback for hisThread

void setup(){
	// Serial.begin(9600);
set_ping_mode();
  Serial.begin(115200);
  digitalWrite(stop_lamp_pin,HIGH);
  digitalWrite(starter_pin,LOW);
  analogWrite(pwm_pin,0);
  digitalWrite(stop_pin,LOW);
  pinMode(pwm_pin,OUTPUT);
	receivedData = "-1";
	// Configure myThread
	// myThread->onRun(niceCallback);
	// myThread->setInterval(500);

	// Configure myThread
	hisThread.onRun(speed);
	// hisThread.setInterval();

	// Adds both threads to the controller
	// controll.add(myThread);
	controll.add(&hisThread); // & to pass the pointer to it
}

void loop(){
if (Serial.available() > 0) {
    // Read the incoming data as a string
    receivedData = Serial.readStringUntil('\n');
}
    // Print the received data to the Serial Monitor
    // Serial.print("Received: ");
    // Serial.println(receivedData);
    if (receivedData == "s1")
      set_speed(212);
    
    else if (receivedData == "s2")
      set_speed(202);
    else if (receivedData == "s3")
      set_speed(209);
    else if (receivedData == "s4")
      set_speed(216);
    else if (receivedData == "s5")
      set_speed(223);
    else if (receivedData == "s6")
      set_speed(230);
    else if (receivedData == "s7")
      set_speed(237);
    else if (receivedData == "s8")
      set_speed(244);
    else if (receivedData == "s9")
      set_speed(251);
    else if (receivedData == "s10")
      set_speed(10);
    else if (receivedData == "in")
      {increase_speed();
      return;
      }
    else if (receivedData == "de")
      {decrease_speed();
      return;
      }
    else if (receivedData == "st")
      {start();
      // speed();
      }
    else if (receivedData == "sp")
    {
      
      receivedData != "-1";
  // controll.remove(&hisThread);
      
        stop();
        return;
        }
    else if (receivedData == "re")
      reset();
    else if (receivedData == "nf")
      nf();
    else if (receivedData == "mg")
      {
      
      receivedData = "-1";
  // controll.remove(&hisThread);
      
        emg_stop();
        return;
        }
    
  
if (receivedData == "-5")
	controll.run();
  // contoroll.de

	// Rest of code
  // float h = 3.1415;
	// h/=2;
}