from Asteroid import Asteroid

class AsteroidMedium(Asteroid):
    """Represents a medium asteroid

    This class inherits from the Asteroid class.
    """
    def __init__(self, x, y):
        """Initializes a medium asteroid.

        Parameters:
            x (int): Initial x-coordinate.
            y (int): Initial y-coordinate.
        """
        super().__init__(96, x, y)