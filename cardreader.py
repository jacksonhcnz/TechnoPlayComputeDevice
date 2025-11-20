import RPi.GPIO as GPIO
import time

# Example: use pins 17, 27, 22, 23 (4-bit number)
PINS = [17, 27, 22, 23, 24]

def setup():
    GPIO.setmode(GPIO.BCM)   # use Broadcom pin numbering
    for pin in PINS:
        GPIO.setup(pin, GPIO.out, pull_up_down=GPIO.PUD_DOWN)

def read_binary_to_decimal():
    value = 0
    for i, pin in enumerate(reversed(PINS)):
        bit = GPIO.input(pin)
        value |= (bit << i)   # set bit i if pin is HIGH
    return str(value)

if __name__ == "__main__":
    try:
        setup()
        while True:
            number_str = read_binary_to_decimal()
            print("Decimal value:", number_str)
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
