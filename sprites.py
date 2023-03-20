import pygame
from main import *
from config import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y)
        
        self.game = game
        self.x = x*tilesize
        self.y = y*tilesize