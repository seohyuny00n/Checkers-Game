from dataclasses import dataclass

# Note to self: Change the y/n to buttons ASAP

# Model for the menu screen
# Source: https://stackoverflow.com/questions/41794196/how-to-input-a-player-name
@dataclass
class MenuScreen:
    """This is the menu screen model."""
    def __init__(self):
        self._user_response_confirmation = ""
        self.player_one_name = ""
        self.player_two_name = ""
        while True:
            print("Welcome to StackEm Checkers.")
            print("Enter 'Y' to proceed.")
            self._user_response = str(input()).upper()

            if self._user_response == "Y":
                # proceed to ask for player names & give additional info
                self.ask_player_information()
            else:
                # if the player inputs a response that is not 'y'.
                print("Please enter 'Y' to begin.")
                self._user_response = str(input()).upper()
                # once the user responds within bounds (y), the next prompt will be asked straight-away
                if self._user_response == "Y":
                    self.ask_player_information()

    def ask_player_information(self):
        """Users will be asked for player names to be referred by. Additional info also given."""
        # instructions?
        print("Please decide who will be Player 1 (Black pieces) and Player 2 (White pieces).")
        print("Player 1 (Black) will have their turn first.")

        # player 1 name request
        self.player_one_name = input("Enter Player 1's name here:")
        # player 2 name request
        self.player_two_name = input("Enter Player 2's name here:")
        # proceed to confirm names
        self.name_confirmation()

    def name_confirmation(self):
        """Users will be asked to confirm their inputted(?) names."""
        print("Is this information correct? (Y/N)")
        print("Player 1: " + self.player_one_name)
        print("Player 2: " + self.player_two_name)

        while True:
            self._user_response_confirmation = str(input()).upper()

            # if the user responds y(confirmed, positive)
            if self._user_response_confirmation == "Y":
                print("Next")

            # if the user responds n(confirmed, negative)
            elif self._user_response_confirmation == "N":
                # ask for player name(s) again
                print("Please re-enter your names.")
                # player one re-enter
                self.player_one_name = input("Enter Player 1's name here:")
                self.player_two_name = input("Enter Player 2's name here:")
                # confirmation (again)
                self.name_confirmation()
            else:
                # if the user responds with a character out of boundaries (y/n)
                print("Error. Must enter 'Y' or 'N'. Please re-enter response.")

# Menu screen instance
menu = MenuScreen()
