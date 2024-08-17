import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pin_button = 18  # BCM PIN 18
GPIO.setup(pin_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# 10s for press button
GPIO.wait_for_edge(pin_button, GPIO.RISING, timeout=5000) 


print("Saliendo del programa...")
GPIO.cleanup()
