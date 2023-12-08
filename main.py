import random
import time

import pygame as pg
import pygame.freetype
from pygame.locals import *
import os
from Player import Player
from Projectile import Projectile
from GUI import GUI
from AsteroidLarge import AsteroidLarge
from AsteroidMedium import AsteroidMedium
from AsteroidSmall import AsteroidSmall
from GameManager import GameManager

# Window Size
WIDTH, HEIGHT = 800, 800
# colors
BG_COLOR = (0, 0, 0)

def main():
    # Initialize pygame
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    # Sound setup
    shoot_sound = pg.mixer.Sound(os.path.join("Assets/Audio", "shoot.mp3"))

    # instantiate player object
    player = Player()
    gm = GameManager()
    gui = GUI(gm)
    allObjects = pg.sprite.Group()
    allObjects.add(player)

    # Projectile Sprite Group
    projectiles = pg.sprite.Group()
    # Asteroid Sprite Group
    asteroids = pg.sprite.Group()

    # spawn starter asteroids
    asteroidBig = AsteroidLarge()
    asteroids.add(asteroidBig)
    asteroidOptions = [AsteroidLarge(), AsteroidMedium(), AsteroidSmall()]

    playerCollided = False
    playerResetTimer = 0
    playerResetDuration = 3000

    delta = 0
    shotDelta = 500
    spawnTimer = 1
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
        if player:
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

        spawnTimer -= delta
        if spawnTimer <= 0:
            asteroid = random.choice(asteroidOptions)
            asteroids.add(asteroid)
            spawnTimer = 2

        # check for collisions between player and asteroid
        if player and pg.sprite.spritecollide(player, asteroids, False) and not playerCollided:
            playerCollided = True
            gm.decreaseLife()
            # gui.update_lives(-1)
            pg.mixer.Sound.play(pg.mixer.Sound(os.path.join("Assets/Audio", "playerExplosion.mp3")))
            # kill player
            player = None
            # start reset timer
            playerResetTimer = pg.time.get_ticks()

        # check if enough time has passed for player to spawn
        if playerResetTimer > 0 and pg.time.get_ticks() - playerResetTimer >= playerResetDuration:
            # reset player
            player = Player()
            playerResetTimer = 0
            playerCollided = False

        # check for collision between projectile and asteroid
        for p in projectiles:
            if p.checkLifeTime():
                projectiles.remove(p)
            for a in asteroids:
                if p.projectileMask.overlap(a.asteroidMask, (a.rect.x - p.rect.x, a.rect.y - p.rect.y)):
                    p.kill()
                    a.kill()
                    gm.increaseScore(a.scorePoints())
                    pg.mixer.Sound.play(pg.mixer.Sound(os.path.join("Assets/Audio", "asteroidExplosion.mp3")))
                    # gui.update_score(a.scorePoints())

        # redraw background
        screen.fill(BG_COLOR)

        # update
        if player:
            player.update(delta)
        asteroids.update()
        projectiles.update()

        # redraw objects
        gui.draw_score(screen)
        gui.draw_lives(screen)
        if player:
            player.draw(screen)
        projectiles.draw(screen)
        asteroids.draw(screen)

        # flip buffer
        pg.display.flip()

        delta = clock.tick(FPS) / 1000.0
        shotDelta += delta

if __name__ == "__main__":
    main()
    pg.quit()
