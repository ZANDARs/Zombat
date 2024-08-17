import pygame
import random

pyg = pygame
pyg.init()

win_width = 700
win_height = 500

FPS = 20

win = pyg.display.set_mode((win_width, win_height))

clock = pyg.time.Clock()
player_image = "textures/player.png"

background_img = pyg.transform.scale(pyg.image.load("textures/background.png"), (700, 500))

bullet_image = "textures/bullet.png"

zombie_images = ["textures/zomb_1.png", "textures/zomb_2.png", "textures/zomb_3.png"]





fire_sound = None
bullets = pyg.sprite.Group()
enemmies = pyg.sprite.Group()