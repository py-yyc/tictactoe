import unittest

import ttt


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = ttt.Game()

    def test_x_moves_twice(self):
        self.game.move('x', 0, 0)
        with self.assertRaises(Exception) as ctx:
            self.game.move('x', 0, 1)
        self.assertEqual("Invalid move", str(ctx.exception))
