import pygame as pg
# from pygame.locals import *
from Player import Player
from Projectile import Projectile
import os

# Window Size
WIDTH, HEIGHT = 800, 800
BG_COLOR = (0, 0, 0)

def main ():
    # Initialize pygame
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    shoot_sound = pg.mixer.Sound(os.path.join("Assets/Audio", "shoot.mp3"))
    # instantiate player object
    player = Player()
    projectiles = pg.sprite.Group()

    delta = 0
    shotDelta = 500
    FPS = 60
    clock.tick(FPS)
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        # player movement
        keys = pg.key.get_pressed()
        playerMoving = False
        if keys[pg.K_w]:
            playerMoving = True
            player.forward()
        if keys[pg.K_a]:
            player.rotate(screen, "left")
        if keys[pg.K_d]:
            player.rotate(screen, "right")
        if keys[pg.K_SPACE]:
            if shotDelta >= 0.15:
                # play shoot sound
                pg.mixer.Sound.play(shoot_sound)
                pg.mixer.music.stop()
                # instantiate projectile and ad to projectile list
                projectile = Projectile(player.rect, player.angle)
                projectiles.add(projectile)
                shotDelta = 0

        if not playerMoving:
            player.decelerate()

        # redraw background
        screen.fill(BG_COLOR)

        # update
        player.update(delta)
        # update bullets
        for p in projectiles:
            p.update()
        player.draw(screen)
        projectiles.draw(screen)

        # flip buffer
        pg.display.flip()

        delta = clock.tick(FPS) / 1000.0
        shotDelta += delta

if __name__ == "__main__":
    main()
    pg.quit()