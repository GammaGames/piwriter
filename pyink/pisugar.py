#!/usr/bin/env python3

import subprocess
import socket

def get_charge():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8423))
    s.sendall(b"get battery")
    battery = s.recv(1024).decode().split(":")[-1].strip()
    return float(battery)


def get_charging():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8423))
    s.sendall(b"get battery_charging")
    charging = s.recv(1024).decode().split(":")[-1].strip()
    return charging == "true"


def main():
    print(get_charge())
    print(get_charging())


if __name__ == "__main__":
    main()
