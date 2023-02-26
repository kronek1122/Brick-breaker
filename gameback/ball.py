import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = 7
        self.speed_y = 7

    
        #pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius )


    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y