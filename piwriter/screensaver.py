#!/usr/bin/env python3

from IT8951 import constants
from PIL import Image, ImageEnhance, ImageFilter
import os
import random
import pathlib
import time
try:
    from piwriter.ttyink import TtyInk
except ImportError:
    from ttyink import TtyInk

SCRIPT_DIRECTORY = pathlib.Path(__file__).parent
IMAGE_DIRECTORY = f"{SCRIPT_DIRECTORY}/../img"

def get_screensaver(dimensions, debug=False):
    start = time.time()
    logo = Image.open(f"{IMAGE_DIRECTORY}/piwriter.png")
    logo_size = int(min(dimensions) / 2.5)
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

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

    logo_pos = [
        int((image.width - logo.width) / 2),
        int((image.height - logo.height) / 2)
    ]
    image.paste(logo, logo_pos, logo)
    if debug:
        print(f"Time to create screensaver: {round(time.time() - start, 3)}s")
    return image


def main():
    with TtyInk(vcom=-1.34, debug=True) as screen:
        screen.display_to_screen(
            get_screensaver(screen.dims),
            full=True,
            display_mode=constants.DisplayModes.GC16,
            debug=True
        )


if __name__ == "__main__":
    main()
