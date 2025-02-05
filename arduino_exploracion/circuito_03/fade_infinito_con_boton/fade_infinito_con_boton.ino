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
    ledFading = !ledFading;  // Iniciar o detener fade
  }
  lastButtonState = button_state;

  fadeNonBlocking();

  Serial.println(button_state);
  delay(50);  // Pequeño debounce
}

void fadeNonBlocking() {
  // Correr fade solo si se oprime botón
  if (ledFading){
    brightness += fadeStep;
    if (brightness >= 255 || brightness <= 0) {
      fadeStep = -fadeStep;  // Cambia la dirección del fade
    }
  } 
  // Detener fade si se oprime de nuevo el boton
  else {
    brightness = 0;
    ledFading = false;
    fadeStep = 5;
  }
  analogWrite(pinLed, brightness);
}
