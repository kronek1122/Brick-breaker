from gameback.paddle import Paddle
from gameback.ball import Ball
from gameback.brick import Brick

import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Brick breaker')
run = True 


ball = Ball(400, 300, 10, (255, 0,0,))
bricks = []

for i in range (10):
    brick = Brick(10 + i * 40, 50, 20, (0, 255, 0))
    bricks.append(brick)

# Groups
paddle = pygame.sprite.GroupSingle()
paddle.add(Paddle(350, 580, 100, 10, (0,0,255)))


while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    screen.fill((255,255,255))
    paddle.draw(screen)
    paddle.update()

    pygame.display.update()

    '''ball.move()
    ball.draw()
    paddle.draw()
    
    for brick in bricks:
        brick.draw()'''
    
pygame.time.delay(60)