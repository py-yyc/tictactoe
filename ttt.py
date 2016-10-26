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
    return Board(board).current_state()

class Board(object):

    def __init__(self, board):
        self.board = board

    def row(self, n):
        return self.board[n*3:n*3+3]


    def col(self, n):
        ret = []
        for i in range(3):
            ret.append( self.board[n+i*3] )

        return ret

    def diag(self, n):
        "0 is diag down-left \, 1 is diag down-right /"
        ret = []
        if n == 0:
            for i in range(3):
                ret.append(self.board[i*4])
        if n == 1:
            for i in range(3):
                ret.append(self.board[2+i*2])

        return ret

    def current_state(self):
        if not isinstance(self.board, types.ListType):
            return GameStates.invalid

        if len(self.board) != 9:
            return GameStates.invalid

        if abs( self.board.count('x') - self.board.count('o') ) > 1:
            return GameStates.invalid

        if self.board.count('x') < self.board.count('o'):
            return GameStates.invalid

        return GameStates.unfinished
