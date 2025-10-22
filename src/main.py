from textual.app import App, ComposeResult, RenderResult
from textual.widgets import Header, Footer, Button, Label, Input ,Static
from textual.widget import Widget
from textual.containers import ScrollableContainer

class AddTask(Static):
    def compose(self) -> ComposeResult:
        yield Label("Add a task")
        yield Input(placeholder="Write your task name......",valid_empty=False)
        yield Button("[b]Add task[/b]",variant="success")
        yield Button("[b]Reset[/b]",variant="error")

class Welcome(Widget):
    def render(self) -> RenderResult:
        return "[b]Hello, World! Welcome to [yellow italic]Osaragi[/yellow italic]. An advanced TUI Todo List App. 100% free and 100% open source [/b]"

class TodoListApp(App):

    BINDINGS = [
        ("D","toggle_dark_mode","Toggle Dark Mode")
        ]

    CSS_PATH = "style.tcss"
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        
        yield ScrollableContainer(
            Welcome(),
            AddTask(),
        )

    def toggle_dark_mode(self) -> None:
        self.dark = not self.dark

if __name__ == "__main__":
    app = TodoListApp()
    app.run()
