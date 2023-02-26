import pygame



class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, width, color):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.color = color
        self.visible = True

    #def draw(self):
        #if self.visible:
            #pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))