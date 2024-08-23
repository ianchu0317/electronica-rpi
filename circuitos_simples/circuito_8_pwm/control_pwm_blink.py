import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# PWM PIN CONFIG
# pwm properties 
channel = 12  # PIN BCM 12
freq = 0.5  # Hz
dc = 50  # %
# setup pin 
GPIO.setup(channel, GPIO.OUT)
p = GPIO.PWM(channel, freq)
p.start(dc)

input("Running program...")

print("Cleaning GPIO...")
p.stop()
GPIO.cleanup()