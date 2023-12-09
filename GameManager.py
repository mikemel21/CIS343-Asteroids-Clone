""" Michael Melei, Justin Burch"""
class GameManager:
    """Class representing the Game Manager

    Manages the player's score and lives.
    """
    def __init__(self, lives=3, score=0):
        self.lives = lives
        self.score = score

    def decreaseLife(self):
        """Decrease the player's lives by 1"""
        self.lives -= 1

    def increaseScore(self, points):
        """Increase the player's score according to the asteroid type

        :param points: Amount of points to increase by; dependent on asteroid type
        """
        self.score += points

    def checkLives(self):
        if self.lives == 1:
            return 1

    '''
    TODO:
        - When player runs out of lives, pause game and display popup w/ option to restart
    '''