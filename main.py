from objects import *

player = Player(100, 100, 5, player_image, 25, 25)

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
#        bullet.fly()
 #       bullet.draw()

    pyg.display.update()
    clock.tick(FPS)