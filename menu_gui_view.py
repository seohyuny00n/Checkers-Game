from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from menu_model import MenuScreen


# i made all of this code from the GUI playground codespace
class MenuScreen:
    """This is the menu screen model."""

    def __init__(self):
        self._user_response_confirmation = ""
        self.player_one_name = ""
        self.player_two_name = ""

app = QApplication([])

# source: previous GUI playground classwork material(s)


class MenuScreenWindow(QMainWindow):
    """The window for the menu screen."""

    def __init__(self) -> None:
        # call superclass initializer
        super(MenuScreenWindow, self).__init__()

        # layout set-up
        self.central_widget = QWidget()
        self.form_layout = QFormLayout()
        self.central_widget.setLayout(self.form_layout)
        self.setCentralWidget(self.central_widget)
        self.setFixedSize(1000, 800)

        # style sheet
        self.central_widget.setStyleSheet("""
QWidget {
    background-color: #A7C7E7;
    color: blue;
}
""")

        # relevant widgets
        self.widgets = {
            "GameName": QLabel("Welcome to StackEm Checkers!"),
            "Instructions1": QLabel("Enter 'Y' to proceed."),
            "EnterY": QLineEdit(),
            "Enter_P1_Name": QLineEdit(),
            "Enter_P2_Name": QLineEdit(),
            "Enter_YN_Confirm": QLineEdit(),
            "Next": QPushButton("Next")
        }

        # adding the widgets to layout
        self.form_layout.addRow(self.widgets["GameName"])
        self.form_layout.addRow(self.widgets["Instructions1"])
        self.form_layout.addRow(self.widgets["EnterY"])
        self.form_layout.addRow(self.widgets["Enter_P1_Name"])
        self.form_layout.addRow(self.widgets["Enter_P2_Name"])
        self.form_layout.addRow(self.widgets["Enter_YN_Confirm"])
        self.form_layout.addRow(self.widgets["Next"])

        # connect signal functions
        self.widgets["EnterY"].returnPressed.connect(self.user_input_entered)
        self.widgets["Enter_P1_Name"].returnPressed.connect(self.p1_name_entered)
        self.widgets["Enter_P2_Name"].returnPressed.connect(self.p2_name_entered)
        self.widgets["Enter_YN_Confirm"].returnPressed.connect(self.confirm_names_entered)
        self.widgets["Next"].clicked.connect(self.next_button_clicked)

        self.menu_screen_model = MenuScreen()

    # add user input for y code here (from model)
    def user_input_entered(self):
        """When the user is asked to input Y to proceed (from QLineEdit)."""
        user_input_proceed  = self.widgets["EnterY"].text().upper()
        if user_input_proceed == "Y":
            # when the user successfully inputs a Y (proceed = pos), proceed to ask for player information, next function
            self.ask_player_information()
        else:
            # if the user inputs a character that is anything outside of Y.
            print("Please enter 'Y' to begin.")

    # ask player information (from model)
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

    # name confirmation (also pulled from model)
    def name_confirmation(self):
        """Users will be asked to confirm their inputted names."""
        print("Is this information correct? (Y/N)")
        print("Player 1: " + self.player_one_name)
        print("Player 2: " + self.player_two_name)

        # hide widgets not needed currently. only show confirmation widget. only showing --> does that work?
        self.widgets["Instructions1"].hide()
        self.widgets["EnterY"].hide()
        self.widgets["Enter_P1_Name"].hide()
        self.widgets["Enter_P2_Name"].hide()
        self.widgets["Enter_YN_Confirm"].show()
        self.widgets["Next"].show()

    def confirm_names_entered(self):
        """When the user confirms the names that they have inputted (saying it's correct)."""
        # source for getting response: ??? (NEED TO PUT IN)
        user_response = self.widgets["Enter_YN_Confirm"].text().upper()

        # if user responds positively (Y)
        if user_response == "Y":
            # the next button must allow the user to move on to the next window.
            print("Next")
        elif user_response == "N":
            # direct (show) the user(s) widgets again asking for name + instructions.
            self.widgets["Enter"].show()
            self.widgets["Enter_P1_Name"].show()
            self.widgets["Enter_P2_Name"].show()
            self.widgets["Enter_YN_Confirm"].hide()
            self.widgets["Next"].hide()
        else:
            # if the user responds with a character that is out of boundaries (/not y nor n).
            print("Error. Must enter 'Y' or 'N'. Please re-enter response.")

# def p1_name_entered(self):
# """When the user inputs characters (hopefully) within QLineEdit."""
# pass
# if the user entered a valid response, ask player 2


# def p2_name_entered(self):
# """When the user inputs characters (hopefully) for QLineEdit."""
# pass

# def next_button_clicked(self):
# """WIP, shows the next screen, which is either the rules or the main checker board screen."""
# pass


model = MenuScreen()
menu = MenuScreenWindow()

menu.show()
app.exec()
