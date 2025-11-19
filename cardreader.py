import time
import RPi.GPIO as GPIO
import keyboard  # You might need to install this via `pip install keyboard`

# Example GPIO pins used
GPIO_PINS = [17, 27, 22, 23, 24]  # Replace with your actual pins

# Set up GPIO
GPIO.setmode(GPIO.BCM)
for pin in GPIO_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def read_gpio_number():
    """Read GPIO pins as bits and return decimal number"""
    value = 0
    for i, pin in enumerate(GPIO_PINS):
        if GPIO.input(pin):
            value += 1 << i  # Set the bit
    return value

try:
    print("Reading GPIO. Press 'q' to quit.")
    while True:
        number = read_gpio_number()
        print(f"Read number: {number}")
        time.sleep(0.1)  # Small delay
        if keyboard.is_pressed('q'):  # Quit shortcut
            print("Quit key pressed. Exiting...")
            break
finally:
    GPIO.cleanup()
