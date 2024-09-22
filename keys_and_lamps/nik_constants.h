#include "HardwareSerial.h"
#include "Arduino.h"
#include <ezButton.h>
#include <Arduino_JSON.h>
#include "max6675.h"
#include <Adafruit_MAX31865.h>
#include <ThreadController.h>
#include <Thread.h>
int initial_speed=140;
int over_speed=240;
int current_speed=initial_speed;
#define RREF      430.0
// The 'nominal' 0-degrees-C resistance of the sensor
// 100.0 for PT100, 1000.0 for PT1000
#define RNOMINAL  100.0
#define BUTTON_NUM 6
#define LED_NUM 5
#define PRESSURE_NUM 4
#define Exhaust2_PIN         31  // Exhaust 2 - MAX6675
#define Exhaust1_PIN         30  // Exhaust 1 - MAX6675
#define DO_PIN               21  // MAX6675 DO PIN
#define CLK_PIN1             20  // Clock Pin - MAX6675






#define Thermocouple1_CS_PIN 24  // Thermocouple1_CS_PIN
#define SDI_PIN1_MAX31865    12  // Thermocouple1_SDI_PIN
#define SDO_PIN1_MAX31865    11  // Thermocouple1_SDO_PIN
#define CLK_PIN1_MAX31865    13  // Thermocouple1_CLK_PIN
// Use software SPI: CS, DI, DO, CLK
Adafruit_MAX31865 thermo = Adafruit_MAX31865(25,8,9,10);
#define Thermocouple2_CS_PIN 25  // Thermocouple2_CS_PIN
#define SDI_PIN2_MAX31865    8  // Thermocouple3_SDI_PIN
#define SDO_PIN2_MAX31865    9  // Thermocouple4_SDO_PIN
#define CLK_PIN2_MAX31865    10  // Thermocouple5_CLK_PIN

#define LED_PIN_Stop         32  // Stop Lamp
#define LED_PIN_Emg_Stop     33    //Emergency Stop Lamp
#define LED_PIN_Dec          34  //Decrease Lamp
#define LED_PIN_Inc          35 //Increase Lamp
#define LED_PIN_5            36
#define LED_PIN_Start        37 // Start Lamp


#define BUTTON_PIN_Stop 40 //Stop Button
#define BUTTON_PIN_Dec 41  //Decrease Button
#define BUTTON_PIN_Start 42 //Start Button
#define BUTTON_PIN_Inc 43 //Increase Button
#define BUTTON_PIN_Emg_Stop 44  //Emergency Stop Button
#define BUTTON_PIN_Reset 45        // Reset Button
#define BUTTON_PIN_7 46
#define BUTTON_PIN_8 47
#define BUTTON_PIN_9 48
#define BUTTON_PIN_10 49
#define BUTTON_PIN_11 50
#define BUTTON_PIN_12 51
#define BUTTON_PIN_13 52
#define BUTTON_PIN_14 53

#define PRESSURE_PIN_1 A15
#define PRESSURE_PIN_2 A14
#define PRESSURE_PIN_3 A13
#define PRESSURE_PIN_4 A12




#define pwm_pin  9


ThreadController controll = ThreadController();
Thread read_sensor_Thread = Thread();
MAX6675 exhaust1(CLK_PIN1 , Exhaust1_PIN, DO_PIN);
MAX6675 exhaust2(CLK_PIN1 , Exhaust2_PIN, DO_PIN);

// Use software SPI: CS, DI, DO, CLK
Adafruit_MAX31865 thermo1 = Adafruit_MAX31865(Thermocouple1_CS_PIN, SDI_PIN1_MAX31865, SDO_PIN1_MAX31865, CLK_PIN1_MAX31865);
Adafruit_MAX31865 thermo2= Adafruit_MAX31865(Thermocouple2_CS_PIN, SDI_PIN2_MAX31865, SDO_PIN2_MAX31865, CLK_PIN2_MAX31865);



