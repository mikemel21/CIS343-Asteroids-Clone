""" Michael Melei, Justin Burch"""
import pygame as pg
import math
import os

class Projectile(pg.sprite.Sprite):
    """Represents a projectile fired by the player.

    This class inherits from pg.sprite.Sprite and provides functionality for creating and managing projectiles.
    Projectiles have a limited lifetime, move in the direction determined by the player's angle, and can check
    boundaries to wrap around the screen.

    Attributes:
        __damage (int): The damage inflicted by the projectile.
        __vel (int): The velocity of the projectile.
        __image (pg.Surface): The image representing the projectile.
        __angle (float): The angle at which the projectile is fired.
        __projectileMask (pg.mask.Mask): The mask for collision detection based on the projectile's image.
        __lifetime (float): The maximum lifetime of the projectile in seconds.
        __creation_time (float): The time when the projectile was created.
        __rect (pg.Rect): The rectangular bounding box for the projectile's image.

    Properties:
        image (pg.Surface): The property for accessing the projectile's image.
        rect (pg.Rect): The property for accessing the projectile's rectangular bounding box.
        projectileMask (pg.mask.Mask): The property for accessing the projectile's collision mask.

    Setters:
        image (pg.Surface): The setter property for updating the projectile's image.
        rect (pg.Rect): The setter property for updating the projectile's rectangular bounding box.

    Methods:
        __init__(playerLocation, playerAngle): Initialize the projectile with the player's location and firing angle.
        checkLifeTime(): Check if the projectile has exceeded its maximum lifetime.
        check_bounds(): Check and adjust the projectile's position if it goes beyond the screen boundaries.
        draw(screen): Draw the projectile on the specified screen.
        update(): Update the position of the projectile based on its velocity and angle.
    """

    def __init__(self, playerLocation, playerAngle):
        """ Initialize the Projectile object.

        Parameters:
            playerLocation (pg.Rect): The player's location from which the projectile is fired.
            playerAngle (float): The angle at which the projectile is fired.

        Attributes:
            __damage (int): The damage inflicted by the projectile.
            __vel (int): The velocity of the projectile.
            __image (pg.Surface): The image representing the projectile.
            __angle (float): The angle at which the projectile is fired.
            __projectileMask (pg.mask.Mask): The mask for collision detection based on the projectile's image.
            __lifetime (float): The maximum lifetime of the projectile in seconds.
            __creation_time (float): The time when the projectile was created.
            __rect (pg.Rect): The rectangular bounding box for the projectile's image.
        """
        super (Projectile, self).__init__()
        self.__damage = 10
        self.__vel = 15
        self.__image = pg.image.load(os.path.join('Assets/Player', 'Projectile1.png'))
        self.__angle = playerAngle
        self.__projectileMask = pg.mask.from_surface(self.__image)
        # create time limit for projectile existence
        self.__lifetime = 1
        self.__creation_time = pg.time.get_ticks() / 1000

        self.rect = self.image.get_rect()
        self.rect.x = playerLocation.x
        self.rect.y = playerLocation.y
        self.rect.centerx = playerLocation.centerx
        self.rect.centery = playerLocation.centery

    @property
    def image(self):
        """The read-only property to access the projectile's image."""
        return self.__image
    @property
    def rect(self):
        """The read-only property to access the projectile's rect box."""
        return self.__rect
    @property
    def projectileMask(self):
        """The read-only property to access the projectile's Mask for collision detection."""
        return self.__projectileMask

    @rect.setter
    def rect(self, value):
        """The setter to set the rect of the projectile."""
        self.__rect = value

    def checkLifeTime(self):
        """ Check if the projectile has exceeded its maximum lifetime.

        Remove projectile if it has exceeded existence time limit
        Returns:
            True (if lifetime is reached)
        """
        cur = pg.time.get_ticks() / 1000
        if cur - self.__creation_time > self.__lifetime:
            return True
        return False

    def check_bounds(self):
        """Check and adjust the projectile's position if it goes beyond the screen boundaries.

        If the position of the projectile is outside the boundaries of the screen, the projectile will wrap to the
        opposite side
        """
        if self.rect.x > 800:
            self.rect.x = 0
        if self.rect.y > 800:
            self.rect.y = 0
        if self.rect.x < 0:
            self.rect.x = 800
        if self.rect.y < 0:
            self.rect.y = 800

    def draw(self, screen):
        """Draw the projectile on the specified screen.
        :param screen: display to draw the projectile on; main window
        """
        screen.blit(self.image, self.rect)

    def update(self):
        """ Update the position of the projectile based on its velocity and angle"""
        radians = math.radians(self.__angle)
        vertical = math.cos(radians) * self.__vel
        horizontal = math.sin(radians) * self.__vel
        self.rect.x -= horizontal
        self.rect.y -= vertical
        self.check_bounds()