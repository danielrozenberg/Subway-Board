# Subway-Board

Displays subway ETA for nearby stations. Ask me if you're curious!

# Hardware

Designed to work with the Raspberry Pi RGB LED Matrix HAT and two 64×32 matrices
chained together, and tested on a Raspberry Pi 2 (LED controller on the RPi,
server running on a separate machine) and on a Raspberry Pi 4 (LED controller
and server both on RPi)

Do the hardware setup as described on
[Adafruit's guide](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi)

# Software (Raspberry Pi LED Matrix Controller)

## Basic setup

- Install _Raspberry Pi OS Lite_ on a fresh micro SD card
- [Activate SSH and configure your wifi](https://www.instructables.com/Control-Raspberry-Pi-Without-Monitor/)
  - On the Raspberry Pi 2 I used a USB wifi dongle which required extra setup.
    If you get a `could not connect to wpa_supplicant` error when trying
    to configure it with `sudo raspi-config`, add the
    [`wlan0` section](https://www.electronicshub.org/setup-wifi-raspberry-pi-2-using-usb-dongle/),
    then restart networking with `sudo systemctl restart networking.service`.
  - My wifi SSID has emojis, so I needed to
    [convert it to hex](https://raspberrypi.stackexchange.com/a/68661)
- Update the OS `sudo apt update && sudo apt upgrade`
- Install dependencies `sudo apt install git python3-dev python3-pil`
- `sudo raspi-config`
  - System Settings → Hostname → Choose a hostname
  - Localisation Options → Locale
  - Localisation Options → Timezone

## Python

- [Set up Python 3 as the default](https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux)
- [Install the LED Matrix Python binding](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/driving-matrices)
  (step 6)

## Controller

- `git clone https://github.com/danielrozenberg/Subway-Board/`
- `cd ~/Subway-Board/led_controller`
- `cp options_EXAMPLE.py options.py`
- Edit `options.py` for your setup with your favourite editor

## System service

- `cd ~/Subway-Board`
- `sudo cp subway-board-led-controller.service /lib/systemd/system/`
- `sudo systemctl daemon-reload`
- `sudo systemctl enable subway-board-led-controller.service`
- `sudo systemctl start subway-board-led-controller.service`
  - Note that this step will not do anything until the server is on.

# Software (Server)

You can set up the server on a separate machine or on the same RPi. However, my
experience is that the RPi 2 is too weak to run both server and LED controller.
The RPi 4 is strong enough.

## Basic setup

- Install dependencies
  `sudo apt install git libjpeg8-dev python3-dev python3-pil`
- Install PyEnv `curl https://pyenv.run | bash` and follow the instructions.
  Don't forget to restart your bash.
- Install Python 3.9.x (whichever is newest) server `pyenv install 3.9.x`
  (replace `x` with the highest autocomplete value)
- Create a virtualenv `pyenv virtualenv 3.9.x subway-board`

## Server

- `git clone https://github.com/danielrozenberg/Subway-Board/` (skip this step
  if you are running the server on the same RPi as the LED controller)
- `cd ~/Subway-Board/server`
- `cp options_EXAMPLE.py options.py`
- Edit `options.py` for your setup with your favourite editor
- Activate the virtualenv `pyenv local subway-board` (this will activate it
  permanently on this directory)
- Install Python dependencies `pip install -r requirements.txt`

## System service

- `cd ~/Subway-Board`
- `sudo cp subway-board-server.service /lib/systemd/system/`
  - If you are running the server on a separate machine, edit the copied file
    and adjust the file paths
- `sudo systemctl daemon-reload`
- `sudo systemctl enable subway-board-server.service`
- `sudo systemctl start subway-board-server.service`
