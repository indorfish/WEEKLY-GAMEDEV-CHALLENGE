#!/usr/bin/env python3.10

from TicTacToe import *

"""
A Player interacts with the game progam flow itself (e.g. restarting, pausing) and with the board obviously.
The Game presents the Board to the Player (upon the player's implicit request by choosing to start the game). The Game also presents the visuals and audio you designed, as you designed them.
The Player interacts with the Board (and the program itself) using the Controller.
We have to distinguish the game (of tictactoe) from the game (the software implementing tictactoe).
To emphasize this distinction, we call the former TicTacToe and the latter GameProgram.

Required tests:
1. Program start up test (the program starts, runs the game loop
2. Program exit test: the program exits when prompted, without crashing. This is pedantry and I won't implement it for such a simple game, but it's worth keeping this in mind.
3. The board is represented accurately. To test this, simulate a sequence of plays and assert that the board has the correct symbol in the relevant cell.
4. The board is drawn accurately. To test this, augment the representation tests with visuals.
5. The game state updates correctly.
4. Controls are correctly mapped and ...

Honestly, there are loads and loads of tests one could write.
Maybe this is where LLMs can come in handy - let an LLM write tests for you, and maybe even execute the tests.
There's no need to overthink such a small game, but when the game you're building gets larger and has many moving parts, you will need to think about how to test it.

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
