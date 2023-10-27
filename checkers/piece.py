from checkers.constants import RED, WHITE, SQUARE_SIZE, GRAY, KINGPIG
import pygame

# NICOLE
class Piece:
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        # is the piece a king piece
        self.king = False
        self.piggyback = False
        
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    def calc_pos(self):
        # calculate x and y position based on the row, col it is in
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def make_king(self):
        # make a reg piece a king piece
        self.king = True
    
    def make_piggyback(self):
        # makes a piece (that is not alr piggybacked) a piggypiece
        self.piggyback = True
    
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        # bigger circle to make "border"
        pygame.draw.circle(win, GRAY, (self.x, self.y), radius + self.OUTLINE)
        # smaller circle
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            if self.piggyback:
                win.blit(KINGPIG, (self.x - KINGPIG.get_width()//2, self.y - KINGPIG.get_height()//2))
            else:
            # blit = put image onto the screen
                win.blit(KINGPIG, (self.x - KINGPIG.get_width()//2, self.y - KINGPIG.get_height()//2))
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
        
    
    def __repr__(self):
        # the internal representation of object
        return str(self.color)
