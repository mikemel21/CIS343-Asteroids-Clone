import math
import random
import pygame as pg
import os

class Asteroid(pg.sprite.Sprite):
    def __init__(self, size):
        super(Asteroid, self).__init__()

        self.__size = size
        self.__image = self.loadImage()
        self.__rect = self.__image.get_rect()
        self.__asteroidMask = pg.mask.from_surface(self.__image)

        self.__rect.x = random.choice([-5, 850])
        self.__rect.y = random.choice([0, 800])
        self.speed = random.uniform(1, 3)
        self.angle = math.atan2(800 / 2 - self.__rect.y, 800 / 2 - self.rect.x)

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

    @property
    def asteroidMask(self):
        return self.__asteroidMask

    def loadImage(self):
        if self.__size == "large":
            return pg.image.load(os.path.join('Assets/Asteroid-Large', 'Asteroid_large1.png')).convert_alpha()
        elif self.__size == "medium":
            return pg.image.load(os.path.join('Assets/Asteroid-Medium', 'Asteroid_medium1.png')).convert_alpha()
        elif self.__size == "small":
            return pg.image.load(os.path.join('Assets/Asteroid-Small', 'Asteroid_small1.png')).convert_alpha()

    def draw(self, screen):
        screen.blit(self.__image, self.__rect)

    def scorePoints(self):
        if self.__size == "large":
            return 20
        elif self.__size == "medium":
            return 50
        elif self.__size == "small":
            return 100

    def update(self):
        self.__rect.x += self.speed * math.cos(self.angle)
        self.__rect.y += self.speed * math.sin(self.angle)

        if self.__rect.centerx > 850:
            self.__rect.centerx = 0
        if self.__rect.centery > 850:
            self.__rect.centery = 0
        if self.__rect.centerx < -10:
            self.__rect.centerx = 800
        if self.__rect.centery < -10:
            self.__rect.centery = 800