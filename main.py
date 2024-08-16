from objects import *

player = Player(100, 100, 5, player_image, 25, 25)
x = 100
y = 200

def random_cord():
    global x
    global y
    cr = random.randint(1, 4)
    if cr == 1:
        x = 10
        y = random.randint(1, 500)
    elif cr == 2:
        x = 700 - 10
        y = random.randint(1, 500)
    elif cr == 3:
        x = random.randint(1, 700)
        y = 10
    elif cr == 4:
        x = random.randint(1, 700)
        y = 500 - 10
random_cord()
player = Player(100, 100, 5, player_image, 25, 25)
zomb = Zombie(x, y, 2, random.choice(["textures/zomb_1.png", "textures/zomb_2.png", "textures/zomb_3.png"]), 25, 25)

game = True

while True:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            exit()


    if game:
        win.blit(background_img, (0, 0))
        player.update()
        player.draw()
        bullets.update()
        bullets.draw(win)
        zomb.movement()
        zomb.draw()
#        bullet.fly()
 #       bullet.draw()

    pyg.display.update()
    clock.tick(FPS)