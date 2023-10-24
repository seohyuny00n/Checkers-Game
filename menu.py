import pygame, sys
from sidebarbuttons import Button

# testing separately for the menu

# bg is from <a href="https://www.freepik.com/free-vector/watercolor-sugar-cotton-clouds-background_22378664.htm#query=pink%20wallpaper&position=1&from_view=search&track=ais">Image by pikisuperstar</a> on Freepik

pygame.init()

SCREEN = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Main Menu")

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

# GAME SCREEN HERE

# MAIN MENU
def main_menu():
    # the main menu stuff
    while True:
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
        
        pygame.display.update()

main_menu()
                
