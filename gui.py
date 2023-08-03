from dataclasses import dataclass


# Model
@dataclass
class MenuScreen:
    def __init__(self):
        print("Welcome to Stackem Checkers. Enter 'Y' to proceed.")
        self._user_response = str(input())

        if self._user_response.upper() == "Y":
            # instructions
            print("Please decide who will be Player 1 (Black) and Player 2 (White).")
            print("Player will have their turn first.")
            # first player request
            self.player_one_name = input("Enter Player 1's name here:")
            # second player name
            print("Enter Player 2's name.")
            self.player_two_name = input("Enter Player 2's name here:")
            # confirmation
            print("Is this information correct? (Y/N)")
            print("Player 1: " + self.player_one_name)
            print("Player 2: " + self.player_two_name)

            while True:
                self._user_response_confirmation = str(input()).upper()

                # if the user responds Y (correct)
                if self._user_response_confirmation == "Y":
                    # move on to the next window (the actual games window)
                    print("Next.")
                # if the user responds N (not correct)
                elif self._user_response_confirmation == "N":
                    # ask for player name(s) again
                    print("Please re-enter your names.")
                    # player one re-enter
                    self.player_one_name = input("Enter Player 1's name here:")
                    # player two re-enter
                    self.player_two_name = input("Enter Player 2's name here:")
                    # confirmation
                    print("Is this information correct? (Y/N)")
                    print("Player 1: " + self.player_one_name)
                    print("Player 2: " + self.player_two_name)
                else:
                    # if the user responds with a character out of boundaries (Y/N).
                    print("Error. Must enter 'Y' or 'N'. Please re-enter response.")
        else:
            # if the user does inputs a response that is not Y.
            print("Please enter 'Y' to start.")
            self._user_response = str(input())

# Menu screen instance
menu = MenuScreen()
