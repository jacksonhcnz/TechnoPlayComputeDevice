import RPi.GPIO as GPIO
import time

PINS = [17, 27, 22, 23, 24]

GPIO.setmode(GPIO.BCM)
for pin in PINS:
    GPIO.setup(pin, GPIO.IN)   # NO pull-up/down

try:
    while True:
        bits = [GPIO.input(p) for p in PINS]
        print(bits)
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
