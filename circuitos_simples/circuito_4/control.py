import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

led = 12
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.HIGH)


GPIO.cleanup()
