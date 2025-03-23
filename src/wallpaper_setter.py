import os
import ctypes
import platform

WALLPAPER_HISTORY_FILE = "wallpaper_history.txt"

def set_wallpaper(image_path, monitor_num=0):
    """
    Sets the wallpaper to the specified image.
    """
    if platform.system() == "Windows":
        # Windows-specific implementation
        image_path = os.path.abspath(image_path)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    elif platform.system() == "Darwin":
        # macOS-specific implementation
        script = f'''
        osascript -e 'tell application "Finder" to set desktop picture to POSIX file "{image_path}"'
        '''
        os.system(script)
    elif platform.system() == "Linux":
        # Linux-specific implementation (GNOME)
        script = f'''
        gsettings set org.gnome.desktop.background picture-uri "file://{image_path}"
        '''
        os.system(script)
    else:
        print("Unsupported operating system.")
        return

    # Save the wallpaper to history
    save_wallpaper_to_history(image_path)

def save_wallpaper_to_history(image_path):
    """
    Saves the wallpaper path to the history file.
    """
    with open(WALLPAPER_HISTORY_FILE, "a") as f:
        f.write(image_path + "\n")

def set_previous_wallpaper(index, monitor_num=0):
    """
    Sets a previously used wallpaper from history by index.
    """
    history = get_wallpaper_history()
    if index < 0 or index >= len(history):
        print("Invalid index.")
        return

    image_path = history[index]
    set_wallpaper(image_path, monitor_num)

def get_wallpaper_history():
    """
    Retrieves the wallpaper history.
    """
    if not os.path.exists(WALLPAPER_HISTORY_FILE):
        return []

    with open(WALLPAPER_HISTORY_FILE, "r") as f:
        history = f.read().splitlines()

    return history