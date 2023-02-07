import pygame

pygame.init()

win = pygame.display.set_mode((600,600))

pygame.display.set_caption('Brick breaker')

run = True 

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 