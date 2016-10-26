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
            n += 1
    if n == 3:
        return True

    if board[2] == who and board[4] == who and board[6] == who:
        return True

    return False

def is_winner(board, who):
    # x, o wins cases (8 cases)
    xt = [who, who, who]
    if board[:3] == xt or board[3:6] == xt or board[6:] == xt:
        return True
    if vertical_win(board, who):
        return True
    if diagonal_win(board, who):
        return True
    return False

def game_state(board):
    """
    Given
    """
    if len(board) != 9:
        return GameStates.invalid
    for c in board:
        if c not in ('x', 'o', '.'):
            return GameStates.invalid
    diff = x_count(board) - o_count(board)
    if diff not in (0, 1):
        return GameStates.invalid

    # x or o winning cases
    if is_winner(board, 'x') and is_winner(board, 'o'):
        return GameStates.invalid
    if is_winner(board, 'x'):
        return GameStates.x_wins
    if is_winner(board, 'o'):
        return GameStates.o_wins

    # draw cases (basically: board has no empty spaces, and we haven't
    # detected a winner yet
    if len([ch for ch in board if ch == '.']) == 0:
        return GameStates.draw

    # everything else is just incomplete
    return GameStates.unfinished
