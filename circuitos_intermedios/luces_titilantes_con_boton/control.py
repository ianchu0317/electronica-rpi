# -*- coding: cp1252 -*-
import RPi.GPIO as GPIO
import time
from random import choice


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# setup LED 
led_pin = [14, 15, 18, 23, 24]  # RPI BCM PIN
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)


# exit program
def finish_program(channel):
	global RUN
	print("Button pressed !!!")
	RUN = False 


# pin button configuration -> function to stop program
pin_button = 17  # RPI BCM PIN 17
GPIO.setup(pin_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
RUN = True
GPIO.add_event_detect(pin_button, GPIO.FALLING, callback=finish_program)


# turn all LED ON
def all_led_on():
	GPIO.output(led_pin, GPIO.HIGH)


# turn all LED OFF
def all_led_off():
	GPIO.output(led_pin, GPIO.LOW)


# turn led one at the time
def zig_zag_led():
	all_led_off()
	for led in led_pin:
		GPIO.output(led, GPIO.HIGH)
		time.sleep(0.06)
		GPIO.output(led, GPIO.LOW)

	for led in reversed(led_pin):
		GPIO.output(led, GPIO.HIGH)
		time.sleep(0.06)
		GPIO.output(led, GPIO.LOW)


# turn led off one at the time
def zig_zag_led_reverse():
	all_led_on()
	for led in led_pin:
		GPIO.output(led, GPIO.LOW)
		time.sleep(0.06)
		GPIO.output(led, GPIO.HIGH)

	for led in reversed(led_pin):
		GPIO.output(led, GPIO.LOW)
		time.sleep(0.06)
		GPIO.output(led, GPIO.HIGH)


# random light up
def random_led():
	all_led_off()
	for _ in range(300):
		led = choice(led_pin)
		GPIO.output(led, GPIO.HIGH)
		time.sleep(0.03)
		GPIO.output(led, GPIO.LOW)


# shine led alternatively
def trident_led():
    all_led_off()
    for led_index in range(len(led_pin)):
        if led_index%2 == 0:
            GPIO.output(led_pin[led_index], GPIO.HIGH)
    time.sleep(0.5)
    for led_index in range(len(led_pin)):
        if led_index%2 != 0:
            GPIO.output(led_pin[led_index], GPIO.HIGH)
        else:
            GPIO.output(led_pin[led_index], GPIO.LOW)
    time.sleep(0.5)


# main loop
def main():
	while RUN:
		# 3 times zig-zag
		for i in range(4):
			zig_zag_led()
		# 3 times all-on-off
		for i in range(3):
			all_led_on()
			time.sleep(0.5)
			all_led_off()
			time.sleep(0.5)
		## 3 times reverse zig-zag
		for i in range(4):
			zig_zag_led_reverse()
		# 3 times all-on-off
		for i in range(3):
			all_led_on()
			time.sleep(0.5)
			all_led_off()
			time.sleep(0.5)
		# alternar de a 3
		for i in range(3):
                        trident_led()
	
		# random led light up
		# random_led()

if __name__ == "__main__":
	main()

print('Cleaning GPIO state..')
GPIO.cleanup()
