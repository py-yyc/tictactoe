"""
TicTacToe

x goes first
board is a list of 9 elements from ['x','o','.']. '.' means empty spot.
"""

states = [
    'x wins',
    'o wins',
    'draw',
    'invalid',
    'incomplete',
]

def game_state(board):
    if len(board) != 9:
        return 'invalid'
    for c in board:
        if c not in ('x', 'o', '.'):
            return 'invalid'
    return 'fixme'
