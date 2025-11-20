import RPi.GPIO as GPIO
import time

# GPIO pins to monitor (5 pins)
GPIO_PINS = [17, 27, 22, 23, 24]  # Adjust as needed

# Setup GPIO
GPIO.setmode(GPIO.BCM)
for pin in GPIO_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def read_pins_as_decimal():
    """Read 5 GPIO pins as binary and return decimal number"""
    value = 0
    for i, pin in enumerate(GPIO_PINS):
        if GPIO.input(pin):
            value += 1 << i  # Treat each pin as a bit
    return value  # Returns an integer (decimal)

try:
    print("Monitoring GPIO pins. Press Ctrl+C to exit.")
    while True:
        number = read_pins_as_decimal()
        print(f"Decimal value: {number}")
        time.sleep(0.1)  # Small delay
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
