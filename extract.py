import os
import random
import string
from PIL import Image, ImageDraw, ImageFont

# Load image
image_path = "./image.jpg"
image = Image.open(image_path)

# Define the x,y coordinates to crop
coordinates = [
    (50, 50),
    (150, 50),
    (250, 50),
    (50, 150),
    (150, 150),
    (250, 150)
]

for x, y in coordinates:
    crop_left = max(0, x - 50)
    crop_upper = max(0, y - 50)
    crop_right = min(image.width, x + 50)
    crop_lower = min(image.height, y + 50)

    cropped_image = image.crop((crop_left, crop_upper, crop_right, crop_lower))

    folder_name = f"{x}_{y}"
    folder_path = f"./output/{folder_name}"
    os.makedirs(folder_path, exist_ok=True)

    file_name = ''.join(random.choices(string.ascii_lowercase, k=4))
    output_path = f"{folder_path}/{folder_name}_{file_name}.jpg"

    cropped_image.save(output_path)