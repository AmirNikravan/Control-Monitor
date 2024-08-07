#include "HardwareSerial.h"
#include "Arduino.h"
const int pwm_pin = 9;
const int stop_pin = 29;
const int starter_pin = 30;
const int start_lamp_pin = 32;
const int stop_lamp_pin = 37;
const int emg_stop_pin = 4;
int current_high = 4;
int current_low = 2;
String receivedData="-1";
const int speed_step = 5;
const int initial_speed = 220;
const int step = 20;
float current_speed = initial_speed;
void set_speed(int val){
  // digitalWrite(pwm_pin,HIGH);
  // delay(delay_high);
  // digitalWrite(pwm_pin,LOW);
  // delay(delay_low);
  // analogWrite(pwm_pin,current_speed + val);
  // current_speed = initial_speed + val*step;
  // Serial.println(current_speed);
  // analogWrite(pwm_pin,current_speed)
  if (val == 212){
        Serial.println("started 1");
  current_speed =val;
  analogWrite(pwm_pin,current_speed);
  delay(200);
  digitalWrite(stop_lamp_pin,LOW);
  delay(100);
  digitalWrite(start_lamp_pin,HIGH);
  delay(100);
  digitalWrite(starter_pin,HIGH);//**********************************starter ping nabayad low she?
  delay(8000);
  digitalWrite(starter_pin,LOW);
  receivedData = "-5";
  }
  current_speed =val;
  receivedData = "-5";
}
void speed(){
	if (current_speed >255)
  current_speed = 255;
  analogWrite(pwm_pin, current_speed);
  

  Serial.println(current_speed);
  // Serial.println(current_speed);
}

void decrease_speed(){
  // current_speed -= step;
  // analogWrite(pwm_pin,current_speed);
  // Serial.println(current_speed);
    current_speed -= step;
    receivedData = "-5";
    return;
    // speed();
}
void increase_speed(){
  // current_speed += step;
  // analogWrite(pwm_pin,current_speed);
  // Serial.println(current_speed);
  current_speed += step;
receivedData = "-5";
  return;
  // speed();
}
// void speed0(){

// }
void start(){
  // analogWrite(pwm_pin,128);
  // delay(100);
    Serial.println("started");
  current_speed = initial_speed;
  analogWrite(pwm_pin,current_speed);
  delay(200);
  digitalWrite(stop_lamp_pin,LOW);
  delay(100);
  digitalWrite(start_lamp_pin,HIGH);
  delay(100);
  digitalWrite(starter_pin,HIGH);//**********************************starter ping nabayad low she?
  delay(5000);
  digitalWrite(starter_pin,LOW);
  receivedData = "-5";
  // set_speed(9);
  // for ( int i = 0 ; i < 600 ; i++){
    // digitalWrite(pwm_pin,HIGH);
  //   // delay(254);
  //   // digitalWrite(pwm_pin,LOW);
  //   delay(10);
  // }

  // for (int i = 0;i < 200;i++  ){
  //   digitalWrite(pwm_pin,HIGH);
  //   delay(current_high);
  //   digitalWrite(pwm_pin,LOW);
  // }
    // delay(current_low);
    // if(Serial.available())
    //   {
    //       digitalWrite(starter_pin,LOW);

    //     digitalWrite(start_lamp_pin,LOW);
    //     delay(100);
    //     return;}
    // }
  // analogWrite(pwm_pin,128);
  // delay(100);
  // digitalWrite(stop_lamp_pin,LOW);
  // delay(100);
  // digitalWrite(starter_pin,HIGH);
  // delay(4000);
// for (int i = 0; i < 5 ;i++){
//   digitalWrite(start_lamp_pin,HIGH);
//   delay(300);
//   digitalWrite(start_lamp_pin,LOW);
//   delay(300);
// }

// set_speed(5);
//   analogWrite(pwm_pin,115);
// delay(100);
// digitalWrite(starter_pin,LOW);
// delay(100);
// digitalWrite(start_lamp_pin,HIGH);
// delay(100);
}
void nf(){
  // analogWrite(pwm_pin,115);
  // set_speed(3);
  // delay(100);
    digitalWrite(starter_pin,LOW);
    delay(1000);

}
void stop(){
  Serial.println("stoped");
  receivedData="-1";
    current_speed = 0;
  delay(45);

  // delay(20);
  analogWrite(pwm_pin,0);
  
  digitalWrite(start_lamp_pin,LOW);
  delay(100);
  digitalWrite(stop_lamp_pin,HIGH);
  delay(100);
  // analogWrite(pwm_pin,0);
  // delay(100);
  // digitalWrite(stop_pin,HIGH);
  // delay(1000);
  // digitalWrite(stop_pin,LOW);
  // delay(100);
  
  
  
  // Serial.print("salam");
}
void emg_stop(){
  current_speed = 0 ;
  receivedData="-1";
  Serial.println("emg stoped");
  delay(20);

digitalWrite(start_lamp_pin,LOW);
delay(20);
  digitalWrite(stop_lamp_pin,HIGH);
  delay(20);
  digitalWrite(stop_pin,HIGH);
  // delay(1000);
  // digitalWrite(stop_pin,LOW);
  // delay(100);
  // analogWrite(pwm_pin,0);
  // delay(500);
  
// digitalWrite(emg_stop_pin,LOW);
}

void set_ping_mode(){
pinMode(pwm_pin,OUTPUT);
pinMode(starter_pin,OUTPUT);
pinMode(start_lamp_pin,OUTPUT);
pinMode(stop_lamp_pin,OUTPUT);
pinMode(stop_pin,OUTPUT);
}
void reset(){
  digitalWrite(stop_pin,LOW);
}