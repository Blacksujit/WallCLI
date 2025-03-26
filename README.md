# 💘WallCLI

![Wall CLI](testimages/webgl_02.gif)

Welcome to the Wallpaper CLI Tool! This tool allows you to fetch and set beautiful wallpapers from various sources like Pexels, Unsplash, NASA APOD, and Reddit. You can also generate custom wallpapers using Stable Diffusion. The tool is designed to be user-friendly and highly customizable.


## 📑 Table of Contents

- [Wall CLI in action](#wall-cli-videos)
- [Samples of fetched and Generated Wallpapers](#samples-of-fetched-and-generated-wallpapers)
- [Folder Structure](#-folder-structure)
- [Features](#features)
- [API Keys](#-api-keys)
- [Installation](#-installation)
- [Usage](#-usage)
    - [Terminal User Interface (For Normal users non techies)](#-terminal-user-interface-for-normal-users-non-techies)
    - [Command Line Interface: (For techies)](#-command-line-interface-for-techies)
- [Example Use Case](#-example-use-case)
- [Contributing](#-contributing)
- [License](#-license)


## WALL-CLI Videos:

-->****Video Explanation:****

[Video explanation Demo](https://drive.google.com/file/d/1rpmvSq1aRGOspeGPQMbO3AlVW1rVMaod/view?usp=drive_link)


--> **For Non-techies(Normal Users):**

[Video Link for Normal Users](https://drive.google.com/file/d/1xEOVnpocP6BbWz6nqJTjKfLzUgOQE3hH/view?usp=sharing)

--> **For Techies:**

[Video Link](https://drive.google.com/file/d/1ri4RZFInxwvGRyigX4g8LT83BtwMi4e9/view?usp=drive_link)



## ✨✅Samples of fetched and Generated Wallpapers:

**1.) Query - Scenary**


![Wall 1](src/wallpapers/city_night_2.jpg)

**2.) Query - Spirituality**

![Wall 2](src/wallpapers/ganga_arti_2.jpg)

**3.) Query - Ganga Arti**

![Wall3](src/wallpapers/hindu_spirituality_1.jpg)

**4.) Query - Mountains**

![Wall 4](src/wallpapers/mountains_2.jpg)

## 📂 Folder Structure

```
wallpaper-cli-tool/
├── src/
|   |---wallpapers/
|   |      |-- nature.jpg 
|   |      |-- sea.png 
|   |      |-- sea2.png 
│   ├── generator.py          # Custom wallpaper generation using Stable Diffusion
│   ├── main.py               # Main entry point for CLI
│   ├── nasa_apod_api.py      # Fetch wallpapers from NASA APOD
│   ├── pexels_api.py         # Fetch wallpapers from Pexels
│   ├── reddit_api.py         # Fetch wallpapers from Reddit
│   ├── tui.py                # Terminal User Interface
│   ├── tui_style.css         # Styles for TUI
│   ├── unsplash_api.py       # Fetch wallpapers from Unsplash
│   └── wallpaper_setter.py   # Set and manage wallpapers
├── requirements.txt          # Project dependencies
├── wallpaper_history.txt     # History of wallpapers
└── test images/              # Test images used in the project for referance
└── Wallpapers/               # Project Wallpapers for reference
└── README.md                 # Project documentation
```

## 🪶Features

**✨ - Fetch wallpapers from multiple sources: Pexels, Unsplash, NASA APOD, and Reddit.**

**✨ - Terminal User Interface (TUI) for easy interaction. for normal PC or windows users**

**✨ - Generate custom wallpapers using Stable Diffusion.**

**✨ - Set wallpapers directly from the command line.**

**✨ - Maintain a history of wallpapers.**

**✨ - Fetch Previous and Next Wallpapers**

**✨ - Set custom resolution for wallpapers , according to your adaptive rate of windows for ex: 124×124 etc.**


## 🔑 API Keys

To use this tool, you need to set up API keys for the various services. Here are the steps to obtain and set the API keys:

`first of all create an  ``.env``  file at the root of your project`

1. **Pexels API Key:**
    - Sign up at [Pexels](https://www.pexels.com/api/).
    - Go to your profile and find the API key.
    - Set the API key in your environment variables:
        ```sh
        export PEXELS_API_KEY='your_pexels_api_key'
        ```

2. **Unsplash API Key:**
    - Sign up at [Unsplash](https://unsplash.com/developers).
    - Create a new application to get the API key.
    - Set the API key in your environment variables:
        ```sh
        export UNSPLASH_API_KEY='your_unsplash_api_key'
        ```

3. **NASA APOD API Key:**
    - Sign up at [NASA API](https://api.nasa.gov/).
    - Get the API key for APOD.
    - Set the API key in your environment variables:
        ```sh
        export NASA_API_KEY='your_nasa_api_key'
        ```

4. **Reddit API Key:**
    - Create an application at [Reddit Apps](https://www.reddit.com/prefs/apps).
    - Get the client ID and secret.
    - Set the API key in your environment variables:
        ```sh
        export REDDIT_CLIENT_ID='your_reddit_client_id'
        export REDDIT_SECRET='your_reddit_secret'
        ```

## 💻 Installation

### From Source

1. Clone the repository:

```
git clone https://github.com/Blacksujit/WallCLI.git
```

```
cd wallpaper-cli-tool
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

### From PyPI:

**You can install the package directly from PyPI:**

-> Visit For pypi project:

[PYPI Wall-CLI Project Link](https://pypi.org/project/wallpaper-cli-tool/)

```
pip install wallpaper-cli-tool 
```

**For Package Installation Steps**:


just u have to put ->>**`wallpaper-cli-tool` instead of `python main.py`  in commands**

``for example:``

```
wallpaper-cli-tool --set-wallpaper "A beautiful sunset" --source reddit
```

## 🪴 Usage

### 🧑‍🔧🦾 Terminal User Interface (For Normal users non techies):

![TUI Interface](image-1.png)

##### **Run the TUI:**

```sh
python src/tui.py
```

***Use the TUI to select predefined queries, enter custom queries, and fetch wallpapers.***

### 🧑‍💻👩‍💻 Command Line Interface: (For techies)

**🫴 navigate to:**

```
cd src
```

**🫴 Fetch and set a wallpaper from Pexels:**

```sh
python main.py --set-wallpaper "hindu Spirituality" --orientation "landscape" --resolution "1920x1080" --monitor 0
```

**🫴 Set Wallpaper from Various Sources like Reddit , unsplash , Nasa apod:**

```sh
python main.py --set-wallpaper "A beautiful sunset" --source reddit
```

```sh
python main.py --set-wallpaper "A beautiful sunset" --source unsplash
```

##### IMP Note: 

**just in case of setting the wallpaers from nasa apod u have to specify the date instead of the query so it works on the geolocation engine , so it works as random sattelite wallpaper API**

```sh
python main.py --set-wallpaper "2022-03-12" --source nasa
```

**🫴 Set Previous used wallpaper:**

```sh
python main.py --previous 2 --monitor 0
```

**🫴 Generate a custom wallpaper:**

```sh
python main.py --source custom --query "a beautiful sunset" --resolution "1024x1024"
```

**🫴 Retrive the wallpaper History:**

```sh
python main.py --list-history
```


## 🌱 Example Use Case

Imagine you want to refresh your desktop wallpaper every day with a new image of nature. You can set up a cron job (on Unix-based systems) or a scheduled task (on Windows) to run the following command daily:

```sh
python src/main.py --source pexels --query "nature" --orientation "landscape" --resolution "1920x1080"
```

This will automatically fetch a new nature wallpaper from Pexels and set it as your desktop background.

## 🎮 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## 🪪 License

This project is licensed under the MIT License.

**Enjoy your new wallpapers!!!**

![Enjoy ur Wallpapers !!](testimages/33e1bf10-174b-47ab-bae1-a77b544b7ce7.jpg)
