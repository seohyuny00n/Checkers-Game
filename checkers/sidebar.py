import pygame, sys
from checkers.sidebarbuttons import Button

# will delete in due time
pygame.init()

SCREEN = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Side Panel Test")

clock = pygame.time.Clock()
FPS = 60

BLACKWOOD = pygame.image.load("blackwood.png")
# maybe resize
# BLACKWOOD = pygame.transform.scale(pygame.image.load("blackwood.png", (400, 800)))

def get_font(size):
    # presents font in desired size 
    return pygame.font.Font("Kaoly Demo-Regular.ttf", size)
# the stuff next to the game board
# contains a turn indicator, scoreboard, and menu&info/rules button

def open_menu():
    # opens up the menu/home screen
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        MENU_TEXT = get_font(45).render("WELCOME TO STACKEM CHECKERS!", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # change this for sure
        MENU_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="white", hovering_color="pink")
        MENU_BACK.changeColor(PLAY_MOUSE_POS)
        MENU_BACK.update(SCREEN)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(MENU_MOUSE_POS):
                    main_menu()
    
        pygame.display.update()

def open_info():
    # opens up to a screen with rules and game info players might find helpful
    while True:
        INFO_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        INFO_TEXT = get_font(45).render("Rules for the game.", True, "black")
        INFO_RECT = INFO_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(INFO_TEXT, INFO_RECT)

        INFO_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="black", hovering_color="pink")
        INFO_BACK.changeColor(INFO_MOUSE_POS)
        INFO_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INFO_BACK.checkForInput(INFO_MOUSE_POS):
                    main_menu()
        
        pygame.display.update()

# the main menu
# will change accordingly
def main_menu():
    while True:
        SCREEN.fill('white')
        SCREEN.blit(BLACKWOOD, (800, 0))

        MAINMENU_MOUSE_POS = pygame.mouse.get_pos()
        MAINMENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MAINMENU_RECT = MAINMENU_TEXT.get_rect(center=(640, 100))

        # change this so that there is no text on the buttons
        # change the assets
        MENU_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250),
                           text_input="MENU")
        INFO_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 600),
                             text_input="INFO", font=get_font(75), base_color="#d7fcd4", hovering_color="white")

        SCREEN.blit()

        for button in [MENU_BUTTON, INFO_BUTTON]:
            # button.changeColor(MAINMENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MAINMENU_MOUSE_POS):
                    open_menu()
                if INFO_BUTTON.checkForInput(MAINMENU_MOUSE_POS):
                    open_info()
        pygame.display.update()