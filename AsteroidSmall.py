""" Michael Melei, Justin Burch"""
from Asteroid import Asteroid

class AsteroidSmall(Asteroid):
    """ Represents a small asteroid.

    This class inherits from the Asteroid class.
    """
    def __init__(self, x, y):
        """Initializes a small asteroid.

        Parameters:
            x (int): Initial x-coordinate.
            y (int): Initial y-coordinate.
        """
        super().__init__(64, x, y)
