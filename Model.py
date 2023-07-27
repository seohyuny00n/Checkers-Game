import json

class Player:
    
    def __init__(self) -> None:
        pass

class Board:
    pass

class Checkers:
    pass  


P1_name = input("Please input your name, P1: ")
P2_name = input("Please input your name, P2: ")

print(f"Okay, {P1_name} and {P2_name}. Let's start.")


white_checker_pieces: dict[str, bool] = {}
# opens checker json file
# stores in
with open("checkers_white_pieces.json") as contents:
    white_checker_pieces = json.load(contents)

# for x in white_checker_pieces:
#     print(x)

black_checker_pieces: dict[str, bool] = {}
# opens checker json file
# stores in
with open("checkers_black_pieces.json") as contents_2:
    black_checker_pieces = json.load(contents_2)

# for x in black_checker_pieces:
#     print(x)

