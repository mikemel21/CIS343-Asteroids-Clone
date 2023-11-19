import pygame as pg
import math
import os

class Projectile(pg.sprite.Sprite):
    """ Class representing the player's projectile
    """
    def __init__(self, playerLocation, playerAngle, vel):
        super (Projectile, self).__init__()
        self.damage = 10
        self._vel = 15
        self.image = pg.image.load(os.path.join('Assets/Player', 'Projectile1.png'))
        self.angle = playerAngle
        self.playerVel = vel

        self.rect = self.image.get_rect()
        self.rect.x = playerLocation.x
        self.rect.y = playerLocation.y
        self.rect.centerx = playerLocation.centerx
        self.rect.centery = playerLocation.centery

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self._vel
        horizontal = math.sin(radians) * self._vel
        self.rect.x -= horizontal
        self.rect.y -= vertical