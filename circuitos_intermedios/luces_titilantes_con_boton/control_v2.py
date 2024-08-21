# -*- coding: cp1252 -*-
import RPi.GPIO as GPIO
import time
from random import choice


# general GPIO setting
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


# exit program
def callback_button(channel):
	global RUN
	global seq_counter

	print("Button pressed !!!")
	if seq_counter + 1 < len(seq_list):
		seq_counter += 1
	else:
		seq_counter = 0
	print("Change to sequence ", seq_counter)
	#RUN = False 


# turn all LED ON
def all_led_on():
	GPIO.output(led_pin, GPIO.HIGH)


# turn all LED OFF
def all_led_off():
	GPIO.output(led_pin, GPIO.LOW)


# turn one led at the time
def run_wave_effect():
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
def run_wave_effect_reverse():
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
def run_random_led(times):
	all_led_off()
	for _ in range(times):
		led = choice(led_pin)
		GPIO.output(led, GPIO.HIGH)
		time.sleep(0.05)
		GPIO.output(led, GPIO.LOW)


# turn on led alternatively
def alternate_triple_leds():
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


# transition sequence
def run_transition():
	for i in range(3):
		all_led_on()
		time.sleep(0.5)
		all_led_off()
		time.sleep(0.5)


# LEDS pinouts setting 
led_pin = [14, 15, 18, 23, 24]  # RPI BCM PIN
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

# pin button configuration to stop program
pin_button = 17  # RPI BCM PIN 17
GPIO.setup(pin_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(pin_button, GPIO.FALLING, callback=callback_button, bouncetime=200)

# program setting
RUN = True
seq_list = [run_wave_effect, run_wave_effect_reverse, alternate_triple_leds, run_transition]  # all sequences
seq_counter = 0


# main loop
def main():
	try:
		while RUN:
			seq_list[seq_counter]()
	# exit loop
	except KeyboardInterrupt:
		print("Exit program !")
		pass

if __name__ == "__main__":
	main()

print('Cleaning GPIO state..')
GPIO.cleanup()
