#!/usr/bin/env python3.10

from TicTacToe import *

"""
Required tests:

"""

demarcation = 30*"_"
ttt = TicTacToe()

# empty board
print(demarcation)
print(ttt)
sz = ttt.boardSize

# board full of X's
for i in range(sz):
    for j in range(sz):
        ttt.writeCell([i,j], SYMBOLS["X"])
print(demarcation)
print(ttt)

# left of board full of O's
for i in range(sz):
    for j in range(sz-1):
        ttt.writeCell([i,j], SYMBOLS["O"])
print(demarcation)
print(ttt)

# diagonal emptied out
for i in range(sz):
    ttt.writeCell([i,i], SYMBOLS["-"])
print(demarcation)
print(ttt)
