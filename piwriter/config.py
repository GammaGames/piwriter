#!/usr/bin/env python3

from configparser import ConfigParser

def get_config():
    config = ConfigParser()
    config.read('piwriter.ini')
    return config
