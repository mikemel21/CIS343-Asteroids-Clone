import math
import random
import pygame as pg
import os

class Asteroid(pg.sprite.Sprite):
    """ Represents an asteroid in space

    This class serves as a base class for the different types of asteroids: large, medium, and small. This class
    provides attributes and methods that are inherited/extended by the various asteroid types.

    Attributes:
            __size (int): The size of the asteroid. This is used to scale the image to the correct size. Sizes can be:
                160 (Large), 96 (Medium), or 64 (Small).
            __image (pg.Surface): The image of the asteroid.
            __rect (pg.Rect): Box for the asteroid's image.
            __asteroidMask (pg.Mask): Mask used for collision detection.
            __speed (int): The speed in which the asteroid moves.

    Properties:
        image (pg.Surface): The read-only property to access the asteroid's image.\n
        rect (pg.Rect): The read-only property to access the asteroid's image bounding box.\n
        asteroidMask (pg.Mask): The read-only property to access the asteroid's collision mask. Detects collisions
            with the asteroid.

    Methods:
        __init__(size, x, y): Initialize asteroid with a given size and initial position coordinates.
        draw(screen): Draw the asteroid on the specified screen.
        scorePoints(): Return the points scored based on what asteroid type was destroyed.
        update(): Update the position of the asteroid.
    """
    def __init__(self, size, x, y):
        """Initializes the Asteroid

        Parameters:
            size (int): The size of the asteroid. Used to scale the image to the correct size based on asteroid type.
            x (int): The x-coordinate of the asteroid's starting position.
            y (int): The y-coordinate of the asteroid's starting position.
        """
        super(Asteroid, self).__init__()

        self.__size = size
        # self.__image = self.loadImage()
        self.__image = pg.image.load(os.path.join('Assets', 'Asteroid.png'))
        self.__image = pg.transform.scale(self.__image, (size, size))
        self.__rect = self.__image.get_rect()
        self.__asteroidMask = pg.mask.from_surface(self.__image)

        self.__rect.x = x
        self.__rect.y = y

        # self.__rect.x = random.randint(-5, 805)
        # self.__rect.y = random.randint(-5, 805)
        self.__speed = random.randint(1, 3)

    @property
    def image(self):
        """The read-only property for accessing the asteroid's image."""
        return self.__image

    @property
    def rect(self):
        """The read-only property to access the asteroid's image bounding box."""
        return self.__rect

    @property
    def asteroidMask(self):
        """The read-only property to access the asteroid's collision mask. Detects collisions with the asteroid."""
        return self.__asteroidMask

    def draw(self, screen):
        """Draw the asteroid on the specified screen

        Args:
            screen: Stores what screen the asteroid is to be drawn on.
        """
        screen.blit(self.__image, self.__rect)

    def scorePoints(self):
        """Return the points scored based on what asteroid type was destroyed

        Returns:
            The point amount that will be added to the player's score.
            Return value will be either: 20 (Large), 50 (Medium), 100 (Small).
        """
        if self.__size == 160:
            return 20
        elif self.__size == 96:
            return 50
        elif self.__size == 64:
            return 100

    def update(self):
        """Update the position of the asteroid."""
        self.__rect.x += self.__speed
        self.__rect.y += self.__speed