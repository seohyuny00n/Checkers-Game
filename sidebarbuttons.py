import pygame
import sys

class ImageButton():
    # button within the game screen 
    def __init__(self, image, pos):
        self.image = pygame.image.load(image)
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        
    def update(self, screen):
        screen.blit(self.image, self.rect)
    
    def checkForInput(self, position):
        # coordinates to check if mouse is clicking/hovering over button boundary
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True