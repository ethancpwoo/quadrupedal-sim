#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

#define SERVO_FREQ 50

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

int flag = 0;

uint8_t FLH = 14;
uint8_t FLT = 13;
uint8_t FLF = 12;

uint8_t FRH = 1;
uint8_t FRT = 2;
uint8_t FRF = 3;

uint8_t BLH = 11; 
uint8_t BLT = 10;
uint8_t BLF = 9;

uint8_t BRH = 4;
uint8_t BRT = 6;
uint8_t BRF = 5;

float x = 0;
float a = 0;
float b = 0;
float c = 0;
float d = 0; 
float e = 0;
float f = 0;
float g = 0;
float h = 0;


void setup() {
  Serial.begin(9600);
  pwm.begin();
  pwm.setOscillatorFrequency(27000000);
  pwm.setPWMFreq(SERVO_FREQ);
  delay(5);
}

void loop() {
  if(flag == 0) {
    if(Serial.available() > 0) {
      //Serial.println("Message is available");
      flag = 1;
      Serial.println("configed");
    }
    else {
      Serial.println("Nothing in buffer");
    }
  }
  else {

    Serial.flush();
    x = Serial.parseFloat();
    a = Serial.parseFloat();
    b = Serial.parseFloat();
    c = Serial.parseFloat();
    d = Serial.parseFloat();
    e = Serial.parseFloat();
    f = Serial.parseFloat();
    g = Serial.parseFloat();
    h = Serial.parseFloat();

    pwm.setPWM(FLH, 0, 282); 
    pwm.setPWM(FRH, 0, 281);
    pwm.setPWM(BLH, 0, 280);
    pwm.setPWM(BRH, 0, 280); //kept values

    pwm.setPWM(FLT, 0, a); // 315 (straight down) 488 (back)
    pwm.setPWM(FRT, 0, e); // 282 (straight down) 92 (back)
    pwm.setPWM(BLT, 0, c); // 88 (straight down) 280 (back)
    pwm.setPWM(BRT, 0, g); // 510 (straight down) 320 (back)

    pwm.setPWM(FLF, 0, b); // 282 (foot down) 100 (up)
    pwm.setPWM(FRF, 0, f); // 315 (foot down) 501 (up)
    pwm.setPWM(BLF, 0, d); // 320 (foot down) 120 (up)
    pwm.setPWM(BRF, 0, h); // 305 (foot down) 491 (up)
  }
}