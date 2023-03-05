import pygame

class Brick(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super().__init__()
        self.color = color
        self.height = height
        self.width = width

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        pygame.draw.rect(self.image, self.color, (0, 0, self.width, self.height))
        self.rect = self.image.get_rect()
