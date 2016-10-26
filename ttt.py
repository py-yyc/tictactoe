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


list_of_possibilities = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(6,4,2)]


def check_win(board, which):
    for poss in list_of_possibilities:
        if board[poss[0]]== which and board[poss[1]]==which and board[poss[2]]==which:
            return True
    return False



def game_state(board):
    if len(board) != 9:
        return GameStates.invalid
         
    if board.count("x") - board.count("o") > 1 or board.count("x") - board.count("o") < 0:
        return GameStates.invalid

    for item in board:
        if item not in ["x", "o", "."]:
            return GameStates.invalid

    if check_win(board, "x"):
        return GameStates.x_wins

    if check_win(board, "o"):
        return GameStates.o_wins

    if "." in board:
        return GameStates.unfinished

    return GameStates.draw
    

 




