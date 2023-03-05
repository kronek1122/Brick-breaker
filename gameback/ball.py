import pygame
from random import randint

class Ball(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super().__init__()

        self.color = color

        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        pygame.draw.rect(self.image, self.color, (0, 0, width, height))
        self.rect = self.image.get_rect()

        self.velocity = [randint(4,8),randint(-8,8)]

    
        #pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius )

    def hit_paddle(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]