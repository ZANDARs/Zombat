from setings import *
import math
class Game_sprite(pyg.sprite.Sprite):

    def __init__(self, x, y, speed, image, width, height):
        super().__init__()

        self.x = x
        self.y = y
        self.speed = speed
        self.image = pyg.transform.scale(pyg.image.load(image).convert_alpha(), (width, height))
        self.width = width
        self.height = height
        self.start_image = self.image

        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.hitbox = pyg.Rect(self.rect.x, self.rect.y, width/2, height/2)

    def rotate(self, angle):
        self.image = pyg.transform.rotate(self.start_image, angle)
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))



    def draw(self):
        win.blit(self.image, self.rect)

class Player(Game_sprite):
    def __init__(self, x, y, speed, image, width, height):
        super().__init__(x, y, speed, image, width, height)
        self.max_hp = 100
        self.hp = self.max_hp
        self.bullets = []

    def update(self):
        self.hitbox.center = self.rect.center
        keys = pyg.key.get_pressed()
        if keys[pyg.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        elif keys[pyg.K_d] and self.rect.x < 675:
            self.rect.x += self.speed
        elif keys[pyg.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif keys[pyg.K_s] and self.rect.y < 475:
            self.rect.y += self.speed

        pos = pyg.mouse.get_pos()
        dx = pos[0] - self.rect.centerx
        dy = self.rect.centery - pos[1]
        ang = math.degrees(math.atan2(dy, dx))

        self.rotate(ang - 90)
