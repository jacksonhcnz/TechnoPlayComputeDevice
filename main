
from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.events import Key
from textual.timer import Timer
from textual.containers import Horizontal
from datetime import datetime
import subprocess


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


class ClockLabel(Static):
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

    #top-bar {
        dock: top;
        height: 3;
        padding: 0 1;
        align-horizontal: right;
    }

    #clock {
        color: white;
    }
    """

    def compose(self) -> ComposeResult:
        # Top-right bar with "System time: HH:MM:SS"
        yield Horizontal(ClockLabel(id="clock"), id="top-bar")
        yield SpinnerText()

    def on_key(self, event: Key) -> None:
        key = event.key.upper()

        script_map = {
            "A": "python script_a.py",
            "B": "python script_b.py",
            "C": "python script_c.py",
        }

        if key in script_map:
            self.run_script(script_map[key])

    def run_script(self, command: str) -> None:
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            self.log(f"Error running script: {e}")


if __name__ == "__main__":
    GameCardApp().run()
