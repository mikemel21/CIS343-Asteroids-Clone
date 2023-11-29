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

        self.__rect = self.__image.get_rect()
        self.__rect.x = playerLocation.x
        self.__rect.y = playerLocation.y
        self.__rect.centerx = playerLocation.centerx
        self.__rect.centery = playerLocation.centery

    @property
    def damage(self):
        return self.__damage

    def draw(self, screen):
        screen.blit(self.__image, self.__rect)

    def update(self, screen):
        radians = math.radians(self.__angle)
        vertical = math.cos(radians) * self.__vel
        horizontal = math.sin(radians) * self.__vel
        self.__rect.x -= horizontal
        self.__rect.y -= vertical