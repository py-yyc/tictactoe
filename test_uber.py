import unittest
import itertools

import ttt
from ttt import GameStates

"""
give assingment
after 15 minutes pause, discussion time
* how many possible game states (9!)
* what possible states can board be in
* introduce GameStates
* groups must pull and merge
give another 15 minutes
"""


def all_boards():
    for a in itertools.product('xo.', repeat=3):
        for b in itertools.product('xo.', repeat=3):
            for c in itertools.product('xo.', repeat=3):
                yield a+b+c


class UberTestTTT(unittest.TestCase):

    def test_bad_boards(self):

        # or something
        self.assertEqual(GameStates.invalid, ttt.game_state(None))
        self.assertEqual(GameStates.invalid, ttt.game_state("xo.ox.ox."))
        self.assertEqual(GameStates.invalid, ttt.game_state([]))
        self.assertEqual(GameStates.invalid, ttt.game_state(['.']*8))
        self.assertEqual(GameStates.invalid, ttt.game_state(['.']*10))
        self.assertEqual(GameStates.invalid, ttt.game_state(['x']*2 + ['.']*7))
        self.assertEqual(GameStates.invalid, ttt.game_state(['o']*2 + ['.']*7))
        # x goes first
        self.assertEqual(GameStates.invalid, ttt.game_state(['o']*1 + ['.']*8))

    def test_all_perms(self):
        results = {}

        for board in all_boards():
            # if board == list("xoxxoxoxo"):
            #     print board
            e = ttt.game_state(list(board))
            results[e] = results.get(e, 0) + 1

        # {0: 13815, 2: 920, 1: 4520, 3: 412, 4: 16}
        print results
        self.assertEqual(3**9, sum(results.values()))

        self.assertEqual(13815, results[GameStates.invalid])
        self.assertEqual(4520, results[GameStates.unfinished])
        self.assertEqual(920, results[GameStates.x_wins])
        self.assertEqual(412, results[GameStates.o_wins])
        self.assertEqual(16, results[GameStates.draw])
