import random
import pygame as pg
import os

class Asteroid(pg.sprite.Sprite):
    def __init__(self, size):
        super(Asteroid, self).__init__()

        self.__size = size
        self.__image = self.loadImage()
        self.__rect = self.__image.get_rect()

        self.__ranPoint = random.choice([(random.randrange(0, 800 - self.__rect.width),
                                          random.choice([-1 * self.__rect.height - 5, 800 + 5])),
                                         (random.choice([-1 * self.__rect.width - 5, 800 + 5]),
                                          random.randrange(0, 800 - self.__rect.height))])
        self.__rect.x, self.__rect.y = self.__ranPoint
        if self.__rect.x < 800 // 2:
            self.__xdir = 1
        else:
            self.__xdir = -1

        if self.__rect.y < 800 // 2:
            self.__ydir = 1
        else:
            self.__ydir = -1
        self.__xvel = self.__xdir * random.randrange(1, 3)
        self.__yvel = self.__ydir * random.randrange(1, 3)

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

    def loadImage(self):
        if self.__size == "large":
            return pg.image.load(os.path.join('Assets/Asteroid-Large', 'Asteroid_large1.png'))
        elif self.__size == "medium":
            return pg.image.load(os.path.join('Assets/Asteroid-Medium', 'Asteroid_medium1.png')).convert_alpha()
        elif self.__size == "small":
            return pg.image.load(os.path.join('Assets/Asteroid-Small', 'Asteroid_small1.png')).convert_alpha()

    def draw(self, screen):
        screen.blit(self.__image, self.__rect)

    def move(self):
        self.__rect.x += self.__xvel
        self.__rect.y += self.__yvel

    def explode(self):
        self.kill()

    def scorePoints(self):
        if self.__size == "large":
            return 20
        elif self.__size == "medium":
            return 50
        elif self.__size == "small":
            return 100

    def update(self):
        pass