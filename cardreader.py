import RPi.GPIO as GPIO

def read_gpio_as_decimal(pins):
    """
    Reads the given GPIO pins, interprets them as bits of a binary number,
    and returns the decimal value as a string.

    Args:
        pins (list[int]): List of GPIO pin numbers (BCM mode). 
                          The first element is the MSB, the last is the LSB.

    Returns:
        str: Decimal string of the binary value.
    """
    GPIO.setmode(GPIO.BCM)

    # Setup pins as input with pulldown
    for pin in pins:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Read bits from pins
    value = 0
    for i, pin in enumerate(reversed(pins)):  # last pin is LSB
        bit = GPIO.input(pin)
        value |= (bit << i)

    GPIO.cleanup()
    return str(value)


# Example usage
pins = [17, 27, 22, 23, 24]   # adjust to your wiring
cardnumber = read_gpio_as_decimal(pins)
print("Card number:", cardnumber)
