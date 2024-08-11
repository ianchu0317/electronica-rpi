import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_R = 15
LED_G = 18
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)

try:
	while True:
		GPIO.output(LED_R, GPIO.HIGH)
		GPIO.output(LED_G, GPIO.LOW)
		time.sleep(1)
		GPIO.output(LED_R, GPIO.LOW)
		GPIO.output(LED_G, GPIO.HIGH)
		time.sleep(1)
except KeyboardInterrupt:
	print("quittting...")

GPIO.cleanup()
