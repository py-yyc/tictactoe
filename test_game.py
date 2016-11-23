import unittest
import sys

import ttt
from ttt import AI, Board, Game


class TestAI(unittest.TestCase):

    def test_eval(self):
        board0 = ttt.Board([
            '.', '.', '.',
            '.', 'x', '.',
            '.', '.', '.',
        ])
        board1 = ttt.Board([
            'x', '.', '.',
            '.', '.', '.',
            '.', '.', '.',
        ])
        self.assertTrue(
            ttt.AI.evaluate(board0, 'x') > ttt.AI.evaluate(board1, 'x')
        )

    def test_eval_1(self):
        board1 = ttt.Board([
            'x', 'o', 'o',
            '.', 'x', '.',
            '.', '.', 'x',
        ])

        self.assertEqual( sys.maxint, ttt.AI.evaluate(board1, 'x') )
        self.assertEqual( -sys.maxint, ttt.AI.evaluate(board1, 'o') )

    def test_assign_1(self):
        board = ttt.Board([
            'x', 'o', '.',
            'o', 'x', '.',
            '.', '.', '.',
        ])
        self.assertEqual( '.', board[8] )
        board[8]='x'
        self.assertEqual( 'x', board[8] )

    def test_next_1(self):
        board = ttt.Board([
            '.', 'o', '.',
            'o', 'x', '.',
            '.', '.', 'x',
        ])
        self.assertEqual( 0, AI(board,'x').next_move() )

    def test_next_2(self):
        return
        board = ttt.Board([
            'x', 'o', '.',
            'o', 'x', '.',
            '.', '.', '.',
        ])
        self.assertEqual( 8, AI(board,'x').next_move() )

    def test_depth_2(self):
        return
        board = ttt.Board([
            'x', 'o', '.',
            'o', '.', '.',
            '.', '.', 'x',
        ])
        self.assertEqual( 4, AI(board,'x').next_move() )


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = ttt.Game()

    def test_invalid_row(self):
        with self.assertRaises(Exception) as ctx:
            self.game.move('x', -1, 0)
        self.assertEqual("Invalid location", str(ctx.exception))

    def test_invalid_row_big(self):
        with self.assertRaises(Exception) as ctx:
            self.game.move('x', 3, 0)
        self.assertEqual("Invalid location", str(ctx.exception))

    def test_invalid_col(self):
        with self.assertRaises(Exception) as ctx:
            self.game.move('x', 0, -1)
        self.assertEqual("Invalid location", str(ctx.exception))

    def test_invalid_col_big(self):
        with self.assertRaises(Exception) as ctx:
            self.game.move('x', 0, 3)
        self.assertEqual("Invalid location", str(ctx.exception))

    def test_x_moves_twice(self):
        self.game.move('x', 0, 0)
        with self.assertRaises(Exception) as ctx:
            self.game.move('x', 0, 1)
        self.assertEqual("Invalid move", str(ctx.exception))

    def test_x_moves_twice_same_location(self):
        return
        self.game.move('x', 0, 0)
        with self.assertRaises(Exception) as ctx:
            self.game.move('x', 0, 0)
        self.assertEqual("Invalid move", str(ctx.exception))
