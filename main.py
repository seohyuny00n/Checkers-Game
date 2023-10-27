import pygame, sys
from assets.button import Button
from checkers.constants import SQUARE_SIZE, BROWN, HEIGHT, HOT_PINK, LIGHT_PINK
from checkers.game import Game
from assets.image import Image

# testing separately for the side bar

# this should open up the game screen with the checkerboard when user clicks PLAY button
# SPRINT 6: find out how to change the caption names

FPS = 60

pygame.init()

SCREEN = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Stackem Checkers")


def draw_sidebar():
    # draw on right of the checker gameboard
    # contains widgets
    sidebar_xpos = 800
    sidebar_width = 400
    sidebar = pygame.draw.rect(SCREEN, BROWN, (sidebar_xpos, 0, sidebar_width, HEIGHT))

    # get current mouse pos outside of the checkerboard bounds
    GAME_MOUSE_POS = pygame.mouse.get_pos()

    # DELETE
    # buttons
    # back to main menu screen button
    GAME_HOME_BUTTON = Button(image=pygame.image.load("graphics/Play Rect.png"), pos=(800 + 300, 200),
                              text_input="HOME", font=get_font(75), base_color="white", hovering_color="#FF939C")
    GAME_HOME_BUTTON.changeColor(GAME_MOUSE_POS)
    # GAME_HOME_BUTTON.update(sidebar)


def get_row_col_from_mouse(pos):
    # selecting and moving piece
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# perhaps make custom background if there is time
# IMAGE SOURCE: bg is from <a href="https://www.freepik.com/free-vector/watercolor-sugar-cotton-clouds-background_22378664.htm#query=pink%20wallpaper&position=1&from_view=search&track=ais">Image by pikisuperstar</a> on Freepik
PINK_MENU_BACKGROUND = pygame.transform.scale(pygame.image.load("graphics/6574814.jpg"), (1200, 800))

# font sources: 
def get_font(size):
    # https://www.dafont.com/super-plants.font
    return pygame.font.Font("graphics/Super Plants.ttf", size)

def get_font_two(size):
    # https://www.dafont.com/evogria.font
    return pygame.font.Font("graphics/Cocogoose Pro-trial.ttf", size)

# state of the screen
MENU_SCREEN = 0
GAME_SCREEN = 1
RULES_SCREEN = 2

# does not start up the game
# starting screen is the menu screen
GAME_SESSION = MENU_SCREEN

