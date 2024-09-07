import RPi.GPIO as GPIO
from time import sleep


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

en_1_ch = 12 # pwm pin
in_1 = 23
in_2 = 24

# config GPIO
GPIO.setup(en_1_ch, GPIO.OUT)
en_1 = GPIO.PWM(en_1_ch, 500)  # 500 Hz
GPIO.setup(in_1, GPIO.OUT)
GPIO.setup(in_2, GPIO.OUT)
en_1.start(40) # 50% dc

def turn_1():
	GPIO.output(in_1, GPIO.HIGH)
	GPIO.output(in_2, GPIO.LOW)
	print("F1 called")

def turn_2():
	GPIO.output(in_1, GPIO.LOW)
	GPIO.output(in_2, GPIO.HIGH)
	print("F2 called")


for x in range(3):
	turn_1()
	sleep(2)
	turn_2()
	sleep(2)


print("Limpiando GPIO...")
en_1.stop()
GPIO.cleanup()