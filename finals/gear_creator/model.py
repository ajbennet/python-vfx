from enum import Enum


class Size(Enum):
    Small = 1
    Medium = 2
    Large = 3


class Location(Enum):
    Top = 1
    Right = 2
    Bottom = 3
    Left = 4


class GearProperty:
    def __init__(self, rotation='frame', size=Size.Medium):
        self.rotation = rotation
        self.size = size
