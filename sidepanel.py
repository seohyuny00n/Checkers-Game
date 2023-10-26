import pygame, sys
from sidebarbuttons import ImageButton
from button import Button

# add a section on the right hand side for:
# score, turn, menu button, rules button
# might not implement the scoreboard

# CONSTANTS for the side bar
# MEASUREMENTS
WIDTH, HEIGHT = 400, 800
# ROWS, COLS = 8, 8
# SQUARE_SIZE = WIDTH//COLS

# COLORS (rgb)
MISTY_ROSE = (255,228,225)
RUDDY_PINK = (225,142,150)

class SidePanel:
    # the sidebar
    # will be on the right side of the checkerboard
    def __init__(self, image, pos):
        self.image = pygame.image.load(image)
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.blit(center=)
        self.create_sidepanel()

    def get_font(size):
        return pygame.font.Font(None, size)

    def draw_background(self, win):
        # fill the window with a background
        win.fill(MISTY_ROSE)
    # TURN INDICATOR HERE 

    # BUTTONS!
    def back_home_button():
        # brings the player back to the main menu screen
        # not sure yet, but most likely resets the game...(DISCUSS)
        while True:
            HOME_MOUSE_POS = pygame.mouse.get_pos()

            # utilize normal buttons first
            # HOME_TEXT = get_font(45).render("HOME")
            # HOME_RECT_ONE = HOME_TEXT.get_rect(center=(1000, 200))
            # SCREEN.blit(HOME_TEXT, HOME_RECT_ONE)

            GAME_HOME_BACK = Button(image=pygame.image.load('Play Rect.png'), pos=(1000, 200),
                                    text_input="HOME", font=get_font(75), base_color="white", hovering_color="pink")
            GAME_HOME_BACK.changeColor(HOME_MOUSE_POS)
            GAME_HOME_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:




            

        
    def create_info_button(self, win):
        # brings the player to the rules screen
        self.
    

    def create_sidepanel(self):
        # create an instance of the sidepanel