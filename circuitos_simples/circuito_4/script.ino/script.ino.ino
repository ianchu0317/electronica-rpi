
int led = 12; // Definir pin de led 

void setup() {
  // Configurar led como salida
  pinMode(led, OUTPUT);

}

void loop() {
  digitalWrite(led, HIGH);  // Prender led
  delay(500);                      // Esperar medio segundo

  digitalWrite(led, LOW);   // Apagar led
  delay(500);  // Esperar medio segundo
}
