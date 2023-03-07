from gameback.paddle import Paddle
from gameback.ball import Ball
from gameback.brick import Brick
from sys import exit
import pygame


pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Brick breaker')
game_active = False 

#Clock
FPS = 60
clock = pygame.time.Clock()

#Fonts
font_game = pygame.font.Font(None,34)
font_main = pygame.font.SysFont('Verdana',50)

#Score, lives, levels
score = 0
lives = 3
level = 1

#Paddle 
paddle = Paddle(100, 10,'white')
paddle.rect.x = 350
paddle.rect.y = 560

#Ball
ball =Ball(7, 'white')
ball.rect.x = 345
ball.rect.y = 195

#Add to group
object_group = pygame.sprite.Group()
object_group.add(paddle)
object_group.add(ball)

#Bricks
all_bricks = pygame.sprite.Group()

def bricks_making(row):
    for i in range(row):
        for j in range(9):
            brick = Brick(78,30, (234,126,85))
            brick.rect.x = 20 + j * 80
            brick.rect.y = 60 + 62 * i
            object_group.add(brick)
            all_bricks.add(brick)
        for n in range(9):
            brick = Brick(78,30, (237,183,56))
            brick.rect.x = 56 + n * 80
            brick.rect.y = 91 + 62 * i
            object_group.add(brick)
            all_bricks.add(brick)

#Ball conditions
def ball_conditions():
    global lives
    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]

def reset_game():
    global score, lives, level
    score = 0
    lives = 3
    level = 1
    for brick in all_bricks: brick.kill()
    bricks_making(level)
    ball.rect.x = 345
    ball.rect.y = 280
    return True 

def ball_brick_collison():
    global level, score
    collision = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in collision:
        ball.collision_brick()
        score += 1
        brick.kill()
    if len(all_bricks)==0:
        text_level_complete = font_game.render(f"LEVEL {level} COMPLETE", 1, 'white')
        screen.blit(text_level_complete, (280,150))
        pygame.display.update()
        pygame.time.wait(1000)
        level +=1
        bricks_making(level)
        ball.rect.x = 345
        ball.rect.y = 350
        if level >= 4:
            text = font_game.render("YOU COMPLETE ALL LEVELS", 1, 'white')
            screen.blit(text, (240,200))
            pygame.display.update()
            pygame.time.wait(2000)
            pygame.quit()
            exit()

#Intro screen
game_name = font_main.render('Brick Breaker', False, 'white')
game_name_rect = game_name.get_rect(center = (400,200))

game_message = font_main.render('Press space to run', False, 'white')
game_message_rect = game_message.get_rect(center = (400,330))

bricks_making(level)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = reset_game()

    if game_active:           
        object_group.update()
        ball_conditions()

        if lives == 0:
            game_active = False

        #Ball-Paddle Collision
        if pygame.sprite.collide_mask(ball, paddle):
            ball.rect.x -= ball.velocity[0]
            ball.rect.y -= ball.velocity[1]
            ball.collision_paddle()

        #Ball hits brick
        ball_brick_collison()
        
        screen.fill((102,102,225))
        pygame.draw.line(screen,'white', [0,40],[800,40],2)
        text_score = font_game.render("Score:" + str(score), 1, 'white')
        screen.blit(text_score,(20,10))
        text_level = font_game.render("Level:" + str(level), 1, 'white')
        screen.blit(text_level,(340,10))
        text_lives = font_game.render("Lives:" + str(lives), 1, 'white')
        screen.blit(text_lives,(650,10))
        
        object_group.draw(screen)
    
    else:
        screen.fill((102,102,225))
        score_message = font_main.render(f'Your score: {score}', False, 'white')
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(game_name, game_name_rect)

        if score == 0: screen.blit(game_message,game_message_rect)
        else: screen.blit(score_message, score_message_rect)
        
    pygame.display.update()
    clock.tick(FPS)
    
