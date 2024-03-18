import cv2
import numpy as np


def convert_to_black_and_white(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    return grayscale_image


def pixelate_image(image_path, output_path, pixel_size):
    # Read the image
    image = convert_to_black_and_white(image_path)

    # Get the image dimensions
    height, width = image.shape[:2]

    # Resize the image to a smaller size
    small_image = cv2.resize(image, (pixel_size, pixel_size), interpolation=cv2.INTER_NEAREST)

    for row_num, row in enumerate(small_image):
        for pixel_num, pixel in enumerate(row):
            if pixel == 161:
                small_image[row_num][pixel_num] = 255

    # Resize the smaller image back to the original size
    pixelated_image = cv2.resize(small_image, (width, height), interpolation=cv2.INTER_NEAREST)

    cv2.imwrite(output_path, pixelated_image)
    return small_image


def generate_char_pic(img):
    chars = ['. ', "' ", '` ', '^ ', '""', '! ', '; ', ': ', 'I', 'l', '! ', 'i ', '< ', '>', '~', '+', '_ ',
             '-', '=', '?', '[', ']', '{', '}', '1', ')', '(', '|', '/', 'f', 't', 'j', 'r', 'x', 'n', 'u', 'c', 'v',
             'z',
             'X', 'Y', 'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b', 'k', 'h', 'a', 'o', 'o',
             '*',
             'M', '#', 'W', '&', '8', '%', 'B', '@', '$'
             ]
    chars = chars[:20]
    chars.reverse()

    detail_num = 256 / len(chars)
    new_list = []

    for row_num, row in enumerate(img):
        new_row_list = [str(item) for item in img[row_num]]

        for pixel_num, pixel in enumerate(row):
            for i in range(len(chars)):
                if pixel < detail_num * (i + 1):
                    new_row_list[pixel_num] = chars[i]
                    break
        new_list.append(new_row_list)

    text = ''
    for index, i in enumerate(new_list):
        text_line = ''
        for char in new_list[index]:
            text_line = text_line + char

        text = text + '\n' + text_line
    return text


def return_text(path, pixels):
    img_pixels = pixelate_image(path,
                                "pixelated/pixelated.png",
                                pixels)

    return generate_char_pic(img_pixels)
