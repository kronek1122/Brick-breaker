import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super().__init__()
        self.color = color
        self.speed = 10


        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        pygame.draw.rect(self.image, self.color, (0, 0, width, height))
        self.rect = self.image.get_rect()

    '''def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x >= 10:
            self.x -= self.speed 
        if keys[pygame.K_RIGHT] and self.x <=790:
            self.x += self.speed'''
