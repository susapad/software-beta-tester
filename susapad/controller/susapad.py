"""Module to manage SusaPad's configuration and connection"""

import time

import serial
import serial.tools.list_ports
from PySide6 import QtCore


class SusaPad:

    def __init__(self, debug: bool = False):
        self.debug = debug
        self.serial: [serial.Serial | None] = None
        self.sensibility: int = 200
        self.rapid_trigger: bool = True

    
    def find(self) -> str:
        """Looks for connected SusaPad device's port"""
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            if "VID:PID=0727:0727" in hwid:
                print("Susapad encontrado!")
                print("{}: {} [{}]".format(port, desc, hwid))
                return port 
        return ""

    def connect(self, port) -> bool:
        """Connect to SusaPad given a port"""
        try:
            self.serial = serial.Serial(port, 9600)
            return True
        except:
            if self.debug:
                return True
            else:
                self.disconect
                return False

    def disconnect(self):
        """Set `self.susapad_port` as None, virtually closing the connection"""
        self.serial = None


    # Settings functions
    def set_rapid_trigger(self, on: bool = True) -> bool:
        """Set if SusaPad's Rapid Trigger is **on** or **off**"""
        n = 1 if on else 0
        return self.__configure_susapad("rt", n)

    def set_sensibility(self, value: int) -> bool:
        """"Set SusaPad's sensibility"""
        return self.__configure_susapad("rts", value)

    def set_hysteresis(self, value: int) -> bool:
        """Set SusaPad's Actuation ponit"""
        r1 = self.__configure_susapad("uh", value)
        r2 = self.__configure_susapad("lh", value - 10)
        return r1 and r2

    def save(self) -> bool:
        try:
            time.sleep(1)
            print(f"save")
            self.serial.write(f"save".encode())
            self.serial.flush()
            return True
        except:
            if self.debug:
                return True
            else:
                return False


    # Internal functions

    def __configure_susapad(self, command: str, value: int) -> bool:
        try:
            time.sleep(1)
            print(f"{command} {value}")
            self.serial.write(f"{command} {value}".encode())
            self.serial.flush()
            return True
        except:
            if self.debug:
                return True
            else:
                return False
