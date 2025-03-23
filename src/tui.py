# import os
# from textual import on
# from textual.app import App, ComposeResult
# from textual.widgets import Header, Footer, Button, Static, ListView, ListItem, Label
# from textual.worker import Worker
# from pexels_api import fetch_image
# from wallpaper_setter import set_wallpaper

# # Predefined wallpaper categories/queries
# PREDEFINED_QUERIES = [
#     "Nature", "City", "Space", 
#     "Mountains", "Beach", "Abstract",
#     "Minimalist", "Animals"
# ]

# class WallpaperTUI(App):
#     """Terminal User Interface for Wallpaper CLI"""
#     CSS_PATH = "tui_style.css"
#     BINDINGS = [("q", "quit", "Quit"), ("s", "set_wallpaper", "Set Wallpaper")]

#     def compose(self) -> ComposeResult:
#         yield Header()
#         yield Footer()
#         yield ListView(id="query_list")
#         yield Static(id="preview", classes="box")
#         yield Static(id="status", classes="box")

#     def on_mount(self) -> None:
#         """Load queries on startup"""
#         list_view = self.query_one("#query_list", ListView)
#         for query in PREDEFINED_QUERIES:
#             list_view.append(ListItem(Label(f"🌄 {query}")))

#     def on_list_view_selected(self, event: ListView.Selected) -> None:
#         """When a query is selected"""
#         self.selected_query = event.item.children[0].renderable.strip("🌄 ")
#         self.run_worker(self.fetch_wallpaper)

#     async def fetch_wallpaper(self) -> None:
#         """Fetch wallpaper in background"""
#         self.query_one("#status").update("[bold yellow]⏳ Fetching wallpaper...[/]")
#         image_path = fetch_image(self.selected_query)
#         if image_path:
#             self.image_path = image_path
#             self.query_one("#preview").update(
#                 f"[bold]Preview:[/]\n{os.path.basename(image_path)}\n"
#                 f"[dim]Query:[/] {self.selected_query}"
#             )
#             self.query_one("#status").update("[bold green]✅ Wallpaper ready! Press 's' to set")
#         else:
#             self.query_one("#status").update("[bold red]❌ Failed to fetch wallpaper")

#     def action_set_wallpaper(self) -> None:
#         """Set the wallpaper"""
#         if hasattr(self, "image_path"):
#             set_wallpaper(self.image_path)
#             self.query_one("#status").update(f"[bold green]✅ Wallpaper set: {self.image_path}")
#         else:
#             self.query_one("#status").update("[bold red]❌ No wallpaper selected")

# if __name__ == "__main__":
#     app = WallpaperTUI()
#     app.run()