# menu will include the info button, play button, and game name/icon
# INFORMATION/RULES
def open_info():
    global GAME_SESSION
    # opens the information screen
    while GAME_SESSION == RULES_SCREEN:
        INFO_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        RULES_TEXT = Button(image=None, pos=(600, 100),
                                text_input="[RULES]", font=get_font(50), base_color="white",  hovering_color="#FF939C")
        RULES_TEXT.update(SCREEN)

        # RULES_IMAGE = Image(image=pygame.transform.scale(pygame.image.load("graphics/rulespig.jpg"),(300, 150)), pos=(600, 100))
        # RULES_IMAGE.update(SCREEN)

        RULES_ONE = Button(image=None, pos=(600, 200),
                                text_input="I. Darker pink side's (bottom pieces) player will go first.", font=get_font_two(20), base_color="#ff8080",  hovering_color="#FF939C")
        RULES_ONE.update(SCREEN)
        
        RULES_TWO = Button(image=None, pos=(600, 240),
                                text_input="Following the rules of traditional checkers, the pieces can be moved", font=get_font_two(20), base_color="#ff8080",  hovering_color="#FF939C")
        RULES_TWO.update(SCREEN)

        RULES_THREE = Button(image=None, pos=(600, 270),
                                text_input="DIAGONALLY left or right on the darker green squares.", font=get_font_two(20), base_color="#ff8080",  hovering_color="#FF939C")
        RULES_THREE.update(SCREEN)

        RULES_FOUR = Button(image=None, pos=(600, 310),
                                text_input="Squares that a piece can move to will be indicated with a WHITE dot/circle.", font=get_font_two(20), base_color="#ff8080",  hovering_color="#FF939C")
        RULES_FOUR.update(SCREEN)

        DIVIDER = Button(image=None, pos=(600, 340),
                                text_input="-", font=get_font_two(20), base_color="white",  hovering_color="#FF939C")
        DIVIDER.update(SCREEN)

        RULES_FIVE =  Button(image=None, pos=(600, 370),
                                text_input="II. Pieces that reach the END of OPPOSITE side will become a KING piece.", font=get_font_two(20), base_color="#ff6666",  hovering_color="#FF939C")
        RULES_FIVE.update(SCREEN)
        
        RULES_SIX =  Button(image=None, pos=(600, 400),
                                text_input="A king piece can move BACKWARDS as well as forwards.", font=get_font_two(20), base_color="#ff6666",  hovering_color="#FF939C")
        RULES_SIX.update(SCREEN)

        DIVIDER_TWO = Button(image=None, pos=(600, 430),
                                text_input="-", font=get_font_two(20), base_color="white",  hovering_color="#FF939C")
        DIVIDER_TWO.update(SCREEN)

        RULES_SEVEN =  Button(image=None, pos=(600, 460),
                                text_input="III. To CAPTURE an opponent's piece, your piece must JUMP OVER IT diagonally onto an EMPTY square.", font=get_font_two(20), base_color="#ff8080",  hovering_color="#FF939C")
        RULES_SEVEN.update(SCREEN)

        RULES_EIGHT =  Button(image=None, pos=(600, 490),
                                text_input="Whoever captures all their opponent's pieces first is declared the WINNER.", font=get_font_two(20), base_color="#ff8080",  hovering_color="#FF939C")
        RULES_EIGHT.update(SCREEN)

        # returns to menu
        INFO_BACK_MENU = Button(image=None, pos=(600, 600),
                                text_input="BACK TO MENU", font=get_font(50), base_color="white",  hovering_color="#FF939C")
        INFO_BACK_MENU.changeColor(INFO_MOUSE_POS)
        INFO_BACK_MENU.update(SCREEN)

        # return to game button
        INFO_BACK_GAME = Button(image=None, pos=(600, 700),
                                text_input="BACK TO GAME", font=get_font(50), base_color="white", hovering_color="#FF939C")
        INFO_BACK_GAME.changeColor(INFO_MOUSE_POS)
        INFO_BACK_GAME.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INFO_BACK_MENU.checkForInput(INFO_MOUSE_POS):
                    # to menu screen
                    GAME_SESSION = MENU_SCREEN
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INFO_BACK_GAME.checkForInput(INFO_MOUSE_POS):
                    # back to game screen instead of menu
                    GAME_SESSION = GAME_SCREEN
                    start_game()

            pygame.display.update()

