#!/usr/bin/env -S python3 -u

import os

from .device import Device


class TrezorOne(Device):
    def power_on(self):
        self.now()
        print("[hardware/usb] Turning power on...")
        os.system(
            "uhubctl -l {} -p {} -a on > /dev/null".format(
                self.uhub_location, self.uhub_port
            )
        )
        self.wait(3)

    def power_off(self):
        self.now()
        print("[hardware/usb] Turning power off...")
        os.system(
            "uhubctl -l {} -p {} -r 100 -a off > /dev/null".format(
                self.uhub_location, self.uhub_port
            )
        )
        self.wait(3)

    def touch(self, location, action):
        self.now()
        print(
            "[hardware/trezor] Touching the {} button by {}...".format(location, action)
        )
        self.serial.write(("{} {}\n".format(location, action)).encode())

    def update_firmware(self, version):
        if "http" in version:
            unofficial = True
            trezorctlcmd = "trezorctl firmware-update -s -u {} &".format(version)
        elif "bin" in version:
            unofficial = True
            trezorctlcmd = "trezorctl firmware-update -s -f {} &".format(version)
        else:
            unofficial = False
            trezorctlcmd = "trezorctl firmware-update -v {} &".format(version)
        self._enter_bootloader(version)

        print("[software/trezorctl] Updating the firmware to {}...".format(version))
        os.system(trezorctlcmd)
        self.wait(3)
        self.touch("right", "click")
        self.wait(20)
        if unofficial:
            self.touch("right", "click")
        self.wait(10)
        self.power_off()
        self.power_on()
        if unofficial:
            self.touch("right", "click")
            self.wait(5)
            self.touch("right", "click")
        self.wait(5)
        os.system("trezorctl get-features|grep version")

    def _enter_bootloader(self, version):
        self.power_off()
        if "1.8" in version:
            self.touch("left", "press")
        else:
            self.touch("all", "press")
        self.wait(2)
        self.power_on()
        self.wait(2)
        self.touch("all", "unpress")
