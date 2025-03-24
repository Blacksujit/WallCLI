import argparse
import random
import sys
import os
from datetime import datetime  # Correct import for datetime

# Ensure the current directory is in the module search path
sys.path.append(os.path.dirname(__file__))

# Use absolute paths for imports
sys.path.append(r'D:\wallpaper-cli-tool\src')

from pexels_api import fetch_image as fetch_image_pexels
from unsplash_api import fetch_image as fetch_image_unsplash
from nasa_apod_api import fetch_image as fetch_image_nasa
from reddit_api import fetch_image as fetch_image_reddit
from wallpaper_setter import set_wallpaper, set_previous_wallpaper, get_wallpaper_history

def fetch_and_set(query, source="pexels", orientation="landscape", resolution=None, monitor_num=0):
    """
    Fetches an image from the specified source and sets it as the wallpaper.
    """
    print(f"Fetching and setting wallpaper for query: {query} from source: {source}")
    if source == "pexels":
        image_path = fetch_image_pexels(query, orientation, resolution)
    elif source == "unsplash":
        image_path = fetch_image_unsplash(query, orientation, resolution)
    elif source == "nasa":
        # Handle NASA APOD API which expects a date in YYYY-MM-DD format
        try:
            datetime.strptime(query, '%Y-%m-%d')
            image_path = fetch_image_nasa(query)
        except ValueError:
            print("Invalid date format for NASA APOD. Using the current date instead.")
            image_path = fetch_image_nasa()
    elif source == "reddit":
        image_path = fetch_image_reddit(query)
    else:
        print(f"Unknown source: {source}")
        return

    if image_path:
        set_wallpaper(image_path, monitor_num)
    else:
        print("Failed to fetch or set the wallpaper.")

def fetch_random_wallpaper(queries, source="pexels", orientation="landscape", resolution=None, monitor_num=0):
    """
    Fetches a random wallpaper from a list of queries.
    """
    query = random.choice(queries)
    print(f"Fetching random wallpaper for query: {query} from source: {source}")
    fetch_and_set(query, source, orientation, resolution, monitor_num)

def list_wallpaper_history():
    """
    Lists all previously set wallpapers.
    """
    history = get_wallpaper_history()
    if not history:
        print("No wallpaper history found.")
    else:
        print("Wallpaper History:")
        for i, path in enumerate(history):
            print(f"{i}: {path}")

def main():
    """
    Main function to handle CLI arguments.
    """
    parser = argparse.ArgumentParser(description="Wallpaper CLI Tool")
    parser.add_argument(
        "--set-wallpaper",
        type=str,
        help="Fetch an image from a source and set it as wallpaper (e.g., --set-wallpaper 'nature')"
    )
    parser.add_argument(
        "--source",
        type=str,
        choices=["pexels", "unsplash", "nasa", "reddit"],
        default="pexels",
        help="Source of the image (pexels, unsplash, nasa, reddit)"
    )
    parser.add_argument(
        "--orientation",
        type=str,
        choices=["landscape", "portrait", "square"],
        default="landscape",
        help="Orientation of the image (landscape, portrait, square)"
    )
    parser.add_argument(
        "--resolution",
        type=str,
        help="Desired resolution of the image (e.g., 1920x1080)"
    )
    parser.add_argument(
        "--monitor",
        type=int,
        default=0,
        help="Monitor number to set the wallpaper (default: 0)"
    )
    parser.add_argument(
        "--random",
        action="store_true",
        help="Fetch and set a random wallpaper from a predefined list of queries"
    )
    parser.add_argument(
        "--previous",
        type=int,
        help="Set a previously used wallpaper from history by index"
    )
    parser.add_argument(
        "--list-history",
        action="store_true",
        help="List all previously set wallpapers"
    )
    args = parser.parse_args()

    predefined_queries = ["nature", "city", "space", "mountains", "beach"]

    if args.list_history:
        list_wallpaper_history()
    elif args.previous is not None:
        set_previous_wallpaper(args.previous, args.monitor)
    elif args.random:
        fetch_random_wallpaper(predefined_queries, args.source, args.orientation, args.resolution, args.monitor)
    elif args.set_wallpaper:
        fetch_and_set(args.set_wallpaper, args.source, args.orientation, args.resolution, args.monitor)
    else:
        print("Use --help for options.")

if __name__ == "__main__":
    main()