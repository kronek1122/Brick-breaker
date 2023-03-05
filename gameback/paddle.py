import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super().__init__()
        self.color = color
        self.height = height
        self.width = width

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill('black')
        self.image.set_colorkey('black')

        pygame.draw.rect(self.image, self.color, (0, 0, self.width, self.height))
        self.rect = self.image.get_rect()

    def move(self,speed):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= speed
        if keys[pygame.K_RIGHT] and self.rect.x < 700:
            self.rect.x += speed

    def update(self):
        self.move(7)

