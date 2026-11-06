from PIL import Image

def image_to_ascii(image_path, new_width=100):
    ASCII_CHARS = "@%#*+=-:. "
    
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            aspect_ratio = height / width
            new_height = int(new_width * aspect_ratio * 0.55)
            img = img.resize((new_width, new_height))
            img = img.convert("L")
            pixels = img.getdata()
            ascii_str = ""
            for pixel in pixels:
                index = pixel * (len(ASCII_CHARS) - 1) // 255
                ascii_str += ASCII_CHARS[index]
            pixel_count = len(ascii_str)
            ascii_img = "\n".join(ascii_str[i:(i + new_width)] for i in range(0, pixel_count, new_width))
            
            return ascii_img
            
    except Exception as e:
        return f"Error loading image: {e}"


def generate(file):
    ascii_art = image_to_ascii(file, new_width=80)
    return ascii_art
def pgenarete(file):
    print(generate(file))