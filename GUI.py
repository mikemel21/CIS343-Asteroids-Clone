import pygame as pg
from pygame import freetype
import os


class GUI:
    """ Represents the game GUI.

    Handles the logic for graphically displaying and updating the player's score and lives. It also handles the Game
        Over screen.

    Attributes:
        gm (GameManager): The GameManager instance in order to display the current score and lives.
        __font_path (string): Stores the path to the GUI text font.
        __font_size (int): Stores the size of the font.
        __font (Font): Stores the font the GUI will use.
        __font_color (tuple): Stores the RGB value of the color of the font.
        __WIDTH (int): Stores the screen width
        __HEIGHT (int): Stores the screen height
        __lives_image (str): Stores the image that will display the lives

    Methods:
        __init__(gamemanager): Initialize the GUI
        draw_score(screen): Displays the score at the top left of the screen.
        draw_lives(screen): Displays the player's lives directly under the score.
        game_over(screen): Displays the "game over" display when the player dies.
    """
    def __init__(self, gamemanager, WIDTH, HEIGHT):
        """ Initializes the GUI

        Parameters:
            gamemanager: The Gamemanager instance in order to display the current score and lives.
            WIDTH (int): The width of the main screen
            HEIGHT (int): The height of the main screen
        """
        pg.freetype.init()
        pg.display.set_caption("Asteroids")
        pg.display.set_icon(pg.image.load(os.path.join("Assets", "icon.jpg")))

        self.gm = gamemanager

        # Font setup
        self.__font_path = os.path.join("Assets", "AsteroidsFont.ttf")
        self.__font_size = 32
        self.__font = pg.freetype.Font(self.__font_path, self.__font_size)
        self.__font_color = (255, 255, 255)

        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT

        # lives image setup
        self.__lives_image = pg.image.load(os.path.join('Assets/Player', 'Player_idle.png')).convert_alpha()
        self.__lives_image = pg.transform.scale(self.__lives_image, (58, 42))
        self.__lives_image = pg.transform.rotate(self.__lives_image, 90)

    def draw_score(self, screen):
        """ Displays the score at the top left of the screen
        """
        self.__font.render_to(screen, (10, 10), "Score: " + str(self.gm.score), self.__font_color, None,
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
        while i < self.gm.lives:
            screen.blit(self.__lives_image, (120 + offset, 40))
            offset += 45
            i += 1

    def game_over(self, screen):
        """Displays the "game over" display when the player dies.
        :param screen: main game window
        """
        Text = "Game Over"
        ScoreText = "Score " + str(self.gm.score)
        dimensions = self.__font.get_rect(Text)
        scoreDimensions = self.__font.get_rect(ScoreText)

        self.__font.render_to(screen, ((self.__WIDTH - dimensions.width) // 2, (self.__HEIGHT - dimensions.height) // 2), Text,
                              self.__font_color, None, size=self.__font_size)
        self.__font.render_to(screen, ((self.__WIDTH - scoreDimensions.width) // 2, ((self.__HEIGHT - scoreDimensions.height) // 2)
                                       - 50), ScoreText, self.__font_color, None, size=self.__font_size)