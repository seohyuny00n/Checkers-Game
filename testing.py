import pygame, sys
from button import Button
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, BLACKWOOD
from checkers.board import Board
from checkers.game import Game

# testing separately for the side bar

# this should open up the game screen with the checkerboard when user clicks PLAY button
# SPRINT 6: find out how to change the caption names

FPS = 60

# bg is from <a href="https://www.freepik.com/free-vector/watercolor-sugar-cotton-clouds-background_22378664.htm#query=pink%20wallpaper&position=1&from_view=search&track=ais">Image by pikisuperstar</a> on Freepik

pygame.init()

SCREEN = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Stackem Checkers")

def get_row_col_from_mouse(pos):
    # selecting and moving piece
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# perhaps make custom background if there is time
PINK_MENU_BACKGROUND = pygame.transform.scale(pygame.image.load("6574814.jpg"), (1200, 800))

def get_font(size):
    # change the font once everythings set
    return pygame.font.Font(None, size)

# menu will include the info button, play button, and game name/icon
# INFORMATION/RULES
def open_info():
    # opens the information screen
    while True:
        INFO_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        INFO_TEXT_ONE = get_font(45).render("All the rules of this game go here.", True, "white")
        INFO_RECT_ONE = INFO_TEXT_ONE.get_rect(center=(600, 400))
        SCREEN.blit(INFO_TEXT_ONE, INFO_RECT_ONE)

        INFO_BACK_MENU = Button(image=None, pos=(600, 600),
                                text_input="BACK TO MENU", font=get_font(75), base_color="white",  hovering_color="pink")
        INFO_BACK_MENU.changeColor(INFO_MOUSE_POS)
        INFO_BACK_MENU.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INFO_BACK_MENU.checkForInput(INFO_MOUSE_POS):
                    main_menu()

            pygame.display.update()


# state of the screen
MENU_SCREEN = 0
GAME_SCREEN = 1

# does not start up the game
# starting screen is the menu screen
GAME_SESSION = MENU_SCREEN

# GAME SCREEN HERE
def start_game():
    # should open the checkers game screen
    # put the back button here?
        clock = pygame.time.Clock()
        game = Game(SCREEN)

        while GAME_SESSION == GAME_SCREEN:
            clock.tick(FPS)

            if game.winner() is not None:
                print(game.winner())
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                # if click is outside of checkerboard bounds
                    if row < 0 or row >= 8 or col < 0 or col >= 8:
                        # implement side bar buttons here
                        return None
                    else:
                    # click is within the board boundaries 
                        piece = game.board.get_piece(row, col)
                        if piece is not None and piece.color == game.turn:
                            game.select(row, col)
            game.update()

# MAIN MENU
def main_menu():
    # the main menu stuff
    global GAME_SESSION
    while GAME_SESSION == MENU_SCREEN:
        # on menu screen
        SCREEN.blit(PINK_MENU_BACKGROUND, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(150).render("MAIN MENU", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 200))

        # change the options rect to make it so that the box is whitish not black
        GAME_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(600, 450),
                             text_input="PLAY", font=get_font(75), base_color="white", hovering_color="#FF939C")
        INFO_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(600, 600),
                             text_input="INFO", font=get_font(75), base_color="white", hovering_color="#FF939C")
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [INFO_BUTTON, GAME_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INFO_BUTTON.checkForInput(MENU_MOUSE_POS):
                    open_info()
                elif GAME_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # switch to game screen
                    GAME_SESSION = GAME_SCREEN
        
        pygame.display.update()

# for the game
while True:
    if GAME_SESSION == MENU_SCREEN:
        main_menu()
    elif GAME_SESSION == GAME_SCREEN:
        start_game()