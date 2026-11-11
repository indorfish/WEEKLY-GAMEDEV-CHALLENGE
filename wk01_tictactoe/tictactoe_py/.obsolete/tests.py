#!/usr/bin/env python3.10

from TicTacToe import *

"""
Required tests:

"""

if __name__ == "__main__":
# main loop
    board = Board(SYMBOLS["X"])
    print(board)
    for i in range(3):
        board.setCell([i,i], SYMBOLS["O"])
    print(board)
