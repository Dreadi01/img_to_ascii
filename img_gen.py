from PIL import Image, ImageDraw, ImageFont
import main
import os


def img_gen(img_path):
    # Create a blank image with white background
    image_width = 1200
    image_height = 1000
    background_color = (255, 255, 255)  # white
    image = Image.new("RGB", (image_width, image_height), background_color)

    # Initialize drawing context
    draw = ImageDraw.Draw(image)

    text = main.return_text(img_path, .1)
    text_color = (0, 0, 0)  # black
    font = ImageFont.truetype("arial.ttf", 10)
    text_position = (0, 0)
    line_spacing = 1
    letter_spacing = 10
    draw.text(text_position, text, fill=text_color, font=font, spacing=line_spacing)

    name = os.path.basename(img_path)
    image.save(f"gen_imgs/text_{name}.png")

