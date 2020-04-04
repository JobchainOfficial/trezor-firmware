import sys

import yaml
from device.t1 import TrezorOne


def main():
    with open("config.yml", "r") as ymlfile:
        config = yaml.safe_load(ymlfile)

    t1 = TrezorOne(config["usb_location"], config["usb_port"], config["arduino_serial"])
    t1.update_firmware(sys.argv[1])


if __name__ == "__main__":
    main()
