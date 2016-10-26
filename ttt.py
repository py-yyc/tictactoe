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


def x_count(board):
    return len([ch for ch in board if ch == 'x'])

def o_count(board):
    return len([ch for ch in board if ch == 'o'])

def game_state(board):
    if len(board) != 9:
        return 'invalid'
    for c in board:
        if c not in ('x', 'o', '.'):
            return 'invalid'
    diff = x_count(board) - y_count(board)
    if diff not in (0, 1):
        return 'invalid'
    # x wins cases (8 cases)
    xt = ['x', 'x', 'x']
    if board[:3] == xt or board[3:6] == xt or board[6:] == xt:
        return 'x wins'
    
