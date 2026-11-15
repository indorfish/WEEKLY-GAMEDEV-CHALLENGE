#!/usr/bin/env python3.10

import TicTacToe as TTT
import time


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

TicTacToe = TTT.TicTacToe()
players = ["X", "O"]

# make sure everything is set up right before inviting user to play
print(GREETING)



"""
=========================================================
GAME LOOP
=========================================================
"""
while (GAME_ACTIVE):
    # request player 1 input
    print(f"Current Player: {TicTacToe.currentSymbol}")
    cellIndex_i = int(input("Which row? "))
    cellIndex_j = int(input("Which column? "))
    cellIndex = [cellIndex_i, cellIndex_j]
    if TicTacToe.updateGame(cellIndex) == False:
        print("Invalid index! (Each entry must be between 0, 1, 2)")
        continue
    elif TicTacToe.updateGame(cellIndex) == None:
        print("Game Over.")
        break

    
    # temporary
    count += 1
    if (count > 20):
        GAME_ACTIVE = False

    time.sleep(0.1) # pauses for one second

"""
=========================================================
CLEAN UP AND EXIT
=========================================================
"""
print(EXIT_MESSAGE)
