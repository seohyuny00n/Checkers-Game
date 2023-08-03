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

    def p1_name_entered(self):
        """When the user inputs characters (hopefully) within QLineEdit."""
        self.player_one_name = ""
        if self.player_one_name == "":
        # if the user entered a valid response, ask player 2
    
    def p2_name_entered(self):

    def confirm_names_entered(self):
    
    def next_button_clicked(self):




model = MenuScreen()
menu = MenuScreenWindow()

menu.show()
app.exec()

    def user_input_entered(self):
        """When the user enters Y on QLineEdit."""
        # source 1: https://stackoverflow.com/questions/66341365/how-do-i-get-the-text-of-an-qlineedit-into-a-method
        # source 2: https://stackoverflow.com/questions/42288320/python-how-to-get-qlineedit-text
        user_reponse = self.widgets["EnterY"].text().strip().upper()
        if user_response == "Y":
            # proceed to ask for player names & give additional info
            self.ask_player_information()
        else:
            # if the player inputs a response that is not 'y'.
            print("Please enter 'Y' to begin.")
            self._user_response = str(input()).upper()
            # once the user responds within bounds (y), the next prompt will be asked straight-away
            if self._user_response == "Y":
                self.ask_player_information()
