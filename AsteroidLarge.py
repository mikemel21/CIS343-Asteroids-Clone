import pygame as pg
from Asteroid import Asteroid

class AsteroidLarge(Asteroid):
    def __init__(self):
        # super(AsteroidLarge, self).__init__()
        super().__init__(160)

    def update(self):
        super().update()