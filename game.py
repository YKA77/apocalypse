import pygame # import pygame commands and functions
from config import * # import variables from config.py
import sys

class Game: # class for the actual game
    def __init__(self):
        self.screen = pygame.display.set_mode(window_width, window_height) # screen resolution 
        self.clock = pygame.time.Clock() 
        self.running = True # game is currently running

    def createTileMap(self): # create the map of the game
        pass

    def create(self):
        pass

    def update(self): # update movement and changes in every frame
        pass

    def events(self): # handles all inputs 
        pass

    def draw(self): # draws the sprites on each frame
        pass

    def main(self):
        pass

game = Game()
game.create() # start running an instance of the game

while game.running == True: # only run the game when the running attribute is set to True
    game.main()

pygame.quit()
sys.exit() 
