import unittest

import ttt

class TestTTT(unittest.TestCase):

    def test_invalid_wrong_size(self):
        board = [
            'x', '.', 'o',
        ]
        self.assertEqual(ttt.GameStates.invalid, ttt.game_state(board))

    def test_invalid_illegal_char(self):
        board = [
            'x', '.', 'o',
            'x', '.', 'o',
            'x', '.', 'O',
        ]
        self.assertEqual(ttt.GameStates.invalid, ttt.game_state(board))

    def test_x_count(self):
        board = [
            'x', '.', 'o',
            'x', '.', 'o',
            'x', '.', '.',
        ]
        self.assertEqual(3, ttt.x_count(board))
        self.assertEqual(2, ttt.o_count(board))

    def test_x_win_0(self):
        board = [
            'x', 'x', 'x',
            'o', '.', 'o',
            '.', '.', '.',
        ]
        self.assertEqual(ttt.GameStates.x_wins, ttt.game_state(board))

    def test_x_win_1(self):
        board = [
            'o', '.', 'o',
            'x', 'x', 'x',
            '.', '.', '.',
        ]
        self.assertEqual(ttt.GameStates.x_wins, ttt.game_state(board))

    def test_x_win_2(self):
        board = [
            'o', '.', 'o',
            '.', '.', '.',
            'x', 'x', 'x',
        ]
        self.assertEqual(ttt.GameStates.x_wins, ttt.game_state(board))

    def test_x_win_vert(self):
        board = [
            'x', '.', 'o',
            'x', '.', '.',
            'x', '.', 'o',
        ]
        self.assertEqual(ttt.GameStates.x_wins, ttt.game_state(board))

    def test_o_win_vert(self):
        board = [
            'x', 'x', 'o',
            '.', '.', 'o',
            'x', '.', 'o',
        ]
        self.assertEqual(ttt.GameStates.o_wins, ttt.game_state(board))

    def test_x_win_diag(self):
        board = [
            'x', '.', 'o',
            '.', 'x', 'o',
            '.', '.', 'x',
        ]
        self.assertEqual(ttt.GameStates.x_wins, ttt.game_state(board))
