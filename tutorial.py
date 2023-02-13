import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Apocalypse')
clock = pygame.time.Clock()
font_test = pygame.font.Font(None, 30)

bg_test = pygame.image.load('images/cave.png')
bg2_test = pygame.image.load('images/cavestructures.png')
killcount = font_test.render('kills:', False, 'White')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg_test, (0, 0))
    screen.blit(bg2_test, (250, 0))
    screen.blit(killcount, (10, 550))
    
    pygame.display.update()
    clock.tick(60)
