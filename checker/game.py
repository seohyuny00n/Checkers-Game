import pygame
from .constants import BLACK, WHITE, BLUE, SQUARE_SIZE
from checkers.board import Board

# responsible for everything: board, pieces etc
# allows user to interact with game
class Game:

    def __init__(self, window) -> None:
        self._init()
        self.window = window

    def update_game_display(self, window) -> None:
        self.board.draw_board_and_pieces(window)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def winner(self):
        # borrows winner method from board
        return self.board.winner()

    # cannot and should not be accessed from outside the class
    # rather than storing these properties twice, they're safely put in init and accessed
    # by the constructor method (class structure allows for class methods to be read all at once by computer)
    def _init(self):
        # selected by user
        self.selected = None
        # game controls the board. the board in main
        self.board = Board()
        # controls who goes first
        self.turn = BLACK
        # valid moves a player can make in a turn stored in dict
        self.valid_moves = {}

    # calls _init method
    # reset method is the same as _init method (initialized) but resets to the intialized state
    def reset(self):
        self._init()
    
    # select determines if a player will move a piece
    def select(self, row, col):
        # this will loop through until result is valid
        if self.selected:
            # trying to move result to whatever row, col is passed in
            # row and col must be valid for result to be true
            # after each select, turn changes (see _move method)
            result = self._move(row, col)
            if not result:
                self.selected = None
                # reselect row and col 
                self.select(row, col)
    
        # if piece is valid, then valid moves can be made
        piece = self.board.get_piece(row, col)
        # a piece that is black or white
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        
        return False
    
    # private as players don't really move pieces, they *select* it
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        # a piece can only move into a space that has no piece. this is represented by 0
        # selected is a piece in select method 
        # selected (piece) can only move into row and col which is in valid moves
        # if not, nothing happens/returns false
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped: 
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        
        return True
    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.window, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        # prevents valid moves from staying after player's turn
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK


