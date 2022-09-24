from enum import Enum


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Location(Enum):
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 4


class GearProperty:
    def __init__(self, rotation='frame', size=Size.MEDIUM):
        self.rotation = rotation
        self.size = size
