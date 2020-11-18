#!/usr/bin/env python3

from PIL import Image
from ttyink import TtyInk
import os
import random


class BgInk(TtyInk):
    def get_screen(self):
        logo = Image.open("../img/piwriter.png")
        logo = logo.resize((int(logo.width / 1.5), int(logo.height / 1.5)), Image.LANCZOS)
        logo_pos = [
            int((800 - logo.width) / 2),
            int((600 - logo.height) / 2)
        ]
        filename = random.choice(os.listdir("../img/bg"))
        image = Image.open("../img/bg/{}".format(filename))
        target_dims = [800, 600]
        # target_ratio = target_dims[0] / target_dims[1]
        # image_ratio = image.width / image.height
        # if image_ratio > target_ratio:
        #     target_dims[1] = int(target_dims[1] * image_ratio)
        # else:
        #     target_dims[0] = int(target_dims[0] * image_ratio)

        image = image.resize(target_dims, Image.LANCZOS)
        image.paste(logo, logo_pos, logo)
        return image



def main():
    with BgInk(vcom=-1.34, debug=True) as screen:
        screen.refresh(full=True, display_mode=constants.DisplayModes.GC16)

        while input("q to quit:") != "q":
            screen.refresh()


if __name__ == "__main__":
    main()
