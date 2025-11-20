import RPi.GPIO as GPIO
import time

# Pins we want to monitor
PINS = [17, 27, 22, 23, 24]

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in PINS:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def loop():
    print("Monitoring GPIO pins. Press CTRL+C to quit.")
    while True:
        status_list = []
        for pin in PINS:
            val = GPIO.input(pin)
            status_list.append(val)

        # Print individual pin states
        print("Pin states:", " ".join([f"{pin}:{val}" for pin, val in zip(PINS, status_list)]))

        time.sleep(0.2)  # Polling speed

def cleanup():
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        cleanup()
