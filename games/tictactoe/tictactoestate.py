from GameBot.games.game.gamestate import GameState
import string
import random

class TicTacToeState(GameState):
    def __init__(self):
        super().__init__()
        self.states = {"": [[0,0,0], [0,0,0], [0,0,0]]}
    
    def addState(self, state):
        return super().addState(state)