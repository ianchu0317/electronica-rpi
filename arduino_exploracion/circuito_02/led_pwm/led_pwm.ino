// set pin numbers
byte pinLed = 11;
int delay_t = 5;

void setup() {
  // put your setup code here, to run once:
  pinMode(pinLed, OUTPUT);
}

void loop() {
  // turn on led
  for (int i = 0; i < 255; i++){
    analogWrite(pinLed, i);
    delay(delay_t); 
  }
  // turn off led
  for (int i = 255; i > 0; i--){
    analogWrite(pinLed, i);
    delay(delay_t); 
  }
}
