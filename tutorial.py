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

zombie_surface = pygame.image.load('images/zombie/zombie1.png')
zombie_rect = zombie_surface.get_rect()
zombie_x_pos = 600
zombie_y_pos = 40

player_surface = pygame.image.load('images/player/playerwalk1.png')
player_rect = player_surface.get_rect()
player_x_pos = 10
player_y_pos = 540

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg_test, (0, 0))
    screen.blit(bg2_test, (250, 0))
    screen.blit(killcount, (10, 550))   
    zombie_x_pos -= 1
    if zombie_x_pos < 480: zombie_x_pos = 600
    screen.blit(zombie_surface, (zombie_x_pos, zombie_y_pos))
    screen.blit(player_surface, (player_x_pos, player_y_pos))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y_pos -= 1
    if keys[pygame.K_s]:
        player_y_pos += 1
    if keys[pygame.K_a]:
        player_x_pos -= 1
    if keys[pygame.K_d]:
        player_x_pos += 1
        
    
    pygame.display.update()
    clock.tick(60)
