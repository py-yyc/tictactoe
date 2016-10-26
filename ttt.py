"""
TicTacToe

x goes first
board is a list of 9 elements from ['x','o','.']. '.' means empty spot.
"""

WIN_COMBOS = [
	(0,1,2),
	(3,4,5),
	(6,7,8),
	(0,3,6),
	(1,4,7),
	(2,5,8),
	(0,4,8),
	(2,4,6)
]

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

def change_numeric(board):
    return [ 0 if z == '.' else z for z in [ 1 if y == 'o' else y for y in [ -1 if x=='x' else x for x in board ]]]

def find_win(board):
	board_n = change_numeric(board)
	for board_combo in WIN_COMBOS:
		a,b,c = board_combo
		sum_threes = sum([board_n[a], board_n[b], board_n[c]])
		if sum_threes != 0:
			if sum_threes == -3:
				return GameStates.x_wins
			elif sum_threes == 3:
				return GameStates.o_wins 
	return None
def is_balanced(board):
    board_n = change_numeric(board)
    if sum(board_n) == 0:
	return True
    else:
	return False

def is_invalid(board):
    board_n = change_numeric(board)
    if sum(board_n) != -1:
	return True
    else:
	return False

def is_finished(board):
    if '.' not in board:
	return True
    else:
	return False

def game_state(board):
	win_status = find_win(board)
	
	if not win_status:
		if is_balanced(board) and not is_finished(board):
			return GameStates.unfinished
		elif is_finished and not is_invalid(board):
			return GameStates.draw
		else:
			return GameStates.invalid
	else:
		if is_invalid(board):
			return GameStates.invalid
		else:
			return win_status
