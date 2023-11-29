import pygame as pg
import math
import os

class Player(pg.sprite.Sprite):
    """ Class representing the Player

    Holds the logic pertaining to Player transform, sprite image, movement, rotation, health, and controls
    """
    def __init__(self):
        super(Player, self).__init__()

        self.health = 100
        self.vel = 0.0
        self.accel = 0.1
        self.max_vel = 4.0
        self.rotation_vel = 4.0
        self.angle = 0.0

        # original image to maintain quality while rotating
        # self.ogImage = pg.image.load(os.path.join('Assets/Player', 'Player_idle.png')).convert_alpha()
        self.image = pg.image.load(os.path.join('Assets/Player', 'Player_idle.png')).convert_alpha()
        # rotate player to face up at start
        self.image = pg.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 400

    @property
    def health (self):
        return self.__health
    @property
    def vel(self):
        return self.__vel
    @property
    def accel(self):
        return self.__accel
    @property
    def max_vel(self):
        return self.__max_vel
    @property
    def rotation_vel(self):
        return self.__rotation_vel
    @property
    def angle(self):
        return self.__angle
    @property
    def image(self):
        return self.__image
    @property
    def rect(self):
        return self.__rect

    @health.setter
    def health(self, hp):
        if 100 >= hp >= 0:
            self.__health = hp
    @vel.setter
    def vel(self, newVel):
        self.__vel = newVel
    @accel.setter
    def accel(self, newAccel):
        self.__accel = newAccel
    @max_vel.setter
    def max_vel(self, newMax):
        self.__max_vel = newMax
    @rotation_vel.setter
    def rotation_vel(self, newRotVel):
        self.__rotation_vel = newRotVel
    @angle.setter
    def angle(self, newAngle):
        self.__angle = newAngle
    @image.setter
    def image(self, newImg):
        self.__image = newImg
    @rect.setter
    def rect(self, newRect):
        self.__rect = newRect

    def __blit_rotate(self, screen, top_left, playerAngle):
        """ rotate player image around center axis

        :param screen: The game window; where the player should be drawn
        :param top_left: Top left of the player rect
        :param playerAngle: The angle the player will be rotated to
        """
        # rotate original image
        rotatedImage = pg.transform.rotate(self.image, playerAngle)
        # rotate image without changing x and y positions; rotate around center
        new_rect = rotatedImage.get_rect(center=self.image.get_rect(topleft = top_left).center)
        screen.blit(rotatedImage, new_rect.topleft)

    def draw (self, screen):
        # redraw player
        self.__blit_rotate(screen, (self.__rect.x, self.__rect.y), self.__angle)

    def forward(self):
        """ Move player forward

        :param
            delta: ensures movement speed is independent from FPS
        """
        self.__vel = min(self.vel + self.__accel, self.__max_vel)
        # convert angle to radians
        radians = math.radians(self.angle)
        # move in direction based on the angle player is at
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        # change x and y
        self.__rect.x -= horizontal
        self.__rect.y -= vertical

    def decelerate(self):
        """
        gradually reduce player speed when not moving
        """
        # decelerate until vel is 0
        self.__vel = max(self.__vel - self.__accel/2, 0)

        radians = math.radians(self.__angle)
        vertical = math.cos(radians) * self.__vel
        horizontal = math.sin(radians) * self.__vel
        self.__rect.x -= horizontal
        self.__rect.y -= vertical

    def rotate(self, screen, rotDir: str):
        """ Change angle player will rotate to based on key press

        :param screen: Game window
        :param rotDir: direction to rotate
        """
        # rotate left
        if rotDir == "left":
            self.__angle += self.__rotation_vel
        # rotate right
        elif rotDir == "right":
            self.__angle -= self.__rotation_vel

    def update(self, delta):
        pass