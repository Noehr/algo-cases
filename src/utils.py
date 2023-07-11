"""
    src/utils.py

    This file provides useful classes, enums, functions, etc. to be used by multiple other modules. 
"""


from enum import Enum




# Color enum for the 6 sides of 
class Color(Enum):
    WHITE = 1
    RED = 2
    BLUE = 3
    YELLOW = 4
    ORANGE = 5
    GREEN = 6


class Moves(Enum):
    R = 1
    F = 2
    U = 3
    L = 4
    D = 5
    B = 6
    R2 = 7
    F2 = 8
    U2 = 9
    L2 = 10
    D2 = 11
    B2 = 12
    RP = 13
    FP = 14
    UP = 15
    LP = 16
    DP = 17
    BP = 18


