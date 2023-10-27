import pygame

# SEOHYUN
class Image():
    "Image widgets that aside from looking pretty, does virtually nothing."
    def __init__(self, image, pos):
            self.image = image
            self.x_pos = pos[0]
            self.y_pos = pos[1]
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
    
    def update(self, screen):
        # add to relevant screen
        screen.blit(self.image, self.rect)