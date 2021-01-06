![preview image](docs/preview.png)

A service to use the Waveshare E-ink display as a screen for the Raspberry Pi 

## Quick Start

Set up your raspberry pi and enter the following:

```sh
curl -s https://github.com/GammaGames/piwriter/raw/main/setup.sh | bash -x
```

## Todo

* create helper functions:
  * connect to wifi
  * toggle wifi
  * reboot?
* create aliases:
  * open file emacs
* system setup:
  * /boot/config.txt
  * python modules
  * apt packages
  * .bashrc
  * set font (goha 8x16)
  * set resolution
  * `sudo systemctl link /home/pi/piwriter/piwriter.service`
* website:
  * home page with giant hero image that covers whole page
  * install script shortcut

```sh
PATH="$HOME/piwriter/bin:$PATH"
```