# GAME SCREEN HERE
def start_game():
        global GAME_SESSION
    # should open the checkers game screen
    # put the back button here?
        clock = pygame.time.Clock()
        game = Game(SCREEN)

        while GAME_SESSION == GAME_SCREEN:
            clock.tick(FPS)

            if game.winner() is not None:
                print(game.winner())

            # get current mouse pos outside of the checkerboard bounds
            GAME_MOUSE_POS = pygame.mouse.get_pos()

            # buttons
            # back to main menu screen button
            GAME_HOME_BUTTON = Button(image=pygame.image.load("graphics/Play Rect.png"), pos=(800 + 200, 200),
                              text_input="HOME", font=get_font(75), base_color="white", hovering_color="#ebc493")
            GAME_HOME_BUTTON.changeColor(GAME_MOUSE_POS)

            # show rules screen button
            RULES_BUTTON = Button(image=pygame.image.load("graphics/Play Rect.png"), pos=(1000, 400),
                                  text_input="RULES", font=get_font(75), base_color="white", hovering_color="#bcacd2")
            RULES_BUTTON.changeColor(GAME_MOUSE_POS)

            # when player 1 has their turn, make it show that the TURN_STATUS_RED button shows 
            # however, when p2 has their turn, make turn status white show instead
            # PLAYER 1 (RED/HOT PINK) 
            TURN_STATUS_RED = Button(image=pygame.transform.scale(pygame.image.load("graphics/pinkrect.png"), (380, 150)), pos=(1000, 600),
                                 text_input="PLAYER 1 TURN", font=get_font(50), base_color=HOT_PINK, hovering_color="#FF939C")
            # PLAYER 2 (WHITE/LIGHT PINK)
            TURN_STATUS_WHITE = Button(image=pygame.image.load("graphics/Play Rect.png"), pos=(1000, 600),
                                       text_input="PLAYER 2 TURN", font=get_font(50), base_color="white", hovering_color="#FF939C")
            
            LIGHTPINK_FLOWER = Image(image=pygame.transform.scale(pygame.image.load("graphics/lightpink_flower.png"), (50, 50)), pos=(1000, 100))
            ORANGE_FLOWER = Image(image=pygame.transform.scale(pygame.image.load("graphics/orange_flower.png"), (50, 50)), pos=(850, 700))
            ORANGE_BIGGER = Image(image=pygame.transform.scale(pygame.image.load("graphics/orange_flower.png"), (60, 60)), pos=(900, 300))
            SALMON_FLOWER = Image(image=pygame.transform.scale(pygame.image.load("graphics/salmon_flower.png"), (50, 50)), pos=(950, 490))
            PURPLE_FLOWER = Image(image=pygame.transform.scale(pygame.image.load("graphics/purple_flower.png"), (50, 50)), pos=(1100, 300))
            PURP_TWO = Image(image=pygame.transform.scale(pygame.image.load("graphics/purple_flower.png"), (60, 60)), pos=(1150, 720))
            

            # draw the side bar
            draw_sidebar()
            # upload the buttons
            GAME_HOME_BUTTON.update(SCREEN)
            RULES_BUTTON.update(SCREEN)
            TURN_STATUS_RED.update(SCREEN)
            # add the flowers to the screen
            LIGHTPINK_FLOWER.update(SCREEN)
            ORANGE_FLOWER.update(SCREEN)
            PURPLE_FLOWER.update(SCREEN)
            SALMON_FLOWER.update(SCREEN)
            ORANGE_BIGGER.update(SCREEN)
            PURP_TWO.update(SCREEN)

            pygame.display.update()

            for event in pygame.event.get():
                row, col = -1, -1
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # if home button is clicked, bring back to main menu
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if GAME_HOME_BUTTON.checkForInput(GAME_MOUSE_POS):
                        GAME_SESSION = MENU_SCREEN
                        main_menu()
                    elif RULES_BUTTON.checkForInput(GAME_MOUSE_POS):
                        GAME_SESSION = RULES_SCREEN
                        open_info()
                    else:
                        pos = pygame.mouse.get_pos()
                        row, col = get_row_col_from_mouse(pos)
                # if click is outside of checkerboard bounds
                    if row < 0 or row >= 8 or col < 0 or col >= 8:
                        # change
                        return None
                    else:
                        # click is within the board boundaries
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

        LOGO = Image(pygame.transform.scale(pygame.image.load("graphics/logo.png"), (730, 550)), pos=(600, 250))
        LOGO.update(SCREEN)

        # change the options rect to make it so that the box is whitish not black
        GAME_BUTTON = Button(image=pygame.image.load("graphics/Play Rect.png"), pos=(600, 540),
                             text_input="PLAY", font=get_font_two(75), base_color="black", hovering_color="white")
        INFO_BUTTON = Button(image=pygame.image.load("graphics/Play Rect.png"), pos=(600, 670),
                             text_input="INFO", font=get_font_two(75), base_color="black", hovering_color="white")

        for button in [INFO_BUTTON, GAME_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INFO_BUTTON.checkForInput(MENU_MOUSE_POS):
                    GAME_SESSION = RULES_SCREEN
                    open_info()
                elif GAME_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # switch to game screen
                    GAME_SESSION = GAME_SCREEN
                    start_game()
        
        pygame.display.update()

# state of the screen
while True:
    if GAME_SESSION == MENU_SCREEN:
        main_menu()
    elif GAME_SESSION == GAME_SCREEN:
        start_game()
    elif GAME_SESSION == RULES_SCREEN:
        open_info()