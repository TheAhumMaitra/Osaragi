import random
from textual import on
from textual.app import App, ComposeResult, RenderResult, ModeError
from textual.widgets import Header, Footer, Button, Label, Input ,Static, Collapsible, Sparkline, Tabs, Markdown, Rule
from textual.widget import Widget
from textual.containers import ScrollableContainer

class AddTask(Static):
    def compose(self) -> ComposeResult:
        yield Label("Add a task")
        yield Rule(line_style="heavy")
        yield Input(placeholder="Write your task name......",id="task_input")
        yield Button("[b]Add task[/b]",variant="success", id="add_task")
        yield Button("[b]Reset[/b]",variant="error",id="reset_task")

class ShowTask(Static):
    pass



class Welcome(Widget):
    def render(self) -> RenderResult:
        return "[b]Hello, World! Welcome to [yellow italic underline bold]Osaragi[/yellow italic underline bold]. An advanced TUI Todo List App. 100% free and 100% open source [/b]"


class HelpPanel(ScrollableContainer):
    """A sidebar panel for help information."""
    def compose(self) -> ComposeResult:
        # Use classes for styling the title later in CSS
        yield Label("Osaragi Help", classes="help_title")
        yield Rule(line_style="heavy")
        yield Label("Version : 1.0.0")
        yield Label("[b]Hello, World! Welcome to [yellow italic underline bold]Osaragi[/yellow italic underline bold]. An advanced TUI Todo List App. 100% free and 100% open source [/b]")
        yield Label("[b underline yellow]Github[/b underline yellow] : https://github.com/TheAhumMaitra/Osaragi")
        yield Label("ID : U38YQ3HTH395H98H395HY35Y")
        yield Label("Developer : Ahum Maitra")
        yield Label("License: MIT")
        yield Label("[b yellow]Press 'h' to close the help panel[/b yellow]")

class Osaragi(App):
    CSS_PATH = "style.tcss"
    BINDINGS = [
        ("^q", "request_quit", "Quit"),
        ("h","toggle_help_panel","Help Panel")
    ]
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Tabs("[bold]Tasks[/bold]")
        yield Footer()

        yield HelpPanel(id="help_panel_sidebar", classes="hidden")

        yield ScrollableContainer(
            Welcome(),
            Rule(line_style="heavy"),
            AddTask(),
            Label("[yellow b underline]Tasks[/yellow b underline]",id="task_text"),
            ShowTask(id="show_task")
        )
    def action_toggle_help_panel(self) -> None:
        """Toggles the visibility of the help panel sidebar."""
        help_panel = self.query_one("#help_panel_sidebar")
        help_panel.toggle_class("hidden")

    @on(Button.Pressed, "#add_task")
    @on(Input.Submitted, "#task_input")
    def handle_tasks(self):
        user_typed_input = self.query_one("#task_input")
        task_list = self.query_one("#show_task",ShowTask)
        task_text = user_typed_input.value.strip()

        if task_text:
            task_list.mount(Label(f"[b]{task_text}[/b]"))

        user_typed_input.clear()

    @on(Button.Pressed, "#reset_task")
    def reset_task(self):
        task_container = self.query_one("#show_task", ShowTask)
        task_container.remove_children()



if __name__ == "__main__":
    app = Osaragi()
    app.run()
