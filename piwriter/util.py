import subprocess


def disable_wifi():
    output = subprocess.run(
        "rfkill block wifi".split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL
    )


def enable_wifi():
    output = subprocess.run(
        "rfkill unblock wifi".split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL
    )


def disable_dhcpd():
    output = subprocess.run(
        "systemctl stop dhcpd.service".split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL
    )


def enable_dhcpd():
    output = subprocess.run(
        "systemctl start dhcpd.service".split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL
    )
