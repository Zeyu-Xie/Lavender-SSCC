import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFont
import tqdm

# Config
size = 48

# Paths
ccs_path = os.path.join(os.path.dirname(__file__), "ccs.txt")
images_dir = os.path.join(os.path.dirname(__file__), f"images_{size}x{size}")
font_path = os.path.join(os.path.dirname(__file__), "STHeiti_Medium.ttc")
if not os.path.exists(images_dir):
    os.makedirs(images_dir, exist_ok=True)

# List: ccs, unicodes
ccs = []
with open(ccs_path, "r") as f:
    ccs = f.read()
unicodes = [ord(cc) for cc in ccs]
N = len(ccs)


# Store images
def char_to_image_simple(ch):
    image = Image.new("L", (size, size), color=255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, size)
    draw.text((0, 0), ch, fill=0, font=font)
    return image


for i in tqdm.tqdm(range(N)):
    cc = ccs[i]
    _unicode = unicodes[i]
    image_path = os.path.join(images_dir, f"{_unicode}.png")
    image = char_to_image_simple(cc)
    plt.imshow(image, cmap="gray", interpolation="nearest")
    plt.axis("off")
    image.save(image_path)
