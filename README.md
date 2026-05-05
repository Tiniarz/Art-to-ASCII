# 🎨 ArtToASCII

![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)
![Made with Love](https://img.shields.io/badge/Made%20with-Love-red)

**ArtToASCII** is an open-source command-line utility designed to transform images into vibrant, high-fidelity ASCII art. Using a character-by-character "human-typing" effect and 24-bit TrueColor support, it brings your pictures to life directly in the terminal.

## 🚀 Features
- **Universal Format Support**: Works with every image format including PNG, JPG, JPEG, WEBP, BMP, and more.
- **TrueColor Rendering**: Scans image pixels to apply accurate colors to every ASCII character.
- **Customizable Width**: Manually set your output width up to a maximum of 200 characters.
- **Ultra-Fast Typewriter Effect**: Renders art with a cinematic, high-speed character-by-character print.
- **Looping Interface**: Process multiple images in a single session without the app closing.

## 🛠️ Requirements
To run this application, you need **Python 3.x** and the following libraries:

### Libraries to Install:
1. **Pillow**: For image processing and pixel scanning.
2. **Colorama**: For cross-platform terminal color support.

You can install them quickly using pip:
```bash
pip install Pillow colorama
💻 Usage
Launch the script: python main.py

Provide the path to your image file (e.g., C:\Images\photo.png).

Enter your preferred width (Max: 200).

To exit the application, type exit when prompted for a path.

ArtToASCII is Open Source. Feel free to modify and share!
