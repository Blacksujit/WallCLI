from setuptools import setup, find_packages

setup(
    name="wallpaper-cli-tool",
    version="1.0.1",
    description="A CLI tool to fetch and set beautiful wallpapers from various sources.",
    long_description="""
    # Wallpaper CLI Tool

    Welcome to the Wallpaper CLI Tool! This tool allows you to fetch and set beautiful wallpapers from various sources like Pexels, Unsplash, NASA APOD, and Reddit. You can also generate custom wallpapers using Stable Diffusion. The tool is designed to be user-friendly and highly customizable.

    ## Features

    - Fetch wallpapers from Pexels, Unsplash, NASA APOD, and Reddit
    - Generate custom wallpapers using Stable Diffusion
    - Set wallpapers on multiple monitors
    - List wallpaper history
    - Command Line Interface (CLI) and Terminal User Interface (TUI)

    ## Installation

    To install the Wallpaper CLI Tool, run:

    ```sh
    pip install wallpaper-cli-tool
    ```

    ## Usage

    To fetch and set a wallpaper, run:

    ```sh
    wallpaper-cli --set-wallpaper "nature" --source pexels
    ```

    For more usage examples and options, refer to the documentation on the [GitHub repository](https://github.com/Blacksujit/WallCLI).
    """,
    long_description_content_type="text/markdown",
    author="Sujit Nirmal",
    author_email="nirmalsujit981@gmail.com",
    url="https://github.com/Blacksujit/WallCLI.git",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "requests",
        "textual",
        "Pillow",
        "python-dotenv",
        "pexels-api",
        "unsplash-api",
        "nasa-apod-api",
        "reddit-api",
        "diffusers",
        "torch",
    ],
    entry_points={
        "console_scripts": [
            "wallpaper-cli=main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

# Added the setup.py for production and pypi project