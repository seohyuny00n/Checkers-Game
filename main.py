import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, BLACKWOOD
from checkers.board import Board
from checkers.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH+400, HEIGHT))
# extra width so that there is space for the other stuff

# name of the game
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    # selecting and moving piece
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() is not None:
            print(game.winner())

        for event in pygame.event.get():
            # will check to see if any events have occurred, and update accordingly
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    # will get rid of window
    pygame.quit()

main()