#define LED_INDEX_Stop 0 
#define LED_INDEX_Start 1
#define LED_INDEX_Inc 2 
#define LED_INDEX_Dec 3
#define LED_INDEX_Emg_Stop 4
int _off_inc=0;
int _off_dec=0;
typedef struct struct_LED
{
  int pin;
  int index;
  bool state;
};
struct_LED LED_Pin[]={{LED_PIN_Stop, LED_INDEX_Stop,HIGH},
                      {LED_PIN_Start,LED_INDEX_Start,LOW},
                      {LED_PIN_Inc,LED_INDEX_Inc,LOW},
                      {LED_PIN_Dec,LED_INDEX_Dec,LOW},
                      {LED_PIN_Emg_Stop,LED_INDEX_Emg_Stop,LOW}                      
                      
                      
                      };

#define BUTTON_INDEX_Stop 0 
#define BUTTON_INDEX_Start 1
#define BUTTON_INDEX_Inc 2 
#define BUTTON_INDEX_Dec 3
#define BUTTON_INDEX_Emg_Stop 4
#define BUTTON_INDEX_Reset 5
typedef struct struct_KEY
{
  ezButton pin;
  int index;
  bool state;
};
struct_KEY KEY_Pin[]={{ezButton(BUTTON_PIN_Stop), BUTTON_INDEX_Stop,HIGH},
                      {ezButton(BUTTON_PIN_Start), BUTTON_INDEX_Start,LOW},
                      {ezButton(BUTTON_PIN_Inc), BUTTON_INDEX_Inc,LOW},
                      {ezButton(BUTTON_PIN_Dec), BUTTON_INDEX_Dec,LOW},
                      {ezButton(BUTTON_PIN_Emg_Stop), BUTTON_INDEX_Emg_Stop,LOW},
                      {ezButton(BUTTON_PIN_Reset), BUTTON_INDEX_Reset,LOW}
                    };
// ----------------------------------------------------------------------------------------------------



// bool KEY_State[]={LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW};
// int LED_Pin[]={LED_PIN_Stop, LED_PIN_Emg_Stop, LED_PIN_Dec, LED_PIN_Inc, LED_PIN_5, LED_PIN_Start};
int Pressure_Pin[]={PRESSURE_PIN_1,PRESSURE_PIN_2,PRESSURE_PIN_3,PRESSURE_PIN_4};

//----------------------------------------------------------------------------------------
void start(){
          LED_Pin[LED_INDEX_Start].state=HIGH;
          LED_Pin[LED_INDEX_Stop].state=LOW;  
          KEY_Pin[BUTTON_INDEX_Stop].state=LOW; 
          KEY_Pin[BUTTON_INDEX_Start].state=HIGH;
          analogWrite(pwm_pin,230);
          delay(1000);
          current_speed=initial_speed;          
          analogWrite(pwm_pin,current_speed);
          Serial.println("started");
}
void stop(){
          LED_Pin[LED_INDEX_Stop].state=HIGH;
          LED_Pin[LED_INDEX_Start].state=LOW;    
          KEY_Pin[BUTTON_INDEX_Start].state=LOW; 
          KEY_Pin[BUTTON_INDEX_Stop].state=HIGH;  
          analogWrite(pwm_pin,0);
        Serial.println("STOPPED");
}
// ----------------------------------------------------------------------------------------------------
void inc(){
    LED_Pin[LED_INDEX_Inc].state=HIGH; 
    KEY_Pin[BUTTON_INDEX_Inc].state=HIGH; 
    _off_inc=0;
    delay(50);
    Serial.println("INC");
    if (current_speed<over_speed)
    {
        current_speed+=3;
        analogWrite(pwm_pin,current_speed);
    }
    else
      Serial.println(" OVER SPEED");
    Serial.println(current_speed);
}
// ----------------------------------------------------------------------------------------------------
void dec(){
    LED_Pin[LED_INDEX_Dec].state=HIGH; 
    KEY_Pin[BUTTON_INDEX_Dec].state=HIGH; 
    _off_dec=0;
    delay(50);
    Serial.println("DEC");
    current_speed-=5;
    analogWrite(pwm_pin,current_speed);    
}
// ----------------------------------------------------------------------------------------------------
void off_inc()
{
  if ((_off_inc!=0)) 
  {
    LED_Pin[LED_INDEX_Inc].state=LOW; 
    KEY_Pin[BUTTON_INDEX_Inc].state=LOW;    
  }
  else
      _off_inc=1;
}
// ----------------------------------------------------------------------------------------------------
void off_dec()
{
  if ((_off_dec!=0)) 
  {
    LED_Pin[LED_INDEX_Dec].state=LOW; 
    KEY_Pin[BUTTON_INDEX_Dec].state=LOW;    
  }
  else
      _off_dec=1;

}
// ----------------------------------------------------------------------------------------------------
void emg_stop()
{
  LED_Pin[LED_INDEX_Stop].state = HIGH;
  LED_Pin[LED_INDEX_Start].state = LOW;
  LED_Pin[LED_INDEX_Emg_Stop].state=HIGH;
  KEY_Pin[BUTTON_INDEX_Emg_Stop].state=HIGH;
  KEY_Pin[BUTTON_INDEX_Reset].state=LOW;  

}
void reset()
{
  LED_Pin[LED_INDEX_Emg_Stop].state=LOW;
  KEY_Pin[BUTTON_INDEX_Emg_Stop].state=LOW;
  KEY_Pin[BUTTON_INDEX_Reset].state=HIGH;  
}
//-----------------------------------------------------------------------------------------------------
void copy(bool* src, bool* dst, int len) {
    memcpy(dst, src, sizeof(src[0])*len);
}
// ----------------------------------------------------------------------------------------------------

