import pygame

pyg = pygame
pyg.init()

win_width = 700
win_height = 500

FPS = 20

win = pyg.display.set_mode((win_width, win_height))

clock = pyg.time.Clock()

background_img = pyg.transform.scale(pyg.image.load("textures/background.png"), (700, 500))