import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super().__init__()
        self.color = color

        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        pygame.draw.rect(self.image, self.color, (0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self,speed):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            print('left')
            self.rect.x -= speed
        if keys[pygame.K_RIGHT] and self.rect.x < 700:
            print('right')
            self.rect.x += speed
    
    def moveLeft(self, speed):
        self.rect.x -= speed
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self,speed):
        self.rect.x += speed
        if self.rect.x > 700:
            self.rect.x = 700

    def update(self):
        self.move(6)

