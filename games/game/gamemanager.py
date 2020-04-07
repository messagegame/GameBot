import string
import random

class GameManager:
    """
    GameState is an abstract class that helps you store data.
    """
    def __init__(self):
        self.games = {}

    def addGame(self, game):
        """
        Given a state, (could be a 2d array, etc, add it to the state dictionary).
        Returns the stateId
        """
        gameId = ''.join(random.choice(string.ascii_letters + string.digits + "-_") for i in range(16))
        while self.games.get(gameId):
            gameId = ''.join(random.choice(string.ascii_letters + string.digits + "-_") for i in range(16))
            
        self.games[gameId] = game

        return gameId