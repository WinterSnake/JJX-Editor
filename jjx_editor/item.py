##-----------------------------##
## Junk Jack X Editor          ##
## Written By: Ryan Smith      ##
##-----------------------------##
## Item + Container Class      ##
##-----------------------------##

## Imports
from __future__ import annotations
from typing import List, Optional


## Functions


## Classes
class Item:
    """"""

    # -Constructor
    def __init__(self, _id: int, amount: int, durability: int) -> Item:
        self.id: int = _id
        self.amount: int = amount
        self.durability: int = durability


class Container:
    """"""

    # -Constructor
    def __init__(
        self, *args: Optional[Item],
        items: List[Optional[Item]] = None
    ) -> Container:
        if items:
            self.items = items
        else:
            self.items = [*args]
        self.size = len(self.items)
