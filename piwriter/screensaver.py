#!/usr/bin/env python3

from IT8951 import constants
from PIL import Image, ImageEnhance, ImageFilter
import os
import random
import pathlib
try:
    from piwriter.ttyink import TtyInk
except ImportError:
    from ttyink import TtyInk

SCRIPT_DIRECTORY = pathlib.Path(__file__).parent
IMAGE_DIRECTORY = f"{SCRIPT_DIRECTORY}/../img"

def get_screensaver(dimensions):
    logo = Image.open(f"{IMAGE_DIRECTORY}/piwriter.png")
    logo_size = int(min(dimensions) / 3)
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    # Create blur behind image
    logo_blur = Image.new("RGB", logo.size, 0xffffff)
    blur_image = Image.new("RGBA", logo.size)
    blur_image.paste(logo_blur, (0, 0), logo)
    for i in range(3):
        blur_image = blur_image.filter(ImageFilter.BLUR)

    filename = random.choice(os.listdir(f"{IMAGE_DIRECTORY}/bg"))
    image = Image.open(f"{IMAGE_DIRECTORY}/bg/{filename}")

    # Crop to screen ratio before resize
    target_ratio = dimensions[0] / dimensions[1]
    image_ratio = image.width / image.height
    if image_ratio > target_ratio:
        # Too wide, crop left and right
        new_width = int(target_ratio * image.height)
        offset = (image.width - new_width) / 2
        resize = (offset, 0, image.width - offset, image.height)
    else:
        # Too tall, crop top and bottom
        new_height = int(image.width / target_ratio)
        offset = (image.height - new_height) / 2
        resize = (0, offset, image.width, image.height - offset)

    image = image.crop(resize).resize(dimensions, Image.LANCZOS)
    conrast = ImageEnhance.Brightness(image)
    image = conrast.enhance(0.3)
    brightness = ImageEnhance.Brightness(image)
    image = brightness.enhance(3.5)

    logo_pos = [
        int((image.width - logo.width) / 2),
        int((image.height - logo.height) / 2)
    ]
    image.paste(blur_image, logo_pos, blur_image)
    image.paste(logo, logo_pos, logo)
    return image


def main():
    with TtyInk(vcom=-1.34, debug=True) as screen:
        screen.display_to_screen(
            get_screensaver(screen.dims),
            full=True,
            display_mode=constants.DisplayModes.GC16
        )


if __name__ == "__main__":
    main()
