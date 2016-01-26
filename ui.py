__author__ = 'Camtr0n'

import player
from abc import ABCMeta, abstractmethod


class AbstractIO(metaclass=ABCMeta):

    invalid_input_message = "\nInvalid input; Please select a number 1-"
    move_already_taken_message = "\nInvalid move, square is already taken; Please select an available square."
    tie_message = "DRAW! You just can't win, can  you?"

    @staticmethod
    def get_decision_occurred_message(decided_player):
        return "\n" + str(decided_player.player_type) + "[Player " + str(decided_player.number) + "] has decided."

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
    def get_choice(self, human_player, board):
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


class Terminal(AbstractIO):

    @staticmethod
    def display_intro():
        print("Welcome to Unbeatable Tic-Tac-Toe!")
        print("Proceed without hope...")
        print("")
        print("Player one is: ", player.Symbol(1).name)
        print("Player two is: ", player.Symbol(2).name)
        print("")
        print("For 3x3 game (default), use the number pad to select your move.")
        print("(Note: you may need to press the Num Lock key to activate your numeric keypad)")
        print("")

    @staticmethod
    def display_board(board):
        print(" " + " | ".join(board.rows[0]))
        for row in board.rows[1:]:
            print("-" * (board.size * 4 - 1))
            print(" " + " | ".join(row))
        print("\n")

    @staticmethod
    def display_number_board(board):
        print(" " + " | ".join(map(str, board.rows[0])))
        for row in board.rows[1:]:
            print("-" * ((board.size * 5) - 1))
            print(" " + " | ".join(row))
        print("\n")

    @staticmethod
    def notify_turn(player_number):
        print("Player[" + str(player_number) + "], your turn.")

    @staticmethod
    def notify_thinking(player_type):
        print(str(player_type) + " is thinking...")

    @staticmethod
    def notify_move_taken():
        print(AbstractIO.move_already_taken_message)

    @staticmethod
    def notify_decision_occurred(decider):
        print(AbstractIO.get_decision_occurred_message(decider))

    @staticmethod
    def notify_tie():
        print(AbstractIO.tie_message)

    @staticmethod
    def notify_invalid_input(size):
        print(AbstractIO.invalid_input_message + str(size ** 2))

    @staticmethod
    def notify_winner(winner):
        print("Player " + str(winner.number) + " has won the game!")

    @staticmethod
    def get_human_input(human_player, board):
        Terminal.notify_turn(human_player.number)
        choice = input("Press 'n' then <ENTER> to redraw board with numbers in empty squares, or\n" +
                        "Press 1-" + str(board.size ** 2) + " to select move and press <ENTER>: ")
        if choice in ("n", "N"):
            return choice

        try:
            choice = int(choice)
        except:
            choice = Terminal.get_human_input(human_player, board)
        return choice

    @staticmethod
    def get_choice(human_player, board):
        choice = Terminal.get_human_input(human_player, board)
        if choice in ("n", "N"):
            Terminal.display_number_board(board.numbers)
            choice = Terminal.get_choice(human_player, board)
        elif choice not in board.valid_inputs:
            Terminal.notify_invalid_input(board.size)
            choice = Terminal.get_choice(human_player, board)

        if board.map_to_move(choice) not in board.available:
            Terminal.notify_move_taken()
            choice = Terminal.get_choice(human_player, board)
        return choice

    @staticmethod
    def play_again():
        answer = input("Would you like to play again? Y/N: ")
        if answer in ("Y", "y"):
            print("\n\n")
            return True
        elif answer in ("N", "n"):
            exit()
        else:
            return Terminal.play_again

    @staticmethod
    def get_player_type(player_number):
        print("What type of player will " + player_number + " be: Human[1] or Computer[2]?")
        choice = input("Enter the number corresponding to the player type: ")
        try:
            choice = int(choice)
        except:
            choice = Terminal.get_player_type(player_number)
        print("")
        return choice if choice in (1, 2) else Terminal.get_player_type(player_number)

