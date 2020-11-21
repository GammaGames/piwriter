![preview image](doc/preview.png)

A service to use the Waveshare E-ink display as a screen for the Raspberry Pi 


## Quick Start

Set up your raspberry pi and enter the following:

```sh
curl -s https://github.com/GammaGames/piwriter/raw/main/setup.sh | bash -x
```

with IT8951 HAT as 

A python tool to use a waveshare e-ink display with a raspberry pi

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
