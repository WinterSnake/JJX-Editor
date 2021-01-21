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
        self, name: str, gender: Gender, skin: int,
        hair_style: int, hair_color: HairColor,
        difficulty: Difficulty = Difficulty.Normal,
        permadeath: bool = False, simple_craft: bool = False,
        perpetual_time: bool = False
    ) -> Player:
        ''''''
        # -Character
        self.name = name
        self.gender = gender
        self.skin = skin
        self.hair_style = hair_style
        self.hair_color = hair_color
        # -Gameplay options
        self.difficulty = difficulty
        self.permadeath = permadeath
        self.simple_craft = simple_craft
        self.perpetual_time = perpetual_time
        # -Inventory

    # -Class Methods
    @classmethod
    def from_file(cls, fp: Union[str, Path]) -> Player:
        '''Returns a player object from a binary player file'''
        pass