void set_pinmode()
{
  for (byte i = 0; i < BUTTON_NUM; i++) {
    KEY_Pin[i].pin.setDebounceTime(30); 
  }	
  for (byte i = 0; i < LED_NUM; i++) {
    pinMode(LED_Pin[i].pin,OUTPUT);
  }	  
  for (byte i = 0; i < PRESSURE_NUM; i++) {
	  pinMode(Pressure_Pin[i],INPUT);

  }	 
  pinMode(pwm_pin,OUTPUT);  
}
// ----------------------------------------------------------------------------------------------------
void init_buttons()
{
  for (byte i = 0; i < BUTTON_NUM; i++)
	KEY_Pin[i].pin.loop();
}
// ----------------------------------------------------------------------------------------------------
void read_buttons()
{
  for (byte i = 0; i < BUTTON_NUM; i++) {
    if (KEY_Pin[i].pin.isReleased()) {
      if (i==BUTTON_INDEX_Start)
      { 
        if (KEY_Pin[BUTTON_INDEX_Start].state)
          Serial.println("Invalid Key Pressed  -- START");
        else
        {
            start();
        }
      }
      else       if (i==BUTTON_INDEX_Stop)
      {
        if (KEY_Pin[BUTTON_INDEX_Stop].state)
          Serial.println("Invalid Key Pressed -- STOP");
        else
        {
          stop();
        }
      }
      else       if (i==BUTTON_INDEX_Inc)
      {
        if (KEY_Pin[BUTTON_INDEX_Inc].state)
          Serial.println("Invalid Key Pressed -- INC");
        else
        {
          inc();
        }
      }      
      else       if (i==BUTTON_INDEX_Dec)
      {
        if (KEY_Pin[BUTTON_INDEX_Dec].state)
          Serial.println("Invalid Key Pressed -- DEC");
        else
        {
          dec();
        }
      }       
      else       if (i==BUTTON_INDEX_Emg_Stop)
      {
        if (KEY_Pin[BUTTON_INDEX_Emg_Stop].state)
          Serial.println("Invalid Key Pressed -- Emg Stop");
        else
        {
          emg_stop();
        }
      } 
      else       if (i==BUTTON_INDEX_Reset)
      {
        if (KEY_Pin[BUTTON_INDEX_Reset].state)
          Serial.println("Invalid Key Pressed -- Reset");
        else
        {
          reset();
        }
      }              
    else
      KEY_Pin[i].state=!KEY_Pin[i].state;
    }
  }
}
// ----------------------------------------------------------------------------------------------------
void write_leds()
{
  for (byte i = 0; i < LED_NUM; i++) {
      digitalWrite(LED_Pin[i].pin,LED_Pin[i].state);

    }
}
// ----------------------------------------------------------------------------------------------------
void turn_on_lamp(int i)
{
	LED_Pin[i].state=HIGH;
}
// ----------------------------------------------------------------------------------------------------
void turn_off_lamp(int i)
{
	LED_Pin[i].state=LOW;
}
// ----------------------------------------------------------------------------------------------------
void toggle_lamp(int i)
{
	LED_Pin[i].state=!LED_Pin[i].state;
}

