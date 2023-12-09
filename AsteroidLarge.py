import pygame as pg
from Asteroid import Asteroid

class AsteroidLarge(Asteroid):
    """Represents a large asteroid.

    This class inherits the Asteroid class.
    """
    def __init__(self, x, y):
        """Initializes a small asteroid.

        Parameters:
            x (int): Initial x-coordinate.
            y (int): Initial y-coordinate.
        """
        super().__init__(160, x, y)