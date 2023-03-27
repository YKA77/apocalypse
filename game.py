import pygame # import pygame commands and functions
from config import * # import variables from config.py
from sprites import * # import classes from sprites.py
import sys

class Spritesheet(): # class for spritesheets
    def __init__(self, path): # initialise the path of the spritesheet
        self.spritesheet = pygame.image.load(path).convert() # load the spritesheet to be used

    def get_sprite(self, x,y, width, height):
        sprite = pygame.Surface([width, height]) # create the surface for the image
        sprite.blit(self.spritesheet, (0,0), (x,y,width,height) ) # loads image onto surface

        return sprite

class Game: # class for the actual game
    def __init__(self):
        self.screen = pygame.display.set_mode((window_width, window_height)) # screen resolution 
        self.clock = pygame.time.Clock() 
        self.running = True # game is currently running
        self.all_sprites = pygame.sprite.LayeredUpdates()

        self.cave_spritesheet = Spritesheet('images/cave.png') # 144, 112

    def createTileMap(self): # create the map of the game
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self,j,i)
                if column=='W': # for every B in the tilemap render a wall block
                    Wall(self,j,i)
                if column=='E':
                    Exit(self,j,i)

    def create(self): # handles the order in which the layers are rendered
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.createTileMap()

    def update(self): # update movement and changes in every frame
        self.all_sprites.update()

    def events(self): # handles all inputs 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if player closes the window then the game stops running
                self.running = False

    def draw(self): # draws the sprites on each frame
        self.screen.fill(black) # colours the screen black
        self.all_sprites.draw(self.screen) # draws all of the sprites onto the map
        self.clock.tick(fps) # update 60 times per second
        pygame.display.update() # actually display what is being drawn

    def main(self): # main game loop
        while self.running == True: 
            self.events()
            self.draw()
            self.update()


game = Game()
game.create() # start running an instance of the game


while game.running == True: # only run the game when the running attribute is set to True
    game.main()

pygame.quit()
sys.exit() 
