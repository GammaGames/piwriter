#!/usr/bin/env python3

from IT8951 import constants
from piwriter.keybounce import keybounce
from piwriter.ttyink import TtyInk
from PIL import Image

def main():
    with TtyInk(vcom=-1.34, image_filter=Image.HAMMING, debug=True) as screen:
        screen.refresh(full=True, display_mode=constants.DisplayModes.GC16)
        waiting = False

        def _update():
            nonlocal waiting
            if not waiting:
                waiting = True
                screen.refresh()
                waiting = False

        keybounce(callback=_update, debug=True)
        input("Updating...")

if __name__ == "__main__":
    main()
