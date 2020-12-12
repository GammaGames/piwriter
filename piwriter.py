#!/usr/bin/env python3

from IT8951.constants import DisplayModes
from PiWriter.keybounce import keybounce
from PiWriter.ttyink import TtyInk
from PiWriter.screensaver import get_screensaver
from PiWriter import util
from PIL import Image
import click
import time


@click.group()
def cli():
    pass


@cli.command()
@click.argument(
    "command",
    type=click.Choice(
        ["enable", "on", "disable", "off", "connect", "setup"],
        case_sensitive=False
    )
)
@click.argument("username", required=False, type=str)
@click.argument("password", required=False, type=str)
@click.option("--debug", is_flag=True, default=False)
def wifi(command, username, password, debug):
    if command in ["enable", "on"]:
        util.enable_wifi()
        util.enable_dhcpd()
    elif command in ["disable", "off"]:
        util.disable_wifi()
        util.disable_dhcpd()
    elif command in ["connect", "setup"]:
        if username is None:
            print("Username is required!")
            quit()
        print(username, password)
    print(command)
    if debug:
        print(f"{'Enabled' if enable else 'Disabled'} wifi")


@cli.command()
@click.option("--debug", is_flag=True, default=False)
def start(debug):
    if debug:
        print("Starting...")
    with TtyInk(image_filter=Image.HAMMING, debug=debug) as screen:
        screen.refresh(full=True, display_mode=DisplayModes.GL16)
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
@click.option("--debug", is_flag=True, default=False)
def stop(debug):
    if debug:
        print("Stopping...")
    with TtyInk(image_filter=Image.HAMMING, debug=debug) as screen:
        screen.display_to_screen(
            get_screensaver(screen.dims, debug=debug),
            full=True,
            display_mode=DisplayModes.GC16
        )


if __name__ == "__main__":
    cli()
