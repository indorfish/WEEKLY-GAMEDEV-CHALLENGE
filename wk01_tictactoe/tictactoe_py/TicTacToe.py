#!/usr/bin/env python3.10


"""
TicTacToe
    an abstract model of the TicTacToe board game.
    
    symbols: a dictionary of symbols.
    boardSize: the side length of the board size, in number of cells. Square dimensions.
    winState: a dictionary of win states to indicate whether game is in progress or is in draw
              or win state.
    
-   Attributes:
    -   Symbols (null, X, O)
    -   3-by-3 Board with cells
    -   win state: PLAYING, WIN, DRAW
-   Methods:
    -   updateBoard(cell, symbol) // implements state update rules
    -   validateWin(board)        // checks for win or playing or draw condition
    -   reset()                   // resets to default values
"""
SYMBOLS = {"-": " ", "X": "X", "O": "O"}
BOARD_SIZE = 3  # 3-by-3
WIN_STATES = {"PLAYING": 0, "WIN": 1, "DRAW": 2}
class TicTacToe:
    # defaults and constant data. Like enums in C
    def __init__(self):
        self.symbols = SYMBOLS
        self.boardSize = BOARD_SIZE
        self.winState = WIN_STATES["PLAYING"]
        self.board = self.init_board(SYMBOLS["-"])
        self.winner = SYMBOLS["-"]

    def init_board(self, initSymbol):
        sz = self.boardSize
        # build the array
        if not self.validateSymbol(initSymbol):
            raise ValueError
        board = [[initSymbol for i in range(sz)] for j in range(sz)]
        return board

    """
    writeCell
    -   cellIndex is an ordered pair [i,j]
    -   symbol should be an item from SYMBOLS
    -   maybe return a value indicating if the write was successful
    """
    def writeCell(self, cellIndex, newSymbol):
        # validate the inputs first. Correct type, valid values. Else this will crash.
        if not self.validateInput(cellIndex, newSymbol):
            raise ValueError
        i = cellIndex[0]
        j = cellIndex[1]
        self.board[i][j] = newSymbol

    """
    readCellState
    -   cellIndex is an ordered pair [i, j]
    -   symbol should be an item from SYMBOLS
    -   return the symbol in the given cell
    """
    def readCellState(self, cellIndex):
        if not self.validateinput(cellIndex):
            raise ValueError
        i = cellIndex[0]
        j = cellIndex[1]
        return self.board[i][j]

    """
    updateWinState
    -   validates and updates win state
    -   checks board for a win state. If there is a winner, tells us the winner.
    """
    def updateWinState(self):
        self.winState = WIN_STATES["DRAW"]


    """
    How the board is printed in the console. 
    Technically should be the Renderer's responsibility.
    """
    def __str__(self):
        board = self.board
        string = ""
        for row in board:
            for cell in row:
                string += str(cell) + " "
            string += "\n"
        return string + "\n"

    """
    validateSymbol
    """
    def validateSymbol(self, symbol):
        return type(symbol) == type(SYMBOLS["-"])

    """
    validateInput
        An input validation function for convenience.
    """
    def validateInput(self, cellIndex, symbol=SYMBOLS["-"]):
        LIST_TYPE = type([[]])
        INT_TYPE = type(1)
        SYMBOL_TYPE = type(SYMBOLS["-"])
        if not cellIndex:
            validCell = False
        else:
            validCell = type(cellIndex) == LIST_TYPE
            validCell = validCell and len(cellIndex) == 2
            # in general create a logical array over all indices and reduce with AND
            validCell = type(cellIndex[0]) == INT_TYPE and type(cellIndex[1]) == INT_TYPE
        if not symbol:
            validSymbol = False
        else:
            validSymbol = type(symbol) == SYMBOL_TYPE
        return validCell and validSymbol


