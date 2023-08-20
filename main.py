import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# important to game window, not checkers game
FPS = 60

pygame.display.set_caption('Checkers')

# pos is position for mouse
def get_row_col_from_mouse(pos):
    x, y = pos
    # returns x coordinate ie row
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


# has an event loop
def main():
    run = True
    # clock maintains fps rate
    clock = pygame.time.Clock()
    game = Game(WIN)

    # piece = board.get_piece(0, 3)
    
    while run:
        clock.tick(FPS)
        
        # prints in terminal
        if game.winner() != None:
            print(f"The winner is {game.winner()}")

        # this checks if any events have occurred
        # events are listed here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get position the mouse clicks/buttondown
                # this translates into row, col via get row col fn
                # row, col is passed into piece (object of the board which confuses me)
                # 
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                # piece = board.get_piece(row, col) - test
                # board.move(piece, 4, 3)
                game.select(row, col)
        
        game.update_game_display(WIN)
    
    pygame.quit()

main()