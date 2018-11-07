# -*- coding: utf-8 -*-
from enum import Enum

from node import *


class TileType(Enum):
    PATH = 1#.: chemin (1)
    GRASS = 2# : herbe (2)
    WATER = 3#X: eau (infranchissable)
    BRIDGE = 4#=: pont (2)
    TREE = 5#*: arbre (infranchissable)

class TileConverter:
    def typeFromChar(char):
        if char == '.':
            return TileType.PATH
        elif char == ' ':
            return TileType.GRASS
        elif char == 'X':
            return TileType.WATER
        elif char == '=':
            return TileType.BRIDGE
        elif char == '*':
            return TileType.TREE
        else:
            return None

class Tile(Node):
    def __init__(self, _row, _col, _type):
       self.tileType = _type
       self.row = _row
       self.col = _col
       super().__init__()

    def isValidPath(self):
        return self.tileType is TileType.PATH or self.tileType is TileType.GRASS or self.tileType is TileType.BRIDGE

    def cost(self):
        if self.tileType is TileType.PATH:
            return 1
        elif self.tileType is TileType.GRASS or self.tileType is TileType.BRIDGE:
            return 2
        else:
            return float('inf')
    
    def __repr__(self):
        return " (Tile: row={}, col={}, type={})".format(self.row, self.col, self.tileType)
        
def testClass():
    t = Tile(1, 2, TileType.BRIDGE)
    print(t, t.cost(), t.isValidPath())
    t = Tile(3, 4, TileType.TREE)
    print(t, t.cost(), t.isValidPath())
    
    print(TileConverter.typeFromChar('.'))
    print(TileConverter.typeFromChar(' '))
    print(TileConverter.typeFromChar('X'))
    print(TileConverter.typeFromChar('='))
    print(TileConverter.typeFromChar('*'))

if __name__ == '__main__':
    testClass()