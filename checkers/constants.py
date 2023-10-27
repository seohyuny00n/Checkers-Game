import pygame

# change the window size so that there will be black space 
# extra black space will be where scores, turns, and home buttons will be
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS



# rgb color codes
# basic colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# moodboard colors
LIGHT_PINK = (255, 204, 218)
MED_PINK = (252, 119, 159)
HOT_PINK = (245, 91, 121)
LIGHT_GREEN = (183, 202, 97)
GRASS_GREEN = (93, 151, 47)
BROWN = (176, 120, 64)

# the crown image, resized
KINGPIG = pygame.transform.scale(pygame.image.load('checkers/kingpig.png'), (50, 30))

# for the game screen
# current image is placeholder, will replace with custom graphics
MENU_BUTTON = pygame.transform.scale(pygame.image.load("homebuttonicon.png"), (44, 25))
# info button for sidebar
INFO_BUTTON = pygame.transform.scale(pygame.image.load("infobutton.png"), (44, 25))

# turn indicaors