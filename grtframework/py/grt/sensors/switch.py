__author__ = "Calvin Huang"

from wpilib import DigitalInput
from grt.core import Sensor


class Switch(Sensor):
    """
    Sensor wrapper for a switch.

    Has boolean attribute pressed.
    """

    pressed = False

    def __init__(self, channel, module=1, reverse=False):
        """
        Initializes the switch on some digital channel and module.
        Normally assumes switches are active low.
        """
        super().__init__()
        self.s = DigitalInput(module, channel)
        self.reverse = reverse

    def poll(self):
        self.pressed = not self.s.Get() ^ self.reverse
