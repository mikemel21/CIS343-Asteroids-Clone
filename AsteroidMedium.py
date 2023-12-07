from Asteroid import Asteroid

class AsteroidMedium(Asteroid):
    def __init__(self):
        # super(AsteroidLarge, self).__init__()
        super().__init__(96)

    def update(self):
        super().update()