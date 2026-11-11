#!/usr/bin/env python3.10

"""
QUICK SKETCH OF A TIC-TAC-TOE GAME IN PYTHON
"""

SYMBOLS = {"null": "", \
              "X": "X", \
              "O":"O"}

# represents a cell in a TTT grid
class Cell:
    def __init__(self, sym="", number=0):
        self.symbol = sym
        self.number = number

    def getID(self):
        return self.number

    def getSymbol(self):
        return self.symbol

    def setID(self, newId):
        self.number = newId

    def setSymbol(self, newSymbol):
        self.symbol = newSymbol


# the Tic-Tac-Toe Board
class Board:
    BOARD_SIZE = 3
    def __init__(self, initSymbol=""):
        sz = Board.BOARD_SIZE
        # also give each cell a unique id. Move this to a private method.
        self.grid = [[Cell(initSymbol) for i in range(sz)] for j in range(sz)]
        self.activeCellIndex = (0, 0)

    def __str__(self):
        grid = self.grid
        string = ""
        for row in grid:
            for cell in row:
                string += cell.getSymbol() + " "
            string += "\n"
        return string + "\n"

    # index is expected to be a pair (i, j)
    def writeCell(self, index, newSym):
        if not index:
            raise ValueError("Index must not be empty!")
        i = index[0]
        j = index[1]
        sz = Board.BOARD_SIZE
        # make sure to check that i and j are within bounds.
        assert i >= 0 and i < sz
        assert j >= 0 and j < sz
        activeCell = self.grid[i][j]
        activeCell.setSymbol(newSym)

    # returns current state of a cell
    def readCell(self, index):
        if not index:
            raise ValueError("Index must not be empty!")
        i = index[0]
        j = index[1]
        sz = Board.BOARD_SIZE
        # make sure to check that i and j are within bounds.
        assert i >= 0 and i < sz
        assert j >= 0 and j < sz
        cell = self.grid[i][j]
        return {"symbol": cell.getSymbol(), "id": cell.getID()}


