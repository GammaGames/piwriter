#!/usr/bin/env python3

from IT8951 import constants
from piwriter.keybounce import keybounce
from piwriter.ttyink import TtyInk
from piwriter.screensaver import get_screensaver
from PIL import Image
import click
import time

@click.group()
def cli():
    pass


@cli.command()
@click.option('--debug', is_flag=True, default=False)
def run(debug):
    with TtyInk(vcom=-1.34, image_filter=Image.HAMMING, debug=debug) as screen:
        screen.refresh(full=True, display_mode=constants.DisplayModes.GLR16)
        waiting = False

        def _update():
            nonlocal waiting
            if not waiting:
                waiting = True
                screen.refresh()
                waiting = False

        keybounce(callback=_update, debug=debug)
        while True:
            time.sleep(1000)


@cli.command()
@click.option('--debug', is_flag=True, default=False)
def sleep(debug):
    with TtyInk(vcom=-1.34, image_filter=Image.HAMMING, debug=debug) as screen:
        screen.display_to_screen(
            get_screensaver(screen.dims, debug=debug),
            full=True,
            display_mode=constants.DisplayModes.GC16
        )


if __name__ == "__main__":
    cli()
