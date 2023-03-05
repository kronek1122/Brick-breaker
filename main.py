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
clock = pygame.time.Clock()
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
 
score = 0
lives = 3



# Groups
'''paddle = pygame.sprite.GroupSingle()
paddle.add(Paddle(350, 580, 100, 10, LIGHTBLUE))'''

object_group = pygame.sprite.Group()

#Paddle 
paddle = Paddle(100, 10,LIGHTBLUE)
paddle.rect.x = 350
paddle.rect.y = 560

#Ball
ball =Ball(10, 10, WHITE)
ball.rect.x = 345
ball.rect.y = 195

#Add to group
object_group.add(paddle)
object_group.add(ball)

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    
    object_group.update()

    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]
    
    #Ball-Paddle Collision
    if pygame.sprite.collide_mask(ball, paddle):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.hit_paddle()

    screen.fill((DARKBLUE)) #
    pygame.draw.line(screen,WHITE, [0,38],[800,38],2) # rysowanie lini

    text_score = font.render("Score:" + str(score), 1, WHITE)
    screen.blit(text_score,(20,10))

    text_lives = font.render("Lives:" + str(lives), 1, WHITE)
    screen.blit(text_lives,(650,10))
    
    object_group.draw(screen)
    

    pygame.display.update()

    clock.tick(60)
    
