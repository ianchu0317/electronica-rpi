// Definición de pines
const byte pinLed = 11;
const byte pinButton = 2;
const int delay_t = 10;

bool ledFading = false;  // Indica si el LED está en proceso de fade
unsigned long lastUpdate = 0;
int brightness = 0;
int fadeStep = 5;
bool lastButtonState = LOW; // Estado anterior del botón

void setup() {
  Serial.begin(9600);
  pinMode(pinLed, OUTPUT);
  pinMode(pinButton, INPUT);  // Se mantiene INPUT porque usas pull-down externo
}

void loop() {
  bool button_state = digitalRead(pinButton);  // Con pull-down, HIGH significa presionado

  // Detectar cuando el botón pasa de LOW a HIGH (flanco de subida)
  if (button_state && !lastButtonState) {
    ledFading = true;  // Iniciar el fade solo una vez por pulsación
  }
  lastButtonState = button_state;

  if (ledFading) {
    fadeNonBlocking();
  }

  Serial.println(button_state);
  delay(50);  // Pequeño debounce
}

void fadeNonBlocking() {

  analogWrite(pinLed, brightness);
  brightness += fadeStep;
  if (brightness >= 255 || brightness <= 0) {
    fadeStep = -fadeStep;  // Cambia la dirección del fade
  }

  if (brightness == 0) {
    ledFading = false;  // Detener la animación cuando el LED esté completamente apagado
  }

}
