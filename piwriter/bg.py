#!/usr/bin/env python3

from IT8951 import constants
from PIL import Image
from ttyink import TtyInk
import os
import random




class BgInk(TtyInk):
    def get_screen(self):
        logo = Image.open("../img/piwriter.png")
        # logo = logo.resize((int(logo.width / 1.5), int(logo.height / 1.5)), Image.LANCZOS)

        filename = random.choice(os.listdir("../img/bg"))
        image = Image.open("../img/bg/{}".format(filename))

        image = image.resize(self.dims, Image.LANCZOS)
        logo_pos = [
            int((image.width - logo.width) / 2),
            int((image.height - logo.height) / 2)
        ]
        image.paste(logo, logo_pos, logo)
        return image



def main():
    with BgInk(vcom=-1.34, debug=True) as screen:
        screen.refresh(full=True, display_mode=constants.DisplayModes.GC16)

        while input("q to quit:") != "q":
            screen.refresh()


if __name__ == "__main__":
    main()
