from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wallpaper-cli-tool",
    version="1.0.0",
    description="A CLI tool to fetch and set beautiful wallpapers from various sources.",
    long_description=long_description,
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
        "Babel==2.12.1",
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