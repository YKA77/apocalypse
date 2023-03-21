import pygame
from main import *
from config import *

class Spritesheet(): # class for spritesheets
    def __init__(self, path): # initialise the path of the spritesheet
        self.spritesheet = pygame.image.load(path).convert() # load the spritesheet to be used

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]) # create the surface for the image
        image.blit(self.spritesheet, (0, 0), (x, y, width, height) ) # loads image onto surface

        return image
    


class Wall(pygame.sprite.Sprite): # class for the wall block
    def __init__(self, game, x, y):
        
        self.game = game
        self.x = x*tilesize # each x position will be every 32 pixels
        self.y = y*tilesize # each y position will be every 32 pixels
        self.layer = wall_layer
        
        self.groups = self.game.all_sprites 
        pygame.sprite.Sprite.__init__(self, self.groups) # adding all of the sprites to one group

        self.width = tilesize # width is 32 pixels
        self.height = tilesize # height is 32 pixels

        self.image = self.game.wall_spritesheet.get_image(144,112, self.width, self.height) # the image of the wall is cropped from the coordinates of the spritesheet
        self.rect = self.image.get_rect() # getting the rectangle from the surface
        self.x = self.rect.x 
        self.y = self.rect.y


class Ground(pygame.sprite.Sprite): # class for the ground block
    def __init__(self, game, x, y):
        
        self.game = game
        self.x = x*tilesize # each x position will be every 32 pixels
        self.y = y*tilesize # each y position will be every 32 pixels
        self.layer = ground_layer
        
        self.groups = self.game.all_sprites 
        pygame.sprite.Sprite.__init__(self, self.groups) # adding all of the sprites to one group

        self.width = tilesize # width is 32 pixels
        self.height = tilesize # height is 32 pixels

        self.image = self.game.wall_spritesheet.get_image(0,144, self.width, self.height) # the image of the ground is cropped from the coordinates of the spritesheet
        self.rect = self.image.get_rect() # getting the rectangle from the surface
        self.x = self.rect.x 
        self.y = self.rect.y


class Exit(pygame.sprite.Sprite): # class for the exit block
    def __init__(self, game, x, y):
        
        self.game = game
        self.x = x*tilesize # each x position will be every 32 pixels
        self.y = y*tilesize # each y position will be every 32 pixels
        self.layer = exit_layer
        
        self.groups = self.game.all_sprites 
        pygame.sprite.Sprite.__init__(self, self.groups) # adding all of the sprites to one group

        self.width = tilesize # width is 32 pixels
        self.height = tilesize # height is 32 pixels

        self.image = self.game.wall_spritesheet.get_image(48,8, self.width, self.height) # the image of the exit is cropped from the coordinates of the spritesheet
        self.rect = self.image.get_rect() # getting the rectangle from the surface
        self.x = self.rect.x 
        self.y = self.rect.y
