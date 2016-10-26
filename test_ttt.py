
import unittest

import ttt

GameStates = ttt.GameStates

x = 'x'
o = 'o'
E = '.'


class TestTTT( unittest.TestCase ):

    def test_unfinished(self):

        empty_board = [E, E, E,
                        E, E, E,
                        E, E, E]

        unfinished_board = [x, E, E,
                        E, E, o,
                        E, E, E]




        self.assertEqual(GameStates.unfinished, ttt.game_state(empty_board) )
        self.assertEqual(GameStates.unfinished, ttt.game_state(unfinished_board) )


    def test_x_win(self):

        x_win_board = [ o, o, x, 
                        x, x, x, 
                        o, o, x ]
        self.assertEqual(GameStates.x_wins, ttt.game_state(x_win_board) )

    def test_o_win(self):

        o_win_board = [ o, o, o, 
                        x, x, E, 
                        x, E, x ]
        self.assertEqual(GameStates.o_wins, ttt.game_state(o_win_board) )

    def test_draw(self):

        draw_board = [ o, x, o, 
                        x, x, o, 
                        x, o, x ]
        self.assertEqual(GameStates.draw, ttt.game_state(draw_board) )

    def test_invalid(self):


        invalid_board_1 = [ o, o, o, 
                           x, x, o, 
                           o, o, x, o ]



        invalid_board_2 = [ o, o, o, 
                            x, x, "p", 
                            o, o, x]

        too_many_x_board = [x, x, E,
                        E, E, o,
                        E, x, E]

        too_many_o_board = [o, x, E,
                        o, E, o,
                        o, x, E]
 
        
        self.assertEqual(GameStates.invalid, ttt.game_state(invalid_board_1) )
        self.assertEqual(GameStates.invalid, ttt.game_state(invalid_board_2) )
        self.assertEqual(GameStates.invalid, ttt.game_state(too_many_x_board) )
        self.assertEqual(GameStates.invalid, ttt.game_state(too_many_o_board) )


if __name__ == '__main__':
    unittest.main()

