#!/usr/bin/env python3.10

import TicTacToe as TTT


"""
=========================================================
INITIALIZE RESOURCES
=========================================================
"""
GREETING = """Hello, Welcome to Tic-Tac-Toe!
    It is a two-player game.
    You are Player 1 (X) by default; Player 2 (O) can be an AI or human player.
    Both players take alternating turns placing their symbol in empty cells.
    The player who first matches three adjacent copies of their symbols, wins!
    For example, for Player 1 to win they have to have three X's in a row, column or diagonal.
"""
EXIT_MESSAGE = """ Thank you for playing! """
GAME_ACTIVE = True
count = 0

TicTacToe = TTT.TicTacToe();

# make sure everything is set up right before inviting user to play
print(GREETING)



"""
=========================================================
GAME LOOP
=========================================================
"""
while (GAME_ACTIVE):
    # code for state update. Note that this game may not need a clock, as it updates
    # only when a player places a symbol
    count += 1
    if (count > 20):
        GAME_ACTIVE = False



"""
=========================================================
CLEAN UP AND EXIT
=========================================================
"""
print(EXIT_MESSAGE)
