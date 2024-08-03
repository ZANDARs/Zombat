from setings import *

class Game_sprite(pyg.sprite.Sprite):

    def __init__(self, x, y, speed, texture, width, height):
        super().__init__()

        self.x = x
        self.y = y
        self.speed = speed
        self.texture = pyg.transform.scale(pyg.image.load(texture).convert_alpha(), (width, height))
        self.width = width
        self.height = height

        self.rect = self.texture.get_rect()
        self.rect.center = x, y

        self.hitbox = pyg.Rect(self.rect.x, self.rect.y, width/2, height/2)

    def drwaw(self):
        win.blit(self.image, self.rect)
