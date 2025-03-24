from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, ListView, ListItem, Label, Button, Input
from textual.containers import Container
from textual.reactive import reactive
from textual.worker import Worker
import os
import sys

sys.path.append(os.path.dirname(__file__))
sys.path.append(r'D:\wallpaper-cli-tool\src')

from pexels_api import fetch_image as fetch_image_pexels
from wallpaper_setter import set_wallpaper, set_previous_wallpaper, get_wallpaper_history

PREDEFINED_QUERIES = [
    "Nature", "City", "Space", 
    "Mountains", "Beach", "Abstract",
    "Minimalist", "Animals","Spirituality", "Technology",
    "Art", "Music", "Food", "Travel",
    "Cars", "Sports", "Fitness", "Fashion"
]

class WallpaperTUI(App):
    CSS_PATH = "tui_style.css"
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("s", "set_wallpaper", "Set Wallpaper"),
        ("h", "list_history", "List History"),
        ("p", "set_previous", "Set Previous")
    ]

    current_image = reactive("")
    status_message = reactive("")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Container(
            ListView(id="query_list"),
            id="left-panel"
        )
        yield Container(
            Static(id="preview", classes="box"),
            Static(id="status", classes="box"),
            Input(placeholder="Enter query or history index", id="main_input"),
            Input(placeholder="Monitor Number", id="monitor", value="0"),
            Button("Fetch", id="fetch_btn"),
            id="right-panel"
        )

    def on_mount(self) -> None:
        list_view = self.query_one("#query_list", ListView)
        for query in PREDEFINED_QUERIES:
            list_view.append(ListItem(Label(f"🌄 {query}")))

    async def action_list_history(self) -> None:
        history = get_wallpaper_history()
        if not history:
            self.status_message = "[red]❌ No history found"
        else:
            history_list = "\n".join([f"{idx}: {os.path.basename(path)}" for idx, path in enumerate(history)])
            self.query_one("#preview").update(
                f"[bold]Wallpaper History:[/]\n{history_list}\n\n"
                "[dim]To set from history:\n"
                "1. Enter index number in the input field below\n"
                "2. Press 'p'[/dim]"
            )
            self.status_message = "[green]✅ History loaded"

    async def action_set_previous(self) -> None:
        try:
            history = get_wallpaper_history()
            print(f"History: {history}")  # Debugging

            if not history:
                self.status_message = "[red]❌ No history available"
                return

            input_val = self.query_one("#main_input").value.strip()
            print(f"Input Value: {input_val}")  # Debugging

            if not input_val.isdigit():
                self.status_message = "[red]❌ Please enter a valid history index"
                return

            index = int(input_val)
            print(f"Index: {index}")  # Debugging

            if index < 0 or index >= len(history):
                self.status_message = f"[red]❌ Index must be 0-{len(history)-1}"
                return

            monitor_num = int(self.query_one("#monitor").value)
            print(f"Monitor Number: {monitor_num}")  # Debugging

            success = set_previous_wallpaper(index, monitor_num)
            print(f"Set Previous Wallpaper Success: {success}")  # Debugging
            
            if success:
                self.current_image = history[index]
                self.query_one("#preview").update(
                    f"[bold]Current:[/]\n{os.path.basename(self.current_image)}\n"
                    f"[dim]From history index: {index}"
                )
                self.status_message = f"[green]✅ Set from history (index {index})"
            else:
                self.status_message = "[red]❌ Failed to set wallpaper"
        except Exception as e:
            self.status_message = f"[red]⚠️ Error: {str(e)}"

    async def on_list_view_selected(self, event: ListView.Selected) -> None:
        query = event.item.children[0].renderable.strip("🌄 ")
        self.query_one("#main_input").value = query
        await self.fetch_wallpaper(query)

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "fetch_btn":
            query = self.query_one("#main_input").value
            if query:
                await self.fetch_wallpaper(query)
            else:
                self.status_message = "[red]❌ Please enter a query"

    async def fetch_wallpaper(self, query: str) -> None:
        self.status_message = "[yellow]⏳ Fetching wallpaper..."
        try:
            image_path = fetch_image_pexels(query)
            if image_path:
                self.current_image = image_path
                self.query_one("#preview").update(
                    f"[bold]Preview:[/]\n{os.path.basename(image_path)}\n"
                    f"[dim]Query:[/] {query}"
                )
                self.status_message = "[green]✅ Ready! Press 's' to set"
            else:
                self.status_message = "[red]❌ Failed to fetch"
        except Exception as e:
            self.status_message = f"[red]⚠️ Error: {str(e)}"

    async def action_set_wallpaper(self) -> None:
        if not self.current_image:
            self.status_message = "[red]❌ No wallpaper loaded"
            return

        try:
            monitor_num = int(self.query_one("#monitor").value)
            set_wallpaper(self.current_image, monitor_num)
            self.status_message = f"[green]✅ Set on monitor {monitor_num}"
        except Exception as e:
            self.status_message = f"[red]❌ Error: {str(e)}"

if __name__ == "__main__":
    app = WallpaperTUI()
    app.run()