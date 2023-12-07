import pygame as pg
import math
import os

class Projectile(pg.sprite.Sprite):
    """ Class representing the player's projectile

    Attributes:
        playerLocation: access to location of the player so projectiles can spawn
        playerAngle: access to angle of player
    """
    def __init__(self, playerLocation, playerAngle):
        """ Initializes projectile instance based on player location and angle

        :param playerLocation: x and y coordinates of player
        :param playerAngle: angle player is facing
        """
        super (Projectile, self).__init__()
        self.__damage = 10
        self.__vel = 15
        self.__image = pg.image.load(os.path.join('Assets/Player', 'Projectile1.png'))
        self.__angle = playerAngle
        self.__projectileMask = pg.mask.from_surface(self.__image)

        self.rect = self.image.get_rect()
        self.rect.x = playerLocation.x
        self.rect.y = playerLocation.y
        self.rect.centerx = playerLocation.centerx
        self.rect.centery = playerLocation.centery
    @property
    def image(self):
        return self.__image
    @property
    def rect(self):
        return self.__rect
    @property
    def projectileMask(self):
        return self.__projectileMask

    @image.setter
    def image(self, value):
        self.__image = value
    @rect.setter
    def rect(self, value):
        self.__rect = value

    def check_bounds(self):
        """Checks if projectile is off the screen; if it is, the projectile location wraps to opposite side. """
        if self.rect.x > 800:
            self.rect.x = 0
        if self.rect.y > 800:
            self.rect.y = 0
        if self.rect.x < 0:
            self.rect.x = 800
        if self.rect.y < 0:
            self.rect.y = 800

    def draw(self, screen):
        """Redraw the projectile
        :param screen: display to draw the projectile on; main window
        """
        screen.blit(self.image, self.rect)

    def update(self):
        """ Update Projectile position"""
        radians = math.radians(self.__angle)
        vertical = math.cos(radians) * self.__vel
        horizontal = math.sin(radians) * self.__vel
        self.rect.x -= horizontal
        self.rect.y -= vertical
        self.check_bounds()




