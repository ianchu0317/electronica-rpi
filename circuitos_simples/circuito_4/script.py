# Importar paquetes
import RPi.GPIO as GPIO
import time

# Configurar modo de enumeracion de pines
GPIO.setmode(GPIO.BOARD)

# Configurar pin 12 físico como salida
led = 12
GPIO.setup(led, GPIO.OUT)

# Titilar cada 1 segundo (total 10 veces)
try:
	for x in range(10):
		GPIO.output(led, GPIO.HIGH)
		print('led on')
		time.sleep(1)
		GPIO.output(led, GPIO.LOW)
		print('led off')
		time.sleep(1)
except KeyboardInterrupt:
	print('quittting...')
	pass

# Limpiar salida de pines
GPIO.cleanup()
