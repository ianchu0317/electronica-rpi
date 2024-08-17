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
GPIO.add_event_detect(PIN, GPIO.FALLING, callback=press, bouncetime=500)

print("Esperando 10s")
time.sleep(10)

print("Limpiando GPIO")
GPIO.cleanup()
