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

        self.hitbox = pyg.Rect(self.rect.x, self.rect.y, width//2, height//2)

    def rotate(self, angle):
        self.image = pyg.transform.rotate(self.start_image, angle)
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

    def change_image(self, new_image):
        self.image = pyg.transform.scale(pyg.image.load(new_image).convert_alpha(), (self.width, self.height))
        self.start_image = self.image


    def draw(self):
        win.blit(self.image, self.rect)

class Player(Game_sprite):
    def __init__(self, x, y, speed, image, width, height):
        super().__init__(x, y, speed, image, width, height)
        self.max_hp = 100
        self.hp = self.max_hp
        self.reload = 0
        self.rate = 10
    def update(self):
        self.hitbox.center = self.rect.center
        keys = pyg.key.get_pressed()
        ms = pyg.mouse.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.centerx -= self.speed
        if keys[pygame.K_d] and self.rect.x < win_width - self.rect.width:
            self.rect.centerx += self.speed
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.centery -= self.speed
        if keys[pygame.K_s] and self.rect.y < win_height - self.rect.height:
            self.rect.centery += self.speed
        if ms[0]:
            if self.reload == 0:
                self.fire()
                self.reload = self.rate

        if self.reload != 0:
            self.reload -= 1

        pos = pyg.mouse.get_pos()
        dx = pos[0] - self.rect.centerx
        dy = self.rect.centery - pos[1]
        ang = math.degrees(math.atan2(dy, dx))

        self.rotate(ang - 90)

    def fire(self):
        #тут має бути звук типу
        pos = pyg.mouse.get_pos()
        dx = pos[0] - self.rect.centerx
        dy = self.rect.centery - pos[1]
        ang = -math.atan2(dy, dx)
        b = Bullet(bullet_image, self.rect.centerx, self.rect.centery, 3, 6, 70, ang)
        bullets.add(b)


class Bullet(Game_sprite):
    def __init__(self, image, x, y, w, h, speed, angle):
        super().__init__(x, y, speed, image, w, h)
        self.angle = angle

    def update(self):
        self.hitbox.center = self.rect.center
        self.rotate(math.degrees(-self.angle) - 90)
        self.rect.x += math.cos(self.angle) * self.speed
        self.rect.y += math.sin(self.angle) * self.speed


class Zombie(Game_sprite):
    def __init__(self, x, y, speed, image, width, height):
        super().__init__(x, y, speed, image, width, height)
        self.max_hp = 1
        self.hp = self.max_hp

    def spawn(self):
        self.change_image(random.choice(zombie_images))
        self.hp = self.max_hp

        cr = random.randint(1, 4)
        if cr == 1:
            x = 10
            y = random.randint(1, win_height)
        elif cr == 2:
            x = win_width - 10
            y = random.randint(1, win_height)
        elif cr == 3:
            x = random.randint(1, win_width)
            y = 10
        elif cr == 4:
            x = random.randint(1, win_width)
            y = win_height - 10
        self.rect.y = y
        self.rect.x = x

    def movement(self, angle):
        self.hitbox.center = self.rect.center
        self.rotate(math.degrees(-angle) - 90)
        self.rect.x += math.cos(angle) * self.speed
        self.rect.y += math.sin(angle) * self.speed
