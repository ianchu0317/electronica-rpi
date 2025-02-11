
// definir pines para ultrasonico
byte echo_pin = 13;
byte trig_pin = 12;


void setup() {
  pinMode(echo_pin, INPUT);
  pinMode(trig_pin, OUTPUT);

  digitalWrite(trig_pin, LOW);

  Serial.begin(9600);     // para output
}


void loop() {
  // enviar pulso con trig
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(10);    // 10 us
  digitalWrite(trig_pin, LOW);

  // recibir pulso con echo
  unsigned long t = pulseIn(echo_pin, HIGH);  
  
  // obtener distancia con tiempo
  long d = t/59;
  
  // output
  Serial.print(d);
  Serial.print(" cm ");
  Serial.println();
  
  delay(100);
}

int getDistanceFromTime(unsigned long pulse_time) {
  const int sound_vel = 0.3432; // cm/us
  int distance = sound_vel * pulse_time / 2;
  return distance;
}