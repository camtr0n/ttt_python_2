__author__ = 'Camtr0n'

from abc import ABCMeta
from math import ceil


class Move:
    def __init__(self, row, col):
        self._move = (int(row), int(col))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    @property
    def row(self):
        return self._move[0]

    @property
    def column(self):
        return self._move[1]


class Board(metaclass=ABCMeta):
    EMPTY = " "


class NestedTupleBoard(Board):
    def __init__(self, size=3):
        self._board = (((self.EMPTY, ) * size), ) * size

    @property
    def size(self):
        return len(self._board)

    @property
    def rows(self):
        return self._board

    @property
    def columns(self):
        return tuple(zip(*self._board))

    @property
    def valid_inputs(self):
        return range(1, (self.size ** 2) + 1)

    @property
    def win_lines(self):
        indices = range(self.size)
        diagonal_1 = tuple([self._board[i][i] for i in indices])
        diagonal_2 = tuple([self._board[i][self.size-(i+1)] for i in indices])
        return self.rows + self.columns + (diagonal_1, diagonal_2)

    @property
    def available(self):
        indices = range(self.size)
        return [Move(i, j) for i in indices for j in indices if self._board[i][j] is self.EMPTY]

    @property
    def full(self):
        return not bool(len(self.available))

    @property
    def copy(self):
        new = NestedTupleBoard(self.size)
        new.update_from_board(self)
        return new

    @property
    def winner(self):
        won = False
        for line in self.win_lines:
            if len(set(line)) == 1 and self.EMPTY not in line:
                won = line[0]
                break
        return won

    @property
    def tied(self):
        return not bool(self.winner) and self.full

    @property
    def center(self):
        middle = (self.size - 1)/2
        return Move(middle, middle)

    @property
    def depth(self):
        return self.size ** 2 - len(self.available)

    @property
    def numbers(self):
        number_board = []
        indices = range(self.size)
        domain = range(1, self.size**2 + 1)
        for i in indices[::-1]:
            number_board_row = []
            for j in indices:
                num = domain[self.size*((self.size-1)-i) + j]
                if Move(i, j) not in self.available:
                    number_board_row.append(" " + self._board[i][j])
                else:
                    number_board_row.append(" "*int(num < 10) + str(num))
            number_board.append(tuple(number_board_row))
        board = NestedTupleBoard(self.size)
        board.update_from_tuple(tuple(number_board)[::-1])
        return board

    def reset(self):
        self._board = NestedTupleBoard(self.size).rows

    def apply_move(self, move, symbol):
        from util import tuple_replace as replace
        source_row = self.rows[move.row]
        new_row = replace(symbol, move.column, source_row)
        new_board = self.copy
        new_board.update_from_tuple(replace(new_row, move.row, self.rows))
        return new_board

    def update_from_board(self, new_board):
        self._board = new_board.rows

    def update_from_tuple(self, tuple_board):
        if len(tuple_board) == self.size:
            self._board = tuple_board
            return True
        else:
            return False

    def map_to_move(self, num):
        row = self.size - ceil(int(num) / self.size)
        col = ((int(num) % self.size) - 1) % self.size
        return Move(row, col)

