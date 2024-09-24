#include "nik_constants.h"
void setup() {
  Serial.begin(115200);
  set_pinmode();
  thermo1.begin(MAX31865_2WIRE);
  thermo2.begin(MAX31865_2WIRE);
	read_sensor_Thread.onRun(read_sensors);

	controll.add(&read_sensor_Thread);

  delay(500);
}

void loop() {

      // delay(4000); 
      // Serial.println(s1.Temp);
  init_buttons();
  read_buttons();
  write_leds();
  off_inc();  
  off_dec();  
  if (Serial.available() > 0) {
    char incomingByte = Serial.read();
    if (incomingByte==49)  ///1
    {
      lamp_test_on();

    }
    else if (incomingByte==50)  //2 
    {
      lamp_test_off();
    
    }  
    else if (incomingByte=='3')   //3
    {
      read_sensors();
      // delay(1000);      
    } 
    else if (incomingByte=='4') //4
    {
      start();     
    }  
    else if (incomingByte=='5') //5
    {
      stop();     
    }      
    else if (incomingByte=='6') //6
    {
      inc();     
    }  
    else if (incomingByte=='7') //7
    {
      dec();     
    }    
    else if (incomingByte=='8') //8
    {
      emg_stop();     
    }           
    else if (incomingByte=='9') //9
    {
      reset();     
    }                  
    else{
      Serial.println("salam");
    }
  } 
  // controll.run();
  // delay(200); 
}