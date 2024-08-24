from objects import *

player = Player(100, 100, 5, player_image, 25, 25)
x = 100
y = 200
zomb_k = 0

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

            if player.hitbox.colliderect(zomb.hitbox):
                player.hp -= 20
                zomb.spawn()

        player.update()
        player.draw()
        bullets.update()
        bullets.draw(win)

        collide = pyg.sprite.groupcollide(bullets, enemmies, True, False)
        for bullet in collide:
            for zomb in collide[bullet]:
                zomb.hp -= 1
                if zomb.hp <= 0:
                    zomb.spawn()
                    zomb_k += 1
#        bullet.fly()
 #       bullet.draw()

        pyg.draw.rect(win, interface_color, interface_rect)
        hp_bar = f"{player.hp}/{player.max_hp}"
        text_hp = font_.render(hp_bar, False, hp_color)
        win.blit(text_hp, (interface_rect.x + 10, interface_rect.y + 10))
        txt_zomb_k = font_.render(str(zomb_k), True, zomb_kill_color)
        win.blit(txt_zomb_k, (interface_rect.x + 600, interface_rect.y + 10))


    pyg.display.update()
    clock.tick(FPS)