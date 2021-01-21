##-----------------------------##
## Junk Jack X Editor          ##
## Written By: Ryan Smith      ##
##-----------------------------##
## Player Class                ##
##-----------------------------##

## Imports
from __future__ import annotations
from pathlib import Path
from enum import Enum
import struct
from typing import Union


## Classes
class Gender(Enum):
    """Gender of player"""
    Male = 0
    Female = 1


class HairColor(Enum):
    """Hair color of player"""
    White = 0x00
    Gray = 0x10
    Black = 0x20
    Brown = 0x30
    Dark_Brown = 0x40
    Light_Brown = 0x50
    Blonde = 0x60
    Dirty_Blonde = 0x70
    Bleach_Blonde = 0x80
    Orange = 0x90
    Scarlet = 0xA0
    Purple = 0xB0
    Navy = 0xC0
    Teal = 0xD0
    Green = 0xE0
    Yellow = 0xF0


class Difficulty(Enum):
    """Local difficulty of player"""
    Peaceful = 0
    Easy = 1
    Normal = 2
    Hard = 3
    Very_Hard = 4


class Player:
    """"""

    # -Constructor
    def __init__(
        self, name: str, gender: Gender, skin_tone: int,
        hair_style: int, hair_color: HairColor,
        difficulty: Difficulty = Difficulty.Normal,
        hardcore: bool = False, simple_craft: bool = False,
        perpetual_time: bool = False
    ) -> Player:
        ''''''
        # -Character
        self.name: str = name
        self.gender: Gender = gender
        self.skin_tone: int = skin_tone
        self.hair_style: int = hair_style
        self.hair_color: HairColor = hair_color
        # -Gameplay options
        self.difficulty: Difficulty = difficulty
        self.hardcore: bool = hardcore
        self.simple_craft: bool = simple_craft
        self.perpetual_time: bool = perpetual_time
        # -Inventory

    # -Class Methods
    @classmethod
    def from_file(cls, fp: Union[str, Path]) -> Player:
        '''Returns a player object from a binary player file'''
        def _get_byte(_int: Union[int, bytes]):
            '''Tries to unpack and return the int value'''
            try:
                return struct.unpack('B', _int)[0]
            except TypeError:
                return _int

        with open(fp, 'rb') as f:
            # -Name [0x58 : 0x66 (0x67 == null terminator)]
            name = (f.read(0x68)[-16:]).decode('utf-8')
            # -Gameplay options [0x71]
            # -hardcore/simple craft/perpetual time
            t = _get_byte(f.read(9)[-1])
            hard = bool(t & 1)
            crft = bool(t & 2)
            time = bool(t & 4)
            # -Character: hair color [0x74]
            t = _get_byte(f.read(4)[-1])
            for c in HairColor:
                if t == c.value:
                    hclr = c
            # -Character: gender/skin tone/hair style [0x75]
            t = _get_byte(f.read(1))
            tu = (t & 0xF0) >> 4
            gndr = Gender.Female if tu % 2 else Gender.Male
            tone = tu >> 1
            hair = t & 0x0F
            # -Gameplay options: difficulty [0x78]
            t = _get_byte(f.read(3)[-1])
            for d in Difficulty:
                if t == d.value:
                    diff = d
            # -Inventory [0x7A : 0x0415]
        # -Return new player object
        return cls(name, gndr, tone, hair, hclr, diff, hard, crft, time)
