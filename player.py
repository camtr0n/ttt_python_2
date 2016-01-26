__author__ = 'Camtr0n'

from enum import Enum
import ai

class PlayerType(Enum):
    Human = 1
    Computer = 2


class Symbol(Enum):
    X = 1
    O = 2
    E = 3


def opposite_symbol(symbol):
    return Symbol(2).name if symbol is Symbol(1).name else Symbol(1).name


class Player:
    def __init__(self, player_type, player_number):
        self._number = player_number
        self._type = PlayerType(player_type)
        self._symbol = Symbol(player_number)

    @property
    def symbol(self):
        return self._symbol.name

    @property
    def player_type(self):
        return self._type.name

    @property
    def number(self):
        return self._number

    def get_next_board(self, game):
        if self.player_type == PlayerType(1).name:
            choice = game.presenter.get_choice(self, game.board)
            move = game.board.map_to_move(choice)
        else:
            game.presenter.notify_turn(game.active_player.number)
            game.presenter.notify_thinking(game.active_player.player_type)
            move = ai.negamax(game.board, self.symbol, self.symbol).move
        return game.board.apply_move(move, self.symbol)
