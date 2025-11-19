# Updated main.py with GPIO reading, displaying value, and gamepad list

from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.timer import Timer
from datetime import datetime
import subprocess
import pygame
import RPi.GPIO as GPIO

# GPIO pins to read
INPUT_PINS = [5, 6, 13, 19]  # Example GPIO pins representing bits

# Setup GPIO
GPIO.setmode(GPIO.BCM)
for pin in INPUT_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

cardnumber = 0


class SpinnerText(Static):
    def __init__(self) -> None:
        super().__init__()
        self.spinner_chars = ["|", "/", "—", "\\"]
        self.index = 0
        self.base_text = "Insert game card"
        self.spinner_timer: Timer | None = None

    def on_mount(self) -> None:
        self.spinner_timer = self.set_interval(0.1, self.update_spinner)

    def update_spinner(self) -> None:
        spin = self.spinner_chars[self.index]
        self.index = (self.index + 1) % len(self.spinner_chars)
        self.update(f"{self.base_text} {spin}")


class Clock(Static):
    def on_mount(self) -> None:
        self.set_interval(1, self.update_time)

    def update_time(self) -> None:
        now = datetime.now().strftime("%H:%M:%S")
        self.update(f"System time: {now}")


class DecimalDisplay(Static):
    """Shows the decimal value generated from GPIO bits."""
    def on_mount(self) -> None:
        self.set_interval(0.2, self.update_value)

    def update_value(self) -> None:
        global cardnumber
        bits = [GPIO.input(pin) for pin in INPUT_PINS]
        value = 0
        for i, bit in enumerate(reversed(bits)):
            value |= (bit << i)
        cardnumber = value
        self.update(f"Card Number: {cardnumber}")


class GamepadList(Static):
    """Top-right list of all connected gamepads."""
    def on_mount(self) -> None:
        self.set_interval(1, self.refresh_gamepads)

    def refresh_gamepads(self) -> None:
        pygame.joystick.quit()
        pygame.joystick.init()
        count = pygame.joystick.get_count()

        if count == 0:
            self.update("Gamepads: None")
            return

        names = []
        for i in range(count):
            js = pygame.joystick.Joystick(i)
            js.init()
            names.append(js.get_name())

        listing = "\n".join(names)
        self.update(f"Gamepads (Connected):\n{listing}")


class GameCardApp(App):
    BINDINGS = [("q", "quit_app", "Quit")]
    CSS = """
    Screen {
        align: center middle;
        background: black;
    }

    SpinnerText {
        text-align: center;
        color: white;
        content-align: center middle;
    }

    #clock {
        dock: top;
        align-horizontal: right;
        padding: 1 2;
        color: white;
    }

    #decimal_display {
        dock: bottom;
        align-horizontal: right;
        padding: 1 2;
        color: yellow;
    }

    #gamepad_list {
        dock: top;
        align-horizontal: right;
        padding: 1 2;
        color: cyan;
    }
    }
    """

        def action_quit_app(self):
        self.exit()

    def compose(self) -> ComposeResult:
        yield Clock(id="clock")
        yield GamepadList(id="gamepad_list")
        yield DecimalDisplay(id="decimal_display")
        yield SpinnerText()

    def on_mount(self) -> None:
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            self.joy_timer = self.set_interval(0.1, self.check_gamepad)
            self.log("Gamepad monitoring enabled")
        else:
            self.log("No joystick detected")

    def on_unmount(self) -> None:
        if hasattr(self, "joy_timer"):
            self.joy_timer.stop()
            self.log("Gamepad monitoring stopped")

    def check_gamepad(self) -> None:
        global cardnumber
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 7:
                    script_name = f"{cardnumber}.py"
                    self.run_script(f"python3 {script_name}")

    def run_script(self, command: str) -> None:
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            self.log(f"Error running script: {e}")


if __name__ == "__main__":
    GameCardApp().run()
