import pygame

# width and height of the whole checkerboard
WIDTH, HEIGHT = 800, 800
# number of rows and cols in checkerboard
ROWS, COLS = 8, 8
# square size as per x-axis
# in this case, 100 (=800/8)
SQUARE_SIZE = WIDTH//COLS

# colors of checker pieces
WHITE = (255, 255, 255)
# black will be used for checkerboard and checker pieces
BLACK = (0, 0, 0)
# ivory white for checkerboard
IVORY_WHITE = (242, 239, 222)
# color for showing user where they can move piece
BLUE = (0, 0, 255)
# border
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('checkers/crown.png'), (44, 25))
