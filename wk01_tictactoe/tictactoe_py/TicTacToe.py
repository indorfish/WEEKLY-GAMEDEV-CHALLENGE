#!/usr/bin/env python3.10

SYMBOLS = {"-": " ", "X": "X", "O": "O"}
DEFAULT_BOARD_SIZE = 3  # 3-by-3
WIN_STATES = {"PLAYING": 0, "WIN": 1, "DRAW": 2}
# state outputs are important status signals for game update requests
STATE_OUTPUTS = { \
    "OCCUPIED": 0, \
    "GAME_OVER": 1, \
    "SUCCESSFUL_WRITE": 2, \
    "INVALID_INPUT": 3 \
}

"""
validateSymbol
"""
def validateSymbol(symbol):
    SYMBOL_TYPE = type(SYMBOLS["-"])
    validSymbol = False

    if not symbol:
        raise ValueError

    # check that it's the correct type
    validSymbol = type(symbol) == SYMBOL_TYPE
    # check that it's the correct range of permitted values
    # or is associative, so it's fine
    v1 = (symbol == SYMBOLS["-"]) or (symbol == SYMBOLS["X"]) or (symbol == SYMBOLS["O"])
    validSymbol = validSymbol and v1
    return validSymbol


"""
validateIndex
    ensure indexing has proper format
"""
def validateIndex(index, size=2, rows=3, columns=3):
    LIST_TYPE = type([[]])
    INT_TYPE = type(1)
    # quite the pessimist, I see
    validIndex = False
    if not index:
        raise ValueError

    # we could just use several assert statements, frankly
    # check that it is a list type [i, j]
    validIndex = type(index) == LIST_TYPE
    # check that it also has the right number of elements
    validIndex = validIndex and len(index) == size
    # check that the items are ints
    # in general create a logical array over all indices and reduce with AND
    validIndexValues = type(index[0]) == INT_TYPE and type(index[1]) == INT_TYPE
    validIndex = validIndex and validIndexValues
    # check that the indices have proper range/bounds
    validRange = index[0] >= 0 and index[1] < columns
    validRange = validRange & (index[0] >= 0 and index[1] < rows)
    validIndex = validIndex & validRange
    return validIndex


"""
validateInput
    An input validation function for convenience.
"""
def validateInput(cellIndex, symbol=SYMBOLS["-"]):
    return validateIndex(cellIndex) and validateSymbol(symbol)


"""
TicTacToe
    an abstract model of the TicTacToe board game.
    Pay special attention to the __init__ and updateGame. Those two are the core of the game
    logic.

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

class TicTacToe:
    # defaults and constant data. Like enums in C
    def __init__(self, initialSymbol=SYMBOLS["X"]):
        assert validateSymbol(initialSymbol) == True
        self.symbols = SYMBOLS
        # marks the symbol whose current turn it is.
        self.currentSymbol = initialSymbol
        # board is initialized with empty symbols
        self.board = Board(SYMBOLS["-"])
        self.winState = WIN_STATES["PLAYING"]
        # the winner is either X or O or None
        self.winningSymbol = None

    """
    updateGame
        updates the state of the game. Index of cell is provided
        First the player requests to write their symbol at a chosen cellIndex.
        It is an essential assumption of TTT that the symbol alternates between X and O,
        thus it is the user's responsibility to ensure that the player state update
        respects this.
        If the requested cell is not empty then the write request is rejected and False is
        returned, indicating a failed state update. This is Moore-like state machine
        If the requested cell is empty, honor the write request.
        Then check if the resulting board state is a winning state. If so, declare the winner
        as the currentSymbol.
        If it's a draw state, then declare draw.
        Else, toggle the currentSymbol

        Needed update: return better output. Try this - the output should be the winner,
        or False, or None.
        False indicates invalid input. None indicates an end state reached.
    """
    def updateGame(self, cellIndex):
        # if the WINNING_STATE is WIN or DRAW, then don't update anything.
        if self.winState != WIN_STATES["PLAYING"]:
            return STATE_OUTPUTS["GAME_OVER"]
        # if the requested index is occupied, return report and update nothing.
        if self.board.readCell(cellIndex) != self.symbols["-"]:
            # it shouldn't be the TTT object printing status.
            print(f"Cell {cellIndex} currently occupied! Try another cell.")
            return STATE_OUTPUTS["OCCUPIED"]
        # otherwise 
        s = self.board.writeCell(cellIndex, self.currentSymbol)
        if not s:
            return 

        # check if board has been placed in winning state. Update as needed
        self.winState = self.updatedWinningState()
        if self.winState == WIN_STATES["PLAYING"]:
            # toggle the symbol. This is a core assumption of TTT
            self.toggleSymbol()
            return STATE_OUTPUTS["SUCCESSFUL"]
        # otherwise declare the winner (if any) and end the game
        elif self.winState == WIN_STATES["DRAW"]:
            self.winningSymbol = self.symbols["-"]
            return None
        else:
            self.winningSymbol = self.currentSymbol
            return self.winningSymbol


    """
    toggleSymbol
        toggles currentSymbol between X and O
    """
    def toggleSymbol(self):
        if (self.currentSymbol == self.symbols["X"]):
            self.currentSymbol = self.symbols["O"]
        elif (self.currentSymbol == self.symbols["O"]):
            self.currentSymbol = self.symbols["X"]

    """
    checkWinningState
    -   checks if current board state is in winning state
    -   updates as needed and returns current state.
    """
    def updatedWinningState(self):
        return self.winState

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
Board
    models the TicTacToe board, so as to simplify TTT's interface.
    Coordinate system: Zero-indexing, positive directions flow to the left and downward
    (the standard in Computer Graphics).
       0  1  2
       --------
    0 |X  O  X |
    1 |O  X  O |
    2 |O  -  X |
       --------
    The Board class does not need to be intelligent. Think of it simply as a register
    or region of memory; it holds data, allows reads and writes and does basic validation.
"""
class Board:
    def __init__(self, initSymbol, boardSize=DEFAULT_BOARD_SIZE):
        grid = [[initSymbol for i in range(boardSize)] \
                 for j in range(boardSize)]

    def writeCell(self, cellIndex, newSymbol):
        # validate the inputs first. Correct type, valid values. Else this will crash.
        if not validateInput(cellIndex, newSymbol):
            raise ValueError
        i = cellIndex[0]
        j = cellIndex[1]
        self.grid[i][j] = newSymbol
        # was the write successful?
        return self.grid[i][j] == newSymbol

    def readCell(self, cellIndex):
        if not validateinput(cellIndex):
            raise ValueError
        i = cellIndex[0]
        j = cellIndex[1]
        return self.board[i][j]

    # read multiple cells at once. Returns a dictionary of index-value pairs.
    def readCells(self, cellIndices):
        if not validateInput(cellIndices):
            raise ValueError
        return None

    def init_board(self, initSymbol):
        sz = self.boardSize
        # build the array
        if not self.validateSymbol(initSymbol):
            raise ValueError
        board = [[initSymbol for i in range(sz)] for j in range(sz)]
        return board


