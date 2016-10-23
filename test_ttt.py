import unittest

import ttt

class TestTTT( unittest.TestCase ):

    def test_1(self):

        self.assertEqual( 0, 0 ) # pass
        self.assertEqual( 1, 0 ) # fail

        something = board = None
        self.assertEqual( something, ttt.game_state( board ) )

        # all built in test functions
        # from: https://docs.python.org/2/library/unittest.html

        # self.assertEqual(a, b)            a == b
        # self.assertNotEqual(a, b)         a != b
        # self.assertTrue(x)                bool(x) is True
        # self.assertFalse(x)               bool(x) is False
        # self.assertIs(a, b)               a is b    2.7
        # self.assertIsNot(a, b)            a is not b    2.7
        # self.assertIsNone(x)              x is None    2.7
        # self.assertIsNotNone(x)           x is not None    2.7
        # self.assertIn(a, b)               a in b    2.7
        # self.assertNotIn(a, b)            a not in b    2.7
        # self.assertIsInstance(a, b)       isinstance(a, b)    2.7
        # self.assertNotIsInstance(a, b)    not isinstance(a, b)    2.7
