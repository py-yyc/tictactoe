import unittest

import ttt

class TestTTT(unittest.TestCase):

    def test_1(self):
        board = [
            'x', '.', 'o',
            'x', '.', 'o',
            'x', '.', '.',
        ]
        self.assertEqual('x wins', ttt.game_state(board))
