#!/usr/bin/env python3

from threading import Timer
import keyboard
import time


last_time = None


def throttle(wait=None):
    global global_wait
    def decorate(fn):
        start_time = None

        def throttled(*args, **kwargs):
            nonlocal start_time
            if start_time is None or time.time() - start_time >= (global_wait if wait is None else wait):
                result = fn(*args, **kwargs)
                start_time = time.time()
                return result
        return throttled
    return decorate


def debounce(wait=None):
    def decorator(fn):
        def debounced(*args, **kwargs):
            try:
                debounced.timer.cancel()
            except AttributeError:
                pass
            debounced.timer = Timer(wait, lambda: fn(*args, **kwargs))
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


@throttle(wait=1.0)
def _throttled(event, callback, debug=False):
    value = _callback(event, callback, debug)
    if debug:
        print(
            f"Throttled {event.name} {'(already processed)' if not value else ''}"
        )


@debounce(wait=0.5)
def _debounced(event, callback, debug=False):
    value = _callback(event, callback, debug)
    if debug:
        print(
            f"Debounced {event.name} {'(already processed)' if not value else ''}"
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
