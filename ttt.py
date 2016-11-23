"""
TicTacToe

x goes first
board is a list of 9 elements from ['x','o','.']. '.' means empty spot.
"""

# import sys
import types


class GameStates(object):
    """
    there are lots of ways to accomplish an enum like object
    this is the one we're going with since it's simple
    """
    invalid = 'invalid'
    unfinished = 'unfinished'
    x_wins = 'x wins'
    o_wins = 'o wins'
    draw = 'draw'


def game_state(board):
    return Board(board).current_state()


def all_moves(board, who):
    if who == 'x' and board.x_count() > board.o_count():
        return
    for row in range(3):
        for col in range(3):
            if board.is_free(col, row):
                yield (col, row)


class AI(object):
    def __init__(self, board, who):
        self._game = Game(board)
        self._who = who

    def next_move(self):
        """
        Return a 2-tuple representing the row, col of our next move
        """

    @staticmethod
    def evaluate(board, who, turn=None):
        """
        Return a value for this board position, given you're playing as
        "who".
        """

        if turn is None:
            turn = 'x' if turn == 'o' else 'o'

        state = board.current_state()

        if who == 'x' and state == GameStates.x_wins or \
                who == 'o' and state == GameStates.o_wins:
            return 1
        elif who == 'x' and state == GameStates.o_wins or \
                who == 'o' and state == GameStates.x_wins:
            return -1
        elif state == GameStates.invalid or state == GameStates.draw:
            return 0
        else:
            # unfinished
            tot = 0

            for i in range(3):
                for j in range(3):
                    new_board = board.clone()
                    if new_board.is_free(i, j):
                        new_board.move(turn, i, j)
                        tot += AI.evaluate(new_board, who, 'x' if turn == 'o' else 'o')

            return tot


class Game(object):
    """
    I represent an in-progress tic-tac-toe game
    """

    def __init__(self, board=None):
        if board is None:
            board = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        self._board = Board(board)

    def move(self, who, col, row):
        """
        Make a move. Raises an exception if you reach an invalid board
        state.
        """
        if col < 0 or col > 2 or row < 0 or row > 2:
            raise Exception("Invalid location")

        if self._board._board[row * 3 + col] != '.':
            raise Exception("Invalid move")

        self._board._board[row * 3 + col] = who

        if self._board.current_state() == GameStates.invalid:
            self._board._board[row * 3 + col] = '.'
            raise Exception("Invalid move")


class Board(object):
    """
    I represent a Tic Tac Toe board.
    """

    def __init__(self, board):
        """
        :param board: an array of 9 chars representing the current
           state. Each char is either 'x', 'o' or '.'
        """
        self._board = board

    def move(self, turn, col, row):
        self._board[row * 3 + col] = turn

    def clone(self):
        return Board(list(self._board))

    def is_free(self, col, row):
        return self._board[row * 3 + col] == '.'

    def x_count(self):
        return len([ch for ch in self._board if ch == 'x'])

    def o_count(self):
        return len([ch for ch in self._board if ch == 'o'])

    def row(self, n):
        return self._board[n*3:n*3+3]

    def col(self, n):
        ret = []
        for i in range(3):
            ret.append(self._board[n+i*3])

        return ret

    def diag(self, n):
        "0 is diag down-left \, 1 is diag down-right /"
        ret = []
        if n == 0:
            for i in range(3):
                ret.append(self._board[i*4])
        if n == 1:
            for i in range(3):
                ret.append(self._board[2+i*2])

        return ret

    def current_state(self):
        if not isinstance(self._board, types.ListType):
            return GameStates.invalid

        if len(self._board) != 9:
            return GameStates.invalid

        for c in self._board:
            if c not in ('x', 'o', '.'):
                return GameStates.invalid

        if abs(self._board.count('x') - self._board.count('o')) > 1:
            return GameStates.invalid

        if self._board.count('x') < self._board.count('o'):
            return GameStates.invalid

        if self.is_winner('x') > 1 or self.is_winner('o') > 1:
            return GameStates.invalid

        if self.is_winner('x') >= 1 and self.is_winner('o') >= 1:
            return GameStates.invalid

        if self.is_winner('x') == 1:
            return GameStates.x_wins

        if self.is_winner('o') == 1:
            return GameStates.o_wins

        if self._board.count(".") == 0:
            return GameStates.draw

        return GameStates.unfinished

    def same(self, three):
        return three.count(three[0]) == 3

    def winner(self, three):
        if self.same(three):
            return three[0]
        return False

    def is_winner(self, c):
        "return number of times c has won"
        count = 0
        for i in range(3):
            r = self.row(i)
            if self.winner(r) == c:
                count += 1

            col = self.col(i)
            if self.winner(col) == c:
                count += 1

        if self.winner(self.diag(0)) == c:
            count += 1

        if self.winner(self.diag(1)) == c:
            count += 1

        return count
