import pygame as pg
from pygame import freetype
import os

class GUI:
    def __init__(self):
        pg.freetype.init()

        self.__score = 0
        self.__lives = 3

        # Font setup
        self.__font_path = os.path.join("Assets", "AsteroidsFont.ttf")
        self.__font_size = 32
        self.__font = pg.freetype.Font(self.__font_path, self.__font_size)
        self.__font_color = (255, 255, 255)

        # lives image setup
        self.__lives_image = pg.image.load(os.path.join('Assets/Player', 'Player_idle.png')).convert_alpha()
        self.__lives_image = pg.transform.scale(self.__lives_image, (58, 42))
        self.__lives_image = pg.transform.rotate(self.__lives_image, 90)

    def draw_score(self, screen):
        """ Displays the score at the top left of the screen
        """
        self.__font.render_to(screen, (10, 10), "Score: " + str(self.__score), self.__font_color, None,
                              size=self.__font_size)
        self.__font.render_to(screen, (10, 50), "Lives: ", self.__font_color, None,
                              size=self.__font_size)

    def draw_lives(self, screen):
        """Displays the player's amount of lives directly under the score
        Lives are displayed as a certain number of ship icons
        :param screen: main game window
        """

        offset = 0
        i = 0
        while i < self.__lives:
            screen.blit(self.__lives_image, (120 + offset, 40))
            offset += 45
            i += 1

    def update_score(self, points):
        """ Updates point value
        update_score is called whenever a player destroys an asteroid

        :param points:
        """
        self.__score += points

    def update_lives(self, life):
        pass