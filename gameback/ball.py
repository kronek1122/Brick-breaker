import pygame
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, color):
        super().__init__()

        self.color = color
        self.radius = radius

        self.image = pygame.Surface((2*self.radius, 2*self.radius))
        self.image.fill('black')
        self.image.set_colorkey('black')

        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

        self.velocity = [random.randint(4,7), 4]


    def collision_brick(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.choice([-6,-5,-4,4,5,6])
    
    def collision_paddle(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.choice([-6,-5,-4,4,5,6])

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
