__author__ = 'Camtr0n'

import unittest
from gameboard import NestedTupleBoard as Board
from gameboard import Move
from player import Symbol
from ai import negamax as computer


class TestAI(unittest.TestCase):

    def setUp(self):
        self.board = Board(3)
        self.e = Board.EMPTY
        self.X = Symbol(1).name
        self.O = Symbol(2).name

    def X_O_e(self):
        return self.X, self.O, self.e

    def test_block_two_in_row(self):
        X, O, e = self.X_O_e()
        self.board.update_from_tuple(((X, X, e),
                                      (e, O, e),
                                      (e, e, e)))
        score = computer(self.board, O, O)
        self.assertTrue(score.move == Move(0, 2))

    def test_block_two_in_col(self):
        X, O, e = self.X_O_e()
        self.board.update_from_tuple(((X, e, e),
                                      (X, O, e),
                                      (e, e, e)))
        score = computer(self.board, O, O)
        self.assertTrue(score.move == Move(2, 0))

    def test_take_center(self):
        X, O, e = self.X_O_e()

        self.board.update_from_tuple(((e, e, e),
                                      (e, e, e),
                                      (e, e, e)))
        score = computer(self.board, X, X)
        self.assertTrue(score.move == self.board.center)

        self.board.update_from_tuple(((X, e, e),
                                      (e, e, e),
                                      (e, e, e)))
        score = computer(self.board, O, O)
        self.assertTrue(score.move == self.board.center)

    def test_prefer_corners(self):
        X, O, e = self.X_O_e()

        self.board.update_from_tuple(((e, e, e),
                                      (e, X, e),
                                      (e, e, e)))
        score = computer(self.board, O, O)
        self.assertTrue(score.move in (Move(2, 0), Move(0, 0), Move(0, 2), Move(2, 2)))

    def test_block_two_in_diagonals(self):
        X, O, e = self.X_O_e()

        self.board.update_from_tuple(((O, e, X),
                                      (e, X, e),
                                      (e, e, e)))
        score = computer(self.board, O, O)
        self.assertTrue(score.move == Move(2, 0))

        self.board.update_from_tuple(((e, e, e),
                                      (e, X, e),
                                      (O, e, X)))
        score = computer(self.board, O, O)
        self.assertTrue(score.move == Move(0, 0))

        self.board.update_from_tuple(((e, e, e),
                                      (e, X, e),
                                      (X, e, O)))
        score = computer(self.board, O, O)
        self.assertTrue(score.move == Move(0, 2))

        self.board.update_from_tuple(((X, e, O),
                                      (e, X, e),
                                      (e, e, e)))
        score = computer(self.board, O, O)
        self.assertTrue(score.move == Move(2, 2))

    def test_take_win_over_block_columns(self):
        X, O, e = self.X_O_e()
        self.board.update_from_tuple(((e, O, X),
                                      (e, O, X),
                                      (e, e, e)))
        score = computer(self.board, X, X)
        self.assertTrue(score.move == Move(2, 2))

        self.board.update_from_tuple(((X, O, e),
                                      (X, O, e),
                                      (e, e, e)))
        score = computer(self.board, X, X)
        self.assertTrue(score.move == Move(2, 0))

    def test_take_win_over_block_rows(self):
        X, O, e = self.X_O_e()
        self.board.update_from_tuple(((X, X, e),
                                      (O, O, e),
                                      (e, e, e)))
        self.assertTrue(computer(self.board, X, X).move == Move(0, 2))

        self.board.update_from_tuple(((e, e, e),
                                      (O, O, e),
                                      (X, X, e)))
        score = computer(self.board, X, X)
        self.assertTrue(score.move == Move(2, 2))

    def test_confirm_tie_score(self):
        X, O, e = self.X_O_e()
        self.board.update_from_tuple(((X, X, O),
                                      (O, O, X),
                                      (X, O, e)))
        score = computer(self.board, O, O)
        self.assertTrue(score.value == 0)

    def test_confirm_initiator_win_score(self):
        X, O, e = self.X_O_e()
        self.board.update_from_tuple(((X, X, O),
                                      (O, X, e),
                                      (X, O, O)))
        score = computer(self.board, O, O)
        self.assertTrue(score.value == 500)

    def test_confirm_opponent_win_score(self):
        X, O, e = self.X_O_e()
        self.board.update_from_tuple(((X, X, O),
                                      (O, X, e),
                                      (X, O, O)))
        score = computer(self.board, O, X)
        self.assertTrue(score.value == -500)


if __name__ == "__main__":
    unittest.main()
