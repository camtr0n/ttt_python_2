__author__ = 'Camtr0n'

from gameboard import NestedTupleBoard as Board
from player import Player, PlayerType
import ui


class Game(object):
    SIZE = 3

    def __init__(self, size):
        self._board = Board(size)
        self._presenter = ui.Terminal
        self._presenter.display_intro()
        self._presenter.display_number_board(self._board.numbers)
        self._p1 = Player(self._presenter.get_player_type("Player 1"), 1)
        self._p2 = Player(self._presenter.get_player_type("Player 2"), 2)
        self._active = self._p1

    def play(self):
        self.draw_board()
        updated_board = self.next_board()
        self.notify_decision()
        self.slurp_board(updated_board)
        if self.board.tied:
            self.draw_board()
            self.declare_tie()
        elif self.board.winner:
            self.draw_board()
            self.declare_winner()
        else:
            self.switch_players()
            self.play()
        if self.play_again():
            Game(Game.SIZE).play()

    @property
    def board(self):
        return self._board

    @property
    def presenter(self):
        return self._presenter

    @property
    def player_1(self):
        return self._p1

    @property
    def player_2(self):
        return self._p2

    @property
    def active_player(self):
        return self._active

    @property
    def inactive_player(self):
        return self.opponent(self.active_player)

    def opponent(self, player):
        return self.player_1 if player is self.player_2 else self.player_2

    def switch_players(self):
        self._active = self.opponent(self.active_player)

    def draw_board(self):
        self.presenter.display_board(self.board)

    def declare_winner(self):
        self.presenter.notify_winner(self.active_player)

    def declare_tie(self):
        self.presenter.notify_tie()

    def notify_decision(self):
        self.presenter.notify_decision_occurred(self.active_player)

    def slurp_board(self, new_board):
        self.board.update_from_board(new_board)

    def play_again(self):
        return self.presenter.play_again()

    def next_board(self):
        return self.active_player.get_next_board(self)


if __name__ == "__main__":
    Game(Game.SIZE).play()
