#!/usr/bin/env -S python3 -u
import datetime
import time

import serial

# TODO:
# move to Pipenv
# run it in Pipenv


class Device:
    def __init__(self, uhub_location, uhub_port, arduino_serial):
        self.uhub_location = uhub_location
        self.uhub_port = uhub_port
        self.arduino_serial = arduino_serial
        self.serial = serial.Serial(arduino_serial, 9600)

    def power_on(self):
        raise NotImplementedError

    def power_off(self):
        raise NotImplementedError

    def touch(self, location, action):
        raise NotImplementedError

    @staticmethod
    def wait(seconds):
        Device.now()
        print("[software] Waiting for {} seconds...".format(seconds))
        time.sleep(seconds)

    @staticmethod
    def now():
        print("\n[timestamp] {}".format(datetime.datetime.now()))
