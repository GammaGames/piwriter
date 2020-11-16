#!/usr/bin/env python3

from configparser import ConfigParser
from IT8951.interface import EPD
from IT8951.display import AutoEPDDisplay
from IT8951 import constants
from PIL import Image
import PIL.ImageOps
import subprocess
import time
import io

config = ConfigParser()
config.read('piwriter.ini')

try:
    TTY_DEVICE = float(config["tty"]["device"])
except KeyError:
    TTY_DEVICE = 1


class TtyInk():
    def __init__(self, vcom=None, display_mode=constants.DisplayModes.GLR16, debug=False):
        start = time.time()
        self.vcom = vcom
        self.display_mode = display_mode
        self.debug = debug
        self.epd = EPD()
        self.display = AutoEPDDisplay(epd=self.epd, vcom=self.vcom)
        self.dims = (self.display.width, self.display.height)
        self.prev = None
        if self.debug:
            print(f"Time to initialize: {round(time.time() - start, 3)}s")
            start = time.time()
        self.display.clear()
        if self.debug:
            print(f"Time to clear: {round(time.time() - start, 3)}s")

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def refresh(self, full=False, display_mode=None):
        start = time.time()
        self.display_to_screen(self.get_screen(), full=full, display_mode=display_mode)

        if self.debug:
            print(f"Time to refresh: {round(time.time() - start, 3)}s")

    def display_to_screen(self, image, full=False, display_mode=None):
        start = time.time()
        paste_coords = [0, 0]
        self.display.frame_buf.paste(image, [0, 0])
        if full:
            self.display.draw_full(self.display_mode if display_mode is None else display_mode)
        else:
            self.display.draw_partial(self.display_mode if display_mode is None else display_mode)

        if self.debug:
            print(f"Time to display: {round(time.time() - start, 3)}s")

    def get_screen(self):
        global TTY_DEVICE
        start = time.time()
        output = subprocess.run(
            f"./piwriter/grab-tty.sh {TTY_DEVICE}".split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL
        )
        if self.debug:
            print(f"Time to capture image: {round(time.time() - start, 3)}s")
            start = time.time()

        image = Image.open(io.BytesIO(output.stdout))
        # image = PIL.ImageOps.invert(image)
        image = image.resize(self.dims, Image.NEAREST)

        if self.debug:
            print(f"Time to transform image: {round(time.time() - start, 3)}s")

        return image

    def wait():
        self.epd.wait_display_ready()


def main():
    with TtyEink(vcom=-1.34, debug=True) as screen:
        screen.refresh(full=True, display_mode=constants.DisplayModes.GC16)

        while input("q to quit:") != "q":
            screen.refresh()


if __name__ == '__main__':
    main()
