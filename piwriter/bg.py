#!/usr/bin/env python3

from IT8951 import constants
from PIL import Image, ImageEnhance
from ttyink import TtyInk
import os
import random

def get_screensaver(dimensions):
    logo = Image.open("../img/piwriter.png")

    filename = random.choice(os.listdir("../img/bg"))
    image = Image.open("../img/bg/{}".format(filename))

    conrast = ImageEnhance.Brightness(image)
    image = conrast.enhance(0.3)
    brightness = ImageEnhance.Brightness(image)
    image = brightness.enhance(3.5)
    image = image.resize(dimensions, Image.LANCZOS)
    logo_pos = [
        int((image.width - logo.width) / 2),
        int((image.height - logo.height) / 2)
    ]
    image.paste(logo, logo_pos, logo)
    return image


def main():
    with TtyInk(vcom=-1.34, debug=True) as screen:
        screen.display_to_screen(
            get_screensaver(screen.dims),
            full=True,
            display_mode=constants.DisplayModes.GC16
        )

        while input("q to quit:") != "q":
            screen.display_to_screen(
                get_screensaver(screen.dims),
                full=True,
                display_mode=constants.DisplayModes.GC16
            )


if __name__ == "__main__":
    main()
