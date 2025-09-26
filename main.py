from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.timer import Timer
from datetime import datetime
import subprocess
import pygame


# Example variable
cardnumber = "1234"


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


class GameCardApp(App):
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
    """

    def compose(self) -> ComposeResult:
        yield Clock(id="clock")
        yield SpinnerText()

    def on_mount(self) -> None:
        """Start monitoring joystick only while TUI is active."""
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
        """Stop monitoring when app closes or loses focus."""
        if hasattr(self, "joy_timer"):
            self.joy_timer.stop()
            self.log("Gamepad monitoring stopped")

    def check_gamepad(self) -> None:
        global cardnumber
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                # "Start" button is usually index 7
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
