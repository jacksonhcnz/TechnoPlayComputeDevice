import RPi.GPIO as GPIO
import time

PINS = [17, 27, 22, 23, 24]

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in PINS:
        GPIO.setup(pin, GPIO.IN)   # no pull-up/down

def read_bits():
    """Return list of inverted bits so idle = 0."""
    return [1 - GPIO.input(pin) for pin in PINS]  # invert each bit

def bits_to_decimal(bits):
    value = 0
    for bit in bits:
        value = (value << 1) | bit
    return value

if __name__ == "__main__":
    try:
        setup()
        last = None
        while True:
            bits = read_bits()
            dec = bits_to_decimal(bits)
            if dec != last:
                print("Bits:", "".join(str(b) for b in bits), " Decimal:", dec)
                last = dec
            time.sleep(0.05)
    except KeyboardInterrupt:
        GPIO.cleanup()
