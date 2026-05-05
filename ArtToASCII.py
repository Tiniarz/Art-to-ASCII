import sys
import time
import os
from PIL import Image
from colorama import init, Style

init(strip=False)

if os.name == 'nt':
    os.system('color')

def get_ansi_color(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def scale_image(image, new_width):
    original_width, original_height = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width * 0.5)
    return image.resize((new_width, new_height))

def map_pixels_to_ascii(image):
    chars = "@#S%?*+;:,."
    grayscale = image.convert("L")
    pixels = grayscale.getdata()
    return [chars[pixel // 25] for pixel in pixels]

def main():
    while True:
        path = input("Enter path (or type 'exit' to quit): ").strip().strip('"')
        if path.lower() == 'exit':
            break
            
        try:
            user_input = input("Enter width (max 200): ")
            width = min(int(user_input), 200)
        except:
            width = 200

        try:
            image = Image.open(path)
            rgb_image = image.convert("RGB")
        except:
            continue

        resized_image = scale_image(rgb_image, width)
        pixels_rgb = list(resized_image.getdata())
        ascii_chars = map_pixels_to_ascii(resized_image)
        
        current_color = None
        
        for i, char in enumerate(ascii_chars):
            r, g, b = pixels_rgb[i]
            new_color = get_ansi_color(r, g, b)
            
            if new_color != current_color:
                sys.stdout.write(new_color)
                current_color = new_color
                
            sys.stdout.write(char)
            
            if (i + 1) % width == 0:
                sys.stdout.write("\n")
                
            sys.stdout.flush()
            time.sleep(0.0001)

        sys.stdout.write(Style.RESET_ALL + "\n\n")

if __name__ == "__main__":
    main()