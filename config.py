import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Apocalypse')
clock = pygame.time.Clock()
font_test = pygame.font.Font(None, 30)
keys = pygame.key.get_pressed()