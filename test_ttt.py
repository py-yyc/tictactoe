import unittest

import ttt

class TestTTT(unittest.TestCase):

    def test_invalid_wrong_size(self):
        board = [
            'x', '.', 'o',
        ]
        self.assertEqual('invalid', ttt.game_state(board))

    def test_invalid_illegal_char(self):
        board = [
            'x', '.', 'o',
            'x', '.', 'o',
            'x', '.', 'O',
        ]
        self.assertEqual('invalid', ttt.game_state(board))

    def test_x_count(self):
        board = [
            'x', '.', 'o',
            'x', '.', 'o',
            'x', '.', '.',
        ]
        self.assertEqual(3, ttt.x_count(board))
        self.assertEqual(2, ttt.o_count(board))

    def test_x_win(self):
        board = [
            'x', 'x', 'x',
            'o', '.', 'o',
            '.', '.', '.',
        ]
        self.assertEqual('x wins', ttt.game_state(board))
