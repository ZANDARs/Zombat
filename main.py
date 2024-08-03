from setings import *

game = True

while True:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            exit()


    if game:
        win.blit(background_img, (0, 0))

    pyg.display.update()
    clock.tick(FPS)