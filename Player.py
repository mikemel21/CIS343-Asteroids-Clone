import pygame as pg
from pygame.transform import rotozoom
from pygame.math import Vector2
import math
import os

class Player(pg.sprite.Sprite):
    """ Class representing the Player

    """

    def __init__(self):
        super(Player, self).__init__()
        self.health = 100
        self.vel = 0
        self.accel = 0.1
        self.max_vel = 4
        self.rotation_vel = 4
        self.angle = 0

        # original image to maintain quality while rotating
        # self.ogImage = pg.image.load(os.path.join('Assets/Player', 'Player_idle.png')).convert_alpha()
        self.image = pg.image.load(os.path.join('Assets/Player', 'Player_idle.png')).convert_alpha()
        # rotate player to face up at start
        self.image = pg.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 400

    def blit_rotate(self, screen, top_left, angle):
        """ rotate player image around center axis

        :param screen: The game window; where the player should be drawn
        :param top_left: Top left of the player rect
        :param angle: The angle the player will be rotated to
        """
        # rotate original image
        rotatedImage = pg.transform.rotate(self.image, angle)
        # rotate image without changing x and y positions; rotate around center
        new_rect = rotatedImage.get_rect(center=self.image.get_rect(topleft = top_left).center)
        screen.blit(rotatedImage, new_rect.topleft)

    def draw (self, screen):
        # screen.blit(self.image, self.rect)
        self.blit_rotate(screen, (self.rect.x, self.rect.y), self.angle)

    def update(self, delta):
        pass

    def forward(self, delta):
        """ Move player forward

        :param
            delta: ensures movement speed is independent from FPS
        """
        self.vel = min(self.vel + self.accel, self.max_vel)
        # convert angle to radians
        radians = math.radians(self.angle)
        # move in direction based on the angle player is at
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        # change x and y
        self.rect.x -= horizontal
        self.rect.y -= vertical

    def decelerate(self):
        """gradually reduce player speed when not moving
        """
        # decelerate until vel is 0
        self.vel = max(self.vel - self.accel/2, 0)

        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        self.rect.x -= horizontal
        self.rect.y -= vertical

    def rotate(self, screen, rotDir: str):
        """ Change angle player will rotate to based on key press

        :param screen: Game window
        :param rotDir: direction to rotate
        """
        # rotate left
        if rotDir == "left":
            self.angle += self.rotation_vel
        # rotate right
        elif rotDir == "right":
            self.angle -= self.rotation_vel
