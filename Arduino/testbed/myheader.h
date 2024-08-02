const int initial_speed = 120;
const int pwm_pin = 9;
float current_speed = 0;
void set_speed(float val){
  float speed = initial_speed + val;
  analogWrite(pwm_pin,speed);
  
  current_speed = speed;
  Serial.println(current_speed);
}