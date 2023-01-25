#Apocalypse
#NEA project 

import pygame
from pygame.locals import *

class Player:

    def __init__(self, lives, position, ammo):
        lives = Player.lives
        position = Player.pos
        ammo = Player.ammo

    def main():
        player = Player()

        while True:
            player.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Apocalypse')

    #background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    #text
    font = pygame.font.Font(None, 144)
    text = font.render("Apocalypse", 1, (145, 15, 15))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)

    #blit
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()


main()
