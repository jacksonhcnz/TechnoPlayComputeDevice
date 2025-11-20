import RPi.GPIO as GPIO
import time

# List of GPIO pins to monitor
GPIO_PINS = [17, 27, 22, 23, 24]  # Adjust as needed

# Setup GPIO
GPIO.setmode(GPIO.BCM)
for pin in GPIO_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Pull-down ensures default LOW

def read_pins():
    """Read GPIO pins and return decimal and binary"""
    value = 0
    for i, pin in enumerate(GPIO_PINS):
        if GPIO.input(pin):
            value += 1 << i  # Treat each pin as a bit
    binary_str = format(value, '05b')  # Format as 5-bit binary string
    return value, binary_str

last_value = None
try:
    print("Monitoring GPIO pins. Press Ctrl+C to exit.")
    while True:
        decimal_value, binary_value = read_pins()
        if decimal_value != last_value:  # Only print when value changes
            print(f"Decimal: {decimal_value}, Binary: {binary_value}")
            last_value = decimal_value
        time.sleep(0.1)  # Small delay
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
