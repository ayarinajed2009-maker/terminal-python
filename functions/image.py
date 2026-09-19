from PIL import Image

def image_to_ascii(image_path, new_width=100):
    # 1. Define ASCII characters from darkest to lightest
    ASCII_CHARS = "@%#*+=-:. "
    
    try:
        # 2. Open the image
        with Image.open(image_path) as img:
            # 3. Resize image maintaining aspect ratio (adjusted for terminal line spacing)
            width, height = img.size
            aspect_ratio = height / width
            # Terminal characters are taller than they are wide, so we scale down the height factor
            new_height = int(new_width * aspect_ratio * 0.55)
            img = img.resize((new_width, new_height))
            
            # 4. Convert image to grayscale (L mode)
            img = img.convert("L")
            
            # 5. Map pixels to ASCII characters
            pixels = img.getdata()
            ascii_str = ""
            for pixel in pixels:
                # Map 0-255 brightness values to our ASCII_CHARS array index
                index = pixel * (len(ASCII_CHARS) - 1) // 255
                ascii_str += ASCII_CHARS[index]
            
            # 6. Format string into rows based on the new width
            pixel_count = len(ascii_str)
            ascii_img = "\n".join(ascii_str[i:(i + new_width)] for i in range(0, pixel_count, new_width))
            
            return ascii_img
            
    except Exception as e:
        return f"Error loading image: {e}"

# --- Run the Code ---
# Replace 'your_image.jpg' with your actual file path
def generate(file):
    ascii_art = image_to_ascii(file, new_width=80)
    return ascii_art
def pgenarete(file):
    print(generate(file))