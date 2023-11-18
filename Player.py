import pygame as pg
import os

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.image.load(os.path.join('Assets/Player', 'Player_idle.png')).convert_alpha()