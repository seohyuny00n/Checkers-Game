from dataclasses import dataclass
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import Qt


app = QApplication()


# source: https://pythonpyqt.com/pyqt-qtextedit/
class RulesDisplay(QWidget):
    """Shows the rules to the player(s)"""
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rules")
        self.resize(700, 500)
        self.setStyleSheet("""
        QWidget {
            background-color: #ffffff;
            font-color: #000000;
        }""")

        # layout
        rules_screen_layout = QVBoxLayout()
        self.setLayout(rules_screen_layout)

        # text block
        self.textEdit = QTextEdit()
        self.textEdit.setPlainText("[Rules]\n1. Player 1 will go first and their turn will be over once they make one move.\n2. Following the rules of traditional checkers, the pieces can be moved diagonally left or right, one square per move.\n3. A point will be added to a player’s score if a piece captures an opponent’s piece.\n4. Once a piece reaches the opposite side of the board, it gains the ability to move backwards (diagonally). King pieces can only be piggy-backed with other king pieces.\n5. The game will end and victory will be determined when a player manages to capture all of their opponent’s pieces.")

        self.textEdit_piggyback = QTextEdit()
        self.textEdit_piggyback.setPlainText("[Gameplay- PIGGYBACKING]\n1.Players will be able to stack one checker on top of another. The maximum number of checkers that are able to be stacked on top of one another is 2.\n2. Once a piece is stacked on top of another, you cannot separate them.\n3. A stacked (/piggy-backed) checker piece will have an advantage in terms of movements, as they will be able to move twice (x2) as many squares diagonally as compared to 1 (which is that of a normal checker piece). However, when they are captured, the other player that captured the piggy-backed piece will receive 2 points. Players should utilize this technique wisely.")

        # q text edit -> read only
        self.textEdit.setReadOnly(True)

        # next button to go to checkers board (real game)
        next_gotoboard_button = QPushButton("NEXT")

        # add widget (rules)
        rules_screen_layout.addWidget(self.textEdit, alignment=Qt.AlignmentFlag.AlignCenter)
        rules_screen_layout.addWidget(self.textEdit_piggyback, alignment=Qt.AlignmentFlag.AlignCenter)

        # add widget(next button-> checkers board)
        rules_screen_layout.addWidget(next_gotoboard_button)


# run code
rules_screen_window = RulesDisplay()
rules_screen_window.show()

app.exec()
