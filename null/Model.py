import json


# player object - what characteristics do they have?
class Player:
    
    def __init__(self) -> None:
        self.P1_score = []
        self.P2_score = []
        # player moves stored
        self.P1_moves_log = []
        self.P2_moves_log = []  


# board object - what can act on it?
class Board:

    def __init__(self) -> None:
            
    
    def move_piece(self) -> None:

    # this would totally return coordinates
    # that means I'd have to load in the board coord.json in this class
    # how to tell comp which coord???
    def get_piece(self):
        return 

# checker object - what describes it?
class Checkers:
    
    def __init__(self, piece, row, col) -> None:
        self.piece = piece
        self.row = row
        self.col = col
        self.king = False

    # makes checkerpiece a king
    def make_king(self) -> bool:
         self.king = True






P1_name = input("Please input your name, P1: ")
P2_name = input("Please input your name, P2: ")

print(f"Okay, {P1_name} and {P2_name}. Let's start.")


white_checker_pieces: dict[str, bool] = {}
# opens checker json file
# stores in white_checker_pieces
with open("checkers_white_pieces.json") as contents:
    white_checker_pieces = json.load(contents)

# for x in white_checker_pieces:
#     print(x)

black_checker_pieces: dict[str, bool] = {}
# opens checker json file
# stores in black_checker_pieces
with open("checkers_black_pieces.json") as contents_2:
    black_checker_pieces = json.load(contents_2)

# for x in black_checker_pieces:
#     print(x)

