""" Michael Melei, Justin Burch"""
import pygame as pg
import math
import os

class Player(pg.sprite.Sprite):
    """ Class representing the Player

    Holds the logic pertaining to Player transform, sprite image, movement, rotation, health, and controls

    Attributes:
        __angle (float): The rotation of the player.
        __vel (float): The player's velocity.
        __accel (float): The acceleration factor applied to the player.
        __max_vel (float): The maximum velocity of the player.
        __rotation_vel (float): The velocity in which the player rotates.
        __image (pg.Surface): The image representing the player.
        __rect (pg.Rect): The rectangular box for the player's image.
        __playerMask (pg.mask.Mask): The Mask for the collision detection of the player.

    Properties:
        image (pg.Surface): The read-only property for accessing the player's image.
        angle (float): The read-only property for accessing the player's current angle.
        rect (pg.Rect): The read-only property for accessing the player's bounding box.
        playerMask (pg.mask.Mask): The read-only property for accessing the player's mask for the collision detection
            of the player.

    Methods:
        __init__(): Initialize the player
        __blit_rotate(screen, top_left, playerAngle): Rotates the image around the center axis
        forward(): Move the player forward
        decelerate(): Gradually reduce the player speed when player stops moving forward
        rotate(): Change the player's angle based on key press.
        update(): Check the player's coordinates. If the player is off the screen, wrap the position to the
            opposite side.
    """
    def __init__(self):
        super(Player, self).__init__()

        self.__angle = 0.0
        self.__vel = 0.0
        self.__accel = 0.1
        self.__max_vel = 4.0
        self.__rotation_vel = 4.0

        # original image to maintain quality while rotating
        # self.ogImage = pg.image.load(os.path.join('Assets/Player', 'Player_idle.png')).convert_alpha()
        self.__image = pg.image.load(os.path.join('Assets/Player', 'Player_idle.png')).convert_alpha()
        # rotate player to face up at start
        self.__image = pg.transform.rotate(self.__image, 90)
        self.__rect = self.__image.get_rect()
        self.__rect.centerx = 400
        self.__rect.centery = 400
        self.__playerMask = pg.mask.from_surface(self.__image)

    @property
    def image(self):
        """The read-only property for accessing the player's image."""
        return self.__image
    @property
    def angle(self):
        """The read-only property for accessing the player's current angle."""
        return self.__angle
    @property
    def rect(self):
        """The read-only property for accessing the player's bounding box."""
        return self.__rect
    @property
    def playerMask(self):
        """The read-only property for accessing the player's mask for the collision detection of the player."""
        return self.__playerMask

    def __blit_rotate(self, screen, top_left, playerAngle):
        """ rotate player image around center axis

        Args:
            screen (pg.Surface): The game window; where the player should be drawn
            top_left (tuple): Top left of the player rect
            playerAngle (float): The angle the player will be rotated to
        """
        # rotate original image
        rotatedImage = pg.transform.rotate(self.__image, playerAngle)
        # rotate image without changing x and y positions; rotate around center
        new_rect = rotatedImage.get_rect(center=self.__image.get_rect(topleft = top_left).center)
        screen.blit(rotatedImage, new_rect.topleft)

    def draw (self, screen):
        """Draws the player on the specified screen

        Parameter:
            screen (pg.Surface): The screen where the player will be drawn.
        """
        # redraw player
        self.__blit_rotate(screen, (self.__rect.x, self.__rect.y), self.__angle)

    def forward(self):
        """Move player forward"""
        self.__vel = min(self.__vel + self.__accel, self.__max_vel)
        # convert angle to radians
        radians = math.radians(self.angle)
        # move in direction based on the angle player is at
        vertical = math.cos(radians) * self.__vel
        horizontal = math.sin(radians) * self.__vel

        # change x and y
        self.__rect.x -= horizontal
        self.__rect.y -= vertical

    def decelerate(self):
        """ gradually reduce player speed when not moving"""
        # decelerate until vel is 0
        self.__vel = max(self.__vel - self.__accel/2, 0)

        radians = math.radians(self.__angle)
        vertical = math.cos(radians) * self.__vel
        horizontal = math.sin(radians) * self.__vel

        self.__rect.x -= horizontal
        self.__rect.y -= vertical

    def rotate(self, rotDir: str):
        """ Change player angle based on key press

        Args:
            rotDir (str): direction to rotate
        """
        # rotate left
        if rotDir == "left":
            self.__angle += self.__rotation_vel
        # rotate right
        elif rotDir == "right":
            self.__angle -= self.__rotation_vel

    def update(self):
        """Check the player's coordinates. If the player is off the screen, wrap the position to the opposite side."""
        if self.rect.x > 800:
            self.rect.x = 0
        if self.rect.y > 800:
            self.rect.y = 0
        if self.rect.x < 0:
            self.rect.x = 800
        if self.rect.y < 0:
            self.rect.y = 800