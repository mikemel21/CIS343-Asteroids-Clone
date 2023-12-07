from Asteroid import Asteroid

class AsteroidSmall(Asteroid):
    def __init__(self):
        # super(AsteroidLarge, self).__init__()
        super().__init__(64)

    def update(self):
        super().update()