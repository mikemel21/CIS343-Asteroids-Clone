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
            __edge: Value chosen by random between "top", "bottom", "left", "right". This randomizes where the asteroids
                spawn.
            __x (int): Initial x value for an asteroid
            __y (int): Initial y value for an asteroid
            __dirX (int): Initial X direction for an asteroid.
            __dirY (int): Initial Y direction for an asteroid.
            __speed (int): The speed in which the asteroid moves.

    Properties:
        image (pg.Surface): The read-only property to access the asteroid's image.\n
        rect (pg.Rect): The read-only property to access the asteroid's image bounding box.\n
        asteroidMask (pg.Mask): The read-only property to access the asteroid's collision mask. Detects collisions
            with the asteroid.

    Methods:
        __init__(size, WIDTH, HEIGHT): Initialize asteroid with a given size and initial position coordinates.
        draw(screen): Draw the asteroid on the specified screen.
        scorePoints(): Return the points scored based on what asteroid type was destroyed.
        update(): Update the position of the asteroid.
    """
    def __init__(self, size, WIDTH, HEIGHT):
        """Initializes the Asteroid

        Parameters:
            size (int): The size of the asteroid. Used to scale the image to the correct size based on asteroid type.
            WIDTH (int): Width of the game screen.
            HEIGHT (int): Height of the game screen.
        """
        super(Asteroid, self).__init__()

        self.__size = size
        # self.__image = self.loadImage()
        self.__image = pg.image.load(os.path.join('Assets', 'Asteroid.png'))
        self.__image = pg.transform.scale(self.__image, (size, size))
        self.__rect = self.__image.get_rect()
        self.__asteroidMask = pg.mask.from_surface(self.__image)

        # Determine a random starting edge
        self.__edge = random.choice(['top', 'bottom', 'left', 'right'])
        self.__x = 0
        self.__y = 0
        # Calculate initial position based on the chosen edge
        if self.__edge == 'top':
            self.__x = random.randint(0, WIDTH)
            self.__y = -30  # Slightly above the top edge
        elif self.__edge == 'bottom':
            self.__x = random.randint(0, WIDTH)
            self.__y = HEIGHT + 30  # Slightly below the bottom edge
        elif self.__edge == 'left':
            self.__x = -30  # Slightly to the left of the left edge
            self.__y = random.randint(0, HEIGHT)
        elif self.__edge == 'right':
            self.__x = WIDTH + 30  # Slightly to the right of the right edge
            self.__y = random.randint(0, HEIGHT)

        self.__rect.center = (self.__x, self.__y)
        self.__dirX = random.uniform(-1, 1)
        self.__dirY = random.uniform(-1, 1)
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
        """Update the position of the asteroid. If an asteroid is out of bounds, the asteroid position will wrap."""
        self.__rect.x += self.__dirX * self.__speed
        self.__rect.y += self.__dirY * self.__speed

        if self.__rect.centerx < -40:
            self.__rect.centerx = 805
        if self.__rect.centerx > 850:
            self.__rect.centerx = -5
        if self.__rect.centery < -2:
            self.__rect.centery = 800
        if self.__rect.centery > 850:
            self.__rect.centery = 0