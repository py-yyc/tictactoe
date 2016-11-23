import unittest

import ttt


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

    def test_close_to_finish(self):
        board2 = ttt.Board([
            'x', 'o', 'x',
            'x', 'o', 'x',
            'o', '.', '.'
        ])
        board3 = ttt.Board([
            'o', 'o', 'x',
            '.', 'x', 'o',
            '.', '.', 'x'
        ])
        self.assertEquals(ttt.AI(board2, 'o').next_move(), (2, 1))
        self.assertEquals(ttt.AI(board3, 'x').next_move(), (2, 0))


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
        self.game.move('x', 0, 0)
        with self.assertRaises(Exception) as ctx:
            self.game.move('x', 0, 0)
        self.assertEqual("Invalid move", str(ctx.exception))
