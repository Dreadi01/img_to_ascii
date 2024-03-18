from PIL import Image, ImageDraw, ImageFont
import main

# Create a blank image with white background
image_width = 1000
image_height = 1000
background_color = (255, 255, 255)  # white
image = Image.new("RGB", (image_width, image_height), background_color)

# Initialize drawing context
draw = ImageDraw.Draw(image)

text = main.return_text("imgs/mqdefault.jpg", 100)
text_color = (0, 0, 0)  # black
font = ImageFont.truetype("arial.ttf", 10)
text_position = (0, 0)
line_spacing = 1
letter_spacing = 10
draw.text(text_position, text, fill=text_color, font=font, spacing=line_spacing)
print(text)

image.save("text_image.png")