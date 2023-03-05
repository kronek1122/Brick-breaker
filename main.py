from gameback.paddle import Paddle
from gameback.ball import Ball
from gameback.brick import Brick

from sys import exit
import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Brick breaker')
game_active = True 

#Clock
FPS = 60
clock = pygame.time.Clock()

#Font
font = pygame.font.Font(None,34)

#Score and Lives
score = 0
lives = 3



#Paddle 
paddle = Paddle(100, 10,'gray')
paddle.rect.x = 350
paddle.rect.y = 560

#Ball
ball =Ball(6, 'white')
ball.rect.x = 345
ball.rect.y = 195

#Add to group
object_group = pygame.sprite.Group()
object_group.add(paddle)
object_group.add(ball)

#Bricks
all_bricks = pygame.sprite.Group()

def bricks_making():
    pass

for i in range(7):
    brick = Brick(80,30, 'red')
    brick.rect.x = 60 + i* 100
    brick.rect.y = 60
    object_group.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(80,30, 'orange')
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    object_group.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(80,30, 'yellow')
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    object_group.add(brick)
    all_bricks.add(brick)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
                    
    object_group.update()

    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            text_game_over = font.render('GAME OVER', 1 ,'white')
            screen.blit(text_game_over,(height/2,width/2))
            pygame.display.update()
            pygame.time.wait(3000)
            pygame.quit()
            exit()

    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]
    
    #Ball-Paddle Collision
    if pygame.sprite.collide_mask(ball, paddle):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.collision()

    #Ball hits brick
    collision = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in collision:
      ball.collision()
      score += 1
      brick.kill()
      if len(all_bricks)==0:
            text_level_complete = font.render("LEVEL COMPLETE", 1, 'white')
            screen.blit(text_level_complete, (height/2,width/2))
            pygame.display.update()
            pygame.time.wait(3000)
            pygame.quit()
            exit()


    screen.fill(('blue'))
    pygame.draw.line(screen,'white', [0,38],[800,38],2) # rysowanie lini

    text_score = font.render("Score:" + str(score), 1, 'white')
    screen.blit(text_score,(20,10))

    text_lives = font.render("Lives:" + str(lives), 1, 'white')
    screen.blit(text_lives,(650,10))
    
    object_group.draw(screen)
    
    pygame.display.update()

    clock.tick(FPS)
    
