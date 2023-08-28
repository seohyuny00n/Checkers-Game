from .constants import SQUARE_SIZE, GREY, CROWN
import pygame

class Piece:
    """Defines piece behavior."""
    
    PADDING = 15
    OUTLINE = 5

    # each piece is unique and thus properties will be needed for each piece
    def __init__(self, row, col, color) -> None:
        """Initalize piece color, king status and position."""
        self.row = row
        self.col = col
        self.color = color
        # king status of piece
        self.king = False
        self.piggyback = False
        self.x = 0
        self.y = 0
        # call within bc calc position will be needed in case of moving twice
        self.calc_position()

    # this method also accounts for the piece being in the middle of the square
    def calc_position(self):
        """calculate position the piece has on a square."""
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        """make piece a king."""
        self.king = True

    def make_piggyback(self):
        """make piece a piggyback."""
        self.piggyback = True

    def draw_piece(self, window):
        """draw piece."""
        radius = SQUARE_SIZE//2 - self.PADDING
        # creates (IS) border by drawing a bigger circle. 
        # area of circle is the smaller circle on top (line 44)
        pygame.draw.circle(window, GREY, (self.x, self.y), radius + self.OUTLINE)
        # radius from centre to edge of square size (space in between is PADDING)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)
        if self.king:
            # calculation draws crown onto checker centre (checker centre is x,y -> 0,0)
            # so, x - half the width of crown aligns crown centre with the middle, but not height
            # y - half the height of crown ensures it is wholly in centre  
            window.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))
        if self.piggyback:

    def move(self, row, col):
        """move piece and change position once it moves."""
        # updates row and col
        self.row = row
        self.col = col
        self.calc_position()

    # internal representation of object
    # for debugging!!
    def __repr__(self) -> str:
        return self.color