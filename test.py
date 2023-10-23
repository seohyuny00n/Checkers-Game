import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60

pygame.display.set_caption('Checkers')

# pos is position for mouse
def get_row_col_from_mouse(pos):
    x, y = pos
    # returns the x coordinate in row
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# main window
def main():
    run = True
    # clock maintains fps rate
    clock = pygame.time.Clock()
    # game = Game()

    while run:
        clock.tick(FPS)

        # checks if any event has occurred
        # events are listed here 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    quit()
main()