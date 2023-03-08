import pygame
from sys import exit
from config import *

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Apocalypse')
clock = pygame.time.Clock()
done = False
clock.tick(60)
font_test = pygame.font.Font(None, 30)
keys = pygame.key.get_pressed()

class zombie:
    def __init__(self, surface, rect, x_pos, y_pos):
        self._surface = surface
        self._rect = rect
        self._x_pos = x_pos
        self._y_pos = y_pos

'''class player:
    def __init__(self, surface, rect x_pos, y_pos)
        self'''

bg_menu = pygame.image.load('images/menutest.png')
bg_test = pygame.image.load('images/cave.png')
bg2_test = pygame.image.load('images/cavestructures.png')
killcount = font_test.render('kills:', False, 'White')

def main_menu():
    screen.blit(bg_menu, (0, 0))
    if keys[pygame.K_SPACE]:
        print("hello world")
    
def game():
    screen.blit(bg_test, (0, 0))
    screen.blit(bg2_test, (250, 0))
    screen.blit(killcount, (10, 550))
    screen.blit(zombie._surface, (600, 40))
       

        
