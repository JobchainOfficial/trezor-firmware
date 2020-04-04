import configparser
import sys

from device.t1 import TrezorOne


def main(version: str):
    config = configparser.ConfigParser()
    config.read_file(open("hardware.cfg"))
    t1 = TrezorOne(
        config["usb"]["location"],
        config["usb"]["port"],
        config["usb"]["arduino_serial"],
    )
    t1.update_firmware(version)


if __name__ == "__main__":
    main(sys.argv[1])
