import pygame
from sidebarbuttons import ImageButton

# add a section on the right hand side for:
# score, turn, menu button, rules button

class SidePanel:
    # the sidebar
    # will be on the right side of the checkerboard
    def __init__(self, image, pos):
        self.image = pygame.image.load(image)
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.blit(center=)
        self.create_sidepanel()

        def create_sidepanel(self):