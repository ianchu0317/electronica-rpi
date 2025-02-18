#include <Servo.h>

Servo myservo;

void setup() {
  myservo.attach(9); 
}

void loop() {
  for (int i = 30; i <= 180; i++) {
    myservo.write(i);
    delay(10);
  }
  
  for (int i = 180; i >= 30; i--){
    myservo.write(i);
    delay(10);
  }
}
