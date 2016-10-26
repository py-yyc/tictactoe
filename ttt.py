"""
TicTacToe

x goes first
board is a list of 9 elements from ['x','o','.']. '.' means empty spot.
"""

import types

class GameStates(object):
    """
    there are lots of ways to accomplish an enum like object
    this is the one we're going with since it's simple
    """
    invalid    = 0
    unfinished = 1
    x_wins     = 2
    o_wins     = 3
    draw       = 4

def game_state(board):
    return states # you decide what should get returned here
