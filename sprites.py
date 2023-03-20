import pygame
from main import *
from config import *

class Spritesheet(): # class for spritesheets
    def __init__(self, path): # initialise the path of the spritesheet

        self.spritesheet = pygame.image.load(file).convert() # load the spritesheet to be used

    def get_image(self, x, y, width, height):
        sprite = pygame.Surface([width, height]) # create the surface for the image
        sprite.blit(spritesheet, (0, 0), (x, y, width, height) ) # loads image onto surface

        return sprite
    


class Wall(pygame.sprite.Sprite): # class for the wall block
    def __init__(self, game, x, y):
        
        self.game = game
        self.x = x*tilesize # each x position will be every 32 pixels
        self.y = y*tilesize # each y position will be every 32 pixels

        self.width = tilesize # width is 32 pixels
        self.height = tilesize # height is 32 pixels
