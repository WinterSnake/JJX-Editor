##-----------------------------##
## Junk Jack X Editor          ##
## Written By: Ryan Smith      ##
##-----------------------------##
## Player Class                ##
##-----------------------------##

## Imports
from __future__ import annotations


## Classes
class Player:
    """"""

    # -Constructor
    def __init__(
        self, name: str, gender: bool, skin: int,
        hair_style: int, hair_color: int, difficulty: int,
        permadeath: bool, simple_craft: bool, perpetual_time: bool
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
