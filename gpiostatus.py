import RPi.GPIO as GPIO
import time

PINS = [17, 27, 22, 23, 24]

GPIO.setmode(GPIO.BCM)

# Try pull-ups for testing
for pin in PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

prev = [None] * len(PINS)

print("Monitoring GPIO… (CTRL+C to quit)")

try:
    while True:
        states = [GPIO.input(pin) for pin in PINS]

        # Only print when there is a change
        if states != prev:
            print(" ".join([f"{pin}:{val}" for pin, val in zip(PINS, states)]))
            prev = states

        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
