#!/usr/bin/env python3

from functools import wraps
from threading import Timer
from configparser import ConfigParser
import keyboard
import time

last_time = None
config = ConfigParser()
config.read('piwriter.ini')

try:
    THROTTLE_TIME = float(config["keybounce"]["throttle_time"])
except KeyError:
    THROTTLE_TIME = 1.0

try:
    DEBOUNCE_TIME = float(config["keybounce"]["debounce_time"])
except KeyError:
    DEBOUNCE_TIME = 0.5


def throttle():
    def decorate(fn):
        global THROTTLE_TIME
        start_time = None

        def throttled(*args, **kwargs):
            nonlocal start_time
            if start_time is None or time.time() - start_time >= THROTTLE_TIME:
                result = fn(*args, **kwargs)
                start_time = time.time()
                return result
        return throttled
    return decorate


def debounce():
    def decorator(fn):
        global DEBOUNCE_TIME
        def debounced(*args, **kwargs):
            try:
                debounced.timer.cancel()
            except AttributeError:
                pass
            debounced.timer = Timer(DEBOUNCE_TIME, lambda: fn(*args, **kwargs))
            debounced.timer.start()
        return debounced
    return decorator


def _check_key(event):
    return (
        len(event.name) == 1 or  # Characters
        event.scan_code == 125 or  # Super
        event.name in [
            "space", "enter", "backspace", "tab", "esc",
            "up", "down", "right", "left",
            "page up", "page down", "start", "end",
            "`"
        ]
    )


def _callback(event, callback, debug=False):
    global last_time
    if last_time != event.time:
        last_time = event.time
        callback()
        if debug:
            print(f"Called {callback.__name__}")
        return True
    return False


@throttle()
def _throttled(event, callback, debug=False):
    global THROTTLE_TIME
    value = _callback(event, callback, debug)
    if debug:
        print(
            f"Throttled {event.name} ({'already processed' if not value else f'{THROTTLE_TIME}s'})"
        )


@debounce()
def _debounced(event, callback, debug=False):
    global DEBOUNCE_TIME
    value = _callback(event, callback, debug)
    if debug:
        print(
            f"Debounced {event.name} ({'already processed' if not value else f'{DEBOUNCE_TIME}s'})"
        )


def keybounce(callback, debug=False):
    def _on_key(event):
        if _check_key(event) and event.event_type == "up":
            _throttled(event, callback, debug)
            _debounced(event, callback, debug)

    hook_fun = keyboard.hook(_on_key)


def main():
    keybounce(callback=lambda: print("---"), debug=True)
    input("Listening...")


if __name__ == "__main__":
    main()
