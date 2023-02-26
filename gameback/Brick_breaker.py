import pygame


pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Brick breaker')
run = True 


keys = pygame.key.get_pressed()

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = 7
        self.speed_y = 7

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
    
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius )


class Paddle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 10
    
    def move(self):
        self.x += self.speed
    
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class Brick:
    def __init__(self, x, y, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.color = color
        self.visible = True

    def draw(self):
        if self.visible:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))

ball = Ball(400, 300, 10, (255, 0,0,))
paddle = Paddle(350, 580, 100, 10, (0,0,255))
bricks = []

for i in range (10):
    brick = Brick(10 + i * 80, 50, 20, (0, 255, 0))
    bricks.append(brick)

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    screen.fill((255,255,255))
    ball.move()
    ball.draw()
    paddle.draw()
    
    for brick in bricks:
        brick.draw()

    pygame.display.update()

pygame.time.delay(60)
