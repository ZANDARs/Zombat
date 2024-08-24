import pygame
import random

from pygame import font

pyg = pygame
pyg.init()

win_width = 700
win_height = 500

FPS = 20

font_ = font.Font(None, 65)

win = pyg.display.set_mode((win_width, win_height + 50))

clock = pyg.time.Clock()
player_image = "textures/player.png"

background_img = pyg.transform.scale(pyg.image.load("textures/background.png"), (win_width, win_height))

bullet_image = "textures/bullet.png"

zombie_images = ["textures/zomb_1.png", "textures/zomb_2.png", "textures/zomb_3.png"]





fire_sound = None
damage_sound = None
coin = None
bullets = pyg.sprite.Group()
enemmies = pyg.sprite.Group()

interface_rect = pyg.Rect(0, win_height, win_width, 50)
interface_color = (150, 150, 100)
hp_color = (249, 0, 0)
zomb_kill_color = (34, 154, 0)