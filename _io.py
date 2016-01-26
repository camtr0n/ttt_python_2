__author__ = 'Camtr0n'


from abc import ABCMeta, abstractmethod


class AbstractIO(metaclass=ABCMeta):

    invalid_input_message = "\nInvalid input; Please select a number 1-"
    move_already_taken_message = "\nInvalid move, square is already taken; Please select an available square."
    tie_message = "DRAW! You just can't win, can  you?"

    @staticmethod
    def get_decision_occurred_message(decided_player):
        return str(decided_player.player_type) + "[Player " + str(decided_player.number) + "] has decided."

    @staticmethod
    def get_winner_message(winning_player):
        return "Player [" + str(winning_player.number) + "] is the WINNER!!! #Sorrynotsorry"

    @abstractmethod
    def display_intro(self):
        """ Display instructions for game """
        pass

    @abstractmethod
    def display_board(self):
        """ Display game board"""
        pass

    @abstractmethod
    def get_move(self, human_player, board):
        """ Get move from a player """
        pass

    @abstractmethod
    def notify_invalid_input(self, size):
        """ Notify user that input is not a valid move, depends on size of board to give accurate prompt """
        pass

    @abstractmethod
    def notify_move_taken(self):
        """ Notify user that selected move has already been taken """
        pass

    @abstractmethod
    def get_player_type(self, number):
        """ Prompt user for selection of player type (Human, Computer, etc) """
        pass

    @abstractmethod
    def play_again(self):
        """ Prompt player to play again at end of game """
        pass

    @abstractmethod
    def notify_decision_occurred(self, decider):
        """ Notify that human or computer has made a decision to help with tracking turns"""
        pass

    @abstractmethod
    def notify_winner(self):
        """ Notify user that human or computer won the game """
        pass

    @abstractmethod
    def notify_tie(self):
        """ Notify user that tie game has been reached  """
        pass
