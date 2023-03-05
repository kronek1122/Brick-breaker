from gameback.paddle import Paddle
from gameback.ball import Ball
from gameback.brick import Brick

import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Brick breaker')
run = True 
clock = pygame.time.Clock()
font = pygame.font.Font(None,34)

WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
 
score = 0
lives = 3

ball = Ball(400, 300, 10, (255, 0,0,))
bricks = []

for i in range (10):
    brick = Brick(10 + i * 40, 50, 20, (0, 255, 0))
    bricks.append(brick)

# Groups
'''paddle = pygame.sprite.GroupSingle()
paddle.add(Paddle(350, 580, 100, 10, LIGHTBLUE))'''

object_group = pygame.sprite.Group()
paddle = Paddle(100, 10,LIGHTBLUE)
paddle.rect.x = 350
paddle.rect.y = 560

#Add to group

object_group.add(paddle)

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    
    object_group.update()

    screen.fill((DARKBLUE)) #
    pygame.draw.line(screen,WHITE, [0,38],[800,38],2) # rysowanie lini

    text_score = font.render("Score:" + str(score), 1, WHITE)
    screen.blit(text_score,(20,10))

    text_lives = font.render("Lives:" + str(lives), 1, WHITE)
    screen.blit(text_lives,(650,10))
    
    object_group.draw(screen)

    pygame.display.update()

    '''ball.move()
    ball.draw()
    paddle.draw()
    
    for brick in bricks:
        brick.draw()'''
    
pygame.time.delay(60)