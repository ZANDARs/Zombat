from objects import *

player = Player(100, 100, 5, player_image, 25, 25)
x = 100
y = 200


player = Player(100, 100, 5, player_image, 25, 25)


game = True

for i in range (15):
    zomb = Zombie(-10, 500, 2, zombie_images[0], 25, 25)
    zomb.spawn()
    enemmies.add(zomb)

while True:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            exit()


    if game:
        win.blit(background_img, (0, 0))
        for zomb in enemmies:
            dx = zomb.rect.centerx - player.rect.centerx
            dy = player.rect.centery - zomb.rect.centery
            ang = -math.atan2(dy, dx) - math.pi

            zomb.movement(ang)
            zomb.draw()


        player.update()
        player.draw()
        bullets.update()
        bullets.draw(win)

        for bullet in bullets:
            hits = pygame.sprite.spritecollide(bullet, enemmies, True)
            if hits:
                print("test")
                # Додаткові дії при зіткненні (наприклад, видалення кулі або зомбі)
                bullets.remove(bullet)
#        bullet.fly()
 #       bullet.draw()

    pyg.display.update()
    clock.tick(FPS)