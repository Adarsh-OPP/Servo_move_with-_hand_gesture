#include <Servo.h>

Servo s1;
Servo s2;
int x = 0;

void setup() {
  s1.attach(3);           
  s2.attach(5);           
  Serial.begin(9600);     
}

void loop() {    
if (Serial.available()) {
  x = Serial.parseInt();

  if (x >= 0 && x <= 180) {
    s1.write(x);
  }
  else if (x >= 181 && x <= 361) {
    s2.write(x-181);
  }
}

 
}
