#!/usr/bin/env python3.10

"""
QUICK SKETCH OF A TIC-TAC-TOE GAME IN PYTHON
"""

SYMBOLS = {"null": "", "X": "X", "O":"O"}

# represents a cell in a TTT grid
class Cell:
    def __init__(self, sym="", id=0):
        self.symbol = sym
        self.id = id

    def getID(self):
        return self.id

    def getSymbol(self):
        return self.symbol

    def setID(self, newId):
        self.id = newId

    def setSymbol(self, newSymbol):
        self.symbol = newSymbol


# the Tic-Tac-Toe Board
class TTTBoard:
    BOARD_SIZE = 3
    def __init__(self, initSymbol=""):
        sz = TTTBoard.BOARD_SIZE
        # also give each cell a unique id. Move this to a private method.
        self.grid = [[Cell(initSymbol) for i in range(sz)] for j in range(sz)]

    def __str__(self):
        grid = self.grid
        string = ""
        for row in grid:
            for cell in row:
                string += cell.getSymbol() + " "
            string += "\n"
        return string + "\n"

    # index is expected to be a pair (i, j)
    def setCell(self, index, newSym):
        if not index:
            return
        i = index[0]
        j = index[1]
        sz = TTTBoard.BOARD_SIZE
        assert i >= 0 and i < sz
        assert j >= 0 and j < sz
        # make sure to check that i and j are within bounds.
        activeCell = self.grid[i][j]
        activeCell.setSymbol(newSym)




# main loop
board = TTTBoard(SYMBOLS["X"])
print(board)
for i in range(3):
    board.setCell([i,i], SYMBOLS["O"])
print(board)
