from dataclasses import dataclass
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import Qt


app = QApplication()


@dataclass
class EnterNamesScreen(QWidget):
    """Player 1 and 2 enter their names here."""

    def __init__(self) -> None:
        super().__init__()
        self.resize(700, 500)
        self.setWindowTitle("Enter Player Names")
        self.setStyleSheet("""
        QWidget {
            background-color: #ffffff;
            font-color: #000000;
        }""")

        enter_names_screen_layout = QVBoxLayout()
        self.setLayout(enter_names_screen_layout)

        # enter player 1 name instruction label & add
        enter_p1_label = QLabel("Please enter player one name here:")
        enter_names_screen_layout.addWidget(enter_p1_label)

        # q line edit to input player 1's name & add
        self.input_player1_name = QLineEdit()
        self.input_player1_name.setFixedWidth(150)
        self.input_player1_name.textChanged.connect(self.check)
        enter_names_screen_layout.addWidget(self.input_player1_name, alignment= Qt.AlignmentFlag.AlignCenter)

        # done button for player 1 & add
        p1_finished_button = QPushButton("Done")
        p1_finished_button.clicked.connect(self.done_player1)
        enter_names_screen_layout.addWidget(p1_finished_button)

        # enter player 2 name instr. label & add
        enter_p2_label = QLabel("Please enter player two name here:")
        enter_names_screen_layout.addWidget(enter_p2_label)

        # q line edit to input player 2's name
        self.input_player2_name = QLineEdit()
        self.input_player2_name.setFixedWidth(150)
        self.input_player2_name.textChanged.connect(self.check_p2)
        enter_names_screen_layout.addWidget(self.input_player2_name, alignment= Qt.AlignmentFlag.AlignCenter)

        # done button for player 2
        p2_finished_button = QPushButton("Done")
        p2_finished_button.clicked.connect(self.done_player2)
        enter_names_screen_layout.addWidget(p2_finished_button)

        # next button (to go to rules page)
        next_gotorules_button = QPushButton("NEXT")
        enter_names_screen_layout.addWidget(next_gotorules_button)

    def done_player1(self):
        text = self.input_player1_name.text()
        print(text)

    def done_player2(self):
        text_p2 = self.input_player2_name.text()
        print(text_p2)

    def check(self):
        for x in self.input_player1_name.text():
            if x == "":
                print("NEXT")
            else:
                print("Please enter a name to begin.")
                return

    def check_p2(self):
        for x in self.input_player2_name.text():
            if x == "":
                print("NEXT")
            else:
                print("Please enter a name to begin.")


# running the program
enter_player_names_window = EnterNamesScreen()
enter_player_names_window.show()

app.exec()
