import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# PWM PIN CONFIG
# pwm properties 
channel = 12  # PIN BCM 12
freq = 60  # Hz
# setup pin 
GPIO.setup(channel, GPIO.OUT)
p = GPIO.PWM(channel, freq)
p.start(1)  # dc = 1

try:
	while True:
		# alternating dc
		for dc in range(1, 101, 1):
			p.ChangeDutyCycle(dc)
			# print(dc)
			time.sleep(0.005)
		for dc in range(100, -1, -1):
			p.ChangeDutyCycle(dc)
			# print(dc)
			time.sleep(0.005)

except KeyboardInterrupt:
	pass

p.stop()
print("Cleaning GPIO...")
GPIO.cleanup()