import RPi.GPIO as GPIO
import time

# GPIO pins (bit order: MSB → LSB)
PINS = [17, 27, 22, 23, 24]

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in PINS:
        GPIO.setup(pin, GPIO.IN)   # no pull-up/down

def read_bits():
    """Return list of bits [b4 b3 b2 b1 b0]."""
    return [GPIO.input(pin) for pin in PINS]

def bits_to_decimal(bits):
    """Convert list of bits into decimal integer."""
    value = 0
    for bit in bits:
        value = (value << 1) | bit
    return value

if __name__ == "__main__":
    try:
        setup()
        last_value = None

        while True:
            bits = read_bits()
            dec = bits_to_decimal(bits)

            if dec != last_value:
                bit_string = "".join(str(b) for b in bits)
                print(f"Bits: {bit_string}   Decimal: {dec}")
                last_value = dec

            time.sleep(0.05)

    except KeyboardInterrupt:
        GPIO.cleanup()