// ----------------------------------------------------------------------------------------------------
float read_tehermocouple(Adafruit_MAX31865 thermo)
{
  uint16_t rtd = thermo.readRTD();

  float ratio = rtd;
  ratio /= 32768;


  // // Check and print any faults
  // uint8_t fault = thermo.readFault();
  // if (fault) {
  //   Serial.print("Fault 0x"); Serial.println(fault, HEX);
  //   if (fault & MAX31865_FAULT_HIGHTHRESH) {
  //     Serial.println("RTD High Threshold"); 
  //   }
  //   if (fault & MAX31865_FAULT_LOWTHRESH) {
  //     Serial.println("RTD Low Threshold"); 
  //   }
  //   if (fault & MAX31865_FAULT_REFINLOW) {
  //     Serial.println("REFIN- > 0.85 x Bias"); 
  //   }
  //   if (fault & MAX31865_FAULT_REFINHIGH) {
  //     Serial.println("REFIN- < 0.85 x Bias - FORCE- open"); 
  //   }
  //   if (fault & MAX31865_FAULT_RTDINLOW) {
  //     Serial.println("RTDIN- < 0.85 x Bias - FORCE- open"); 
  //   }
  //   if (fault & MAX31865_FAULT_OVUV) {
  //     Serial.println("Under/Over voltage"); 
  //   }
  //   thermo.clearFault();
  // }
  // Serial.println();
  return thermo.temperature(RNOMINAL, RREF);
  // delay(1000);  
}
void read_sensors() {
  JSONVar sensors;
  float t1=read_tehermocouple(thermo1);
  float t2=read_tehermocouple(thermo2);
  // float t3=read_tehermocouple(thermo3);
  // float t4=read_tehermocouple(thermo4);
  // float t5=read_tehermocouple(thermo5);

  float t3=1;
  float t4=1;
  float t5=1;  
  // Making a JSON Object
  
  sensors["t"]["t1"] = t1;
  sensors["t"]["t2"] = t2;
  sensors["t"]["t3"] = t3;
  sensors["t"]["t4"] = t4;
  sensors["t"]["t5"] = t5;
  sensors["t"]["t8"] = random(1000);
  sensors["t"]["t9"] = random(1000);
  float c1=exhaust1.readCelsius();
  sensors["t"]["t6"] = c1;
    float c2=exhaust2.readCelsius();
  sensors["t"]["t7"] = c2;
 
    for (byte i = 0; i < PRESSURE_NUM; i++) {
		  float x=analogRead(Pressure_Pin[i]);
		 sensors["p"]["p"+String(i+1)] =x/50;
	}

 sensors["p"]["p1"] =random(1000);
 sensors["p"]["p1"] =random(1000); 
 sensors["p"]["p2"] =  random(1000);
 sensors["p"]["p3"] = random(1000);
 sensors["p"]["p4"] = random(1000);
  sensors["p"]["p5"] = random(1000);

  for (byte i = 0; i < BUTTON_NUM; i++) {
    char k[3];
	sensors["k"]["k"+String(i+1)] =KEY_Pin[i].state;
  }

  for (byte i = 0; i < LED_NUM; i++) {
	sensors["l"]["l"+String(i+1)] =LED_Pin[i].state;
  }



  Serial.println(sensors);
  delay(900);
}
// ----------------------------------------------------------------------------------------------------

void lamp_test_on()
{
	for (byte i=0;i<LED_NUM;i++)
		turn_on_lamp(i);
}
// ----------------------------------------------------------------------------------------------------

void lamp_test_off()
{
	for (byte i=0;i<LED_NUM;i++)
		turn_off_lamp(i);
}

