import pygame
from config import *

class Wall(pygame.sprite.Sprite): # class for the wall block
    def __init__(self, game, x, y):
        
        self.game = game
        self._layer = wall_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*tilesize # each x position will be every 32 pixels
        self.y = y*tilesize # each y position will be every 32 pixels
        
        self.groups = self.game.all_sprites 
        pygame.sprite.Sprite.__init__(self, self.groups) # adding all of the sprites to one group

        self.width = tilesize # width is 32 pixels
        self.height = tilesize # height is 32 pixels

        self.image = self.game.cave_spritesheet.get_sprite(144,112, self.width, self.height) # the image of the wall is cropped from the coordinates of the spritesheet
        self.rect = self.image.get_rect() # getting the rectangle from the surface
        self.rect.x = self.x 
        self.rect.y = self.y


class Ground(pygame.sprite.Sprite): # class for the wall block
    def __init__(self, game, x, y):
        
        self.game = game
        self._layer = ground_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*tilesize # each x position will be every 32 pixels
        self.y = y*tilesize # each y position will be every 32 pixels
        
        self.groups = self.game.all_sprites 
        pygame.sprite.Sprite.__init__(self, self.groups) # adding all of the sprites to one group

        self.width = tilesize # width is 32 pixels
        self.height = tilesize # height is 32 pixels

        self.image = self.game.cave_spritesheet.get_sprite(0,144, self.width, self.height) # the image of the wall is cropped from the coordinates of the spritesheet
        self.rect = self.image.get_rect() # getting the rectangle from the surface
        self.rect.x = self.x 
        self.rect.y = self.y

class Exit(pygame.sprite.Sprite): # class for the wall block
    def __init__(self, game, x, y):
        
        self.game = game
        self._layer = exit_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*tilesize # each x position will be every 32 pixels
        self.y = y*tilesize # each y position will be every 32 pixels
        
        self.groups = self.game.all_sprites 
        pygame.sprite.Sprite.__init__(self, self.groups) # adding all of the sprites to one group

        self.width = tilesize # width is 32 pixels
        self.height = tilesize # height is 32 pixels

        self.image = self.game.cave_spritesheet.get_sprite(48,8, self.width, self.height) # the image of the wall is cropped from the coordinates of the spritesheet
        self.rect = self.image.get_rect() # getting the rectangle from the surface
        self.rect.x = self.x 
        self.rect.y = self.y
