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

def vertical_win(board, who):
    for col in range(3):
        num = 0
        for row in range(3):
            if board[row * 3 + col] == who:
                num += 1
        if num == 3:
            return True
    return False

def diagonal_win(board, who):
    n = 0
    for p in range(3):
        if board[(p * 3) + p] == who:
            print board[(p * 3) + p], (p * 3) + p
            n += 1
    if n == 3:
        return True
    return False

def game_state(board):
    if len(board) != 9:
        return GameStates.invalid
    for c in board:
        if c not in ('x', 'o', '.'):
            return GameStates.invalid
    diff = x_count(board) - o_count(board)
    if diff not in (0, 1):
        return GameStates.invalid
    stuff = [
        ('x', GameStates.x_wins),
        ('o', GameStates.o_wins),
    ]
    # x, o wins cases (8 cases)
    for who, result in stuff:
        xt = [who, who, who]
        if board[:3] == xt or board[3:6] == xt or board[6:] == xt:
            return result
        if vertical_win(board, who):
            return result
        if diagonal_win(board, who):
            return result

    # draws cases FIXME
    return GameStates.incomplete
