#include <Servo.h>

// create an object
Servo myServo;

void setup() {
  myServo.attach(5);
}

void loop() {
  
  for(int i=0;i<=180;i++) {
    myServo.write(i); // 0 .... 180
    delay(10);
  }
  
  for(int i=180;i>=0;i--) {
    myServo.write(i); // 180 .... 0
    delay(10);
  }  
}
