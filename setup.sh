#!/usr/bin/env bash

sudo mkdir -p /etc/systemd/system/networking.sevice.d/
sudo vim /etc/systemd/system/networking.sevice.d/reduce-timeout.conf


systemctl disable apt-daily-upgrade.service
