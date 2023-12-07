import pygame as pg
from Asteroid import Asteroid

class AsteroidLarge(Asteroid):
    def __init__(self):
        # super(AsteroidLarge, self).__init__()
        super().__init__("large")

    def update(self):
        super().update()