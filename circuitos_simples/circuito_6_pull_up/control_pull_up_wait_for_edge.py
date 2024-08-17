import RPi.GPIO as GPIO
import time

# configurar programa
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# configurar pin
PIN = 18
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def press():
	print("Interruptor presionado !")


# waiting event
GPIO.wait_for_edge(PIN, GPIO.FALLING)
press()

# Salida del programa
print("Limpiando GPIO")
GPIO.cleanup()

print("Saliendo del programa...")
exit()
