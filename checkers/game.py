# the gameplay
import pygame
from checkers.constants import RED, WHITE, BLUE, SQUARE_SIZE
from checkers.constants import LIGHT_PINK, MED_PINK, HOT_PINK, LIGHT_GREEN, GRASS_GREEN
from checkers.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
    
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = HOT_PINK
        # shows the current valid moves that the player can make
        self.valid_moves = {}
    
    def winner(self):
        return self.board.winner()
   
    def reset(self):
        self._init()
    
# nicole's code
    @property
    def status_indicator(self):
        return self.turn

    @status_indicator.setter
    def status_indicator(self, current_turn):
        if current_turn:
            self.turn = current_turn


    def select(self, row, col):
        if self.selected:
            # selected piece is valid
            result = self._move(row, col)
            if not result:
                # if row selected is not valid,
                # then try to select diff piece
                self.selected = None
                # re-select and call method agin
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        
        return False
    
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
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
        # visual indication of where players can validly move their pieces
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, WHITE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        # utilize this for player turn visualization
        self.valid_moves = {}
        if self.turn == HOT_PINK:
            self.turn = LIGHT_PINK
        else:
            self.turn = HOT_PINK