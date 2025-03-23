from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, ListView, ListItem, Label, Button, Input
from textual.containers import Container
from textual.reactive import Reactive
from textual.events import Key
from textual.worker import Worker
import os
import sys

# Ensure the current directory is in the module search path
sys.path.append(os.path.dirname(__file__))

# Use absolute paths for imports
sys.path.append(r'D:\wallpaper-cli-tool\src')

from pexels_api import fetch_image as fetch_image_pexels
from unsplash_api import fetch_image as fetch_image_unsplash
from nasa_apod_api import fetch_image as fetch_image_nasa
from reddit_api import fetch_image as fetch_image_reddit
from wallpaper_setter import set_wallpaper, set_previous_wallpaper, get_wallpaper_history

# Predefined wallpaper categories/queries
PREDEFINED_QUERIES = [
    "Nature", "City", "Space", 
    "Mountains", "Beach", "Abstract",
    "Minimalist", "Animals"
]

class WallpaperTUI(App):
    """Terminal User Interface for Wallpaper CLI"""
    CSS_PATH = "tui_style.css"
    BINDINGS = [("q", "quit", "Quit"), ("s", "set_wallpaper", "Set Wallpaper"), ("h", "list_history", "List History"), ("p", "set_previous", "Set Previous")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield ListView(id="query_list")
        yield Static(id="preview", classes="box")
        yield Static(id="status", classes="box")
        yield Input(placeholder="Custom Query", id="custom_query")
        yield Input(placeholder="Orientation (landscape/portrait/square)", id="orientation")
        yield Input(placeholder="Resolution (e.g., 1920x1080)", id="resolution")
        yield Input(placeholder="Monitor Number", id="monitor")
        yield Button(label="Fetch Custom Wallpaper", id="fetch_custom")

    def on_mount(self) -> None:
        """Load queries on startup"""
        list_view = self.query_one("#query_list", ListView)
        for query in PREDEFINED_QUERIES:
            list_view.append(ListItem(Label(f"🌄 {query}")))

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """When a query is selected"""
        self.selected_query = event.item.children[0].renderable.strip("🌄 ")
        self.run_worker(self.fetch_wallpaper)

    async def fetch_wallpaper(self) -> None:
        """Fetch wallpaper in background"""
        self.query_one("#status").update("[bold yellow]⏳ Fetching wallpaper...[/]")
        image_path = fetch_image_pexels(self.selected_query)
        if image_path:
            self.image_path = image_path
            self.query_one("#preview").update(
                f"[bold]Preview:[/]\n{os.path.basename(image_path)}\n"
                f"[dim]Query:[/] {self.selected_query}"
            )
            self.query_one("#status").update("[bold green]✅ Wallpaper ready! Press 's' to set")
        else:
            self.query_one("#status").update("[bold red]❌ Failed to fetch wallpaper")

    async def action_set_wallpaper(self) -> None:
        """Set the wallpaper"""
        if hasattr(self, "image_path"):
            set_wallpaper(self.image_path)
            self.query_one("#status").update(f"[bold green]✅ Wallpaper set: {self.image_path}")
        else:
            self.query_one("#status").update("[bold red]❌ No wallpaper selected")

    async def action_list_history(self) -> None:
        """List wallpaper history"""
        history = get_wallpaper_history()
        if not history:
            self.query_one("#status").update("[bold red]❌ No wallpaper history found")
        else:
            history_list = "\n".join([f"{i}: {path}" for i, path in enumerate(history)])
            self.query_one("#preview").update(f"[bold]Wallpaper History:[/]\n{history_list}")

    async def action_set_previous(self) -> None:
        """Set a previously used wallpaper from history"""
        monitor_num = int(self.query_one("#monitor").value)
        previous_index = int(self.query_one("#custom_query").value)
        set_previous_wallpaper(previous_index, monitor_num)
        self.query_one("#status").update(f"[bold green]✅ Wallpaper set from history index: {previous_index}")

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events"""
        if event.button.id == "fetch_custom":
            query = self.query_one("#custom_query").value
            orientation = self.query_one("#orientation").value
            resolution = self.query_one("#resolution").value
            monitor_num = int(self.query_one("#monitor").value)
            self.run_worker(self.fetch_custom_wallpaper, query, orientation, resolution, monitor_num)

    async def fetch_custom_wallpaper(self, query: str, orientation: str, resolution: str, monitor_num: int) -> None:
        """Fetch custom wallpaper in background"""
        self.query_one("#status").update("[bold yellow]⏳ Fetching custom wallpaper...[/]")
        image_path = fetch_image_pexels(query, orientation, resolution)
        if image_path:
            self.image_path = image_path
            self.query_one("#preview").update(
                f"[bold]Preview:[/]\n{os.path.basename(image_path)}\n"
                f"[dim]Query:[/] {query}"
            )
            self.query_one("#status").update("[bold green]✅ Custom wallpaper ready! Press 's' to set")
        else:
            self.query_one("#status").update("[bold red]❌ Failed to fetch custom wallpaper")

if __name__ == "__main__":
    app = WallpaperTUI()
    app.run()