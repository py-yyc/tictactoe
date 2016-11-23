import unittest

import ttt


class TestAI(unittest.TestCase):

    def test_eval(self):
        board0 = ttt.Board([
            '.', '.', '.'
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
